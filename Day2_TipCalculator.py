# Creating a greeting message
print("Welcome to tip calculator!")

# Asking for total bill
bill_amount = float(input("What was the total bill? $"))

# Asking for tip
tip_percent = int(input("How much percent tip would you like to give? 10, 20, or 15? "))
# Calculating tip
tip = bill_amount*tip_percent/100

# Number of people splitting
total_people = int(input("How many people to split the bill? "))

# Total amount after adding tip
amount_per_person = (bill_amount+tip)/total_people
# Rounding the final amount to 2 decimal place
round_amount = round(amount_per_person, 2)
# Formatting the amount at 2 decimal place
final_amount = "{:.2f}".format(amount_per_person)

# Display amount one should pay
print(f"Each person should pay: ${final_amount}")
