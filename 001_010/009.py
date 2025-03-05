"""009 - Viết chương trình để in tất cả các số nguyên tố từ 1 đến 100
- Giải thích đề bài
Bài tập yêu cầu bạn viết một chương trình để in tất cả các số nguyên tố từ 1 đến 100.

- Thuật toán giải quyết
Đầu vào:
    Không có đầu vào từ người dùng.
Đầu ra:
    In ra tất cả các số nguyên tố từ 1 đến 100.
- Định nghĩa số nguyên tố
    Một số nguyên tố là một số tự nhiên lớn hơn 1, chỉ có hai ước là 1 và chính nó.

- Các bước thực hiện:
    Định nghĩa hàm is_prime(n):

    Hàm này nhận một tham số n là một số nguyên và kiểm tra xem số đó có phải là số nguyên tố hay không.
    Nếu n nhỏ hơn hoặc bằng 1, trả về False vì các số này không phải là số nguyên tố.
    Sử dụng vòng lặp for để kiểm tra từ 2 đến căn bậc hai của n (int(n**0.5) + 1). Nếu n chia hết cho bất kỳ số nào trong khoảng này, trả về False.
    Nếu không có số nào trong khoảng này chia hết n, trả về True.
    Định nghĩa hàm print_primes_up_to_100():

    Hàm này duyệt qua các số từ 1 đến 100.
    Sử dụng vòng lặp for để kiểm tra từng số trong khoảng từ 1 đến 100.
    Gọi hàm is_prime(number) để kiểm tra xem số đó có phải là số nguyên tố hay không.
    Nếu số đó là số nguyên tố, in ra số đó trên cùng một dòng, cách nhau bởi một dấu cách.
    Gọi hàm print_primes_up_to_100():

    Gọi hàm này để thực hiện việc in ra các số nguyên tố từ 1 đến 100."""

def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

def print_primes_up_to_100():
    for number in range(1, 101):
        if is_prime(number):
            print(number, end=" ")

print_primes_up_to_100()