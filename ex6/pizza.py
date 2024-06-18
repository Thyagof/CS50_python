import sys
import csv
from tabulate import tabulate

def main():
    menu = open_file(".csv")
    print(tabulate(menu[1:], menu[0], tablefmt="grid"))

def open_file(file_format):
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1].endswith(file_format):
            try:
                table = []
                with open(sys.argv[1], "r") as file:
                    reader = csv.reader(file)
                    for row in reader:
                        table.append(row)
                return table
            except FileNotFoundError:
                sys.exit("File does not exist")
        else:
            sys.exit("Not a CSV file")
if __name__ == "__main__":
    main()
