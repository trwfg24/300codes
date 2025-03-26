"""
Viết hàm để kiểm tra một số có phải là số nguyên tố không
Giải thích đề bài
Bài tập yêu cầu bạn viết một hàm để kiểm tra xem một số có phải là số nguyên tố hay không.

Định nghĩa số nguyên tố
Một số nguyên tố là một số tự nhiên lớn hơn 1, chỉ có hai ước là 1 và chính nó.

Thuật toán giải quyết
Để kiểm tra xem một số n có phải là số nguyên tố hay không, bạn có thể làm theo các bước sau:

Nếu n nhỏ hơn hoặc bằng 1, thì n không phải là số nguyên tố.
Nếu n là 2 hoặc 3, thì n là số nguyên tố.
Nếu n chia hết cho 2 hoặc 3, thì n không phải là số nguyên tố.
Kiểm tra các số lẻ từ 5 đến căn bậc hai của n. Nếu n chia hết cho bất kỳ số nào trong khoảng này, thì n không phải là số nguyên tố.
Các bước thực hiện:
Định nghĩa hàm is_prime(n):

Hàm này nhận một tham số n là một số nguyên và kiểm tra xem số đó có phải là số nguyên tố hay không.
Nếu n nhỏ hơn hoặc bằng 1, trả về False vì các số này không phải là số nguyên tố.
Nếu n là 2 hoặc 3, trả về True vì 2 và 3 là các số nguyên tố.
Nếu n chia hết cho 2 hoặc 3, trả về False.
Sử dụng vòng lặp while để kiểm tra các số từ 5 đến căn bậc hai của n. Nếu n chia hết cho bất kỳ số nào trong khoảng này, trả về False.
Nếu không có số nào trong khoảng này chia hết n, trả về True.
Nhập số nguyên từ người dùng:

Sử dụng hàm input() để nhận dữ liệu từ người dùng.
Chuyển đổi dữ liệu từ chuỗi sang số nguyên bằng hàm int().
Sử dụng try-except để bắt lỗi nếu người dùng nhập vào không phải là số nguyên hợp lệ, từ đó in ra thông báo lỗi.
Hiển thị kết quả:

Gọi hàm is_prime() với tham số là số nguyên mà người dùng đã nhập.
In ra kết quả kiểm tra số nguyên tố.
"""
import math

def is_prime(n):
    if n <= 1:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:  # Kiểm tra i và i+2 (tức 6k-1 và 6k+1)
            return False
        i += 6  # Bỏ qua các số không có dạng 6k ± 1

    return True

try:
    number = int(input("nhap vao so can kiem tra"))
    if is_prime(number):
        print(f"so {number} la so nguyen to")
    else:
        print(f"so {number} khong phai la so nguyen to")
except:
    print("vui long nhap vao mot so tu nhien")

