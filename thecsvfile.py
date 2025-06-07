# thecsvfile.py



import os

data = [[1, 2, 3, 4, 5, 6],
        [7, 8, 9, 10, 11, 12],
        [13, 14, 15, 16, 17, 18]]

csv_file = "the_file.csv"

try:
    # We first check if the file exists by using "os" module.
    if os.path.exists(csv_file):
        file = open(csv_file, "a")  # Appends if file exists
    else:
        file = open(csv_file, "w")  # Otherwise, creates a new file and writes

    # We write or append data to file in CSV format
    for row in data:
        line = ",".join(str(item) for item in row)
        file.write(line + "\n") 

except Exception as e:
    print("Something bad happened:", e)

finally:
    try:
        file.close()    # We close the file to ensure the resource is released.
    except NameError:   # If file was never opened, we catch the error.
        pass            # This is to avoid an error if the file variable was never created.
