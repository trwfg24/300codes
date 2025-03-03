"""007-Viết chương trình để kiểm tra một năm có phải năm nhuận không
Giải thích đề bài
Bài tập yêu cầu bạn viết một chương trình để kiểm tra xem một năm có phải là năm nhuận hay không
Một năm là năm nhuận nếu:
1. Năm đó chia hết cho 4 và không chia hết cho 100 hoặc
2. Năm đó chia hết cho 400

Thuật toán giải quyết
Đầu vào:
- Một năm
Đầu ra:
- Thông báo cho ngời dùng biết năm đó có phải năm nhuận không

Các bước thực hiện
1. Định nghĩa hàm is_leap_year(year)
2. Nhập nm từ người dùng
3. Hiển thị kết quả"""

def is_leap_year(year):
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return f"{year} la nam nhuan"
    else:
        return f"{year} khong phai nam nhuan"

try:
    year = int(input("Nhap vao nam can kiem tra"))
    print(is_leap_year(year))
except:
    print("Gia tri nhap vao khong hop le")