""" 008 - Viết chương trình để đếm số lượng số chẵn và lẻ trong một danh sách
- Giải thích đề bài
Bài tập yêu cầu bạn viết một chương trình để đếm số lượng số chẵn và số lẻ trong một danh sách các số nguyên.

- Thuật toán giải quyết
 Đầu vào:
Một danh sách các số nguyên.
 Đầu ra:
Số lượng số chẵn.
Số lượng số lẻ.
- Các bước thực hiện:
 Định nghĩa hàm count_even_odd(numbers):

 Hàm này nhận một danh sách numbers chứa các số nguyên.
 Khởi tạo hai biến count_even và count_odd để đếm số lượng số chẵn và số lẻ.
 Sử dụng vòng lặp for để duyệt qua từng số trong danh sách:
 Nếu số đó chia hết cho 2 (number % 2 == 0), tăng biến count_even lên 1.
 Ngược lại, tăng biến count_odd lên 1.
 Trả về số lượng số chẵn và số lẻ.
 Nhập danh sách các số nguyên từ người dùng:

 Sử dụng hàm input() để nhận dữ liệu từ người dùng dưới dạng chuỗi.
 Tách chuỗi thành các phần tử bằng cách sử dụng split() và chuyển đổi từng phần tử thành số nguyên bằng cách sử dụng int(). Sử dụng list comprehension để thực hiện việc này: [int(num) for num in input_list.split()].
Hiển thị kết quả:

 Gọi hàm count_even_odd() với tham số là danh sách các số nguyên mà người dùng đã nhập.
 In ra số lượng số chẵn và số lẻ dựa trên kết quả trả về của hàm.
"""

def count_even_odd(numbers):
    count_even = 0
    count_odd = 0

    for i in numbers:
        if i % 2 == 0:
            count_even += 1
        else:
            count_odd += 1

    return count_even, count_odd

try:
    input_list = input("Nhap vao cac so nguyen cac nhau boi dau cach")
    numbers = [int(num) for num in input_list.split()]

    count_even, count_odd = count_even_odd(numbers)

    print(f"so luong so chan: {count_even}")
    print(f"so luong so le: {count_odd}")
except:
    print("Gia tri khong hop le")