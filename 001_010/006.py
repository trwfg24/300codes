"""006-Viết chương trình để in bảng cửu chương
Giải thích đề bài
Bài tập yêu cầu bạn viết một chương trình để in bảng cửu chương từ 1 đến 10. Bảng cửu chương là baảng nhân, nơi mỗi ố từ 1 đến 10 được nhân với các số từ 1 đê 10.

Thuật toán giải quyết
Đầu vào:
- Không có đầu vào từ người dùng
Đầu ra:
- In ra bảng cửu chương từ 1 đến 10

Các bước thực hiện:
1. Sử dụng vòng lặp lồng nhau để duyệt qua các số từ 1 dến 10
2. Ở vòng lặp ngoài, duyệt qua từng số ừ 1 đến 10
3. Ở vòng lặp trong, duyệt qua từng số từ 1 đến 10
4. In ra kết quả của phép nhân giũa số bị nhân và số nhân"""

#Chương trình in bẳng cửu chương từ 1 đến 10
def print_multiplication_table():
    for i in range(1,11):
        print(f"Bang cuu chuong {i}:")
        for j in range(1,11):
            print(f"{i} * {j} = {i*j}")
        print()

print_multiplication_table()