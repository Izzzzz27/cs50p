x = input("Input")
y =""
for i in range (len(x)):
    if x[i]== "a" or x[i] == "e" or x[i] == "u" or x[i] == "i" or x[i] == "o" or x[i] == "O":
        continue

    y= y + x[i]
print(y)
