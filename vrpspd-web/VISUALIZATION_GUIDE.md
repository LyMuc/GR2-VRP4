# 📊 Visualization Implementation Guide

## ✅ Đã hoàn thành

### 1. **Backend Visualization Module** (`algorithms/visualization.py`)

#### Chức năng chính:
- ✅ **MDS (Multi-Dimensional Scaling)**: Chuyển cost matrix thành tọa độ 2D
- ✅ **Color Generation**: Tạo màu sắc đẹp cho từng route
- ✅ **Plotly Data Structure**: Tạo cấu trúc dữ liệu cho Plotly.js
- ✅ **Route Paths**: Tính toán đường đi cho từng tuyến

#### Functions:
```python
generate_coordinates_from_cost_matrix(cost_matrix)  # MDS transformation
generate_route_colors(num_routes)                   # Color palette
create_plotly_data(routes, cost_matrix, demand, pickup)  # Data prep
create_plotly_figure_json(visualization_data)       # Plotly config
```

### 2. **API Integration** (`app.py`)

API `/api/solve` bây giờ trả về thêm:
```json
{
  "success": true,
  "results": {...},
  "problem_info": {...},
  "visualization": {
    "data": [...],     // Plotly traces
    "layout": {...}    // Plotly layout config
  }
}
```

### 3. **Frontend Rendering** (`static/js/app.js`)

Function `renderVisualization(plotlyFigure)`:
- Nhận JSON config từ backend
- Dùng `Plotly.newPlot()` để vẽ
- Responsive và interactive

### 4. **Visual Elements**

#### Depot (Kho):
- 🟥 Red square marker (size 20)
- Label: "Depot (0)"

#### Customers (Khách hàng):
- 🔵 Light blue circles (size 12)
- Labels: Customer ID (1, 2, 3, ...)
- Tooltips: Customer info + Delivery/Pickup quantities

#### Routes (Tuyến đường):
- 🎨 Colored lines (mỗi route màu khác nhau)
- 🔺 Direction indicators (small triangles)
- Line width: 2px

### 5. **Color Palette**

10 màu predefined cho routes:
- Blue, Orange, Green, Red, Purple
- Brown, Pink, Gray, Olive, Cyan

Nếu > 10 routes: random colors được generate

## 📖 Cách sử dụng

### Test Visualization:
```bash
python test_visualization.py
```

Output:
- Generates coordinates using MDS
- Creates Plotly figure
- Saves to `static/uploads/test_visualization.json`

### Web Application:
1. Start server: `python app.py`
2. Upload `.txt` file
3. Select algorithm (Savings/VND)
4. Click "Giải bài toán"
5. **Visualization tự động hiển thị**

## 🎨 Visualization Features

### Interactive:
- ✅ Zoom in/out
- ✅ Pan (drag to move)
- ✅ Hover to see details
- ✅ Toggle routes on/off (click legend)
- ✅ Download as PNG

### Responsive:
- ✅ Auto-resize với window
- ✅ Mobile-friendly
- ✅ Equal axis scaling (x:y = 1:1)

### Informative:
- ✅ Customer IDs displayed
- ✅ Route numbers in legend
- ✅ Delivery/Pickup in tooltips
- ✅ Direction indicators

## 🔧 Customization

### Thay đổi màu routes:
Edit `generate_route_colors()` in `visualization.py`

### Thay đổi marker sizes:
Edit `create_plotly_figure_json()`:
```python
'marker': {
    'size': 20,  # depot size
    'size': 12,  # customer size
}
```

### Thay đổi line width:
```python
'line': {
    'width': 3,  # thicker lines
}
```

## 📊 Technical Details

### MDS Algorithm:
- **Input**: Distance/cost matrix (n×n)
- **Output**: 2D coordinates that preserve distances
- **Library**: scikit-learn
- **Parameters**: 
  - `n_components=2` (2D space)
  - `dissimilarity='precomputed'` (use provided matrix)
  - `random_state=42` (reproducible)

### Plotly Traces:
1. **Depot trace**: Scatter (1 point)
2. **Customers trace**: Scatter (n-1 points)
3. **Route traces**: Lines (k routes)
4. **Direction indicators**: Scatter (small markers)

Total traces = 2 + k + (number of segments)

## 🐛 Troubleshooting

### Problem: No visualization shown
- Check console for errors
- Verify `result.visualization` in network tab
- Ensure Plotly.js loaded: check `<script>` tag

### Problem: Weird coordinate layout
- MDS needs symmetric cost matrix
- Check cost_matrix format
- Increase MDS iterations if needed

### Problem: Colors look bad
- Edit `color_palette` in `generate_route_colors()`
- Use professional color schemes (ColorBrewer)

### Problem: Too slow
- MDS is O(n²) - slow for large n
- Consider pre-computing coordinates
- Cache visualization data

## 📈 Performance

### MDS Complexity:
- Small (< 50 nodes): Instant
- Medium (50-200): < 1 second
- Large (> 200): Few seconds

### Rendering:
- Plotly.js handles thousands of points
- Typical VRPSPD: 20-100 customers → Fast

## 🔜 Future Enhancements

Possible improvements:
- [ ] Animation of route construction
- [ ] 3D visualization option
- [ ] Custom marker icons (truck, warehouse)
- [ ] Export routes as image/PDF
- [ ] Real map integration (Google Maps API)
- [ ] Time windows visualization
- [ ] Load progression along route

---

**Status**: ✅ Fully implemented and tested  
**Version**: 1.0.0  
**Date**: January 2026
