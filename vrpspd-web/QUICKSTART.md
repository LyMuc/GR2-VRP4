# 🚀 Quick Start Guide - VRPSPD Web Application

## Bước 1: Cài đặt và chạy

```bash
cd vrpspd-web

# Cài đặt dependencies
pip install -r requirements.txt

# Chạy test algorithms
python test_algorithms.py

# Chạy test visualization
python test_visualization.py

# Khởi động web server
python app.py
```

## Bước 2: Truy cập web

Mở trình duyệt và vào: **http://localhost:5000**

## Bước 3: Sử dụng

1. **Upload file**: Click "Chọn file dữ liệu (.txt)" và chọn file txt
2. **Chọn thuật toán**: 
   - ☑ Savings-based (nhanh, kết quả cơ bản)
   - ☑ Savings + VND (chậm hơn, kết quả tốt hơn)
3. **Click "Giải bài toán"**: Đợi kết quả
4. **Xem kết quả**: Chi phí, thời gian, routes

## 📊 Kết quả bạn sẽ thấy

- **Chi phí tối ưu**: Tổng quãng đường tối thiểu
- **Số tuyến**: Số xe cần dùng
- **Thời gian tính toán**: Thời gian chạy thuật toán
- **Cải thiện**: % cải thiện nếu dùng VND
- **Chi tiết các tuyến**: Route của từng xe
- **📈 Visualization**: Biểu đồ tương tác với Plotly
  - Zoom, pan, hover
  - Màu sắc khác nhau cho mỗi route
  - Customer IDs và delivery/pickup info
- **Excel Export**: Xuất kết quả ra file Excel
- **Batch Processing**: Upload nhiều file cùng lúc
- **Best Known Solutions**: So sánh với BKS

## 🔧 Test với file mẫu

File test đã được tạo tự động tại: `static/uploads/test_data.txt`

Bạn có thể upload file này để test.

## 📝 Format file input

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