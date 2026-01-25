# TÓM TẮT HỆ THỐNG - VRPSPD WEB APPLICATION
## Tài liệu chuẩn bị slide thuyết trình

---

## 1. TỔNG QUAN HỆ THỐNG

### Giới thiệu
**Hệ thống Web giải bài toán VRPSPD** (Vehicle Routing Problem with Simultaneous Pickup and Delivery)

### Mục tiêu
- Giải bài toán tối ưu hóa lộ trình vận chuyển
- Giao diện web thân thiện, dễ sử dụng
- Hỗ trợ xử lý đơn lẻ và hàng loạt
- Trực quan hóa kết quả trên bản đồ
- Xuất báo cáo Excel chuyên nghiệp

---

## 2. CHỨC NĂNG HỆ THỐNG

### 2.1. Xử lý File Đơn (Single File Processing)
**Input:**
- File dữ liệu định dạng .txt
- Ma trận chi phí, Delivery, Pickup, Vehicle capacity

**Process:**
- Upload file lên server
- Parse và validate dữ liệu
- Hiển thị thông tin bài toán (số khách hàng, số xe, tải trọng)

**Output:**
- Thông tin bài toán được hiển thị
- Sẵn sàng cho bước giải

### 2.2. Giải Thuật Toán (Algorithm Solving)
**Thuật toán hỗ trợ:**
1. **Savings-based Algorithm** (Clarke-Wright)
   - Thuật toán tham lam
   - Kết hợp các tuyến dựa trên tiết kiệm chi phí
   - Thời gian: O(n²)

2. **Variable Neighborhood Descent (VND)**
   - Tối ưu hóa local search
   - 4 neighborhoods: Swap, 2-opt, Relocate, Cross-exchange
   - Cải thiện lời giải từ Savings

**Kết quả:**
- Tổng chi phí (Total Cost)
- Số lượng tuyến (Number of Routes)
- Chi tiết từng tuyến (Route Details)
- Thời gian tính toán (Computation Time)
- % cải thiện (khi chạy cả 2 thuật toán)

### 2.3. Trực Quan Hóa (Visualization)
**Công nghệ:**
- Plotly.js - Interactive charts

**Tính năng:**
- Hiển thị bản đồ 2D các điểm khách hàng
- Các tuyến đường với màu sắc khác nhau
- Depot (kho) được đánh dấu rõ ràng
- Hover để xem thông tin chi tiết
- Chế độ toàn màn hình (Fullscreen)
- Responsive, tương tác mượt mà

**Thông tin hiển thị:**
- Vị trí các khách hàng
- Lộ trình di chuyển từng xe
- Delivery/Pickup tại mỗi điểm
- Tải trọng tích lũy

### 2.4. Xuất Báo Cáo Excel (Excel Export)
**File đơn:**
- **Summary Sheet**: Thông tin tổng quan
- **Savings Results**: Kết quả thuật toán Savings
- **VND Results**: Kết quả thuật toán VND
- **Comparison**: So sánh 2 thuật toán

**Định dạng:**
- Headers màu sắc
- Borders, alignment
- Conditional formatting
- Auto-width columns
- Timestamp trong tên file

### 2.5. Xử Lý Hàng Loạt (Batch Processing)
**Input:**
- Nhiều file .txt cùng lúc (multiple file upload)

**Process:**
- Upload tất cả file
- Giải từng file tuần tự
- Hiển thị progress (X/Y files)
- Tổng hợp kết quả

**Output:**
- Bảng tổng hợp tất cả file
- Thống kê: Total files, Success, Failed
- Average improvement
- Master Excel với tất cả kết quả

**Master Excel:**
- **Summary Sheet**: Thống kê tổng quan
- **Comparison Sheet**: So sánh tất cả file
  - File name, Customers, Vehicles
  - Savings cost, VND cost
  - Improvement %
  - Computation time

---

## 3. CÔNG NGHỆ SỬ DỤNG

