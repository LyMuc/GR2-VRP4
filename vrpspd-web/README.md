# VRPSPD Web Solver

Web application để giải bài toán **Vehicle Routing Problem with Simultaneous Pickup and Delivery (VRPSPD)** sử dụng thuật toán Clarke-Wright Savings và Variable Neighborhood Descent (VND).

## 🚀 Cài đặt

### Bước 1: Clone hoặc tải project

```bash
cd vrpspd-web
```

### Bước 2: Tạo virtual environment (khuyến nghị)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### Bước 3: Cài đặt dependencies

```bash
pip install -r requirements.txt
```

## 🎯 Chạy ứng dụng

```bash
python app.py
```

Mở trình duyệt và truy cập: `http://localhost:5000`

## 📂 Cấu trúc Project

```
vrpspd-web/
├── app.py                      # Flask application chính
├── requirements.txt            # Python dependencies
├── algorithms/                 # Module thuật toán
│   ├── __init__.py
│   ├── file_parser.py         # Parse file txt
│   ├── savings.py             # Clarke-Wright Savings
│   ├── vnd.py                 # Variable Neighborhood Descent
│   └── utils.py               # Utility functions
├── templates/
│   └── index.html             # Giao diện web
├── static/
│   ├── css/
│   │   └── style.css          # Custom CSS
│   ├── js/
│   │   └── app.js             # JavaScript logic
│   └── uploads/               # Thư mục lưu file upload
└── README.md
```

## 📝 Hướng dẫn sử dụng

### 1. Upload File

- Click "Chọn file dữ liệu (.txt)"
- Chọn file txt với format:
  ```
  Cost matrix
  0 10 15 20
  10 0 35 25
  15 35 0 30
  20 25 30 0
  
  Delivery quantities
  1200 1700 1500
  
  Pick-up quantities
  0 1200 1700
  
  Vehicle capacity
  6000 6000 6000
  ```

### 2. Chọn Thuật toán

- **Savings-based**: Thuật toán Clarke-Wright cơ bản
- **Savings + VND**: Kết hợp Savings với VND để cải thiện

### 3. Giải bài toán

- Click "Giải bài toán"
- Xem kết quả: chi phí, thời gian, các tuyến đường

### 4. Xuất Excel (Đang phát triển)

- Click "Xuất Excel" để tải file kết quả

## ✨ Tính năng hiện tại

✅ Upload và parse file txt  
✅ Chạy thuật toán Savings  
✅ Chạy thuật toán VND  
✅ Hiển thị kết quả và so sánh  
✅ Hiển thị chi tiết các tuyến  
✅ Giao diện responsive với Bootstrap  
✅ **Visualization với Plotly.js** (NEW!)
  - MDS transformation (cost matrix → 2D coordinates)
  - Interactive graph (zoom, pan, hover)
  - Color-coded routes với direction indicators
  - Tooltips hiển thị delivery/pickup info

## 🔜 Tính năng đang phát triển

🔨 Xuất Excel với nhiều sheet  
🔨 Upload multiple files  
🔨 Thêm điểm thủ công  
🔨 So sánh nhiều instance  

## 🛠️ Tech Stack

- **Backend**: Flask (Python 3.8+)
- **Frontend**: HTML, Bootstrap 5, JavaScript
- **Algorithms**: NumPy, SciPy
- **Visualization**: Plotly.js (planned)
- **Excel Export**: openpyxl, pandas (planned)

## 📚 Format File Input

File txt phải có format:
- **Cost matrix**: Ma trận chi phí di chuyển (n×n)
- **Delivery quantities**: Lượng hàng cần giao cho mỗi khách hàng
- **Pick-up quantities**: Lượng hàng cần nhận từ mỗi khách hàng
- **Vehicle capacity**: Tải trọng của mỗi xe

## 🐛 Troubleshooting

### Lỗi: ModuleNotFoundError
```bash
pip install -r requirements.txt
```

### Lỗi: Port 5000 already in use
Sửa trong `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

## 📧 Contact

Nếu có vấn đề hoặc câu hỏi, hãy tạo issue trên GitHub.

---

**Phiên bản**: 1.0.0 (Beta)  
**Ngày cập nhật**: January 2026
