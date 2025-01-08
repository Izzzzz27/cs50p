import validators
import sys
x = input("Email: ")
if validators.email(x):
    print("Valid")
    sys.exit()
else:
    print("Invalid")
    sys.exit()