### 3.1. Backend
**Framework:**
- **Flask 3.0.3** - Python web framework
  - Lightweight, flexible
  - RESTful API design
  - 6 API endpoints

**Ngôn ngữ:**
- **Python 3.13**

**Thư viện tính toán:**
- **NumPy 2.1.3** - Ma trận, tính toán số
- **SciPy 1.14.1** - Thuật toán tối ưu
- **scikit-learn 1.5.2** - MDS, distance matrix

**Thư viện xử lý dữ liệu:**
- **Pandas 2.2.3** - DataFrame, data manipulation
- **openpyxl 3.1.5** - Excel file generation

### 3.2. Frontend
**Framework CSS:**
- **Bootstrap 5.3.0**
  - Responsive grid system
  - Pre-built components
  - Mobile-first design

**JavaScript Libraries:**
- **Plotly.js 2.27.0** - Interactive visualization
  - 2D scatter plots
  - Line charts for routes
  - Hover tooltips
  - Fullscreen mode

**Icons:**
- **Font Awesome 6.0** - UI icons

**Công nghệ:**
- **Vanilla JavaScript** - DOM manipulation, AJAX
- **CSS3** - Custom styling, animations
- **HTML5** - Semantic markup

### 3.3. API Architecture
**Design Pattern:**
- RESTful API
- JSON request/response
- Stateless communication

**Endpoints:**
1. `GET /` - Trang chủ
2. `POST /api/upload` - Upload file đơn
3. `POST /api/solve` - Giải thuật toán
4. `POST /api/export-excel` - Xuất Excel đơn
5. `POST /api/batch-upload` - Upload nhiều file
6. `POST /api/batch-solve` - Giải hàng loạt
7. `POST /api/batch-export-excel` - Xuất Master Excel

---

## 4. THIẾT KẾ HỆ THỐNG

### 4.1. Kiến Trúc Tổng Thể
```
┌─────────────────────────────────────────────┐
│         PRESENTATION LAYER                  │
│   ┌─────────────────────────────────┐      │
│   │  Web Browser (Client)           │      │
│   │  - Bootstrap 5 UI               │      │
│   │  - Plotly.js Visualization      │      │
│   │  - JavaScript Logic             │      │
│   └─────────────────────────────────┘      │
└─────────────────┬───────────────────────────┘
                  │ HTTP/JSON
                  │
┌─────────────────▼───────────────────────────┐
│         APPLICATION LAYER                   │
│   ┌─────────────────────────────────┐      │
│   │  Flask Web Server               │      │
│   │  - Route Handlers               │      │
│   │  - Request/Response             │      │
│   │  - File Management              │      │
│   └─────────────────────────────────┘      │
└─────────────────┬───────────────────────────┘
                  │
┌─────────────────▼───────────────────────────┐
│         BUSINESS LOGIC LAYER                │
│   ┌──────────────┬──────────────────┐      │
│   │ Algorithms   │ Services         │      │
│   │ - Savings    │ - File Parser    │      │
│   │ - VND        │ - Visualization  │      │
│   │ - Utils      │ - Excel Export   │      │
│   │              │ - Batch Processor│      │
│   └──────────────┴──────────────────┘      │
└─────────────────────────────────────────────┘
```

### 4.2. Cấu Trúc Module

#### Module 1: Core Algorithms (`algorithms/`)
**file_parser.py** (80 lines)
- `read_vrpspd_file()` - Đọc và parse file dữ liệu
- Validate format
- Extract: cost matrix, delivery, pickup, capacity

**savings.py** (200 lines)
- `solve_savings()` - Thuật toán Clarke-Wright
- Calculate savings matrix
- Merge routes based on savings
- Return: routes, total cost, computation time

**vnd.py** (300 lines)
- `solve_vnd()` - Variable Neighborhood Descent
- Initial solution từ Savings
- 4 neighborhood structures:
  - Swap customers
  - 2-opt route optimization
  - Relocate customer
  - Cross-exchange between routes
- Local search until no improvement

