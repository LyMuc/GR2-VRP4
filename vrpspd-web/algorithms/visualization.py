"""
Visualization Module for VRPSPD
Tạo visualization data từ cost matrix và routes bằng MDS
"""

import numpy as np
from sklearn.manifold import MDS


def generate_coordinates_from_cost_matrix(cost_matrix):
    """
    Tạo tọa độ 2D từ cost matrix bằng Multi-Dimensional Scaling (MDS).
    
    QUAN TRỌNG: Function này CHỈ dùng cho VISUALIZATION, KHÔNG ảnh hưởng đến thuật toán.
    Cost matrix gốc được giữ nguyên, chỉ tạo symmetric copy để vẽ.
    
    Args:
        cost_matrix (list): Ma trận chi phí n×n (KHÔNG bị thay đổi)
        
    Returns:
        list: Danh sách tọa độ [[x0, y0], [x1, y1], ...]
    """
    # Convert to numpy array (CREATE COPY - original unchanged!)
    distance_matrix = np.array(cost_matrix)
    
    # Make matrix symmetric (MDS requirement)
    # Use average of matrix and its transpose: (A + A^T) / 2
    # NOTE: This ONLY affects visualization coordinates, NOT algorithm results!
    distance_matrix = (distance_matrix + distance_matrix.T) / 2
    
    # Ensure non-negative distances
    distance_matrix = np.maximum(distance_matrix, 0)
    
    # Apply MDS
    mds = MDS(n_components=2, dissimilarity='precomputed', random_state=42, normalized_stress=False)
    coordinates = mds.fit_transform(distance_matrix)
    
    # Convert to list format
    coords_list = coordinates.tolist()
    
    return coords_list


def generate_route_colors(num_routes):
    """
    Tạo màu sắc khác nhau cho các tuyến đường.
    
    Args:
        num_routes (int): Số lượng tuyến
        
    Returns:
        list: Danh sách màu RGB theo format 'rgb(r, g, b)'
    """
    # Predefined colors for better contrast
    color_palette = [
        'rgb(31, 119, 180)',   # Blue
        'rgb(255, 127, 14)',   # Orange
        'rgb(44, 160, 44)',    # Green
        'rgb(214, 39, 40)',    # Red
        'rgb(148, 103, 189)',  # Purple
        'rgb(140, 86, 75)',    # Brown
        'rgb(227, 119, 194)',  # Pink
        'rgb(127, 127, 127)',  # Gray
        'rgb(188, 189, 34)',   # Olive
        'rgb(23, 190, 207)',   # Cyan
    ]
    
    # If more routes than predefined colors, generate random colors
    if num_routes <= len(color_palette):
        return color_palette[:num_routes]
    else:
        colors = color_palette.copy()
        for i in range(num_routes - len(color_palette)):
            # Generate random RGB
            r = np.random.randint(50, 200)
            g = np.random.randint(50, 200)
            b = np.random.randint(50, 200)
            colors.append(f'rgb({r}, {g}, {b})')
        return colors


def create_plotly_data(routes, cost_matrix, demand=None, pickup=None):
    """
    Tạo dữ liệu để vẽ bằng Plotly.js.
    
    Args:
        routes (list): Danh sách các tuyến [[1, 2, 3], [4, 5], ...]
        cost_matrix (list): Ma trận chi phí
        demand (list, optional): Lượng hàng giao
        pickup (list, optional): Lượng hàng nhận
        
    Returns:
        dict: Visualization data
    """
    # Generate 2D coordinates from cost matrix
    coordinates = generate_coordinates_from_cost_matrix(cost_matrix)
    
    # Depot (node 0)
    depot = {
        'x': coordinates[0][0],
        'y': coordinates[0][1]
    }
    
    # Customers (nodes 1, 2, ...)
    customers = []
    for i in range(1, len(coordinates)):
        customer = {
            'id': i,
            'x': coordinates[i][0],
            'y': coordinates[i][1]
        }
        if demand:
            customer['delivery'] = demand[i] if i < len(demand) else 0
        if pickup:
            customer['pickup'] = pickup[i] if i < len(pickup) else 0
        customers.append(customer)
    
    # Generate colors for routes
    colors = generate_route_colors(len(routes))
    
    # Routes data
    routes_data = []
    for idx, route in enumerate(routes):
        # Create path: depot -> customers -> depot
        route_with_depot = [0] + route + [0]
        path = [coordinates[node] for node in route_with_depot]
        
        routes_data.append({
            'route_number': idx + 1,
            'color': colors[idx],
            'path': path,
            'nodes': route_with_depot
        })
    
    return {
        'coordinates': coordinates,
        'depot': depot,
        'customers': customers,
        'routes': routes_data
    }


