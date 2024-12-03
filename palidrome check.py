
num = int(input('Enter a number'))

is_palindrome = str(num) == str(num)[::-1]

if is_palindrome:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
