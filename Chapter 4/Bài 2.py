def tinh_diem_trung_binh(ds_sv):
    tong = sum(ds_sv.values())
    so_sv = len(ds_sv)
    return tong / so_sv


students = {
    "An": 8,
    "Bình": 7,
    "Chi": 9
}

dtb = tinh_diem_trung_binh(students)

print("Điểm trung bình:", dtb)