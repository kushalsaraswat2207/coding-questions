def is_palindrome(number):
    number = str(number)
    return number == number[::-1]


n = input("Enter a number: ")

if is_palindrome(n):
    print("Palindrome")
else:
    print("Not a palindrome")