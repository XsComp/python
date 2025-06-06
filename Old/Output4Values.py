# Filename - Output4Values.py

def main():
    
    # Ask the user to input four string values
    
    Love = input("Enter the name of a beautiful thing : ")
    Beautiful = input("What is the most beautiful THING you have ever seen? : ")
    Smell = input("What is your favorite smell : ")
    Qute = input("Make up a cute nickname for a super cure girl : ")
    
    # Print all values in one line, separated by a semicolon, with ". Output complete!" at the end
    
    print(f"You {Love}. You look like a {Beautiful} and smell like a {Smell}... {Qute}. Output complete!", end="")

if __name__ == "__main__":
    main()