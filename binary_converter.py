binary_table = ["0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010"]

def get_binary():
    while True:
        user_input = input("Please enter a number between 1 and 10 (type 'exit' to quit): ").strip().lower()

        # Let the user exit the loop
        if user_input == "exit":
            print("C ya l8ter alig8or!")
            break

        try:
            decimal = int(user_input)

            if decimal < 1 or decimal > 10:
                print("Error: Value must be between 1 and 10.\n"
                "Try holding up your hands — no number higher than the amount of fingers.\n" \
                "While you're at it, make sure it's not 0 or negative...\n")
                continue

            binary = binary_table[decimal - 1]
            print(f"\nDecimal | Binary")
            print("-" * 16)
            print(f"{decimal:<7} | {binary}\n")

        except ValueError:
            print(f"Error: Please enter a valid number between 1 and 10.\nDoes \"{user_input}\" look like a number too you?\n")

# Run the function
get_binary()
