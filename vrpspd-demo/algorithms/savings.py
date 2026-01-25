"""
Clarke-Wright Savings Algorithm for VRPSPD
Thuật toán Savings-based cho Vehicle Routing Problem with Simultaneous Pickup and Delivery
"""

import time
from .utils import (
    route_distance, 
    feasibility_check_route, 
    convert_routes_to_vector,
    calculate_total_cost
)


def find_route_index(routes, cust):
    """Tìm chỉ số của tuyến chứa khách hàng cust."""
    for idx, r in enumerate(routes):
        if cust in r:
            return idx
    return None


def solve_savings(cost_matrix, demand, pickup, capacity, num_vehicles):
    """
    Giải bài toán VRPSPD bằng thuật toán Clarke-Wright Savings.
    
    Args:
        cost_matrix (list): Ma trận chi phí di chuyển
        demand (list): Lượng hàng giao (bao gồm depot = 0)
        pickup (list): Lượng hàng nhận (bao gồm depot = 0)
        capacity (int): Tải trọng xe
        num_vehicles (int): Số lượng xe
        
    Returns:
        dict: {
            'routes': list of lists,
            'solution_vector': list,
            'total_cost': float,
            'num_routes': int,
            'computation_time': float,
            'route_details': list of dict
        }
    """
    start_time = time.time()
    
    # Initialize routes: one per customer
    customers = list(range(1, len(cost_matrix)))
    routes = [[i] for i in customers]
    
    # Compute savings
    savings = []
    for i in customers:
        for j in customers:
            if j <= i:
                continue
            s = cost_matrix[0][i] + cost_matrix[0][j] - cost_matrix[i][j]
            savings.append(((i, j), s))
    
    savings.sort(key=lambda x: x[1], reverse=True)
    
    # Process savings
    for (i, j), s in savings:
        ri = find_route_index(routes, i)
        rj = find_route_index(routes, j)
        
        if ri is None or rj is None or ri == rj:
            continue
        
        route_i = routes[ri]
        route_j = routes[rj]
        
        # Check endpoints only
        if not (i == route_i[0] or i == route_i[-1]):
            continue
        if not (j == route_j[0] or j == route_j[-1]):
            continue
        
        new_route = None
        
        # Try four possible concatenations
        if i == route_i[-1] and j == route_j[0]:
            cand = route_i + route_j
            feasible, _, _ = feasibility_check_route(cand, capacity, demand, pickup)
            if feasible:
                new_route = cand
        
        if new_route is None and i == route_i[0] and j == route_j[-1]:
            cand = route_j + route_i
            feasible, _, _ = feasibility_check_route(cand, capacity, demand, pickup)
            if feasible:
                new_route = cand
        
        if new_route is None and i == route_i[0] and j == route_j[0]:
            cand = list(reversed(route_i)) + route_j
            feasible, _, _ = feasibility_check_route(cand, capacity, demand, pickup)
            if feasible:
                new_route = cand
        
        if new_route is None and i == route_i[-1] and j == route_j[-1]:
            cand = route_i + list(reversed(route_j))
            feasible, _, _ = feasibility_check_route(cand, capacity, demand, pickup)
            if feasible:
                new_route = cand
        
        if new_route is not None:
            # Merge routes (remove higher index first)
            if ri > rj:
                del routes[ri]
                del routes[rj]
            else:
                del routes[rj]
                del routes[ri]
            routes.append(new_route)
    
    # Calculate results
    end_time = time.time()
    computation_time = end_time - start_time
    
    solution_vector = convert_routes_to_vector(routes)
    total_cost = calculate_total_cost(solution_vector, cost_matrix)
    
    # Prepare route details
    route_details = []
    for idx, route in enumerate(routes, 1):
        dist = route_distance(route, cost_matrix)
        feas, max_load, final_load = feasibility_check_route(route, capacity, demand, pickup)
        total_del = sum(demand[i] for i in route)
        total_pick = sum(pickup[i] for i in route)
        
        route_details.append({
            'route_number': idx,
            'route': route,
            'route_with_depot': [0] + route + [0],
            'distance': round(dist, 2),
            'feasible': feas,
            'max_load': max_load,
            'total_delivery': total_del,
            'total_pickup': total_pick
        })
    
    return {
        'routes': routes,
        'solution_vector': solution_vector,
        'total_cost': round(total_cost, 2),
        'num_routes': len(routes),
        'computation_time': round(computation_time, 4),
        'route_details': route_details,
        'exceeds_vehicles': len(routes) > num_vehicles
    }
