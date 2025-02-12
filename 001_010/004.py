"""004-Chương trình tính tiền taxi du trên số km đã đi

Giải thích đề bài
Bài tập yêu cầu bạn viết một chương trình để tính tiền taxi dựa trên số km mà người dùng đã đi. Giá cước taxi có thể được tính theo các mức giá khác nhau dựa trên số km đã đi.

Giả định về gi cước (có thể thay đổi theo yêu cầu cụ thể):
1. Km đầu tiên: 10.000 VND
2. Từ km thứ 2 đến km thứ 10: 8.500 VND
3. Từ km thứ 11 trở đi: 7.500 VND

Thuật toán giải quyết
Đầu vào:
- Số km mà người dùng đã đi (một số thực).
Đầu ra:
- Tổng tiền taxi

Các bước thực hiện:
1. Nhập số km đã đi từ người dùng
2. Tính tổng tiền taxi dựa trên số km đã đi theo các mức giá đã cho
3. In ra tổng tiền taxi
"""

#Chương trình tính tiền taxi dựa trên số km đã đi
def calculate_taxi_fare(km):
    if km <= 1:
        fare = 10.000
    elif km <= 10:
        fare = 10.000 + (km - 1) * 8.500
    else:
        fare = 10.000 + 9 * 8.500 + (km - 10) * 7.500
    return fare

try:
    km = int(input("Nhap vao km: "))
    result = calculate_taxi_fare(km)
    print("Tong taxi la:",result,"VND")
except ValueError:
    print("Vui long nhap vao mot so hop le.")