import sys
import csv
from tabulate import tabulate
from lines import open_file

def main():
    menu = open_file(".csv")
    
    print(tabulate(menu[1:], menu[0], tablefmt="grid"))

if __name__ == "__main__":
    main()