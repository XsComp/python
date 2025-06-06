'''
Many of the questions on the PRG exam require you to use exception handling
to deal with any programming errors that could happen.
It is not necessary to cater for every type of exception that can occur
but keep in mind that sometimes applying proper exception handling
can make it much easier to create your solution to the problem.

Generally speaking, most questions have 2 marks available for exception handling
These questions will say something about managing errors or dealing with exceptions
'''

# Define a list of cars
cars = ["Toyota Corolla", "VW Golf GTI", "BMW M3", "Nissan GTR", "Porche GT3 RS"]

'''
The bare minimum, generic approach 1/2 Exception Handling marks
'''
# Output a price point menu
print("1. NOK 150,000.00")
print("2. NOK 400,000.00")
print("3. NOK 900,000.00")
print("4. NOK 1,200,000.00")
print("5. NOK 1,500,000.00")

# Beginning of the try block
try:
    # Get user input and cast the value to an integer
    selection = int(input("Select a price point (1-5): "))
    # Output the associated car for the chosen price point
    print("A vehicle at that price point is the", cars[selection-1])
# Beginning of the except block
except Exception as e: # Handle any exception with the alias 'e'
    print("An error occurred:", e)

print("\n")

'''
The better more explicit and informative approach 2/2 Exception Handling marks
'''
# Output a price point menu
print("1. NOK 150,000.00")
print("2. NOK 400,000.00")
print("3. NOK 900,000.00")
print("4. NOK 1,200,000.00")
print("5. NOK 1,500,000.00")

try:
    # Get user input and cast the value to an integer
    selection = int(input("Select a price point (1-5): "))
    # Output the associated car for the chosen price point
    print("A vehicle at that price point is the", cars[selection-1])
# Catch value conversion errors
except ValueError as v:
    print("You entered text instead of a number.")
    print(f"You need to enter a number between 1 and {len(cars)}.")
# Catch list indexing errors
except IndexError as i:
    print(f"Invalid selection. You need to enter a number between 1 and {len(cars)}")
# Catch other types of exceptions that are not index or value errors
except Exception as e:
    print("An unknown error occurred:", e)
finally:
    print("The program will now exit.")