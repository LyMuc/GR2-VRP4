# VRPSPD Web Application - Complete!

## Đã hoàn thành:

### Bước 1: Project Setup & Algorithm Refactoring 
- Flask backend structure
- Algorithm modules (Savings, VND)
- File parser
- Basic UI

### Bước 2: Visualization 
-  MDS transformation
-  Plotly.js interactive graphs
-  10 color-coded routes
-  Fullscreen modal
-  Collapsible route details

### Bước 3: Excel Export 
-  Single file Excel export
-  3 sheets: Summary, Route Details, Comparison
-  Professional formatting
-  Auto download

### Bước 4: Batch Processing 
-  Multiple file upload
-  Batch solve với progress tracking
-  Batch results table
-  Master Excel export (3 sheets)
-  Summary statistics
-  Top performers ranking

---

## Cách sử dụng:

### Server đang chạy tại:
```
http://127.0.0.1:5000
http://192.168.1.9:5000
```

### Mode 1: Single File Processing

1. **Upload File**
   - Click "Chọn file dữ liệu (.txt)"
   - Select file .txt (format VRPSPD)
   - Problem info sẽ hiển thị

2. **Chọn Algorithm**
   - ☑️ Savings-based (Clarke-Wright)
   - ☑️ Savings + VND (tốt hơn, lâu hơn)

3. **Giải**
   - Click "Giải bài toán"
   - Xem kết quả trong bảng
   - Xem visualization (có thể phóng to fullscreen)

4. **Xuất Excel**
   - Click "Xuất Excel"
   - File tự động download

### Mode 2: Batch Processing

1. **Switch to Batch Mode**
   - Click button "Batch" ở trên cùng

2. **Upload Multiple Files**
   - Click "Chọn nhiều file (.txt)"
   - Select nhiều files (Ctrl+Click hoặc Shift+Click)
   - Danh sách files hiện ra

3. **Chọn Algorithms**
   - Giống như single mode
   - Apply cho tất cả files

4. **Giải Hàng Loạt**
   - Click "Giải hàng loạt"
   - Xem progress indicator
   - Kết quả hiện trong bảng:
     * Summary statistics
     * Chi tiết từng file
     * Status (Success/Failed)
     * Improvement %

5. **Xuất Master Excel**
   - Click "Xuất Master Excel"
   - File có 3 sheets:
     * Summary: Tổng hợp
     * Comparison: So sánh chi tiết
     * Best Results: Top 10 performers (medal system)

---

## Project Structure:

```
vrpspd-web/
├── app.py                      # Flask application (286 lines)
├── requirements.txt            # Dependencies
│
├── algorithms/
│   ├── __init__.py
│   ├── file_parser.py         # Parse VRPSPD files
│   ├── savings.py             # Clarke-Wright algorithm
│   ├── vnd.py                 # Variable Neighborhood Descent
│   ├── utils.py               # Helper functions
│   ├── visualization.py       # MDS + Plotly
│   ├── excel_export.py        # Single file Excel
│   ├── batch_processor.py     # Batch processing logic
│   └── batch_excel_export.py  # Master Excel generation
│
├── templates/
│   └── index.html             # Main UI (198 lines)
│
├── static/
│   ├── css/
│   │   └── style.css          # Custom styles
│   ├── js/
│   │   └── app.js             # Frontend logic (689 lines)
│   └── uploads/               # Uploaded files
│
└── tests/
    ├── test_algorithms.py
    ├── test_visualization.py
    ├── test_excel_export.py
    └── test_batch_excel.py
```

---

## 🔧 API Endpoints:

### Single Mode:
- `POST /api/upload` - Upload file
- `POST /api/solve` - Solve VRPSPD
- `POST /api/export-excel` - Export Excel

### Batch Mode:
- `POST /api/batch-upload` - Upload multiple files
- `POST /api/batch-solve` - Batch processing
- `POST /api/batch-export-excel` - Export Master Excel

---

## Excel Format:

### Single File Export:
1. **Summary Sheet**: Problem info + Results comparison
2. **Route Details Sheet**: Chi tiết từng tuyến
3. **Comparison Sheet**: Savings vs VND (nếu chạy cả 2)

### Batch Export:
1. **Summary Sheet**: Total statistics + Cost summary
2. **Comparison Sheet**: All files comparison table
3. **Best Results Sheet**: Top 10 ranked by improvement (medals)

---

## Features:

### UI/UX:
-  Bootstrap 5 responsive design
-  Font Awesome icons
-  Loading indicators
-  Toast notifications
-  Fullscreen visualization modal
-  Collapsible sections
-  Mode switching (Single/Batch)
-  File list preview

### Visualization:
-  Interactive Plotly graphs
-  10 color-coded routes
-  Hover tooltips
-  Zoom & Pan
-  Direction indicators (arrows)
-  Depot highlighted
-  Fullscreen mode (ESC to close)

### Algorithms:
-  Clarke-Wright Savings heuristic
-  VND with 5 neighborhood structures:
  - Swap(1,1) inter-route
  - Relocate inter-route
  - Shift(2,0) inter-route
  - Swap(2,1) inter-route
  - Swap(2,2) inter-route
-  Intra-route optimization
-  Feasibility checking (capacity + pickup/delivery)

---

## 🧪 Testing:

### Test Files Available:
```
static/uploads/test_data.txt
static/uploads/Mitra-2-16.txt
static/uploads/Mitra-1-01.txt
static/uploads/60_6_10.txt
```

### Test Scripts:
```bash
# Test algorithms
python test_algorithms.py

# Test visualization
python test_visualization.py

# Test Excel export
python test_excel_export.py

# Test batch Excel
python test_batch_excel.py
```

---


