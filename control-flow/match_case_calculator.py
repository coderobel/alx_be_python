num1 = input("Enter the first number:")
num2 = input("Enter the second number:")
operation = input("Choose the operation (+, -, *, /):")
sum = 0
product = 0
quotient = 0
difference = 0
match operation:
    case "+":
        sum = int(num1) + int(num2)
        print("The result is " + str(sum))
    case "-":
        difference = int(num1) - int(num2)
        print("The result is " + str(difference))
    case "*":
        product = int(num1) * int(num2)
        print("The result is " + str(product))
    case "/":
        quotient =  int(num1) / int(num2)
        print("The result is " + str(quotient))
