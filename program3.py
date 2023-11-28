a = int(input("Enter the number of pennies: "))
b = int(input("Enter the number of nickels: "))
c = int(input("Enter the number of dimes: "))
d = int(input("Enter the number of quarters: "))

x=Penny_value = 1
y=Nickle_value= 5
z= Dime_value = 10
c=Quarter_value = 25
v=Pennis_in_dollar = 100

totalCent = (a * x) + (b * y ) + (c * z) + (d * v)
totalDollars = totalCent / v


if totalDollars > 1:
    print("Oo,Entered amount was more than one dollar.")
elif totalDollars < 1:
    print("Sorry,Entered amount was less than one dollar.")
else:
    print("Congratulations! The amount you entered was exactly one dollar! You win the game!")
