print("Enter a number")
num = int(input())
a = 0
b = 1
i = 0
print(a)
print(b)
while i < num:
    c = a + b
    a = b
    b = c
    print(c)
    i = i + 1
print("This is Fibonacci Serice upto " + str(num))
