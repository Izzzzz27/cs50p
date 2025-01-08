import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    x=re.search(r'.+src="https?://(?:www\.)?youtube\.com/embed/(.+?)"',s)
    if x :
        return( "https://youtu.be/" + x.group(1))
    
if __name__ == "__main__":
    main()
