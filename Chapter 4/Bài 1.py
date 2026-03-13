def thong_ke_tuple(t):
    tong = sum(t)
    lon_nhat = max(t)
    nho_nhat = min(t)

    return tong, lon_nhat, nho_nhat


numbers = (3, 7, 2, 9, 5)

tong, max_val, min_val = thong_ke_tuple(numbers)

print("Tổng:", tong)
print("Lớn nhất:", max_val)
print("Nhỏ nhất:", min_val)