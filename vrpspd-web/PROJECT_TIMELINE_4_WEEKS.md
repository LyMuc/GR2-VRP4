# Kế hoạch thực hiện dự án VRPSPD Web Application - 4 Tuần

## 📅 TUẦN 1: Project Setup & Core Algorithm Implementation

### 🎯 Mục tiêu:
Xây dựng nền tảng cơ bản của ứng dụng web, refactor thuật toán từ Jupyter Notebook sang modules Python, và implement backend API.

### 📋 Công việc cần làm:

#### 1.1. Project Setup (2 ngày)
- Khởi tạo cấu trúc project Flask
- Setup virtual environment
- Cài đặt dependencies (Flask, numpy, scipy, pandas, etc.)
- Tạo folder structure:
  - `algorithms/`: Chứa thuật toán
  - `templates/`: HTML templates
  - `static/`: CSS, JS, uploaded files
  - `tests/`: Test scripts
- Tạo file `requirements.txt`
- Setup Git repository (optional)

#### 1.2. Algorithm Refactoring (3 ngày)
- **File Parser Module** (`algorithms/file_parser.py`):
  - Parse file .txt format VRPSPD
  - Đọc cost matrix, delivery, pickup, vehicle capacity
  - Validation dữ liệu đầu vào
  
- **Savings Algorithm** (`algorithms/savings.py`):
  - Implement Clarke-Wright Savings heuristic
  - Calculate savings matrix
  - Route construction
  - Feasibility checking (capacity constraints)
  
- **VND Algorithm** (`algorithms/vnd.py`):
  - Implement 5 neighborhood structures:
    - Swap(1,1) inter-route
    - Relocate inter-route
    - Shift(2,0) inter-route
    - Swap(2,1) inter-route
    - Swap(2,2) inter-route
  - Intra-route optimization
  - Time limit handling (60s)
  
- **Utils Module** (`algorithms/utils.py`):
  - Helper functions: calculate route cost, check feasibility
  - Route validation functions

#### 1.3. Backend API Development (2 ngày)
- Setup Flask application (`app.py`):
  - Configure upload folder, file size limits
  - Create API routes:
    - `POST /api/upload`: Upload file
    - `POST /api/solve`: Solve VRPSPD
  - Error handling và validation
  - CORS configuration (if needed)

#### 1.4. Basic Frontend (1 ngày)
- Create `index.html`:
  - Bootstrap 5 layout
  - File upload form
  - Algorithm selection checkboxes
  - Solve button
  - Basic results display area
- Create `app.js`:
  - File upload handler
  - Solve API call
  - Display results in table format

#### 1.5. Testing & Documentation (2 ngày)
- Write unit tests cho algorithms
- Integration testing cho API endpoints
- Test với sample data files
- Viết README.md cơ bản
- Document API endpoints

### 📦 Sản phẩm Tuần 1:

#### Mã nguồn:
```
vrpspd-web/
├── app.py                          # Flask application (150 lines)
├── requirements.txt                # Dependencies list
├── algorithms/
│   ├── __init__.py                 # Module exports
│   ├── file_parser.py              # File parser (80 lines)
│   ├── savings.py                  # Savings algorithm (200 lines)
│   ├── vnd.py                      # VND algorithm (300 lines)
│   └── utils.py                    # Utility functions (100 lines)
├── templates/
│   └── index.html                  # Basic UI (120 lines)
├── static/
│   ├── js/
│   │   └── app.js                  # Frontend logic (150 lines)
│   ├── css/
│   │   └── style.css               # Basic styles
│   └── uploads/                    # Upload directory
└── tests/
    ├── test_algorithms.py          # Algorithm tests
    └── test_api.py                 # API tests
```

#### Tài liệu:
- **README.md**: 
  - Project overview
  - Installation instructions
  - How to run
  - API documentation
  
- **ALGORITHM_DOCUMENTATION.md**:
  - Clarke-Wright Savings explanation
  - VND neighborhood structures
  - Complexity analysis
  - Example calculations

- **Test Reports**:
  - Unit test results
  - Sample input/output examples

#### Deliverables:
✅ Working Flask application với basic UI  
✅ File upload functionality  
✅ Savings và VND algorithms đã test  
✅ API endpoints functional  
✅ Basic results display (text/table format)  

