frutis = {"apple": 130, "banana": 110, "Avocado": 50, "Kiwifruit": 90 , "pear" : 100, "Sweet Cherries": 100}
x = input("Item: ")
if x not in frutis:
    exit()
print(frutis[x])
