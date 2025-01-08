import sys
l=len(sys.argv)
if l<2:
    sys.exit("Too few command lines arguements")
if l>2:
    sys.exit("Too many command lines arguements")
l2=len(sys.argv[1])
if sys.argv[1][l2-3:l2]!= ".py":
    sys.exit("not a python file")

try:
    i=0
    file = open(sys.argv[1],"r")
    for line in file:
        if line.lstrip().startswith("#")==True or line.lstrip()=="":
            continue
        i=i+1
    print(i)
except FileNotFoundError:
    sys.exit("File does not exist")
