# Hướng Dẫn Sử Dụng Test Suite VRPSPD

## 📋 Tổng Quan

Bộ test suite này cung cấp kịch bản thử nghiệm hoàn chỉnh cho VRPSPD Web Application, bao gồm:

- **Documentation**: `VRPSPD_TEST_SCENARIOS.md` - Mô tả chi tiết các kịch bản test
- **Code**: `test_complete_scenarios.py` - Code thực thi các test

## 🎯 Các Loại Test

### 1. **Unit Tests** (TC001-TC008, TC015)
Kiểm tra các module và thuật toán riêng lẻ:
- Module imports
- File parser
- Savings algorithm
- VND algorithm
- Visualization
- Excel export (single & batch)
- Error handling

### 2. **Performance Tests** (TC016)
Kiểm tra hiệu năng với instance lớn (50 customers)

### 3. **API Tests** (TC009-TC013)
Kiểm tra các REST API endpoints (cần Flask server chạy)

### 4. **End-to-End Tests** (TC018)
Kiểm tra workflow hoàn chỉnh qua giao diện web

## 🚀 Cách Sử Dụng

### Cài Đặt Dependencies

```bash
pip install flask openpyxl numpy plotly werkzeug
```

### Chạy Tests

#### Chạy tất cả tests:
```bash
python test_complete_scenarios.py --all
```

#### Chỉ chạy unit tests:
```bash
python test_complete_scenarios.py --unit
```

#### Chỉ chạy performance tests:
```bash
python test_complete_scenarios.py --performance
```

#### Chạy API tests (cần server):
```bash
# Terminal 1: Start server
python app.py

# Terminal 2: Run API tests
python test_complete_scenarios.py --api
```

#### End-to-end test (manual):
```bash
# Xem hướng dẫn trong VRPSPD_TEST_SCENARIOS.md - TC018
python test_complete_scenarios.py --e2e
```

### Không Truyền Arguments (Default)

```bash
python test_complete_scenarios.py
```
→ Chạy tất cả tests (tương đương `--all`)

## 📊 Kết Quả Test

### Console Output

Test sẽ hiển thị kết quả trực tiếp trên console với màu sắc:
- ✅ **Green** = Passed
- ❌ **Red** = Failed
- ⚠️ **Yellow** = Warning/Skipped

Ví dụ:
```
======================================================================
[TC003] Kiểm Tra Thuật Toán Savings
======================================================================
✅ Result structure valid
✅ Total cost: 52.00
✅ Number of routes: 2
✅ Computation time: 0.0023s
✅ All customers visited exactly once
✅ All routes satisfy capacity constraints
```

### Test Report File

Sau khi chạy, report được tự động lưu vào:
```
test_results/test_report_YYYYMMDD_HHMMSS.txt
```

Ví dụ nội dung:
```
======================================================================
VRPSPD TEST REPORT
======================================================================
Date: 25/01/2026 14:30:45
Environment: Local Development

TEST SUMMARY:
- Total Tests: 12
- Passed: 11 ✅
- Failed: 0 ❌
- Skipped: 1 ⚠️
- Success Rate: 91.7%

DETAILS:
----------------------------------------------------------------------
[TC001] Kiểm Tra Module Import: ✅ PASS
    Message: All modules imported successfully
    Duration: 0.15s

[TC002] Kiểm Tra File Parser: ✅ PASS
    Message: Parsed 3 customers successfully
    Duration: 0.02s
...
```

## 📁 Cấu Trúc Thư Mục Sau Khi Chạy Test

```
vrpspd-web/
├── static/
│   └── uploads/
│       └── test_data/          # Test data files
│           ├── standard_test.txt
│           ├── large_test.txt
│           ├── batch_test_1.txt
│           ├── batch_test_2.txt
│           └── ...
├── test_results/               # Test outputs
│   ├── test_report_20260125_143045.txt
│   ├── test_viz.json
│   ├── test_results.xlsx
│   └── test_batch_results.xlsx
├── VRPSPD_TEST_SCENARIOS.md   # Documentation
├── test_complete_scenarios.py  # Test code
└── README_TESTING.md          # This file
```

## 🧪 Chi Tiết Các Test Cases

### TC001: Module Import
Kiểm tra tất cả modules có import được không

**Expected:** Tất cả modules import thành công

### TC002: File Parser
Parse file VRPSPD format

**Expected:** 
- Cost matrix: 4x4
- Customers: 3
- Capacity: 6000

### TC003: Savings Algorithm
Chạy thuật toán Savings

**Expected:**
- Total cost > 0
- All customers visited once
- Routes satisfy capacity

### TC004: VND Algorithm
Cải thiện solution từ Savings

**Expected:**
- VND cost ≤ Savings cost
- Improvement ≥ 0%
- Routes vẫn valid

### TC005: Visualization
Tạo dữ liệu visualization

**Expected:**
- Coordinates cho tất cả nodes
- Plotly figure valid
- JSON export thành công

### TC006: Excel Export (Single)
Xuất kết quả ra Excel

**Expected:**
- File .xlsx được tạo
- Có các sheets: Summary, Routes, Comparison
- Data chính xác

### TC007: Batch Processing
Xử lý nhiều files

**Expected:**
- Tất cả files được process
- Success/Failed count đúng

### TC008: Batch Excel Export
Xuất batch results

**Expected:**
- Master Excel file
- Overview sheet + Instance sheets

