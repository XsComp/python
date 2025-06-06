'''
String Handling Sample Question:
Given the following variables:
'''

name = "jane doe"
items = ["mascara","lipstick","hair extensions", "handbag"]
prices:list[float] = [48.49, 19, 109.99, 250]
total = 0
currency = 'nok'

'''
Devise a strategy to produce the following invoice
by utilizing the variables provided.

-------------------------------------
INVOICE                  NO.      123
-------------------------------------
               Jane Doe              
-------------------------------------
Mascara                  NOK    48.49
Lipstick                 NOK    19.00
Hair Extensions          NOK   109.99
Handbag                  NOK   250.00
-------------------------------------
Total                    NOK   427.48
-------------------------------------

You may declare any additional variables you feel you need.
'''

for price in prices:
    total += price

formatted_total = "{:.2f}".format(float(total))

# good answer 9/10
# What did I miss? Can you fix it to get 10/10?
print("10/10 Answer")
# Use of title, center, upper, rjust, ljust and number formatting
print("-" * 40)
print(f"{'invoice'.upper().ljust(28)}{'no.'.upper().rjust(3)}{'123'.rjust(9)}")
print("-" * 40)
print(name.title().center(40))
print("-" * 40)
for entry in zip(items, prices):
    print(f"{entry[0].title().ljust(28)}{currency.upper().rjust(3)}{str(entry[1]).rjust(9)}")
print("-" * 40)
print(f"{'total'.title().ljust(28)}{currency.upper().rjust(3)}{str(formatted_total).rjust(9)}")
print("-" * 40)

# Bad answer 1/10
print("\n1/10 Answer")
# Hard coded, no use of formatting functions or variable manipulation
print("----------------------------------------")
print("INVOICE                     NO.      123")
print("----------------------------------------")
print("                Jane Doe                ")              
print("----------------------------------------")
print("Mascara                     NOK    48.49")
print("Lipstick                    NOK    19.00")
print("Hair Extensions             NOK   109.99")
print("Handbag                     NOK   250.00")
print("----------------------------------------")
print("Total                       NOK   427.48")
print("----------------------------------------")
