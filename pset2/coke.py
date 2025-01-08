x = 50
print("Amount Due", x)
while x != 0:
    i = int(input("Insert Coin: "))

    if i == 25 or i == 10 or i == 5:
        x=x-i
        if x == 0:
            print("Change Owed: 0")
            break
        if x<0:
            print(f"Change Owed: {int((x*x)/10)}")

            exit()
        print (f"Amount Due: {x}")





    else:
        print("Amount Due:", x)
        exit()
