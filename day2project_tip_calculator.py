#If the bill was $150.00, split between 5 people, with 12% tip.
print("Welcome to the Tip Calculator!")
bill = float(input("What was the total Bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

#Each person should pay (150.00 / 5) * 1.12 = 33.6
bill_with_tip = ((tip/100)*bill)+bill
print(f"Total bill with tip: {bill_with_tip}")
bill_per_person = bill_with_tip/people

#Format the result to 2 decimal places = 33.60
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each Person should pay: ${final_amount}")
