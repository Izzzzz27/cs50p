x = input("camel case: ")
snakecase = ""
for i in range (len(x)):
    if x[i].isupper():
        snakecase = snakecase + "_" + x[i].lower()
    else:
        snakecase = snakecase + x[i]
print(snakecase)
