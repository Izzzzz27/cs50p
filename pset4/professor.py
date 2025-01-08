import random


def main():
    level=get_level()
    i =0
    q=0
    while i < 10:
        x,y=generate_integer(level)
        f=int(input(f"{x} + {y} = "))
        if f == x+y:
            i+=1
            q+=1
            continue

        elif f!= x+y:
            print("EEE")
            i+=1

    print("Score of",q)
def get_level():

    while True:
        try:
            level = int(input("Level:"))
            if level == 1 or level == 2 or level == 3:
                return level
        except ValueError:
            continue
def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100,999)
    return x,y
if __name__ == "__main__":
    main()
