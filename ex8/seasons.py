from datetime import date
import inflect
import re
import sys

p = inflect.engine()

def main():
    birth_date = input("Date of birth: ")
    try:
        year, month, day = check_birthday(birth_date)
    except:
        sys.exit("Invalid date")
    
    birth = date(int(year), int(month), int(day))
    today = date.today()
    diff = today - birth
    total_minutes = diff.days * 24 * 60
    print(p.number_to_words(total_minutes, andword="").capitalize() + " minutes")

def check_birthday(birth_date):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth_date):
        year, month, day = birth_date.split("-")
        return year, month, day

if __name__ == "__main__":
    main()