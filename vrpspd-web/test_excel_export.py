"""
Test script cho Excel Export
"""

from algorithms.excel_export import create_excel_report
import os

# Sample results data (giống như từ solve API)
sample_results = {
    'savings': {
        'total_cost': 1234.56,
        'num_routes': 5,
        'computation_time': 0.123,
        'routes': [[0, 1, 2, 3, 0], [0, 4, 5, 0], [0, 6, 7, 8, 0]],
        'route_details': [
            {
                'route_number': 1,
                'route_with_depot': [0, 1, 2, 3, 0],
                'distance': 345.67,
                'total_delivery': 45,
                'total_pickup': 30
            },
            {
                'route_number': 2,
                'route_with_depot': [0, 4, 5, 0],
                'distance': 234.89,
                'total_delivery': 30,
                'total_pickup': 25
            },
            {
                'route_number': 3,
                'route_with_depot': [0, 6, 7, 8, 0],
                'distance': 654.00,
                'total_delivery': 55,
                'total_pickup': 40
            }
        ]
    },
    'vnd': {
        'total_cost': 1123.45,
        'num_routes': 5,
        'computation_time': 2.456,
        'improvement': 9.0,
        'routes': [[0, 1, 2, 3, 0], [0, 4, 5, 0], [0, 6, 7, 8, 0]],
        'route_details': [
            {
                'route_number': 1,
                'route_with_depot': [0, 1, 3, 2, 0],
                'distance': 320.50,
                'total_delivery': 45,
                'total_pickup': 30
            },
            {
                'route_number': 2,
                'route_with_depot': [0, 4, 5, 0],
                'distance': 234.89,
                'total_delivery': 30,
                'total_pickup': 25
            },
            {
                'route_number': 3,
                'route_with_depot': [0, 6, 7, 8, 0],
                'distance': 568.06,
                'total_delivery': 55,
                'total_pickup': 40
            }
        ]
    }
}

sample_problem_info = {
    'num_customers': 8,
    'num_vehicles': 3,
    'capacity': 100
}

if __name__ == '__main__':
    print("Testing Excel Export...")
    
    try:
        # Create Excel file
        filepath = create_excel_report(
            results=sample_results,
            problem_info=sample_problem_info,
            filename='TEST_VRPSPD_Results.xlsx'
        )
        
        print(f"✓ Excel file created successfully: {filepath}")
        
        # Check if file exists
        if os.path.exists(filepath):
            file_size = os.path.getsize(filepath)
            print(f"✓ File exists with size: {file_size} bytes")
        else:
            print("✗ File not found!")
        
        print("\nTest completed! Check the file at:", os.path.abspath(filepath))
        
    except Exception as e:
        print(f"✗ Test failed: {e}")
        import traceback
        traceback.print_exc()
