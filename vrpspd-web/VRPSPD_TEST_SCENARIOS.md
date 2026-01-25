# Kịch Bản Thử Nghiệm VRPSPD Web Application

## Tổng Quan

Tài liệu này mô tả kịch bản thử nghiệm chi tiết cho tất cả các tính năng của VRPSPD Web Application.

---

## Mục Tiêu Thử Nghiệm

1. **Đảm bảo tính đúng đắn** của các thuật toán giải VRP với Pickup & Delivery
2. **Kiểm tra độ ổn định** của web application trong các tình huống khác nhau
3. **Xác minh tính năng xuất báo cáo** Excel
4. **Đánh giá hiệu năng** xử lý batch files
5. **Kiểm tra trải nghiệm người dùng** và giao diện web

---

## Các Kịch Bản Thử Nghiệm

### **TC001: Kiểm Tra Module Import**

**Mục đích:** Xác minh tất cả các module Python được import đúng cách

**Tiền điều kiện:**
- Python environment đã được cài đặt
- Tất cả dependencies đã được cài (Flask, openpyxl, numpy, etc.)

**Các bước thực hiện:**
1. Import tất cả modules từ package `algorithms`
2. Kiểm tra các hàm chính có thể truy cập được

**Kết quả mong đợi:**
- Không có lỗi import
- Tất cả các hàm chính có thể gọi được

---

### **TC002: Kiểm Tra File Parser**

**Mục đích:** Kiểm tra khả năng đọc và parse file input đúng định dạng

**Tiền điều kiện:**
- Module `file_parser` đã được import
- File test data có cấu trúc đúng

**Các bước thực hiện:**
1. Tạo test file với định dạng chuẩn VRPSPD
2. Gọi hàm `read_vrpspd_file()`
3. Kiểm tra dữ liệu đầu ra

**Test Data:**
```
Cost matrix
0 9 14 23
9 0 21 22
14 21 0 25
23 22 25 0

Delivery quantities
1200 1700 1500

Pick-up quantities
0 1200 1700

Vehicle capacity
6000
```

**Kết quả mong đợi:**
- Cost matrix: 4x4 (1 depot + 3 customers)
- Demand vector: [1200, 1700, 1500]
- Pickup vector: [0, 1200, 1700]
- Capacity: 6000
- Không có lỗi parse

---

### **TC003: Kiểm Tra Thuật Toán Savings**

**Mục đích:** Xác minh thuật toán Savings hoạt động đúng và trả về kết quả hợp lệ

**Tiền điều kiện:**
- File đã được parse thành công (TC002)
- Dữ liệu input hợp lệ

**Các bước thực hiện:**
1. Sử dụng dữ liệu từ TC002
2. Gọi `solve_savings(cost_matrix, demand, pickup, capacity, num_vehicles)`
3. Kiểm tra kết quả trả về

**Kết quả mong đợi:**
- `total_cost` > 0
- `num_routes` >= 1 và <= số xe
- `computation_time` được ghi nhận
- `routes` là list các route hợp lệ
- `solution_vector` có độ dài = số customer
-  Mỗi route không vượt quá capacity

**Kiểm tra bổ sung:**
- Tổng demand của mỗi route ≤ vehicle capacity
- Tất cả customers được phục vụ đúng 1 lần
- Mỗi route bắt đầu và kết thúc tại depot (node 0)

---

### **TC004: Kiểm Tra Thuật Toán VND**

**Mục đích:** Xác minh VND cải thiện lời giải từ Savings

**Tiền điều kiện:**
- Savings đã chạy thành công (TC003)
- Initial solution vector đã có

**Các bước thực hiện:**
1. Lấy `solution_vector` từ kết quả Savings
2. Gọi `solve_vnd(initial_vector, cost_matrix, demand, pickup, capacity)`
3. So sánh kết quả với Savings

**Kết quả mong đợi:**
-  `total_cost` (VND) ≤ `total_cost` (Savings)
-  `improvement` >= 0 (%)
-  `routes` vẫn hợp lệ
-  Ràng buộc capacity vẫn được thỏa mãn
-  `computation_time` được ghi nhận

**Kiểm tra bổ sung:**
- Số routes có thể thay đổi nhưng vẫn hợp lệ
- Nếu improvement = 0%, route có thể giống Savings
- Nếu improvement > 0%, total_cost phải nhỏ hơn



---

### **TC005: Kiểm Tra Visualization**

**Mục đích:** Xác minh dữ liệu visualization được tạo đúng và có thể render bằng Plotly

**Tiền điều kiện:**
- Đã có routes từ Savings hoặc VND
- Module visualization đã được import

**Các bước thực hiện:**
1. Lấy routes từ thuật toán đã chạy
2. Gọi `create_plotly_data(routes, cost_matrix, demand, pickup)`
3. Gọi `create_plotly_figure_json(viz_data)`
4. Kiểm tra JSON output

**Kết quả mong đợi:**
-  `coordinates` chứa tọa độ tất cả nodes
-  `depot` có tọa độ (x, y)
-  `routes` chứa path cho mỗi route
-  Plotly figure có `data` và `layout`
-  Có thể serialize thành JSON

