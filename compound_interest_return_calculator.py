#1

import os
os.system('clear')

#2

print("\nFor how many years do you plan to save money?\n")
years = int(input("Please enter in full years: "))

#3

print("\nWhat is your principal investment?\n")
principal_amount = float(input("Please enter your principal investment: "))

#4

print("\nWhat is your monthly contribution?\n")
monthly_contribution = float(input("Please enter your monthly contribution: "))

#5

print("\nWhat is your expected annual return on investment?\n")
interest = float(input("Please enter your expected annual return rate in decimal numbers (10% = 0.1): "))

print('')

# Two Parts: 1. Compound returns for the principal 2. Future Value of a series of monthly contributions

final_wealth = 0

for i in range(0, years):
    if final_wealth == 0:
        final_wealth = principal_amount
    
    final_principal_value = principal_amount * (1 + (interest / 12))**(12 * years)
    final_monthly_contribution_value = monthly_contribution * (((1 + (interest / 12))**(12 * years) - 1) / (interest / 12)) * (1 * (interest / 12))
    final_wealth = final_principal_value + final_monthly_contribution_value

print(f"{final_wealth} is your accumulated wealth after {years} years.")