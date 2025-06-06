def print_roof(height):
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        blocks = 'X' * (2 * i + 1)
        print(spaces + blocks)

def print_walls(height, width):
    for _ in range(height):
        print('|' + ' ' * (width - 2) + '|')

def print_base(width):
    print('-' * width)

def main():
    print("Welcome to MegaHouse Builder! 🏰")
    try:
        roof_height = int(input("Enter roof height (suggested: 3-10): "))
        wall_height = int(input("Enter wall height (suggested: 2-8): "))
    except ValueError:
        print("Please enter valid numbers next time!")
        return

    # Width of the house is based on the bottom width of the roof
    house_width = roof_height * 2 - 1

    print("\nBuilding your house...\n")
    
    print_roof(roof_height)
    print_walls(wall_height, house_width)
    print_base(house_width)
    print("Your MegaHouse is ready! 🏠✨")

if __name__ == "__main__":
    main()
    