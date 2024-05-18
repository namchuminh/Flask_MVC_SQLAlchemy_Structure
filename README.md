# Flask MVC SQLAlchemy 
- Xây dựng cấu trúc cho 1 dự án Flask theo mô hình MVC có sử dụng SQLAlchemy

# Tổ chức thư mục
```
project/
|
├── templates/
|   └── index.html
|
├── migrations/ **
|   └── ...
|
├── routes/
|   └── user_bp.py
|
├── models/
|   └── User.py
|
├── controllers/
|   └── UserController.py
|
├── app.py
└── config.py
```

# Hướng dẫn cài đặt
- Tạo thư mục cho dự án cần sử dụng
- Clone source code này về thư mục đã tạo:
```
git clone https://github.com/namchuminh/Flask_MVC_SQLAlchemy_Structure.git
```

- Tạo CSDL, thay đổi chuỗi kết nối trong file `config.py`
```
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/flask_ecommerce'
```

# Hướng dẫn về migrations
- Lệnh: ```flask db init``` - Khởi tạo thư mục migrations trong dự án
- Lệnh: ```flask db migrate -m "mo ta migrate" ``` - Tạo một migration mới dựa trên các thay đổi trong mô hình dữ liệu
- Lệnh: ```flask db upgrade``` - Áp dụng các migrations lên cơ sở dữ liệu
- Lệnh: ```flask db downgrade``` - Hoàn tác các migrations đã áp dụng trước đó

# Khởi chạy
- Lệnh chạy server: ``python app.py``
- Mặc định server sẽ chạy trên: <b>127.0.0.1:5000</b>