**Kiểm tra bổ sung:**
- Số trace = số routes + 1 (depot marker)
- Mỗi route có màu khác nhau
- Depot được highlight



---

### **TC006: Kiểm Tra Excel Export (Single File)**

**Mục đích:** Xác minh xuất Excel cho 1 instance thành công

**Tiền điều kiện:**
- Đã có results từ Savings và/hoặc VND
- Module excel_export đã được import

**Các bước thực hiện:**
1. Chuẩn bị results dictionary
2. Gọi `create_excel_report(results, problem_info, filename)`
3. Kiểm tra file Excel được tạo

**Kết quả mong đợi:**
-  File .xlsx được tạo thành công
-  File có kích thước > 0
-  File có các sheet: Summary, Routes, Comparison (nếu có cả 2 algorithm)
-  Dữ liệu trong Excel đúng với results

**Kiểm tra bổ sung:**
- Summary sheet có thông tin problem
- Routes sheet liệt kê tất cả routes
- Comparison sheet so sánh Savings vs VND (nếu có)
- Formatting đẹp, dễ đọc



---

### **TC007: Kiểm Tra Batch Processing**

**Mục đích:** Xác minh xử lý nhiều file cùng lúc

**Tiền điều kiện:**
- Có ít nhất 3 file test khác nhau
- Module batch_processor đã được import

**Các bước thực hiện:**
1. Chuẩn bị list files
2. Gọi `process_batch_files(files, algorithms)`
3. Kiểm tra batch_results

**Kết quả mong đợi:**
-  Tất cả files được xử lý
-  Mỗi file có kết quả hoặc error message
-  Success count + Failed count = Total files
-  Results của mỗi file hợp lệ

**Kiểm tra bổ sung:**
- Xử lý song song nếu có thể
- Một file lỗi không ảnh hưởng files khác
- Error messages rõ ràng



---

### **TC008: Kiểm Tra Batch Excel Export**

**Mục đích:** Xuất Master Excel cho batch results

**Tiền điều kiện:**
- Đã có batch_results từ TC007
- Module batch_excel_export đã được import

**Các bước thực hiện:**
1. Lấy batch_results từ batch processing
2. Tạo summary
3. Gọi `create_batch_excel_report(batch_results, summary, filename)`

**Kết quả mong đợi:**
-  Master Excel file được tạo
-  File có Overview sheet với summary
-  File có sheet cho từng instance
-  Dữ liệu chính xác



---

### **TC009: Kiểm Tra Flask API - Upload Single File**

**Mục đích:** Test API endpoint `/api/upload`

**Tiền điều kiện:**
- Flask server đã chạy
- Test file sẵn sàng

**Các bước thực hiện:**
1. POST file đến `/api/upload`
2. Kiểm tra response JSON

**Request:**
```
POST /api/upload
Content-Type: multipart/form-data
file: <test_data.txt>
```

**Kết quả mong đợi:**
```json
{
  "success": true,
  "filename": "test_data.txt",
  "filepath": "static/uploads/test_data.txt",
  "data": {
    "num_customers": 3,
    "num_vehicles": 1,
    "capacity": 6000
  }
}
```
---

### **TC010: Kiểm Tra Flask API - Solve**

**Mục đích:** Test API endpoint `/api/solve`

**Tiền điều kiện:**
- File đã được upload (TC009)
- Server đang chạy

**Các bước thực hiện:**
1. POST request với filepath và algorithms
2. Kiểm tra response

**Request:**
```json
{
  "filepath": "static/uploads/test_data.txt",
  "algorithms": ["savings", "vnd"]
}
```

**Kết quả mong đợi:**
```json
{
  "success": true,
  "results": {
    "savings": {...},
    "vnd": {...}
  },
  "problem_info": {...},
  "visualization": {...}
}
```
---

### **TC011: Kiểm Tra Flask API - Export Excel**

**Mục đích:** Test API endpoint `/api/export-excel`

**Các bước thực hiện:**
1. POST results data
2. Kiểm tra file download

**Kết quả mong đợi:**
-  Response là file .xlsx
-  Headers đúng (Content-Disposition, Content-Type)
-  File có thể mở được



---

### **TC012: Kiểm Tra Flask API - Batch Upload**

**Mục đích:** Test `/api/batch-upload`

**Các bước thực hiện:**
1. POST multiple files
2. Kiểm tra response

**Kết quả mong đợi:**
```json
{
  "success": true,
  "files": [...],
  "count": 3
}
```



---

### **TC013: Kiểm Tra Flask API - Batch Solve**

**Mục đích:** Test `/api/batch-solve`

**Các bước thực hiện:**
1. POST files data và algorithms
2. Kiểm tra batch processing

**Kết quả mong đợi:**
```json
{
  "success": true,
  "batch_results": [...],
  "summary": {
    "total_files": 3,
    "successful": 3,
    "failed": 0
  }
}
```



---

### **TC014: Kiểm Tra Giao Diện Web - UI Components**