---

## 📅 TUẦN 2: Visualization & UI Enhancement

### 🎯 Mục tiêu:
Implement visualization tương tác cho routes, enhance UI/UX, và tích hợp Plotly.js để hiển thị đồ thị 2D.

### 📋 Công việc cần làm:

#### 2.1. Visualization Module (3 ngày)
- **MDS Transformation** (`algorithms/visualization.py`):
  - Implement MDS (Multidimensional Scaling) để convert cost matrix → 2D coordinates
  - Handle symmetric matrix requirement
  - Optimization cho performance
  
- **Plotly Data Generation**:
  - Create scatter plots cho customers và depot
  - Generate line traces cho routes (10 colors)
  - Add direction indicators (arrows)
  - Hover tooltips với customer info
  - Legend configuration

- **API Integration**:
  - Update `/api/solve` endpoint để return visualization data
  - JSON serialization cho Plotly figures

#### 2.2. Frontend Visualization (2 ngày)
- **Plotly.js Integration**:
  - Load Plotly.js library
  - Render interactive graph
  - Configure layout: axis labels, title, colors
  - Zoom, pan, hover functionality
  
- **Fullscreen Modal**:
  - Create modal overlay cho fullscreen view
  - Responsive resize
  - ESC key to close
  - Fullscreen button trong visualization header

#### 2.3. UI/UX Improvements (2 ngày)
- **Enhanced Results Display**:
  - Comparison table với colors
  - Improvement percentage highlighting
  - Route details section (collapsible)
  - Summary cards với icons
  
- **Loading Indicators**:
  - Spinner animation khi processing
  - Progress messages
  - Disable buttons during processing
  
- **Toast Notifications**:
  - Success/error messages
  - Auto-dismiss after 5s
  - Position: top-center

#### 2.4. Responsive Design (1 ngày)
- Mobile-friendly layout
- Tablet optimization
- Grid system adjustments
- CSS enhancements:
  - Custom color scheme
  - Button styles
  - Card shadows
  - Animation effects

#### 2.5. Testing & Bug Fixes (2 ngày)
- Test visualization với different data sizes
- Cross-browser compatibility
- Performance optimization
- Fix MDS symmetric matrix bug
- User acceptance testing

### 📦 Sản phẩm Tuần 2:

#### Mã nguồn (Updated):
```
vrpspd-web/
├── algorithms/
│   └── visualization.py            # NEW: Visualization module (250 lines)
├── templates/
│   └── index.html                  # UPDATED: With visualization (180 lines)
├── static/
│   ├── js/
│   │   └── app.js                  # UPDATED: Plotly integration (280 lines)
│   └── css/
│       └── style.css               # UPDATED: Enhanced styles (150 lines)
└── tests/
    └── test_visualization.py       # NEW: Visualization tests
```

#### Tài liệu:
- **VISUALIZATION_GUIDE.md**:
  - MDS algorithm explanation
  - Plotly configuration
  - Customization guide
  - Troubleshooting common issues
  
- **UI_UX_DOCUMENTATION.md**:
  - Color scheme rationale
  - Layout decisions
  - Accessibility considerations
  - Responsive breakpoints

- **User Guide v1.0**:
  - How to upload files
  - How to interpret visualization
  - Fullscreen mode usage
  - Tips and tricks

#### Deliverables:
✅ Interactive 2D route visualization  
✅ Fullscreen modal functionality  
✅ Enhanced UI với Bootstrap 5  
✅ Loading indicators và notifications  
✅ Collapsible route details  
✅ Responsive design for mobile/tablet  

---

## 📅 TUẦN 3: Excel Export & Data Reporting

### 🎯 Mục tiêu:
Implement tính năng export kết quả ra Excel với formatting chuyên nghiệp, multiple sheets, và charts.

### 📋 Công việc cần làm:

#### 3.1. Excel Export Module (3 ngày)
- **Core Export Function** (`algorithms/excel_export.py`):
  - Install openpyxl library
  - Create `create_excel_report()` function
  - Implement 3 sheets:
    - **Summary Sheet**: Problem info + Algorithm comparison
    - **Route Details Sheet**: Chi tiết từng tuyến
    - **Comparison Sheet**: Savings vs VND metrics
  
