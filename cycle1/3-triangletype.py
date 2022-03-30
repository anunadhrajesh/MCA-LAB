print("Input lengths of the triangle sides: ")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
    print("It is a Equilateral triangle")
elif x == y or y == z or z == x:
    print("It is a Isosceles triangle")
else:
    print("It is a Scalene triangle")
