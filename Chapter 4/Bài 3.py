students = {
    "An": 8,
    "Bình": 7,
    "Chi": 9
}

key = input("Nhập tên sinh viên cần kiểm tra: ")

if key in students:
    print("Key tồn tại trong dictionary")
else:
    print("Key không tồn tại")