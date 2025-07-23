#import
import sys

#Welcome Message

print("Welcome to Calculator")
#Debriefing and control

try:
    num1= int(input("Enter the first number:"))
except ValueError:
    print("Dont use Letters!")
    sys.exit()
operat = input("Choose an operation(+, -, / or *):")
try:
    num2 = int(input("Enter the second number:"))
except ValueError:
    print("Dont use Letters!")
    sys.exit()

#Main Process
if operat == "+":
    print("Your Result:", num1 + num2)
elif operat == "-":
    print("Your Result:", num1 - num2)
elif operat == "*":
    print("Your Result:", num1 * num2)
elif operat == "/":
    if num2 == 0:
        print("Do not operate with zero.")
    else:
        print("Your Result:", num1 / num2)
else:
    print("You did not enter the operation correctly.")