**utils.py** (100 lines)
- `route_distance()` - Tính khoảng cách tuyến
- `calculate_total_cost()` - Tổng chi phí
- `convert_routes_to_vector()` - Chuyển đổi format
- `convert_vector_to_routes()` - Chuyển đổi ngược

#### Module 2: Visualization (`algorithms/`)
**visualization.py** (250 lines)
- `generate_coordinates_from_cost_matrix()` - Tạo tọa độ 2D từ ma trận
  - Sử dụng MDS (Multidimensional Scaling)
- `create_plotly_data()` - Tạo dữ liệu Plotly
  - Depot marker
  - Customer points
  - Route lines
- `create_plotly_figure_json()` - Tạo JSON cho Plotly.js

#### Module 3: Excel Export (`algorithms/`)
**excel_export.py** (350 lines)
- `export_to_excel()` - Xuất kết quả đơn
- Tạo multiple sheets
- Formatting: colors, borders, alignment
- Auto-width columns

**batch_excel_export.py** (320 lines)
- `export_batch_to_excel()` - Xuất Master Excel
- Summary statistics
- Comparison table
- Conditional formatting

#### Module 4: Batch Processing (`algorithms/`)
**batch_processor.py** (150 lines)
- `process_batch_files()` - Xử lý nhiều file
- Parse từng file
- Giải thuật toán
- Tổng hợp kết quả
- Error handling

#### Module 5: Web Application (`app.py`)
**Routes & Handlers:**
- `/` - Render homepage
- `/api/upload` - Handle file upload
- `/api/solve` - Execute algorithms
- `/api/export-excel` - Generate Excel
- `/api/batch-*` - Batch operations

**File Management:**
- Upload to `static/uploads/`
- Temporary storage
- Cleanup after processing

#### Module 6: Frontend (`templates/`, `static/`)
**templates/index.html** (225 lines)
- Single page application
- Bootstrap grid layout
- Mode toggle (Single/Batch)
- Results display
- Visualization container
- Fullscreen modal

**static/js/app.js** (737 lines)
- File upload handling
- AJAX API calls
- Results rendering
- Plotly visualization
- Mode management
- Batch processing UI

**static/css/style.css** (189 lines)
- Custom styling
- Fullscreen modal
- Responsive design
- Animations

### 4.3. Data Flow

#### Single File Processing:
```
User → Upload File → Server (Parse) → Display Info →
User Select Algo → Solve → Results + Visualization →
Export Excel
```

#### Batch Processing:
```
User → Upload Multiple Files → Server (Parse All) →
Display File List → User Click Solve All →
Process Each File → Aggregate Results →
Display Summary Table → Export Master Excel
```

### 4.4. Thống Kê Code

**Tổng số dòng code:** ~3,500 lines

**Phân bố:**
- Python (Backend + Algorithms): ~2,300 lines (66%)
- JavaScript (Frontend Logic): ~680 lines (19%)
- HTML: ~225 lines (6%)
- CSS: ~189 lines (5%)
- Other (Config, README): ~106 lines (4%)

**Số lượng file:**
- Python files: 10
- Template files: 1
- Static files: 2 (JS, CSS)
- Config files: 2
- **Total: 15 files**

**API Endpoints:** 7 endpoints

**Test Coverage:** 6 test files

---

## 5. ƯU ĐIỂM HỆ THỐNG

### 5.1. Về Hiệu Năng
✅ Thuật toán Savings: O(n²) - nhanh với bài toán vừa và nhỏ
✅ VND tối ưu hóa hiệu quả (~10-30% cải thiện)
✅ Batch processing: xử lý nhiều file tự động
✅ Computation time < 1s cho bài toán 20-30 khách hàng

### 5.2. Về Giao Diện
✅ Responsive design - hoạt động trên mọi thiết bị
✅ Interactive visualization - trực quan, dễ hiểu
✅ User-friendly - không cần training
✅ Real-time feedback - progress indicator

