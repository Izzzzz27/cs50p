import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    matches = re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
    if matches:
        for i in range(1,5):
            if int(matches.group(i))>255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()
