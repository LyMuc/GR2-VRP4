"""
Variable Neighborhood Descent (VND) Algorithm for VRPSPD
Thuật toán VND hai cấp (Inter-Intra) để cải thiện lời giải
"""

import time
from .utils import (
    convert_vector_to_routes,
    convert_routes_to_vector,
    calculate_total_cost,
    route_distance,
    feasibility_check_and_repair
)


# ==================== NEIGHBORHOOD MOVES ====================

def swap_one_one_inter_route(solution_vector, route_idx_A, route_idx_B, cust_idx_A, cust_idx_B):
    """Swap(1,1): Tráo đổi 1 khách hàng giữa 2 tuyến."""
    routes = convert_vector_to_routes(solution_vector)
    
    if not (0 <= route_idx_A < len(routes) and 0 <= route_idx_B < len(routes)):
        return None
    
    route_A = routes[route_idx_A]
    route_B = routes[route_idx_B]
    
    if not (0 <= cust_idx_A < len(route_A) and 0 <= cust_idx_B < len(route_B)):
        return None
    
    route_A[cust_idx_A], route_B[cust_idx_B] = route_B[cust_idx_B], route_A[cust_idx_A]
    
    return convert_routes_to_vector(routes)


def relocate_inter_route(solution_vector, route_idx_from, route_idx_to, i, j):
    """Shift(1,0): Di chuyển 1 khách hàng từ tuyến này sang tuyến khác."""
    routes = convert_vector_to_routes(solution_vector)
    
    if not (0 <= route_idx_from < len(routes) and 0 <= route_idx_to < len(routes)):
        return None
    
    route_from = routes[route_idx_from]
    route_to = routes[route_idx_to]
    
    if len(route_from) <= 1:
        return None
    
    if not (0 <= i < len(route_from) and 0 <= j <= len(route_to)):
        return None
    
    customer_to_move = route_from.pop(i)
    route_to.insert(j, customer_to_move)
    
    if not route_from:
        routes.pop(route_idx_from)
    
    return convert_routes_to_vector(routes)


def shift_two_zero_inter_route(solution_vector, route_idx_from, route_idx_to, block_start_idx, insert_idx):
    """Shift(2,0): Di chuyển khối 2 khách hàng từ tuyến này sang tuyến khác."""
    routes = convert_vector_to_routes(solution_vector)
    
    if not (0 <= route_idx_from < len(routes) and 0 <= route_idx_to < len(routes) and route_idx_from != route_idx_to):
        return None
    
    route_from = routes[route_idx_from]
    route_to = routes[route_idx_to]
    
    if len(route_from) < 2 or not (0 <= block_start_idx < len(route_from) - 1):
        return None
    
    if not (0 <= insert_idx <= len(route_to)):
        return None
    
    block_to_move = route_from[block_start_idx : block_start_idx + 2]
    del route_from[block_start_idx : block_start_idx + 2]
    
    new_route_to = route_to[:insert_idx] + block_to_move + route_to[insert_idx:]
    routes[route_idx_to] = new_route_to
    
    if not route_from:
        final_routes = [r for r in routes if r]
        return convert_routes_to_vector(final_routes)
    else:
        routes[route_idx_from] = route_from
        return convert_routes_to_vector(routes)


def swap_two_one_inter_route(solution_vector, route_idx_A, route_idx_B, block_start_idx_A, cust_idx_B):
    """Swap(2,1): Tráo đổi khối 2 khách hàng với 1 khách hàng."""
    routes = convert_vector_to_routes(solution_vector)
    
    if not (0 <= route_idx_A < len(routes) and 0 <= route_idx_B < len(routes) and route_idx_A != route_idx_B):
        return None
    
    route_A = routes[route_idx_A]
    route_B = routes[route_idx_B]
    
    if len(route_A) < 2 or not (0 <= block_start_idx_A < len(route_A) - 1):
        return None
    
    if not (0 <= cust_idx_B < len(route_B)):
        return None
    
    block_from_A = route_A[block_start_idx_A : block_start_idx_A + 2]
    customer_from_B = route_B[cust_idx_B]
    
    new_route_A = route_A[:block_start_idx_A] + [customer_from_B] + route_A[block_start_idx_A + 2:]
    new_route_B = route_B[:cust_idx_B] + block_from_A + route_B[cust_idx_B + 1:]
    
    routes[route_idx_A] = new_route_A
    routes[route_idx_B] = new_route_B
    
    return convert_routes_to_vector(routes)


