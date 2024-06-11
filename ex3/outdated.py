MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    month, day, year = get_and_check_date()
    print_formatted(month, day, year)

def get_and_check_date():
    while True:
        try:
            date = input("Date: ").strip()
        except KeyError:
            continue

        if "/" in date:
            m, d, y = date.split("/")
        elif " " in date and "," in date:
            m, d, y = date.split(" ")
            d = d.strip(",")
        else: 
            continue
        
        if m.isalpha():
            try:
                m = MONTHS.index(m) + 1
            except ValueError:
                continue
        else:
            m = int(m)

        if int(d) > 31 or int(d) < 1 or m < 1 or m > 12:
            continue

        return m, int(d), int(y)

def print_formatted(m,d,y):
    print(f"{y}-{m:02}-{d:02}")

if __name__ == "__main__":
    main()