import sys
import csv

def main():
    lines = open_file(".py")
    print(count_lines(lines))

def open_file(file_format):
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1].endswith(file_format):
            try:
                if file_format != ".csv":
                    with open(sys.argv[1], "r") as file:
                        lines = file.readlines()
                    return lines
                else:
                    table = []
                    with open(sys.argv[1], "r") as file:
                        reader = csv.reader(file)
                        for row in reader:
                            table.append(row)
                    return table
            except FileNotFoundError:
                sys.exit("File does not exist")
        else:
            sys.exit("Not a Python file")

def count_lines(lines):
    i = 0
    for line in lines:
        if line not in ['\n', '\r\n']:
            i+=1
    return i

if __name__ == "__main__":
    main()