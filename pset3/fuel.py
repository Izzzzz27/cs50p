
while True:
    try:
        x=input("Fraction: ")
        x=x.split("/")
        x[0]=int(x[0])
        x[1]=int(x[1])

    except ValueError:
        pass
    except ZeroDivisionError:
        x=0
        print(x)
        exit
    else:
        if x[0]>x[1]:
            continue
        break
y=round(float(x[0]/x[1]*100))
if y <= 1:
    print("E")
elif y >= 99:
    print("F")
else:
    print(y, "%", sep="")
