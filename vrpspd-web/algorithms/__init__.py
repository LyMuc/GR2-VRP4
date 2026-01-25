"""
Algorithms Package for VRPSPD Web Application
"""

# ============================================
# STEP 1: Core Algorithm Modules
# ============================================
from .file_parser import read_vrpspd_file
from .savings import solve_savings
from .vnd import solve_vnd
from .utils import (
    route_distance,
    calculate_total_cost,
    convert_routes_to_vector,
    convert_vector_to_routes
)

# ============================================
# STEP 2: Visualization Module
# ============================================
from .visualization import (
    create_plotly_data,
    create_plotly_figure_json,
    generate_coordinates_from_cost_matrix
)

# ============================================
# STEP 1: Exports
# ============================================
__all__ = [
    # STEP 1: Core functions
    'read_vrpspd_file',
    'solve_savings',
    'solve_vnd',
    'route_distance',
    'calculate_total_cost',
    'convert_routes_to_vector',
    'convert_vector_to_routes',
    
    # STEP 2: Visualization functions
    'create_plotly_data',
    'create_plotly_figure_json',
    'generate_coordinates_from_cost_matrix'
]
