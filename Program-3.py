def odd_series(x):
    count = x if x % 2 != 0 else x - 1  # only print if x is odd, else x-1
    num = 1
    c = 0
    while c < count:
        print(num, end=" ")
        num += 2
        c += 1

x = int(input("Enter a number: "))

if x > 0:
    odd_series(x)
else:
    print("Enter a positive integer!")