- **Professional Formatting**:
  - Cell styles: fonts, colors, borders
  - PatternFill cho headers và highlights
  - Number formatting (decimals, percentages)
  - Column width auto-adjustment
  - Alignment: center, left, vertical center
  
- **Data Organization**:
  - Title rows với merge cells
  - Header rows với bold white text on blue
  - Zebra striping (alternate row colors)
  - Highlight best results (green)
  - Total rows với bold fonts

#### 3.2. API Endpoint (1 ngày)
- **New Route** (`/api/export-excel`):
  - Receive results data và problem info
  - Generate Excel file with timestamp filename
  - Store in `static/uploads/`
  - Return file for download using `send_file()`
  - Set proper MIME type
  - Error handling

#### 3.3. Frontend Integration (1 ngày)
- **Export Button**:
  - Enable after successful solve
  - Click handler: `handleExport()`
  - API call to `/api/export-excel`
  - Blob download handling
  - Automatic filename generation
  
- **UI Updates**:
  - Export button styling
  - Loading state during export
  - Success notification
  - Error handling

#### 3.4. Advanced Features (2 ngày)
- **Charts trong Excel** (optional):
  - Bar chart comparing costs
  - Pie chart for route distribution
  - Line chart for improvement trend
  
- **Conditional Formatting**:
  - Auto-highlight improvements > 5%
  - Color scale for costs
  - Data bars for visual comparison
  
- **Multiple Export Formats**:
  - XLSX (primary)
  - CSV (alternative, simple)
  - PDF (future enhancement)

#### 3.5. Testing & Documentation (1 ngày)
- Test với different data sizes
- Verify Excel formatting
- Cross-platform compatibility (Windows/Mac/Linux)
- Memory optimization for large files
- Write export documentation

### 📦 Sản phẩm Tuần 3:

#### Mã nguồn (Updated):
```
vrpspd-web/
├── app.py                          # UPDATED: Add export endpoint (210 lines)
├── requirements.txt                # UPDATED: Add openpyxl
├── algorithms/
│   └── excel_export.py             # NEW: Excel generation (350 lines)
├── static/
│   └── js/
│       └── app.js                  # UPDATED: Export functionality (340 lines)
└── tests/
    └── test_excel_export.py        # NEW: Export tests
```

#### Tài liệu:
- **EXCEL_EXPORT_GUIDE.md**:
  - Sheet descriptions
  - Formatting conventions
  - Cell styling guide
  - How to customize templates
  
- **DATA_REPORTING_MANUAL.md**:
  - Interpreting Excel reports
  - Key metrics explained
  - Comparison methodology
  - Business insights

- **Sample Reports**:
  - `Sample_Report_Small.xlsx` (10 customers)
  - `Sample_Report_Medium.xlsx` (30 customers)
  - `Sample_Report_Large.xlsx` (60 customers)

#### Deliverables:
✅ Professional Excel export với 3 sheets  
✅ Auto-download functionality  
✅ Cell formatting và styling  
✅ API endpoint `/api/export-excel`  
✅ Test reports với sample data  
✅ Export documentation  

---

## 📅 TUẦN 4: Batch Processing & Final Integration

### 🎯 Mục tiêu:
Implement batch processing để xử lý nhiều files cùng lúc, tạo Master Excel report, và finalize toàn bộ project.

### 📋 Công việc cần làm:

#### 4.1. Batch Processing Backend (3 ngày)
- **Batch Processor Module** (`algorithms/batch_processor.py`):
  - `process_batch_files()`: Xử lý multiple files
  - Sequential processing với error handling per file
  - `create_batch_summary()`: Aggregate statistics
  - Progress tracking capability
  
- **Batch API Endpoints**:
  - `POST /api/batch-upload`: Upload multiple files
  - `POST /api/batch-solve`: Process all files
  - `POST /api/batch-export-excel`: Export Master Excel
  - Error handling và validation
  
- **Master Excel Export** (`algorithms/batch_excel_export.py`):
  - `create_batch_excel_report()` function
  - 3 sheets cho batch results:
    - **Summary**: Overall statistics + cost summary
    - **Comparison**: All files comparison table (10 columns)
    - **Best Results**: Top 10 ranked by improvement
  - Medal system: 🥇 Gold, 🥈 Silver, 🥉 Bronze
  - Professional formatting

