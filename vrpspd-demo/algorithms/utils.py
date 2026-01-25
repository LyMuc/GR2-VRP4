"""
Utility Functions for VRPSPD
Các hàm phụ trợ cho thuật toán
"""


def route_distance(route, cost_matrix):
    """
    Tính khoảng cách của một tuyến đường.
    
    Args:
        route (list): Danh sách các customer indices
        cost_matrix (list): Ma trận chi phí
        
    Returns:
        float: Tổng khoảng cách
    """
    if not route:
        return 0
    d = cost_matrix[0][route[0]]
    for a, b in zip(route, route[1:]):
        d += cost_matrix[a][b]
    d += cost_matrix[route[-1]][0]
    return d


def total_delivery(route, demand):
    """Tính tổng lượng hàng giao cho một tuyến."""
    return sum(demand[i] for i in route)


def feasibility_check_route(route, Q, demand, pickup):
    """
    Kiểm tra tính khả thi của một tuyến (VRPSPD).
    
    Returns:
        tuple: (feasible: bool, max_load_seen, final_load)
    """
    if not route:
        return True, 0, 0
    
    Dr = sum(demand[i] for i in route)
    load = Dr
    
    if load > Q:
        return False, load, load
    
    max_load = load
    for i in route:
        load = load - demand[i] + pickup[i]
        if load < 0:
            return False, max_load, load
        if load > max_load:
            max_load = load
        if load > Q:
            return False, max_load, load
    
    return True, max_load, load


def check_single_route_feasibility(route, Q, demand, pickup):
    """
    Kiểm tra tính hợp lệ về tải trọng cho một tuyến đường.
    
    Args:
        route (list): Danh sách các khách hàng trong một tuyến
        Q (int): Tải trọng của xe
        demand (list): Lượng hàng giao
        pickup (list): Lượng hàng nhận
        
    Returns:
        bool: True nếu tuyến đường hợp lệ
    """
    if not route:
        return True
    
    total_d = sum(demand[c] for c in route)
    total_p = sum(pickup[c] for c in route)
    
    if total_d > Q or total_p > Q:
        return False
    
    load = total_d
    for customer in route:
        load = load - demand[customer] + pickup[customer]
        if not (0 <= load <= Q):
            return False
    
    return True


def feasibility_check_and_repair(routes, Q, demand, pickup):
    """
    Kiểm tra tính hợp lệ của tất cả các tuyến.
    Nếu một tuyến không hợp lệ, thử đảo ngược nó.
    
    Returns:
        tuple: (bool, list of lists) - (is_feasible, repaired_routes)
    """
    repaired_routes = []
    for route in routes:
        if check_single_route_feasibility(route, Q, demand, pickup):
            repaired_routes.append(route)
            continue
        
        reversed_route = list(reversed(route))
        if check_single_route_feasibility(reversed_route, Q, demand, pickup):
            repaired_routes.append(reversed_route)
            continue
        
        return (False, None)
    
    return (True, repaired_routes)


def convert_routes_to_vector(routes):
    """
    Chuyển đổi danh sách tuyến sang vector representation.
    
    Args:
        routes (list of lists): [[1, 2], [3, 4]]
        
    Returns:
        list: [0, 1, 2, 0, 3, 4, 0]
    """
    solution_vector = [0]
    for route in routes:
        solution_vector.extend(route)
        solution_vector.append(0)
    return solution_vector


def convert_vector_to_routes(vector):
    """
    Chuyển đổi vector representation về danh sách tuyến.
    
    Args:
        vector (list): [0, 1, 2, 0, 3, 4, 0]
        
    Returns:
        list of lists: [[1, 2], [3, 4]]
    """
    routes = []
    current_route = []
    for node in vector[1:]:
        if node != 0:
            current_route.append(node)
        else:
            if current_route:
                routes.append(current_route)
            current_route = []
    return routes


def calculate_total_cost(solution_vector, cost_matrix):
    """
    Tính tổng chi phí cho một lời giải.
    
    Args:
        solution_vector (list): Vector representation của lời giải
        cost_matrix (list): Ma trận chi phí
        
    Returns:
        float: Tổng chi phí
    """
    routes = convert_vector_to_routes(solution_vector)
    total_cost = 0
    for route in routes:
        if not route:
            continue
        total_cost += cost_matrix[0][route[0]]
        for i in range(len(route) - 1):
            total_cost += cost_matrix[route[i]][route[i+1]]
        total_cost += cost_matrix[route[-1]][0]
    return total_cost
