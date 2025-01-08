
dict = {}

while True:
    try:
        item = input().upper()
        if item in dict:
            dict[item] = dict[item] + 1
        else:
            dict[item] = 1
    except EOFError:
        for i in dict:
            print(dict[i], i)
        break
