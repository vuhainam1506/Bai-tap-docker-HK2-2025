# Sử dụng image node:18-alpine làm base image
FROM node:18-alpine

# Thiết lập thư mục làm việc trong container
WORKDIR /app

# Sao chép file package.json và package-lock.json (nếu có)
COPY package.json package-lock.json* ./

# Cài đặt dependencies
RUN npm install

# Sao chép toàn bộ mã nguồn vào container
COPY . .

# Build ứng dụng React
RUN npm run build

# Mở cổng 3000 để truy cập từ bên ngoài (mặc định của React development server)
EXPOSE 3000

# Lệnh chạy ứng dụng khi container khởi động
CMD ["npm", "start"]