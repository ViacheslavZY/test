a = int(input())
b = int(input())
c = int(input())
if a and b and c > 0 and (max(a, b, c) < (a + b + c - max(a, b, c))):
    p = (a + b + c) / 2
    print("Площадь треугольника = ", (p * (p - a) * (p - b) * (p - c)) ** 0.5)
else:
    print("Треугольника с такими сторонами не существует!")
