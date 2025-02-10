"""002 - Viết chương trình kiểm tra số chăn hay lẻ

Giải thích đề bài
Bài tập yêu câu bạn viết một chương trình để kiểm tra xem một số nguyên mà người dùng nhập vào là số chẵn hay số lẻ

Thuật toán giải quyết
Đầu vào:
- Một số nguyên mà người dùng nhập vào.DĐ
Đầu ra:
- Thông báo cho người dùng biết số đó là số chẵn hay số lẻ.

Các bước thực hiện:
1. Nhập một số nguyên từ người dùng.
2. Kiểm tra số đó có chia hết cho 2 không:
 - Nếu chia hết cho 2, thì số đó là số chẵn.
 - Nếu không chia hết cho 2, thì số đó là số lẻ."""

# Chương trình kiểm tra số chẵn hay lẻ

def check_even_old(n):
    if n % 2 == 0:
        return "So ban nhap la so chan."
    else:
        return "So ban nhap la so le."

try:
    number = int(input("Nhap vao mot so nguyen: "))
    result = check_even_old(number)
    print(result)
except ValueError:
    print("Vui long nhap vao mot so nguyen.")