def swap_two_two_inter_route(solution_vector, route_idx_A, route_idx_B, block_start_idx_A, block_start_idx_B):
    """Swap(2,2): Tráo đổi khối 2 khách hàng với khối 2 khách hàng."""
    routes = convert_vector_to_routes(solution_vector)
    
    if not (0 <= route_idx_A < len(routes) and 0 <= route_idx_B < len(routes) and route_idx_A != route_idx_B):
        return None
    
    route_A = routes[route_idx_A]
    route_B = routes[route_idx_B]
    
    if len(route_A) < 2 or not (0 <= block_start_idx_A < len(route_A) - 1):
        return None
    
    if len(route_B) < 2 or not (0 <= block_start_idx_B < len(route_B) - 1):
        return None
    
    block_from_A = route_A[block_start_idx_A : block_start_idx_A + 2]
    block_from_B = route_B[block_start_idx_B : block_start_idx_B + 2]
    
    new_route_A = route_A[:block_start_idx_A] + block_from_B + route_A[block_start_idx_A + 2:]
    new_route_B = route_B[:block_start_idx_B] + block_from_A + route_B[block_start_idx_B + 1:]
    
    routes[route_idx_A] = new_route_A
    routes[route_idx_B] = new_route_B
    
    return convert_routes_to_vector(routes)


# ==================== INTRA-ROUTE VND ====================

def vnd_intra_search(solution_vector, cost_matrix, capacity, demand, pickup):
    """
    VND cục bộ trên từng tuyến (intra-route).
    """
    current_routes = convert_vector_to_routes(solution_vector)
    improved_routes = []
    
    intra_neighborhoods = [
        lambda r, i, j: (r[:i] + [r[j]] + r[i+1:j] + [r[i]] + r[j+1:]),  # General Swap
        lambda r, i, j: (r[:i] + r[i+1:j] + [r[i]] + r[j:]),  # Relocate
        lambda r, i, j: (r[:i] + r[i+2:j] + [r[i], r[i+1]] + r[j:]),  # Block Insertion
        lambda r, i, j: (r[:i+1] + r[i+1:j+1][::-1] + r[j+1:]),  # 2-Opt
    ]
    
    for route in current_routes:
        if len(route) <= 1:
            improved_routes.append(route)
            continue
        
        best_route = route
        best_route_cost = route_distance(best_route, cost_matrix)
        
        k = 0
        while k < len(intra_neighborhoods):
            improvement_found = False
            
            if k == 0:  # General Swap
                neighbors_gen = (intra_neighborhoods[k](best_route, i, j) 
                               for i in range(len(best_route)) 
                               for j in range(i + 1, len(best_route)))
            elif k == 1:  # Relocate
                neighbors_gen = (intra_neighborhoods[k](best_route, i, j) 
                               for i in range(len(best_route)) 
                               for j in range(len(best_route) + 1) 
                               if i != j and i != j-1)
            elif k == 2:  # Block Insertion
                if len(best_route) < 3:
                    neighbors_gen = iter([])
                else:
                    neighbors_gen = (intra_neighborhoods[k](best_route, i, j) 
                                   for i in range(len(best_route)-1) 
                                   for j in range(len(best_route)-1) 
                                   if j != i and j != i+1)
            elif k == 3:  # 2-Opt
                if len(best_route) < 3:
                    neighbors_gen = iter([])
                else:
                    neighbors_gen = (intra_neighborhoods[k](best_route, i, j) 
                                   for i in range(len(best_route) - 1) 
                                   for j in range(i + 2, len(best_route)))
            
            for neighbor_route in neighbors_gen:
                is_feasible, _ = feasibility_check_and_repair([neighbor_route], capacity, demand, pickup)
                
                if is_feasible:
                    neighbor_cost = route_distance(neighbor_route, cost_matrix)
                    if neighbor_cost < best_route_cost:
                        best_route = neighbor_route
                        best_route_cost = neighbor_cost
                        improvement_found = True
                        break
            
            if improvement_found:
                k = 0
            else:
                k += 1
        
        improved_routes.append(best_route)
    
    return convert_routes_to_vector(improved_routes)


# ==================== MAIN VND ALGORITHM ====================

