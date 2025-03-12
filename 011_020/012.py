"""Viết hàm để tính tổng các số từ 1 đến n
Giải thích đề bài
Bài tập yêu cầu bạn viết một hàm để tính tổng các số từ 1 đến n.

Thuật toán giải quyết
Để tính tổng các số từ 1 đến n, ta có thể sử dụng công thức tính tổng của một dãy số liên tiếp hoặc sử dụng vòng lặp để tính tổng.

Công thức tính tổng của các số từ 1 đến n là: Tổng = (n * (n + 1))/2

Các bước thực hiện:
Định nghĩa hàm sum_of_numbers(n):

Hàm này nhận một tham số n là một số nguyên và tính tổng các số từ 1 đến n bằng công thức: Tổng = (n * (n + 1))/2
Nếu n nhỏ hơn 1, trả về thông báo lỗi.
Trả về kết quả tổng theo công thức.
Nhập số nguyên dương từ người dùng:

Sử dụng hàm input() để nhận dữ liệu từ người dùng.
Chuyển đổi dữ liệu từ chuỗi sang số nguyên bằng hàm int().
Sử dụng try-except để bắt lỗi nếu người dùng nhập vào không phải là số nguyên hợp lệ, từ đó in ra thông báo lỗi.
Hiển thị kết quả:

Gọi hàm sum_of_numbers() với tham số là số nguyên dương mà người dùng đã nhập.
In ra kết quả tổng các số từ 1 đến số đó."""

def sum_of_numbers(n):
    return (n * (n + 1)) / 2

try:
    number = int(input("Nhap vao so nguyen duong n "))
    if number < 1:
        print("Loi")
    else:
        kq = sum_of_numbers(number)
        print(f"Tong cac so nguyen tu 1 den {number} la {kq}")
except:
    print("Gia tri nhap vao khong hop le")