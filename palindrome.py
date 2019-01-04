num = input('Enter any number : ')
try:
    val = int(num)
    if num == str(num)[::-1]:
       print("enter the given number is PALINDROME")
    else:
       print("enter the given number is NOT a palindrome")
except ValueError:
       print("That's not a valid number, Try Again !")