#### 4.2. Frontend Batch UI (2 ngày)
- **Mode Toggle**:
  - Radio buttons: Single File / Batch
  - UI switching logic
  - Button text changes dynamically
  
- **Batch Upload UI**:
  - Multiple file input
  - File list preview với badges
  - Remove file functionality
  - Upload progress indicator
  
- **Batch Results Display**:
  - Summary statistics card
  - Results table với 9 columns:
    - #, File, Customers, Savings Cost, Savings Time
    - VND Cost, VND Time, Improvement, Status
  - Color coding: Success (green), Failed (red)
  - Sortable columns
  
- **Batch Export**:
  - Master Excel download
  - Timestamp in filename
  - Success notification

#### 4.3. Performance Optimization (1 ngày)
- **Backend Optimization**:
  - Caching cost matrix calculations
  - Memory management cho large batches
  - Async processing consideration
  - Timeout handling (60s per file)
  
- **Frontend Optimization**:
  - Lazy loading for large tables
  - Pagination for batch results
  - Debouncing for search/filter
  - Minimize API calls

#### 4.4. Final Testing & QA (2 ngày)
- **Integration Testing**:
  - End-to-end testing: Upload → Solve → Export
  - Batch processing với 10-20 files
  - Error scenarios testing
  - Cross-browser compatibility
  
- **Performance Testing**:
  - Load testing với large files
  - Memory leak detection
  - API response time measurement
  - Concurrent user handling
  
- **User Acceptance Testing**:
  - Test với real VRPSPD datasets
  - UI/UX feedback
  - Bug fixing
  - Edge case handling

#### 4.5. Documentation & Deployment Prep (2 ngày)
- **Complete Documentation**:
  - **README_COMPLETE.md**: Full project overview
  - **API_DOCUMENTATION.md**: All endpoints với examples
  - **USER_MANUAL.md**: Step-by-step guide
  - **DEPLOYMENT_GUIDE.md**: Production setup
  
- **Code Cleanup**:
  - Remove debug code
  - Code formatting consistency
  - Add comments và docstrings
  - Remove unused imports
  
- **Deployment Preparation**:
  - Configuration for production
  - Environment variables setup
  - Security considerations
  - WSGI server configuration (Gunicorn)
  - Docker setup (optional)

### 📦 Sản phẩm Tuần 4:

#### Mã nguồn (Final):
```
vrpspd-web/
├── app.py                          # FINAL: 286 lines với batch endpoints
├── requirements.txt                # FINAL: All dependencies
├── algorithms/
│   ├── __init__.py                 # Module exports
│   ├── file_parser.py              # 80 lines
│   ├── savings.py                  # 200 lines
│   ├── vnd.py                      # 300 lines
│   ├── utils.py                    # 100 lines
│   ├── visualization.py            # 250 lines
│   ├── excel_export.py             # 350 lines
│   ├── batch_processor.py          # NEW: 150 lines
│   └── batch_excel_export.py       # NEW: 320 lines
├── templates/
│   └── index.html                  # FINAL: 198 lines với batch UI
├── static/
│   ├── js/
│   │   └── app.js                  # FINAL: 680 lines với batch logic
│   ├── css/
│   │   └── style.css               # FINAL: 200 lines
│   └── uploads/
│       └── (sample files)
└── tests/
    ├── test_algorithms.py          # Algorithm tests
    ├── test_visualization.py       # Visualization tests
    ├── test_excel_export.py        # Excel export tests
    ├── test_batch_processing.py    # NEW: Batch tests
    └── test_batch_excel.py         # NEW: Batch Excel tests
```

#### Tài liệu (Complete):
- **README_COMPLETE.md** (Comprehensive):
  - Project overview
  - Features list (4 major features)
  - Installation guide
  - Usage instructions (Single + Batch)
  - API documentation
  - Project structure
  - Testing guide
  - Future enhancements
  
- **BATCH_PROCESSING_GUIDE.md**:
  - How batch processing works
  - Upload multiple files
  - Interpret batch results
  - Master Excel format
  - Performance considerations
  
