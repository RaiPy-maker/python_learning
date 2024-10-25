rows = int(input("Please insert the amount of row: "))
column = int(input("Please insert the amount of colums: "))
symbol = input("Please enter a symbol ")

for x in range(0, rows):
    for i in range(0, column):
        print(symbol, end="")
    print()
