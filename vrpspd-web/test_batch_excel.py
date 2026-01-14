"""
Simple test for batch Excel export (without running full algorithms)
"""

from algorithms.batch_excel_export import create_batch_excel_report
import os

# Sample batch results (giống như từ API)
sample_batch_results = [
    {
        'filename': 'test_file_1.txt',
        'success': True,
        'problem_info': {
            'num_customers': 16,
            'num_vehicles': 4,
            'capacity': 100
        },
        'results': {
            'savings': {
                'total_cost': 1234.56,
                'num_routes': 4,
                'computation_time': 0.123
            },
            'vnd': {
                'total_cost': 1123.45,
                'num_routes': 4,
                'computation_time': 2.456,
                'improvement': 9.0
            }
        }
    },
    {
        'filename': 'test_file_2.txt',
        'success': True,
        'problem_info': {
            'num_customers': 20,
            'num_vehicles': 5,
            'capacity': 120
        },
        'results': {
            'savings': {
                'total_cost': 2345.67,
                'num_routes': 5,
                'computation_time': 0.234
            },
            'vnd': {
                'total_cost': 2100.34,
                'num_routes': 5,
                'computation_time': 3.567,
                'improvement': 10.46
            }
        }
    },
    {
        'filename': 'test_file_3.txt',
        'success': True,
        'problem_info': {
            'num_customers': 12,
            'num_vehicles': 3,
            'capacity': 80
        },
        'results': {
            'savings': {
                'total_cost': 890.12,
                'num_routes': 3,
                'computation_time': 0.089
            },
            'vnd': {
                'total_cost': 845.78,
                'num_routes': 3,
                'computation_time': 1.234,
                'improvement': 4.98
            }
        }
    }
]

sample_summary = {
    'total_files': 3,
    'successful': 3,
    'failed': 0,
    'avg_improvement': 8.15,
    'total_cost_savings': 4470.35,
    'total_cost_vnd': 4069.57
}

if __name__ == '__main__':
    print("Testing Batch Excel Export...")
    
    try:
        # Create Excel file
        filepath = create_batch_excel_report(
            batch_results=sample_batch_results,
            summary=sample_summary,
            filename='TEST_Batch_Export.xlsx'
        )
        
        print(f"✓ Batch Excel file created successfully: {filepath}")
        
        # Check if file exists
        if os.path.exists(filepath):
            file_size = os.path.getsize(filepath)
            print(f"✓ File exists with size: {file_size} bytes")
        else:
            print("✗ File not found!")
        
        print(f"\nTest completed! Check the file at: {os.path.abspath(filepath)}")
        print("\nExpected content:")
        print("  - Sheet 1: Summary with statistics")
        print("  - Sheet 2: Comparison table with all files")
        print("  - Sheet 3: Best Results ranked by improvement")
        
    except Exception as e:
        print(f"✗ Test failed: {e}")
        import traceback
        traceback.print_exc()
