# CalculateAreaOfShape.py

# Funksjon som regner ut arealet til ulike former
def calculate_area_of_shape(shape, base=0, length=0, height=0, width=0, radius=0):
    shape = shape.lower()
    
    if shape == "square":
        area = length * length
        print(f"Arealet av kvadratet er: {area:.2f}")
        
    elif shape == "circle":
        area = 3.14159 * (radius ** 2)
        print(f"Arealet av sirkelen er: {area:.2f}")
        
    elif shape == "cube":
        area = 6 * (length ** 2)
        print(f"Overflatearealet av kuben er: {area:.2f}")

    elif shape == "triangle":
        area = (base * height) / 2
        print(f"Arealet av trekanten er: {area:.2f}")
        
    else:
        print("Ukjent form. Prøv 'square', 'circle' eller 'cube'.")

# Hovedseksjonen
if __name__ == "__main__":
    calculate_area_of_shape(shape="square", length=5)
    calculate_area_of_shape(shape="circle", radius=3)
    calculate_area_of_shape(shape="cube", length=4)
    calculate_area_of_shape(shape="triangle", height=6, base=4)