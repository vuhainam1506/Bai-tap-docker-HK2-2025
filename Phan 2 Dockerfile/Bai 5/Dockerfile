# Stage 1: Build ứng dụng Go
FROM golang:1.21 AS builder

# Thiết lập thư mục làm việc
WORKDIR /app

# Sao chép mã nguồn vào container
COPY main.go ./

# Build ứng dụng Go thành file nhị phân
RUN go mod init hello-go && go build -o hello-go

# Stage 2: Chạy ứng dụng với image nhẹ
FROM alpine:latest

# Thiết lập thư mục làm việc
WORKDIR /app

# Sao chép file nhị phân từ stage builder
COPY --from=builder /app/hello-go ./

# Mở cổng 8080
EXPOSE 8080

# Chạy ứng dụng
CMD ["./hello-go"]