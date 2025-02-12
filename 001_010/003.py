"""003-Viết chương trình tìm số lớn nhất trong ba số.

Giải thích đề bài
Bài tập yêu cầu bạn viết một chương trình để tìm số lớn nhất trong ba số nguyên mà người dùng nhập vào.

Thuật toán giải quyết
Đầu vào:
- Ba số nguyên mà người dùng nhập vào
Đầu ra:
- Thông báo cho người dùng biết số lớn nhất trong ba số đó

Các bước thực hiện:
1. Nhập ba số nguyên từ người dùng.
2. So sánh ba số để tìm ra số lớn nhất:
- Sử dụng các cấu trúc điều kiện if-elif-else để so sánh từng cặp số và xác định số lớn nhất."""

#Chương trình tìm số lớn nhất trong ba số

def find_max_of_three(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

try:
    num1 = int(input("Nhap vao mot so nguyen thu 1: "))
    num2 = int(input("Nhap vao mot so nguyen thu 2: "))
    num3 = int(input("Nhap vao mot so nguyen thu 3: "))
    result = find_max_of_three(num1,num2,num3)
    print("So lon nhat trong ba so ban nhap la:",result)
except ValueError:
    print("Vui long nhap vao mot so nguyen.")