- **API_DOCUMENTATION.md**:
  - All 6 endpoints documented
  - Request/response examples
  - Error codes
  - Rate limiting (if applicable)
  
- **USER_MANUAL.md**:
  - Getting started
  - Single file processing
  - Batch processing
  - Visualization guide
  - Excel export usage
  - Troubleshooting FAQ
  
- **DEPLOYMENT_GUIDE.md**:
  - Server requirements
  - Installation steps
  - Environment configuration
  - WSGI setup (Gunicorn)
  - Nginx configuration
  - Security best practices
  - Backup strategies

- **DEVELOPMENT_LOG.md**:
  - Week-by-week progress
  - Challenges faced
  - Solutions implemented
  - Lessons learned

#### Sample Data & Reports:
- `static/uploads/`:
  - `test_data.txt`
  - `Mitra-1-01.txt`
  - `Mitra-2-16.txt`
  - `60_6_10.txt`
  
- `sample_outputs/`:
  - `Single_Export_Example.xlsx`
  - `Batch_Master_Report.xlsx`
  - `visualization_screenshot.png`

#### Deliverables:
✅ Complete batch processing functionality  
✅ Master Excel export với 3 sheets  
✅ Mode switching (Single ↔️ Batch)  
✅ Batch results table với time columns  
✅ Comprehensive documentation (5 major docs)  
✅ Test suite (5 test files)  
✅ Sample data và reports  
✅ Production-ready application  
✅ Deployment guide  

---

## 📊 Tổng kết 4 tuần:

### Thống kê mã nguồn:
- **Total Lines of Code**: ~3,500 lines
- **Python Backend**: ~2,300 lines
  - Algorithms: ~1,200 lines
  - Flask app: ~300 lines
  - Export modules: ~650 lines
  - Tests: ~150 lines
- **Frontend**: ~1,200 lines
  - JavaScript: ~680 lines
  - HTML: ~200 lines
  - CSS: ~200 lines
  - Documentation: ~120 lines

### Tài liệu tạo ra:
1. README_COMPLETE.md
2. ALGORITHM_DOCUMENTATION.md
3. VISUALIZATION_GUIDE.md
4. UI_UX_DOCUMENTATION.md
5. EXCEL_EXPORT_GUIDE.md
6. DATA_REPORTING_MANUAL.md
7. BATCH_PROCESSING_GUIDE.md
8. API_DOCUMENTATION.md
9. USER_MANUAL.md
10. DEPLOYMENT_GUIDE.md
11. DEVELOPMENT_LOG.md

### Features hoàn thiện:
✅ **Single File Processing**:
   - Upload file
   - Solve with Savings/VND
   - Interactive visualization
   - Excel export

✅ **Batch Processing**:
   - Multiple file upload
   - Batch solve
   - Aggregate results
   - Master Excel export

✅ **Visualization**:
   - 2D route plotting
   - Interactive Plotly.js
   - Fullscreen mode
   - 10 color-coded routes

✅ **Excel Export**:
   - Single file: 3 sheets
   - Batch: 3 sheets với rankings
   - Professional formatting
   - Auto-download

✅ **UI/UX**:
   - Bootstrap 5 responsive design
   - Mode switching
   - Loading indicators
   - Toast notifications
   - Collapsible sections

### Công nghệ sử dụng:
- **Backend**: Flask 3.0, Python 3.13
- **Frontend**: Bootstrap 5, Plotly.js, vanilla JavaScript
- **Data Processing**: numpy, scipy, pandas
- **Excel**: openpyxl
- **Visualization**: scikit-learn (MDS), Plotly
- **Testing**: pytest, unittest

---

## 🎯 Kết luận:

Kế hoạch 4 tuần này đảm bảo:
- **Tuần 1**: Nền tảng vững chắc (algorithms + API)
- **Tuần 2**: Trải nghiệm người dùng tốt (visualization + UI)
- **Tuần 3**: Báo cáo chuyên nghiệp (Excel export)
- **Tuần 4**: Scalability và production-ready (batch processing)

Mỗi tuần có deliverables rõ ràng, testing đầy đủ, và documentation chi tiết. Project có thể demo được sau mỗi tuần với tính năng mới.
