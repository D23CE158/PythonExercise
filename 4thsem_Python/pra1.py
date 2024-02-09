amount = int(input("Enter the total amount:"))
rate = float(input("Enter the interest rate:"))
duration = int(input("Enter the duration(in years):"))
total_interest = (amount * rate * duration)/100
print(f"Your Yearly interst is:{total_interest}")