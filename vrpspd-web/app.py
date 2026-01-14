"""
Flask Web Application for VRPSPD Solver
"""

from flask import Flask, render_template, request, jsonify, send_file
import os
import json
from werkzeug.utils import secure_filename
import traceback

from algorithms import read_vrpspd_file, solve_savings, solve_vnd
from algorithms.visualization import create_plotly_data, create_plotly_figure_json
from algorithms.excel_export import create_excel_report
from algorithms.batch_processor import process_batch_files, create_batch_summary
from algorithms.batch_excel_export import create_batch_excel_report

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['SECRET_KEY'] = 'vrpspd-secret-key-2026'

ALLOWED_EXTENSIONS = {'txt'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    """Trang chủ."""
    return render_template('index.html')


@app.route('/api/upload', methods=['POST'])
def upload_file():
    """
    Upload single file và parse dữ liệu.
    
    Returns:
        JSON: {
            'success': bool,
            'filename': str,
            'data': {
                'num_customers': int,
                'num_vehicles': int,
                'capacity': int
            }
        }
    """
    try:
        if 'file' not in request.files:
            return jsonify({'success': False, 'error': 'No file uploaded'})
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'success': False, 'error': 'No file selected'})
        
        if not allowed_file(file.filename):
            return jsonify({'success': False, 'error': 'Only .txt files allowed'})
        
        # Save file
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Parse file
        cost_matrix, demand, pickup, vehicle_caps, capacity, num_vehicles = read_vrpspd_file(filepath)
        
        # Store data in session or temp storage (for now, we'll return it)
        return jsonify({
            'success': True,
            'filename': filename,
            'filepath': filepath,
            'data': {
                'num_customers': len(cost_matrix) - 1,  # Exclude depot
                'num_vehicles': num_vehicles,
                'capacity': capacity
            }
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'traceback': traceback.format_exc()
        })


@app.route('/api/solve', methods=['POST'])
def solve():
    """
    Chạy thuật toán giải VRPSPD.
    
    Request JSON:
        {
            'filepath': str,
            'algorithms': ['savings', 'vnd']  # or ['savings'] or ['vnd']
        }
    
    Returns:
        JSON: {
            'success': bool,
            'results': {
                'savings': {...},
                'vnd': {...}
            }
        }
    """
    try:
        data = request.get_json()
        filepath = data.get('filepath')
        algorithms = data.get('algorithms', ['savings'])
        
        if not filepath or not os.path.exists(filepath):
            return jsonify({'success': False, 'error': 'File not found'})
        
        # Parse file
        cost_matrix, demand, pickup, vehicle_caps, capacity, num_vehicles = read_vrpspd_file(filepath)
        
        results = {}
        
        # Run Savings if selected
        if 'savings' in algorithms:
            savings_result = solve_savings(cost_matrix, demand, pickup, capacity, num_vehicles)
            results['savings'] = savings_result
        
        # Run VND if selected (requires Savings first)
        if 'vnd' in algorithms:
            if 'savings' not in results:
                # Run Savings first to get initial solution
                savings_result = solve_savings(cost_matrix, demand, pickup, capacity, num_vehicles)
                results['savings'] = savings_result
            
            initial_vector = results['savings']['solution_vector']
            vnd_result = solve_vnd(initial_vector, cost_matrix, demand, pickup, capacity, max_time_seconds=60)
            results['vnd'] = vnd_result
        
        # Generate visualization data for best result
        best_result = results.get('vnd') or results.get('savings')
        if best_result:
            visualization_data = create_plotly_data(best_result['routes'], cost_matrix, demand, pickup)
            plotly_figure = create_plotly_figure_json(visualization_data)
        else:
            plotly_figure = None
        
        return jsonify({
            'success': True,
            'results': results,
            'problem_info': {
                'num_customers': len(cost_matrix) - 1,
                'num_vehicles': num_vehicles,
                'capacity': capacity
            },
            'visualization': plotly_figure
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'traceback': traceback.format_exc()
        })


@app.route('/api/export-excel', methods=['POST'])
def export_excel():
    """
    Xuất kết quả ra file Excel.
    """
    try:
        data = request.get_json()
        
        # Validate data
        if not data or 'results' not in data:
            return jsonify({
                'success': False,
                'error': 'Missing results data'
            })
        
        results = data['results']
        problem_info = data.get('problem_info', {})
        filename = data.get('filename', 'VRPSPD_Results.xlsx')
        
        # Generate Excel file
        filepath = create_excel_report(results, problem_info, filename)
        
        # Return file for download
        return send_file(
            filepath,
            as_attachment=True,
            download_name=filename,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'traceback': traceback.format_exc()
        })


@app.route('/api/batch-upload', methods=['POST'])
def batch_upload():
    """
    Upload multiple files for batch processing.
    """
    try:
        if 'files[]' not in request.files:
            return jsonify({
                'success': False,
                'error': 'No files uploaded'
            })
        
        files = request.files.getlist('files[]')
        uploaded_files = []
        
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                
                uploaded_files.append({
                    'filename': filename,
                    'filepath': filepath
                })
        
        return jsonify({
            'success': True,
            'files': uploaded_files,
            'count': len(uploaded_files)
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'traceback': traceback.format_exc()
        })


@app.route('/api/batch-solve', methods=['POST'])
def batch_solve():
    """
    Solve multiple VRPSPD instances.
    """
    try:
        data = request.get_json()
        files_data = data.get('files', [])
        algorithms = data.get('algorithms', ['savings'])
        
        if not files_data:
            return jsonify({
                'success': False,
                'error': 'No files to process'
            })
        
        # Process batch
        batch_results = process_batch_files(files_data, algorithms)
        
        # Create summary
        summary = create_batch_summary(batch_results)
        
        return jsonify({
            'success': True,
            'batch_results': batch_results,
            'summary': summary
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'traceback': traceback.format_exc()
        })


@app.route('/api/batch-export-excel', methods=['POST'])
def batch_export_excel():
    """
    Xuất batch results ra Master Excel.
    """
    try:
        data = request.get_json()
        
        # Validate data
        if not data or 'batch_results' not in data:
            return jsonify({
                'success': False,
                'error': 'Missing batch results data'
            })
        
        batch_results = data['batch_results']
        summary = data.get('summary', {})
        filename = data.get('filename', 'VRPSPD_Batch_Results.xlsx')
        
        # Generate Excel file
        filepath = create_batch_excel_report(batch_results, summary, filename)
        
        # Return file for download
        return send_file(
            filepath,
            as_attachment=True,
            download_name=filename,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'traceback': traceback.format_exc()
        })


if __name__ == '__main__':
    # Create upload folder if not exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    # Run app
    app.run(debug=True, host='0.0.0.0', port=5000)
