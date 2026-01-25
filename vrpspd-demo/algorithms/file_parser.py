"""
File Parser Module for VRPSPD
Đọc và parse các file txt chứa dữ liệu VRPSPD
"""


def read_vrpspd_file(file_path):
    """
    Đọc file VRPSPD và trả về các thông số cần thiết.
    
    Args:
        file_path (str): Đường dẫn đến file txt
        
    Returns:
        tuple: (cost_matrix, delivery, pickup, vehicle_capacities, capacityOfVehicle, numberOfVehicles)
    """
    with open(file_path, "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip() and "~" not in line]

    cost_matrix = []
    delivery = []
    pickup = []
    vehicle_capacities = []

    i = 0

    # 1. Read cost matrix
    if i < len(lines) and "Cost matrix" in lines[i]:
        i += 1

    # Đọc từng dòng số -> ma trận
    while i < len(lines) and "Delivery quantities" not in lines[i]:
        row = list(map(float, lines[i].split()))
        cost_matrix.append(row)
        i += 1

    # 2. Read delivery
    if i < len(lines) and "Delivery quantities" in lines[i]:
        i += 1

    if i < len(lines):
        delivery = list(map(int, map(float, lines[i].split())))
        i += 1

    # 3. Read pickup
    if i < len(lines) and "Pick-up quantities" in lines[i]:
        i += 1

    if i < len(lines):
        pickup = list(map(int, map(float, lines[i].split())))
        i += 1

    # 4. Read vehicle capacity (LIST of capacities)
    if i < len(lines) and "Vehicle capacity" in lines[i]:
        i += 1
        if i < len(lines):
            vehicle_capacities = list(map(float, lines[i].split()))
            i += 1

    # === ADD DEPOT ===
    delivery = [0] + delivery
    pickup = [0] + pickup

    # === FINAL VARIABLES ===
    numberOfVehicles = len(vehicle_capacities)

    # If all vehicles have same capacity -> use that as capacityOfVehicle
    if len(set(vehicle_capacities)) == 1:
        capacityOfVehicle = vehicle_capacities[0]
    else:
        # Different capacity vehicles - use max
        capacityOfVehicle = max(vehicle_capacities)

    return cost_matrix, delivery, pickup, vehicle_capacities, capacityOfVehicle, numberOfVehicles
