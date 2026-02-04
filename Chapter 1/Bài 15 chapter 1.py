for i in range(3):
    print(f"\nSinh viên {i+1}")
    name = input("Tên: ")
    math_score = float(input("Điểm Toán: "))
    physics_score = float(input("Điểm Lý: "))
    chemistry_score = float(input("Điểm Hóa: "))

    average = (math_score + physics_score + chemistry_score) / 3
    print(f"{name} có điểm trung bình: {average:.2f}")