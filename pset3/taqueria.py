x = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
z=0
while True:
    try:
        item = input("Item: ")
        item = item.title()
        if item in x:

            f=x[item]

            z=z+f
            print(f"Total: ${z:.2f}")
        else:
            continue
    except EOFError:
        print()
        break
