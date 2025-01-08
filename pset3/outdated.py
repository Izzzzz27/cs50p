dict = {
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
}

while True:
    x = input("Date: ")
    if "/" in x:
        g = x.split("/")
        if int(g[0])>12 or int(g[1])>30:
            continue
    elif " " in x:
        g = x.split(" ")
        g[1]=g[1].replace(",", " ")
        if int(g[1])>30:
            continue
    else:
        continue

    if g[0] in dict:
        g[0]=dict[g[0]]
    g.reverse()
    print(f"{int(g[0]):02}", end="-")
    print(f"{int(g[2]):02}", end="-")
    print(f"{int(g[1]):02}")
    break

       