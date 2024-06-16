import sys
import csv

def main():
    table = open_file()

    write_file(table)

def open_file():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        try:
            table = []
            with open(sys.argv[1], "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    table.append({"name": row["name"], "house": row["house"]})
            return table
        except FileNotFoundError:
            sys.exit("Could not read " + sys.argv[1])

def write_file(table):
    with open(sys.argv[2], "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first_name", "last_name", "house"])
        writer.writeheader()
        for row in table:
            last, first = row["name"].split(" ")
            last = last.strip(',\"')
            writer.writerow({"first_name": first, "last_name": last, "house": row["house"]})

if __name__ == "__main__":
    main()