### 5.3. Về Tính Năng
✅ 2 thuật toán khác nhau để so sánh
✅ Visualization với Plotly.js chuyên nghiệp
✅ Excel export với formatting đẹp
✅ Batch processing tiết kiệm thời gian
✅ Master Excel tổng hợp toàn diện

### 5.4. Về Kiến Trúc
✅ Modular design - dễ maintain và mở rộng
✅ RESTful API - chuẩn industry
✅ Separation of concerns - frontend/backend tách biệt
✅ Clean code - có comments, type hints

---

## 6. HƯỚNG PHÁT TRIỂN

### Tính Năng Mới
- [ ] Thêm thuật toán: Genetic Algorithm, Ant Colony
- [ ] Hỗ trợ thêm format file: CSV, JSON
- [ ] Database storage - lưu lịch sử giải
- [ ] User authentication - multi-user support
- [ ] Real-time collaboration
- [ ] API documentation (Swagger)

### Cải Tiến
- [ ] Optimization: Parallel processing cho batch
- [ ] Caching: Redis cho kết quả thường dùng
- [ ] WebSocket: Real-time progress updates
- [ ] Export thêm PDF, JSON
- [ ] Comparison với optimal solution (nếu có)
- [ ] Mobile app version

---

## 7. DEMO SCENARIOS

### Scenario 1: Single File
1. Upload file `n23k5_E-n23-k3_09.txt` (23 customers)
2. Show problem info displays
3. Select both algorithms
4. Click Solve → Show results in ~0.5s
5. Show visualization with routes
6. Click fullscreen → Interactive chart
7. Export Excel → Show formatted report

**Expected Results:**
- Savings: ~500-600 cost
- VND: ~450-550 cost (10-20% improvement)
- 3-5 routes
- Clear visualization

### Scenario 2: Batch Processing
1. Toggle to Batch mode
2. Select 5 files: different sizes
3. Show file list
4. Click Solve All → Show progress (1/5, 2/5, ...)
5. Show results table with all files
6. Export Master Excel
7. Open Excel → Show Summary + Comparison sheets

**Expected Results:**
- All 5 files processed successfully
- Summary: avg improvement ~15-25%
- Comparison table easy to read
- Total time < 5s

---

## 8. KẾT LUẬN

### Đạt Được
✅ Xây dựng hệ thống web hoàn chỉnh giải VRPSPD
✅ Tích hợp 2 thuật toán tối ưu hiệu quả
✅ Giao diện đẹp, trực quan với Bootstrap + Plotly
✅ Chức năng xuất báo cáo Excel chuyên nghiệp
✅ Batch processing xử lý hàng loạt
✅ Code sạch, modular, dễ maintain

### Công Nghệ
- **Backend**: Flask, Python 3.13
- **Frontend**: Bootstrap 5, Plotly.js
- **Libraries**: NumPy, SciPy, Pandas, openpyxl
- **Architecture**: RESTful API, MVC pattern

### Kết Quả
- **~3,500 dòng code** được tổ chức tốt
- **7 API endpoints** xử lý đầy đủ chức năng
- **4 chức năng chính** hoạt động ổn định
- **2 thuật toán** cho kết quả tốt
- **Thời gian phát triển**: 4 tuần theo timeline

---

## 9. TÀI LIỆU THAM KHẢO

### Documents trong project:
- `README.md` - Hướng dẫn cài đặt và sử dụng
- `QUICKSTART.md` - Quick start guide
- `PROJECT_TIMELINE_4_WEEKS.md` - Timeline phát triển
- `VISUALIZATION_GUIDE.md` - Hướng dẫn visualization
- `STEP2_COMPLETE.md` - Tài liệu Step 2
- `STEP3_EXCEL_EXPORT.md` - Tài liệu Step 3
- `STEP4_BATCH_PROCESSING.md` - Tài liệu Step 4

### Test files:
- 6 test files để verify từng module
- Sample data: 16 test files

---

**Tài liệu này cung cấp đầy đủ thông tin để tạo slide thuyết trình chuyên nghiệp! 📊✨**
