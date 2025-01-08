import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    x=re.findall(r"\b[u][m]\b",s,re.IGNORECASE)
    return len(x)


...


if __name__ == "__main__":
    main()
