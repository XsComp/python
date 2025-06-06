# MetricConverter.py

# Vi definerer funksjonen som tar imot ett tall (i inches)
def metric_converter(inches):
    # 1 inch = 2.54 cm
    centimetres = inches * 2.54
    print(f"{inches} inches er lik {centimetres:.2f} centimeter.")

# Hovedseksjonen der vi bruker funksjonen
if __name__ == "__main__":
    # Eksempel på kall
    metric_converter(10)