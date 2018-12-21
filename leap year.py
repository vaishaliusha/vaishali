def printLeapYear():
  print("Input enter the Year is a Leap Year")
def printNotLeapYear():
  print("Input enter the Year is not a Leap Year")
input_year = int(input("Enter the Year is leap or not: "))
if input_year % 4 == 0:
if input_year % 100 == 0 :
if input_year % 400 == 0 :
    printLeapYear()
 else :
    printNotLeapYear()
 else :
    printLeapYear()
 else :
    printNotLeapYear()
