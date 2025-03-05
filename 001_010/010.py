""" 010 - Viết chương trình để tìm ước số chung lớn nhất (USCLN) của hai số
- Giải thích đề bài
Bài tập yêu cầu bạn viết một chương trình để tìm ước số chung lớn nhất (USCLN) của hai số nguyên.

- Định nghĩa ước số chung lớn nhất
Ước số chung lớn nhất (USCLN) của hai số nguyên a và b là số lớn nhất chia hết cả hai số a và b.

- Thuật toán giải quyết
Để tìm USCLN, ta có thể sử dụng thuật toán Euclid, một phương pháp hiệu quả và dễ hiểu:

Nếu b = 0 thì USCLN(a, b) = a.
Ngược lại, tính USCLN(b, a % b).
- Các bước thực hiện: Định nghĩa hàm gcd(a, b):

    Hàm này nhận hai tham số a và b là hai số nguyên.
    Sử dụng vòng lặp while để lặp cho đến khi b bằng 0.
    Trong mỗi lần lặp, gán giá trị a cho b và b cho a % b (phép chia lấy dư).
    Khi b bằng 0, giá trị của a là USCLN của hai số ban đầu.
Nhập hai số nguyên từ người dùng:

    Sử dụng hàm input() để nhận dữ liệu từ người dùng.
    Chuyển đổi dữ liệu từ chuỗi sang số nguyên bằng hàm int().
    Sử dụng try-except để bắt lỗi nếu người dùng nhập vào không phải là số nguyên hợp lệ, từ đó in ra thông báo lỗi.
Hiển thị kết quả:

    Gọi hàm gcd() với hai tham số là hai số nguyên mà người dùng đã nhập.
In ra kết quả USCLN của hai số."""

def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a

try:
    num1 = int(input("Nhap vao so nguyen thu nhat: "))
    num2 = int(input("Nhap vao so nguyen thu hai: "))

    ucln = gcd(num1, num2)

    print(f"UCLN cua {num1} va {num2} la {ucln}")
except:
    print("Gia tri nhap vao khong hop le")