"""
Test Visualization Module
"""

from algorithms import read_vrpspd_file, solve_savings
from algorithms.visualization import create_plotly_data, create_plotly_figure_json
import json

def test_visualization():
    """Test visualization với file mẫu."""
    
    print("=" * 60)
    print("TESTING VISUALIZATION MODULE")
    print("=" * 60)
    
    # Load test data
    test_file = 'static/uploads/test_data.txt'
    
    print("\n1. Loading data...")
    cost_matrix, demand, pickup, vehicle_caps, capacity, num_vehicles = read_vrpspd_file(test_file)
    print(f"   ✓ Loaded {len(cost_matrix) - 1} customers")
    
    print("\n2. Solving with Savings algorithm...")
    result = solve_savings(cost_matrix, demand, pickup, capacity, num_vehicles)
    print(f"   ✓ Found {result['num_routes']} routes")
    print(f"   ✓ Total cost: {result['total_cost']}")
    
    print("\n3. Generating visualization data...")
    viz_data = create_plotly_data(result['routes'], cost_matrix)
    print(f"   ✓ Generated coordinates for {len(viz_data['coordinates'])} nodes")
    print(f"   ✓ Depot at: ({viz_data['depot']['x']:.2f}, {viz_data['depot']['y']:.2f})")
    print(f"   ✓ Created {len(viz_data['routes'])} route paths")
    
    print("\n4. Creating Plotly figure...")
    plotly_figure = create_plotly_figure_json(viz_data)
    print(f"   ✓ Generated {len(plotly_figure['data'])} traces")
    print(f"   ✓ Layout title: {plotly_figure['layout']['title']['text']}")
    
    # Save figure to JSON file for inspection
    output_file = 'static/uploads/test_visualization.json'
    with open(output_file, 'w') as f:
        json.dump(plotly_figure, f, indent=2)
    print(f"\n5. Saved visualization to: {output_file}")
    
    print("\n" + "=" * 60)
    print("VISUALIZATION TEST PASSED! ✓")
    print("=" * 60)
    print("\nYou can now:")
    print("  1. Start the web app: python app.py")
    print("  2. Upload test_data.txt")
    print("  3. Click 'Giải bài toán' to see visualization")

if __name__ == '__main__':
    import os
    os.makedirs('static/uploads', exist_ok=True)
    test_visualization()
