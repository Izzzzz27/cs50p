
def main():
    ...
    x=input("Fraction: ")
    y=0
    print(convert(x))


def convert(x):

    while True:
        try:
            x=x.split("/")
            x[0]=int(x[0])
            x[1]=int(x[1])

        except ValueError:
            raise ValueError
        except ZeroDivisionError:
            x=0
            return x
            exit
        else:
            if x[0]>x[1]:
                continue
            break
    return round(float(x[0]/x[1]*100))



def gauge(x):
    ...
    if x <= 1:
        return"E"
    elif x >= 99:
        return "F"
    else:
        return f"{x}%"


if __name__ == "__main__":
    main()
