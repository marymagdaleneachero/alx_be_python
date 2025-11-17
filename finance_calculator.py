# User Input for Financial Details:
monthly_income = int(input("Enter your monthly income: "))
monthly_xpenses = int(input("Enter your total monthly expenses: "))

# Calculate Monthly Savings
monthly_savings = monthly_income - monthly_xpenses

# Project Annual Savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
