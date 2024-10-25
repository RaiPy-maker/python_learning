# INTEREST CALCULATOR

principle = 0
rate = 0
time = 0

principle = float(input("Please enter the amount of money you would like to loan: "))

while principle <= 0:
    principle = float(input("Please enter the amount of money you would like to loan: "))
    if principle <= 0:
        print("Please enter a valid amount")

while rate <= 0:
    rate = float(input("Please enter the interest rate \n(do not use symbols): "))
    if rate <= 0:
        print("Please enter a valid amount")

while time <= 0:
    time = float(input("Please enter the time for the loan: "))
    if time <= 0:
        print("Please enter a valid amount")


result = principle * pow((1 + rate / 100), time)

print(f"\n\n Heres the calculatet interest \n\n In {time} years with the rate of {rate}% the ${principle:,.2f} will be {result:,.2f}")