def create_plotly_figure_json(visualization_data):
    """
    Tạo JSON config cho Plotly.newPlot().
    
    Args:
        visualization_data (dict): Output từ create_plotly_data()
        
    Returns:
        dict: Plotly figure configuration
    """
    traces = []
    
    # Trace 1: Depot (red square)
    depot = visualization_data['depot']
    traces.append({
        'x': [depot['x']],
        'y': [depot['y']],
        'mode': 'markers',
        'marker': {
            'size': 20,
            'color': 'red',
            'symbol': 'square',
            'line': {'width': 2, 'color': 'darkred'}
        },
        'name': 'Depot',
        'text': ['Depot (0)'],
        'hoverinfo': 'text'
    })
    
    # Trace 2: Customers (blue circles)
    customers = visualization_data['customers']
    customer_x = [c['x'] for c in customers]
    customer_y = [c['y'] for c in customers]
    
    # Create hover text with delivery/pickup info if available
    customer_text = []
    for c in customers:
        text = f"Customer {c['id']}"
        if 'delivery' in c and 'pickup' in c:
            text += f"<br>Delivery: {c['delivery']}<br>Pickup: {c['pickup']}"
        customer_text.append(text)
    
    traces.append({
        'x': customer_x,
        'y': customer_y,
        'mode': 'markers+text',
        'marker': {
            'size': 12,
            'color': 'lightblue',
            'line': {'width': 2, 'color': 'darkblue'}
        },
        'text': [str(c['id']) for c in customers],
        'textposition': 'top center',
        'textfont': {'size': 10, 'color': 'black'},
        'name': 'Customers',
        'hovertext': customer_text,
        'hoverinfo': 'text'
    })
    
    # Traces 3+: Routes (colored lines with arrows)
    for route_data in visualization_data['routes']:
        path = route_data['path']
        route_x = [p[0] for p in path]
        route_y = [p[1] for p in path]
        
        traces.append({
            'x': route_x,
            'y': route_y,
            'mode': 'lines',
            'line': {
                'color': route_data['color'],
                'width': 2
            },
            'name': f"Route {route_data['route_number']}",
            'hoverinfo': 'name'
        })
        
        # Add arrows by adding scatter points in the middle of each segment
        # This creates a visual direction indicator
        for i in range(len(path) - 1):
            mid_x = (path[i][0] + path[i+1][0]) / 2
            mid_y = (path[i][1] + path[i+1][1]) / 2
            
            # Small marker to indicate direction
            traces.append({
                'x': [mid_x],
                'y': [mid_y],
                'mode': 'markers',
                'marker': {
                    'size': 6,
                    'color': route_data['color'],
                    'symbol': 'triangle-right'
                },
                'showlegend': False,
                'hoverinfo': 'skip'
            })
    
    # Layout
    layout = {
        'title': {
            'text': 'VRPSPD Routes Visualization',
            'font': {'size': 18}
        },
        'xaxis': {
            'title': 'X Coordinate',
            'showgrid': True,
            'zeroline': False
        },
        'yaxis': {
            'title': 'Y Coordinate',
            'showgrid': True,
            'zeroline': False,
            'scaleanchor': 'x',
            'scaleratio': 1
        },
        'hovermode': 'closest',
        'showlegend': True,
        'legend': {
            'x': 1.02,
            'y': 1,
            'xanchor': 'left'
        },
        'plot_bgcolor': 'white',
        'paper_bgcolor': 'white'
    }
    
    return {
        'data': traces,
        'layout': layout
    }
