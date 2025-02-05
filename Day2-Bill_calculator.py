print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15"))
people = int(input("How many people to split the bill?"))
tip_as_percentage = tip/100
total_tip_amount = bill + tip_as_percentage
total_bill = bill + total_tip_amount
bill_per_person = total_tip_amount/people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay {final_amount}$")