**Mục đích:** Test giao diện người dùng

**Các bước thực hiện:**
1. Mở http://localhost:5000
2. Kiểm tra tất cả elements

**Kết quả mong đợi:**
-  File upload area hiển thị
-  Algorithm selection checkboxes
-  Solve button
-  Results area
-  Visualization canvas
-  Export buttons



---

### **TC015: Kiểm Tra Error Handling**

**Mục đích:** Test xử lý lỗi

**Test cases:**

#### TC015.1: Upload file sai định dạng
- Upload .pdf file
- Kết quả: Error message "Only .txt files allowed"

#### TC015.2: Upload file rỗng
- Upload empty file
- Kết quả: Error message rõ ràng

#### TC015.3: File thiếu dữ liệu
- Upload file thiếu Cost matrix
- Kết quả: Parse error message

#### TC015.4: Solve không có file
- Call solve API mà không upload file trước
- Kết quả: "File not found" error

#### TC015.5: Capacity không hợp lệ
- File có capacity = 0
- Kết quả: Validation error



---

### **TC016: Kiểm Tra Performance - Large Instance**

**Mục đích:** Test với dữ liệu lớn

**Test data:**
- 50 customers
- 5 vehicles
- Random demands & pickups

**Các bước thực hiện:**
1. Upload large file
2. Solve với Savings
3. Solve với VND (time limit 60s)
4. Measure times

**Kết quả mong đợi:**
-  Savings: < 5 seconds
-  VND: < 60 seconds
-  Không crash
-  Memory usage hợp lý



---

### **TC017: Kiểm Tra Batch với Mixed Results**

**Mục đích:** Test batch khi có file success và failed

**Các bước thực hiện:**
1. Chuẩn bị 5 files: 3 valid, 2 invalid
2. Run batch processing
3. Kiểm tra results

**Kết quả mong đợi:**
-  3 files successful
-  2 files failed với error message
-  Summary đúng
-  Excel export vẫn hoạt động



---

### **TC018: Kiểm Tra End-to-End Workflow**

**Mục đích:** Test toàn bộ workflow từ đầu đến cuối

**Các bước thực hiện:**
1. Mở web app
2. Upload file test
3. Select algorithms: Savings + VND
4. Click "Giải bài toán"
5. Xem visualization
6. Export Excel
7. Verify Excel file

**Kết quả mong đợi:**
-  Tất cả steps thành công
-  Results hiển thị đúng
-  Visualization render đẹp
-  Excel file đầy đủ thông tin



---

## Test Coverage Matrix

| Feature | TC001 | TC002 | TC003 | TC004 | TC005 | TC006 | TC007 | TC008 | TC009-014 | TC015 | TC016 | TC017 | TC018 |
|---------|-------|-------|-------|-------|-------|-------|-------|-------|-----------|-------|-------|-------|-------|
| Import |  | | | | | | | | | | | | |
| File Parser | |  | | | | | | | |  | | | |
| Savings | | |  | | | | | | | |  | |  |
| VND | | | |  | | | | | | |  | |  |
| Visualization | | | | |  | | | | | | | |  |
| Excel Export | | | | | |  | | | | | | |  |
| Batch Processing | | | | | | |  | | | | |  | |
| Batch Excel | | | | | | | |  | | | |  | |
| Web API | | | | | | | | |  |  | | |  |
| Error Handling | | | | | | | | | |  | |  | |

---

## Hướng Dẫn Chạy Test

### **Chạy All Tests**
```bash
python test_complete_scenarios.py --all
```

### **Chạy Unit Tests Only**
```bash
python test_complete_scenarios.py --unit
```

### **Chạy API Tests Only**
```bash
python test_complete_scenarios.py --api
```

### **Chạy Performance Tests**
```bash
python test_complete_scenarios.py --performance
```

### **Chạy End-to-End Test**
```bash
python test_complete_scenarios.py --e2e
```

---

## 📝 Test Report Template

```
===========================================
VRPSPD TEST REPORT
===========================================
Date: [DD/MM/YYYY]
Tester: [Name]
Environment: [Dev/Staging/Prod]

TEST SUMMARY:
- Total Tests: XX
- Passed: XX 
- Failed: XX ❌
- Skipped: XX ⚠️

DETAILS:
[TC001] Import Test:  PASS
[TC002] File Parser:  PASS
[TC003] Savings:  PASS
...

FAILED TESTS:
[None]

NOTES:
[Any observations]

===========================================
```

---

## 🔧 Test Environment Requirements

### **Software:**
- Python 3.8+
- Flask 2.0+
- openpyxl
- numpy
- plotly

### **Hardware:**
- RAM: 4GB minimum
- CPU: 2 cores minimum
- Disk: 1GB free space

### **Network:**
- Port 5000 available for Flask

---

##  Test Checklist

- [ ] Tất cả dependencies đã cài đặt
- [ ] Test files đã được chuẩn bị
- [ ] Flask server có thể khởi động
- [ ] Upload folder đã được tạo
- [ ] Có quyền ghi file
- [ ] Browser có thể truy cập localhost:5000

---