### TC015: Error Handling
Test xử lý lỗi

**Expected:**
- Các file invalid đều raise error
- Error messages rõ ràng

### TC016: Performance
Test với 50 customers

**Expected:**
- Savings: < 5s
- VND: < 60s
- No crash

## 🎨 Customization

### Thay Đổi Test Configuration

Edit trong `test_complete_scenarios.py`:

```python
TEST_CONFIG = {
    'upload_folder': 'static/uploads',
    'test_data_folder': 'static/uploads/test_data',
    'output_folder': 'test_results',
    'vnd_time_limit': 10,  # Thay đổi time limit cho VND
    'server_url': 'http://localhost:5000'
}
```

### Thêm Test Case Mới

1. Tạo function `tcXXX_test_name(suite)`:

```python
def tc999_my_new_test(suite):
    """TC999: Mô tả test."""
    test_id = "TC999"
    test_name = "Tên Test"
    print_test_header(test_id, test_name)
    
    start_time = time.time()
    
    try:
        # Your test code here
        
        duration = time.time() - start_time
        result = TestResult(test_id, test_name, 'PASS', "Success", duration)
        suite.add_result(result)
        return True
        
    except Exception as e:
        duration = time.time() - start_time
        result = TestResult(test_id, test_name, 'FAIL', str(e), duration)
        suite.add_result(result)
        return False
```

2. Thêm vào `run_unit_tests()` hoặc suite khác:

```python
def run_unit_tests():
    # ... existing tests ...
    
    # Add new test
    tc999_my_new_test(suite)
    
    return suite
```

### Tạo Test Data Tùy Chỉnh

```python
def create_my_custom_test():
    test_data = """Cost matrix
0 10 20 30
10 0 15 25
20 15 0 20
30 25 20 0

Delivery quantities
100 200 150

Pick-up quantities
50 75 100

Vehicle capacity
500
"""
    filepath = 'my_custom_test.txt'
    with open(filepath, 'w') as f:
        f.write(test_data)
    return filepath
```

## 🔍 Debugging Tests

### Verbose Mode

Thêm print statements:

```python
print_info("Debug info here")
print(f"Variable value: {my_var}")
```

### Run Single Test

Comment out các tests khác trong suite:

```python
def run_unit_tests():
    suite = TestSuite()
    
    # tc001_test_imports(suite)
    # tc002_test_file_parser(suite)
    tc003_test_savings(suite, ...)  # Only this one
    
    return suite
```

### Check Exceptions

```python
try:
    # test code
except Exception as e:
    print(f"Exception: {e}")
    import traceback
    traceback.print_exc()
```

## ✅ Pre-Test Checklist

Trước khi chạy test, đảm bảo:

- [ ] Python 3.8+ đã cài
- [ ] Tất cả dependencies đã install
- [ ] Thư mục `static/uploads` tồn tại
- [ ] Có quyền ghi file
- [ ] Port 5000 available (cho API tests)
- [ ] Đủ disk space (ít nhất 100MB)

## 🐛 Troubleshooting

### Lỗi: ModuleNotFoundError

```bash
# Cài đặt lại dependencies
pip install -r requirements.txt
```

### Lỗi: Permission Denied

```bash
# Windows: Run as Administrator
# Linux/Mac: chmod permissions
chmod +x test_complete_scenarios.py
```

### Lỗi: Flask server not running (API tests)

```bash
# Start server trước
python app.py

# Đợi message: "Running on http://0.0.0.0:5000"
```

### Tests chạy chậm

- Giảm `vnd_time_limit` trong config
- Comment out performance tests
- Dùng file test nhỏ hơn

### Excel file không mở được

- Kiểm tra openpyxl version: `pip install --upgrade openpyxl`
- Thử mở bằng Excel/LibreOffice khác

## 📞 Support

**Issues?**
- Check `VRPSPD_TEST_SCENARIOS.md` cho chi tiết test cases
- Xem test report file trong `test_results/`
- Chạy với Python debugger: `python -m pdb test_complete_scenarios.py`

## 📈 Test Coverage

| Module | Coverage | Notes |
|--------|----------|-------|
| file_parser | ✅ 100% | TC002, TC015 |
| savings | ✅ 100% | TC003, TC007, TC016 |
| vnd | ✅ 100% | TC004, TC007, TC016 |
| visualization | ✅ 100% | TC005 |
| excel_export | ✅ 100% | TC006 |
| batch_processor | ✅ 100% | TC007 |
| batch_excel_export | ✅ 100% | TC008 |
| Flask routes | ⚠️ Manual | TC009-TC014, TC018 |

## 🎯 Next Steps

Sau khi tất cả tests PASS:

1. ✅ Chạy web app: `python app.py`
2. ✅ Test manual qua browser
3. ✅ Upload real data files
4. ✅ Verify results
5. ✅ Export Excel và kiểm tra
6. ✅ Test batch processing với nhiều files

## 📚 Tài Liệu Liên Quan

- `VRPSPD_TEST_SCENARIOS.md` - Chi tiết test scenarios
- `README.md` - Hướng dẫn sử dụng app
- `QUICKSTART.md` - Quick start guide
- `test_all.py` - Quick test script (cũ)
- `test_algorithms.py` - Algorithm tests (cũ)

---

**Version:** 1.0  
**Last Updated:** 25/01/2026  
**Author:** QA Team
