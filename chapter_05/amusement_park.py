age = 12

if age < 4:
    price = 0
elif age < 18 or age >= 65:
    price = 5
else:
    price = 10
print(f"Your admission cost is ${str(price)}.")
