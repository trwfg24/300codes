"""
001-Viết chương trình để kiểm tra số nguyên dương hay âm.

Giải thích đề bài
Bài tập yêu cầu bạn viết một chương trình để kiểm tra xem một số nguyên mà người dùng nhập vào là số dương hay âm.

Thuật toán giải quyết
Đầu vào:
- Một số nguyên mà người dùng nhập vào.
Đầu ra:
- Thông báo cho người dùng bết số đó là số dương hay âm

Các bước thực hện:
1. Nhập một số nguyên từ người dùng.
2. Kiểm tra số đó có lớn hơn 0 không:
- Nếu lớn hơn 0, thì đó là số dương.
- Nếu nhỏ hơn 0, thì đó là số âm.
- Nêu bằng 0, chúng ta có thể xem như là một trường hợp đặc biệt và thông báo rằng số đó không phải là số dương cũng không phải là số âm.
"""

#Chương trình kiểm tra số nguyên dương hay âm
def check_number(n):
    if n > 0:
        return "So ban nhap la so duong."
    elif n < 0:
        return "So ban nhap la so am."
    else:
        return "So ban nhap khong phai so duong cung khong phai so am."

try:
    number = int(input("Nhap vao mot so nguyen: "))
    result = check_number(number)
    print(result)
except ValueError:
    print("Vui long nhap vao mot so nguyen.")