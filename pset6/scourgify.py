import sys
import csv
l=len(sys.argv)
if l<3:
    sys.exit("Too few command lines arguements")
if l>3:
    sys.exit("Too many command lines arguements")
l2=len(sys.argv[1])
if sys.argv[1][l2-4:l2]!= ".csv":
    sys.exit("not a csv file")
try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        with open(sys.argv[2], 'w') as file2:
            writer = csv.DictWriter(file2, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in reader:
                row["first"] = row.pop("name")
                last_name, first_name = row["first"].split(", ")
                row["first"] = first_name
                row["last"] = last_name
                writer.writerow(row)
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

\

