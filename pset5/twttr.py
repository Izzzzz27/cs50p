
def main():
    x = input("Input")
    y =""
    f=shorten(x)
    print(f)


def shorten(x):
    y=""
    for i in range (len(x)):
        if x[i]== "a" or x[i] == "e" or x[i] == "u" or x[i] == "i" or x[i] == "o" or x[i] == "O":
            continue

        y= y + x[i]
    return y

if __name__ == "__main__":
    main()
