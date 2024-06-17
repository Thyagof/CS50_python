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
    print(format_date(month, day, year))

def get_and_check_date():
    while True:
        date = input("Date: ")
        try:
            m, d, y = date.split("/")
            if (int(m)>=1 and int(m)<=12) and (int(d)>=1 and int(d)<=31):
                break
        except:
            try:
                m, d, y = date.split(" ")
                for i in range(len(MONTHS)):
                    if m == MONTHS[i]:
                        m = i+1
                if "," in d:
                    d = d.replace(",","")
                else:
                    continue
                if (int(m)>=1 and int(m)<=12) and (int(d)>=1 and int(d)<=31):
                    break
            except:
                pass
    return int(m), int(d), int(y)

def format_date(m,d,y):
    return f"{y}-{m:02}-{d:02}"

if __name__ == "__main__":
    main()
