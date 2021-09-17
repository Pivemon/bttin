from math import sqrt
print("Giải phương trình bậc 2: ax^2 + bx + c = 0, điều kiện: delta > 0")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
delta = b ** 2 - 4 * a * c

if delta > 0:
        print("Phương trình có 2 nghiệm phân biệt!")
        print("x1 = ", float((-b - sqrt(delta)) / (2 * a)))
        print("x2 = ", float((-b + sqrt(delta)) / (2 * a)))
else:
    print('Phương trình vô nghiệm')    