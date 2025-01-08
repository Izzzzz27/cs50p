f=input("Expression: ")
x, y, z = f.split(" ")
x=float(x)

z=float(z)
if y == "+":
    print(x+z)
elif y == "-":
    print(x-z)
elif y == "/":
    print(x/z)
elif y == "*":
    print(x*z)
