"""005-Viết chương trình để tính điểm trung bình và xếp loại học sinh.

Giải thích đề bài
Bài tập yêu cầu bạn viết một chương trình để tính điểm trung bình của học sinh dựa trên các điểm số của các môn học và xếp loại học sinh dựa trên điểm trung bình.

Giả định và điểm số và xếp loại:
- Điểm trung bình >= 8.5: Xuất sắc
- Điểm trung bình >= 7.0 và < 8.5: Giỏi
- Điểm trung bình >= 5.5 và < 7.0: Khá
- Điểm trung bình >= 4.0 và < 5.5: Trung bình
- Điểm trung bình < 4.0: Yếu
- Thuật toán giải quyết
Đầu vào:
Điểm số của các môn học (một danh sách các số thực).

Đầu ra:
Điểm trung bình.
Xếp loại học sinh.

Các bước thực hiện:
1. Nhập điểm số của các môn học từ người dùng.
2. Tính điểm trung bình.
3. Xếp loại học sinh dựa trên điểm trung bình.
4. In ra điểm trung bình và xếp loại."""

#Chương trình tính điểm trung bình và xếp loại học sinh
def calculate_average(scores):
    return sum(scores) / len(scores)

def classify_student(average):
    if average >= 8.5:
        return "Xuat sac"
    elif average >= 7.0:
        return "Gioi"
    elif average >= 5.5:
        return "Kha"
    elif average >= 4.0:
        return "Trung binh"
    else:
        return "Yeu"

try:
    scores = []
    num_subjects = int(input("Nhap vao so luong mon hoc: "))
    if num_subjects <= 0:
        print("So luong mon hoc phai duoc nho nhat 1.")
    else:
        for i in range(num_subjects):
            score = float(input("Nhap vao diem mon hoc thu " + str(i + 1) + ": "))
            if score < 0 or score > 10:
                print("Diem mon hoc phai duoc nho nhat 0 va nho nhat 10.")
                break
            scores.append(score)

        if len(scores) == num_subjects:
            average = calculate_average(scores)
            classification = classify_student(average)
            print(f"Diem trung binh cua hoc sinh la: {average:.2f}")
            print(f"Xep loai hoc sinh la: {classification}")
except ValueError:
    print("Vui long nhap vao so luong mon hoc hop le.")