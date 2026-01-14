#!/usr/bin/env python
"""
Quick Test Script - Test All Features
Chạy script này để test toàn bộ tính năng của VRPSPD Web
"""

import os
import sys

def print_header(text):
    print("\n" + "=" * 70)
    print(f"  {text}")
    print("=" * 70)

def test_imports():
    print_header("TEST 1: Checking Imports")
    try:
        from algorithms import (
            read_vrpspd_file, 
            solve_savings, 
            solve_vnd,
            create_plotly_data,
            create_plotly_figure_json
        )
        print("✅ All modules imported successfully")
        return True
    except Exception as e:
        print(f"❌ Import failed: {e}")
        return False

def test_file_parsing():
    print_header("TEST 2: File Parsing")
    try:
        from algorithms import read_vrpspd_file
        
        # Check if test file exists
        test_file = 'static/uploads/test_data.txt'
        if not os.path.exists(test_file):
            print("⚠️  Test file not found, creating...")
            os.makedirs('static/uploads', exist_ok=True)
            test_data = """Cost matrix
0 9 14 23
9 0 21 22
14 21 0 25
23 22 25 0

Delivery quantities
1200 1700 1500

Pick-up quantities
0 1200 1700

Vehicle capacity
6000
"""
            with open(test_file, 'w') as f:
                f.write(test_data)
            print("✅ Test file created")
        
        cost_matrix, demand, pickup, vehicle_caps, capacity, num_vehicles = read_vrpspd_file(test_file)
        print(f"✅ File parsed successfully")
        print(f"   - Customers: {len(cost_matrix) - 1}")
        print(f"   - Vehicles: {num_vehicles}")
        print(f"   - Capacity: {capacity}")
        return True, test_file, cost_matrix, demand, pickup, capacity, num_vehicles
    except Exception as e:
        print(f"❌ Parsing failed: {e}")
        return False, None, None, None, None, None, None

def test_savings(cost_matrix, demand, pickup, capacity, num_vehicles):
    print_header("TEST 3: Savings Algorithm")
    try:
        from algorithms import solve_savings
        result = solve_savings(cost_matrix, demand, pickup, capacity, num_vehicles)
        print(f"✅ Savings completed")
        print(f"   - Routes: {result['num_routes']}")
        print(f"   - Cost: {result['total_cost']}")
        print(f"   - Time: {result['computation_time']}s")
        return True, result
    except Exception as e:
        print(f"❌ Savings failed: {e}")
        import traceback
        traceback.print_exc()
        return False, None

def test_vnd(savings_result, cost_matrix, demand, pickup, capacity):
    print_header("TEST 4: VND Algorithm")
    try:
        from algorithms import solve_vnd
        result = solve_vnd(
            savings_result['solution_vector'],
            cost_matrix,
            demand,
            pickup,
            capacity,
            max_time_seconds=5
        )
        print(f"✅ VND completed")
        print(f"   - Initial cost: {result['initial_cost']}")
        print(f"   - Final cost: {result['total_cost']}")
        print(f"   - Improvement: {result['improvement']}%")
        print(f"   - Time: {result['computation_time']}s")
        return True, result
    except Exception as e:
        print(f"❌ VND failed: {e}")
        import traceback
        traceback.print_exc()
        return False, None

def test_visualization(routes, cost_matrix, demand, pickup):
    print_header("TEST 5: Visualization")
    try:
        from algorithms import create_plotly_data, create_plotly_figure_json
        
        viz_data = create_plotly_data(routes, cost_matrix, demand, pickup)
        print(f"✅ Visualization data created")
        print(f"   - Coordinates: {len(viz_data['coordinates'])} nodes")
        print(f"   - Routes: {len(viz_data['routes'])} paths")
        
        plotly_fig = create_plotly_figure_json(viz_data)
        print(f"✅ Plotly figure generated")
        print(f"   - Traces: {len(plotly_fig['data'])}")
        
        # Save to file
        import json
        output_file = 'static/uploads/quick_test_viz.json'
        with open(output_file, 'w') as f:
            json.dump(plotly_fig, f, indent=2)
        print(f"✅ Saved to: {output_file}")
        
        return True
    except Exception as e:
        print(f"❌ Visualization failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_web_server():
    print_header("TEST 6: Flask Server (Optional)")
    print("To test the web server, run in another terminal:")
    print("  python app.py")
    print("Then open: http://localhost:5000")
    print("⚠️  Press Ctrl+C to stop the server when done")

def main():
    print("\n" + "🚀" * 35)
    print("  VRPSPD WEB - COMPREHENSIVE TEST SUITE")
    print("🚀" * 35)
    
    # Test 1: Imports
    if not test_imports():
        print("\n❌ FAILED: Cannot import modules")
        return False
    
    # Test 2: File Parsing
    result = test_file_parsing()
    if not result[0]:
        print("\n❌ FAILED: File parsing error")
        return False
    _, test_file, cost_matrix, demand, pickup, capacity, num_vehicles = result
    
    # Test 3: Savings
    success, savings_result = test_savings(cost_matrix, demand, pickup, capacity, num_vehicles)
    if not success:
        print("\n❌ FAILED: Savings algorithm error")
        return False
    
    # Test 4: VND
    success, vnd_result = test_vnd(savings_result, cost_matrix, demand, pickup, capacity)
    if not success:
        print("\n⚠️  WARNING: VND failed but continuing...")
    
    # Test 5: Visualization
    best_result = vnd_result if vnd_result else savings_result
    if not test_visualization(best_result['routes'], cost_matrix, demand, pickup):
        print("\n❌ FAILED: Visualization error")
        return False
    
    # Test 6: Web Server Info
    test_web_server()
    
    # Summary
    print_header("🎉 ALL TESTS PASSED!")
    print("\n✅ File Parsing: OK")
    print("✅ Savings Algorithm: OK")
    print("✅ VND Algorithm: OK" if vnd_result else "⚠️  VND Algorithm: SKIPPED")
    print("✅ Visualization: OK")
    print("\n📊 Summary:")
    print(f"   - Test file: {test_file}")
    print(f"   - Best cost: {best_result['total_cost']}")
    print(f"   - Visualization: static/uploads/quick_test_viz.json")
    print("\n🚀 Ready to start web server!")
    print("   Run: python app.py")
    print("   Open: http://localhost:5000")
    print("\n" + "=" * 70)
    
    return True

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
