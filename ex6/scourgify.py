import sys
import csv

def main():
    check_command_line_arg()
    table = open_file()
    write_file(table)

def open_file():
    try:
        table = []
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                table.append({"name": row["name"], "house": row["house"]})
        return table
    except FileNotFoundError:
        sys.exit("Could not read " + sys.argv[1])

def check_command_line_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")

def write_file(table):
    with open(sys.argv[2], "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in table:
            last, first = row["name"].split(",")
            writer.writerow({"first": first.strip(), "last": last, "house": row["house"]})

if __name__ == "__main__":
    main()