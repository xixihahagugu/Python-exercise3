#exercise2.5
talents = input("Enter talents")
pounds = input("Enter pounds")
lots = input("Enter lots")
grams = 20*32*13.3*float(talents)+32*13.3*float(pounds)+13.3*float(lots)
kilograms = int(10**-3*grams)
grams_left = grams % 1000
print(f"The weight in modern units: {kilograms} kilograms and {grams_left:.2f}grams")

