lower = int(input("Enter lower range: "))
upper = int(input("Enter the upper range: "))

for num in range(lower, upper):
    if num > 1:
        for i in range(2, num):
            if(num % i) == 0:
                print(num)
                break

