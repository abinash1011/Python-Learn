def convert(x_miles):
    to_km = round((1.6 * x_miles), 2)
    return f"{x_miles} miles is {to_km} kms"
    
x = convert(10.35645)
print(x)