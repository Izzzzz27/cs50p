import sys
import tabulate
import csv
l=len(sys.argv)
if l<2:
    sys.exit("Too few command lines arguements")
if l>2:
    sys.exit("Too many command lines arguements")
l2=len(sys.argv[1])
if sys.argv[1][l2-4:l2]!= ".csv":
    sys.exit("not a python file")
try:
    file = open (sys.argv[1])
    reader = csv.DictReader(file)
    print(tabulate.tabulate(reader, headers="keys" , tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")
