def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    for i in range(len(s)):
            if i == len(s)-1:
                continue
            if s[i].isdigit() and s[i+1].isdigit():

                return False
    if len(s) < 7 and len(s) > 1 and s[0:2].isdigit()==False :
        return True
    else:
        return False


main()
