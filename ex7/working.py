import re

def main():
    print(convert(input("Hours: ").strip()))

def convert(s):
    if matches := re.search(r"^(([0-9][0-2]*):?([0-5][0-9])?) ([A-P]M) to (([0-9][0-2]*):?([0-5][0-9]+)?) ([A-P]M)$", s):
        pieces = matches.groups()
        if int(pieces[1]) > 12 or int(pieces[5]) > 12:
            raise ValueError
        first_time = converted_time(pieces[1],pieces[2],pieces[3])
        second_time = converted_time(pieces[5],pieces[6],pieces[7])
        return first_time + " to " + second_time
    else:
        raise ValueError
        
def converted_time(hour, minute, am_pm):
    if am_pm == "PM":
        if int(hour) == 12:
           hour = 12
        else:
           hour = int(hour) + 12
    else:
        if int(hour) == 12:
            hour = 0
        else:
            hour = int(hour)
    if minute == None:
        minute = int("0")
    else:
        minute = int(minute)
    return f"{hour:02}:{minute:02}"



if __name__ == "__main__":
    main()