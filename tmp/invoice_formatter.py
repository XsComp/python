# invoice_formatter.py



# We define variables in lowercase and unformatted, as per instruction.
name = "jane doe"
address = "14 main road"
invoice_no = 12345
amount_due = 4000
description = "jumping castle"
items = 2
cost = 2000

# We use a simple formula for calculating the total amount
total = items * cost

# We use the tab character (\t) for horizontal spacing as shown in the course material
print("\t\t\t" + "invoice".upper())
print()

'''
The following way of aligning the text using f-strings was found online
I used it here to match the layout style shown in the assignment.
https://docs.python.org/3/library/string.html#format-specification-mini-language
'''

# We print the customer name and invoice number with formatting,
print(f"{name:<40}{'invoice no:'.upper():<15}{invoice_no:>5}")

# the address and amount due, formatted with two decimal places,
print(f"{address:<38}{'amount due:'.upper():<15}{amount_due:>5.2f}")
print()

# the table headers with uppercase formatting and alignment,
print(f"{'description'.upper():<20}{'items'.upper():>10}{'cost'.upper():>15}{'total'.upper():>15}")
print("-" * 60)

# the line item details with the rewuested alignment and decimal formatting,
print(f"{description:<20}{items:>10}{cost:>15.2f}{total:>15.2f}")
print("-" * 60)

# before lastly print the total row, aligned with the totals column
print(f"{'total'.title():<45}{total:>15.2f}")
print("-" * 60)
