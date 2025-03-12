"""Viết hàm để tính giai thừa của một số
Giải thích đề bài
Bài tập yêu cầu bạn viết một hàm để tính giai thừa của một số nguyên. Giai thừa của một số nguyên dương n (ký hiệu là n!) là tích của tất cả các số nguyên dương từ 1 đến n.

Thuật toán giải quyết
Để tính giai thừa của một số nguyên dương n, ta có thể sử dụng hai phương pháp:

Đầu vào:

Một số nguyên dương n.
Đầu ra:

Giai thừa của số nguyên dương n.
Các bước thực hiện:


Định nghĩa hàm factorial_recursive(n):

Hàm này nhận một tham số n là một số nguyên và tính giai thừa của nó bằng cách sử dụng đệ quy.
Nếu n nhỏ hơn 0, trả về thông báo lỗi.
Nếu n bằng 0 hoặc 1, trả về 1 (cơ sở của đệ quy).
Ngược lại, trả về n nhân với giai thừa của n-1.
Nhập số nguyên dương từ người dùng:

Sử dụng hàm input() để nhận dữ liệu từ người dùng.
Chuyển đổi dữ liệu từ chuỗi sang số nguyên bằng hàm int().
Sử dụng try-except để bắt lỗi nếu người dùng nhập vào không phải là số nguyên hợp lệ, từ đó in ra thông báo lỗi.
Hiển thị kết quả:

Gọi hàm  factorial_recursive() với tham số là số nguyên dương mà người dùng đã nhập.
In ra kết quả giai thừa của số đó."""

def factorial_recursive(n):
    if n < 0:
        return "Error"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

try:
    num = int(input("Nhap vao so nguyen n "))
    kq = factorial_recursive(num)
    print(f"Giai thua cua {num} la {kq}")
except:
    print("Gia tri nhap vao khong hop le")