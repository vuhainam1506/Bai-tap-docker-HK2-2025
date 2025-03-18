# Sử dụng image python:3.9 làm base image
FROM python:3.9

# Thiết lập thư mục làm việc trong container
WORKDIR /app

# Sao chép file requirements.txt và cài đặt dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ mã nguồn vào container
COPY . .

# Mở cổng 5000 để truy cập từ bên ngoài
EXPOSE 5000

# Thiết lập biến môi trường để Flask chạy ở chế độ production
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Lệnh chạy ứng dụng khi container khởi động
CMD ["flask", "run"]