n = int(input("Nhập n: "))
if n < 2:
    print("Không phải số nguyên tố")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Không phải số nguyên tố")
            break
    else:
        print("Là số nguyên tố")