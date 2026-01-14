"""
Test script để kiểm tra các module algorithms
"""

from algorithms import read_vrpspd_file, solve_savings, solve_vnd

def test_algorithms():
    """Test với một file mẫu."""
    
    # Tạo file test đơn giản
    test_data = """Cost matrix;
0 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28
10 0 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
11 10 0 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
12 11 10 0 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
13 12 11 10 0 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
14 13 12 11 10 0 10 11 12 13 14 15 16 17 18 19 20 21 22 23
15 14 13 12 11 10 0 10 11 12 13 14 15 16 17 18 19 20 21 22
16 15 14 13 12 11 10 0 10 11 12 13 14 15 16 17 18 19 20 21
17 16 15 14 13 12 11 10 0 10 11 12 13 14 15 16 17 18 19 20
18 17 16 15 14 13 12 11 10 0 10 11 12 13 14 15 16 17 18 19
19 18 17 16 15 14 13 12 11 10 0 10 11 12 13 14 15 16 17 18
20 19 18 17 16 15 14 13 12 11 10 0 10 11 12 13 14 15 16 17
21 20 19 18 17 16 15 14 13 12 11 10 0 10 11 12 13 14 15 16
22 21 20 19 18 17 16 15 14 13 12 11 10 0 10 11 12 13 14 15
23 22 21 20 19 18 17 16 15 14 13 12 11 10 0 10 11 12 13 14
24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 0 10 11 12 13
25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 0 10 11 12
26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 0 10 11
27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 0 10
28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 11 11 10 0
~
Delivery quantities;
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
~
Pick-up quantities;
5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
~
Vehicle capacity; 
10 10 10 10 10 10 10 10 10 10 
~
"""
    
    # Lưu test file
    test_file = 'static/uploads/test_data.txt'
    with open(test_file, 'w') as f:
        f.write(test_data)
    
    print("=" * 60)
    print("TESTING VRPSPD ALGORITHMS")
    print("=" * 60)
    
    # Test file parser
    print("\n1. Testing File Parser...")
    cost_matrix, demand, pickup, vehicle_caps, capacity, num_vehicles = read_vrpspd_file(test_file)
    print(f"   ✓ Number of customers: {len(cost_matrix) - 1}")
    print(f"   ✓ Number of vehicles: {num_vehicles}")
    print(f"   ✓ Vehicle capacity: {capacity}")
    
    # Test Savings algorithm
    print("\n2. Testing Savings Algorithm...")
    savings_result = solve_savings(cost_matrix, demand, pickup, capacity, num_vehicles)
    print(f"   ✓ Total cost: {savings_result['total_cost']}")
    print(f"   ✓ Number of routes: {savings_result['num_routes']}")
    print(f"   ✓ Computation time: {savings_result['computation_time']}s")
    print(f"   ✓ Routes: {savings_result['routes']}")
    
    # Test VND algorithm
    print("\n3. Testing VND Algorithm...")
    vnd_result = solve_vnd(
        savings_result['solution_vector'],
        cost_matrix,
        demand,
        pickup,
        capacity,
        max_time_seconds=10
    )
    print(f"   ✓ Initial cost: {vnd_result['initial_cost']}")
    print(f"   ✓ Final cost: {vnd_result['total_cost']}")
    print(f"   ✓ Improvement: {vnd_result['improvement']}%")
    print(f"   ✓ Computation time: {vnd_result['computation_time']}s")
    print(f"   ✓ Routes: {vnd_result['routes']}")
    
    print("\n" + "=" * 60)
    print("ALL TESTS PASSED! ✓")
    print("=" * 60)

if __name__ == '__main__':
    import os
    os.makedirs('static/uploads', exist_ok=True)
    test_algorithms()
