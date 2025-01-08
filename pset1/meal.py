def main():
    answer = input("What time is it? ")
    s=convert (answer)
    if s >= 7 and s <=8:
        print("breakfast time")
    elif s >= 12 and s <= 13:
        print("lunch time")
    elif s >= 18 and s <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    nminutes = float(minutes)/60
    return float(hours)+nminutes
if __name__ == "__main__":
    main()
