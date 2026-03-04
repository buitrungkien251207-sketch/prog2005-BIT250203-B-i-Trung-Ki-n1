arr = list(map(int, input("Nhập các số: ").split()))

total = 0
print("Các số chẵn:")
for num in arr:
    if num % 2 == 0:
        print(num)
        total += num

print("Tổng các số chẵn:", total)