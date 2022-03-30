print("Equation: ax^2 + bx + c")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = b ** 2 - 4 * a * c
d1 = d**0.5
if d < 0:
    print("The roots are imaginary.")
elif d == 0:
    r = -b / 2 * a
    print("single root: ", round(r, 2))
else:
    r1 = (-b + d1)/2 * a
    r2 = (-b - d1)/2 * a
    print("two roots")
    print("First root: ", round(r1, 2))
    print("Second root: ", round(r2, 2))
