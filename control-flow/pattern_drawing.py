rows = int(input("Enter the size of the pattern: "))
num = 0
while int(num) < rows:
    for i in range(1, rows + 1):
        print("*",end="")
    print()
    num += 1