def solve_vnd(initial_vector, cost_matrix, demand, pickup, capacity, max_time_seconds=60):
    """
    Giải bài toán VRPSPD bằng thuật toán VND hai cấp.
    
    Args:
        initial_vector (list): Lời giải ban đầu (từ Savings)
        cost_matrix (list): Ma trận chi phí
        demand (list): Lượng hàng giao
        pickup (list): Lượng hàng nhận
        capacity (int): Tải trọng xe
        max_time_seconds (int): Thời gian chạy tối đa
        
    Returns:
        dict: {
            'routes': list of lists,
            'solution_vector': list,
            'total_cost': float,
            'num_routes': int,
            'computation_time': float,
            'initial_cost': float,
            'improvement': float,
            'route_details': list of dict
        }
    """
    start_time = time.time()
    
    current_vector = initial_vector
    current_cost = calculate_total_cost(current_vector, cost_matrix)
    initial_cost = current_cost
    
    best_vector = current_vector
    best_cost = current_cost
    
    # Inter-route neighborhoods (Ordering 2)
    inter_neighborhoods = [
        # Swap(1,1)
        lambda vec: (swap_one_one_inter_route(vec, r_A_idx, r_B_idx, i, j) 
                    for r_A_idx, r_A in enumerate(convert_vector_to_routes(vec)) 
                    for r_B_idx, r_B in enumerate(convert_vector_to_routes(vec)) 
                    if r_A_idx < r_B_idx 
                    for i in range(len(r_A)) 
                    for j in range(len(r_B))),
        # Shift(1,0)
        lambda vec: (relocate_inter_route(vec, r_from_idx, r_to_idx, i, j) 
                    for r_from_idx, r_from in enumerate(convert_vector_to_routes(vec)) 
                    for r_to_idx, r_to in enumerate(convert_vector_to_routes(vec)) 
                    if r_from_idx != r_to_idx 
                    for i in range(len(r_from)) 
                    for j in range(len(r_to) + 1)),
        # Shift(2,0)
        lambda vec: (shift_two_zero_inter_route(vec, r_from_idx, r_to_idx, i, j) 
                    for r_from_idx, r_from in enumerate(convert_vector_to_routes(vec)) 
                    if len(r_from) >= 2 
                    for r_to_idx, r_to in enumerate(convert_vector_to_routes(vec)) 
                    if r_from_idx != r_to_idx 
                    for i in range(len(r_from) - 1) 
                    for j in range(len(r_to) + 1)),
        # Swap(2,1)
        lambda vec: (swap_two_one_inter_route(vec, r_A_idx, r_B_idx, i, j) 
                    for r_A_idx, r_A in enumerate(convert_vector_to_routes(vec)) 
                    if len(r_A) >= 2 
                    for r_B_idx, r_B in enumerate(convert_vector_to_routes(vec)) 
                    if r_A_idx != r_B_idx 
                    for i in range(len(r_A) - 1) 
                    for j in range(len(r_B))),
        # Swap(2,2)
        lambda vec: (swap_two_two_inter_route(vec, r_A_idx, r_B_idx, i, j) 
                    for r_A_idx, r_A in enumerate(convert_vector_to_routes(vec)) 
                    if len(r_A) >= 2 
                    for r_B_idx, r_B in enumerate(convert_vector_to_routes(vec)) 
                    if r_A_idx < r_B_idx and len(r_B) >= 2 
                    for i in range(len(r_A) - 1) 
                    for j in range(len(r_B) - 1)),
    ]
    
    k = 0
    while k < len(inter_neighborhoods) and (time.time() - start_time) < max_time_seconds:
        improvement_found = False
        neighbor_generator = inter_neighborhoods[k](current_vector)
        
        best_neighbor_in_k_vector = None
        best_neighbor_in_k_cost = current_cost
        
        for neighbor_vector in neighbor_generator:
            if (time.time() - start_time) > max_time_seconds:
                break
            if neighbor_vector is None:
                continue
            
            neighbor_routes = convert_vector_to_routes(neighbor_vector)
            is_feasible, repaired_routes = feasibility_check_and_repair(neighbor_routes, capacity, demand, pickup)
            
            if is_feasible:
                intensified_vector = vnd_intra_search(convert_routes_to_vector(repaired_routes), 
                                                     cost_matrix, capacity, demand, pickup)
                intensified_cost = calculate_total_cost(intensified_vector, cost_matrix)
                
                if intensified_cost < best_neighbor_in_k_cost:
                    best_neighbor_in_k_vector = intensified_vector
                    best_neighbor_in_k_cost = intensified_cost
        
        if best_neighbor_in_k_vector is not None:
            current_vector = best_neighbor_in_k_vector
            current_cost = best_neighbor_in_k_cost
            
            if current_cost < best_cost:
                best_vector = current_vector
                best_cost = current_cost
            
            improvement_found = True
        
        if improvement_found:
            k = 0
        else:
            k += 1
    
    # Calculate results
    end_time = time.time()
    computation_time = end_time - start_time
    
    routes = convert_vector_to_routes(best_vector)
    improvement = ((initial_cost - best_cost) / initial_cost * 100) if initial_cost > 0 else 0
    
    # Prepare route details
    route_details = []
    for idx, route in enumerate(routes, 1):
        dist = route_distance(route, cost_matrix)
        total_del = sum(demand[i] for i in route)
        total_pick = sum(pickup[i] for i in route)
        
        route_details.append({
            'route_number': idx,
            'route': route,
            'route_with_depot': [0] + route + [0],
            'distance': round(dist, 2),
            'total_delivery': total_del,
            'total_pickup': total_pick
        })
    
    return {
        'routes': routes,
        'solution_vector': best_vector,
        'total_cost': round(best_cost, 2),
        'num_routes': len(routes),
        'computation_time': round(computation_time, 4),
        'initial_cost': round(initial_cost, 2),
        'improvement': round(improvement, 2),
        'route_details': route_details
    }
