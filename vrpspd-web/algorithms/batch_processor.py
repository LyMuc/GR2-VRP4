"""
Batch Processor Module for VRPSPD
Xử lý nhiều file cùng lúc và tạo báo cáo tổng hợp
"""

from algorithms import read_vrpspd_file, solve_savings, solve_vnd
import os
from datetime import datetime


def process_batch_files(files_data, algorithms):
    """
    Xử lý batch files.
    
    Args:
        files_data (list): List of dict with 'filename' and 'filepath'
        algorithms (list): List of algorithm names ['savings', 'vnd']
        
    Returns:
        list: List of results cho từng file
    """
    batch_results = []
    
    for file_data in files_data:
        filename = file_data['filename']
        filepath = file_data['filepath']
        
        try:
            # Parse file
            cost_matrix, demand, pickup, vehicle_capacities, capacity, num_vehicles = read_vrpspd_file(filepath)
            
            # Results cho file này
            file_result = {
                'filename': filename,
                'success': True,
                'problem_info': {
                    'num_customers': len(cost_matrix) - 1,
                    'num_vehicles': num_vehicles,
                    'capacity': capacity
                },
                'results': {}
            }
            
            # Run Savings
            if 'savings' in algorithms:
                savings_result = solve_savings(cost_matrix, demand, pickup, capacity, num_vehicles)
                file_result['results']['savings'] = savings_result
            
            # Run VND
            if 'vnd' in algorithms:
                if 'savings' not in file_result['results']:
                    savings_result = solve_savings(cost_matrix, demand, pickup, capacity, num_vehicles)
                    file_result['results']['savings'] = savings_result
                
                initial_vector = file_result['results']['savings']['solution_vector']
                vnd_result = solve_vnd(initial_vector, cost_matrix, demand, pickup, capacity, max_time_seconds=60)
                file_result['results']['vnd'] = vnd_result
            
            batch_results.append(file_result)
            
        except Exception as e:
            batch_results.append({
                'filename': filename,
                'success': False,
                'error': str(e)
            })
    
    return batch_results


def create_batch_summary(batch_results):
    """
    Tạo summary table cho batch results.
    
    Args:
        batch_results (list): Results from process_batch_files
        
    Returns:
        dict: Summary statistics
    """
    summary = {
        'total_files': len(batch_results),
        'successful': sum(1 for r in batch_results if r['success']),
        'failed': sum(1 for r in batch_results if not r['success']),
        'avg_improvement': 0.0,
        'total_cost_savings': 0,
        'total_cost_vnd': 0
    }
    
    improvements = []
    total_savings_cost = 0
    total_vnd_cost = 0
    
    for result in batch_results:
        if result['success'] and 'vnd' in result.get('results', {}):
            vnd = result['results']['vnd']
            savings = result['results'].get('savings', {})
            
            if 'improvement' in vnd:
                improvements.append(vnd['improvement'])
            
            total_savings_cost += savings.get('total_cost', 0)
            total_vnd_cost += vnd.get('total_cost', 0)
    
    if improvements:
        summary['avg_improvement'] = sum(improvements) / len(improvements)
    
    summary['total_cost_savings'] = total_savings_cost
    summary['total_cost_vnd'] = total_vnd_cost
    
    return summary
