def main():
    percentage = convert()
    print(gauge(percentage))

def convert():
    while True:
        try:
            f = input("What's x/y: ")
            x, y = f.split("/")
            x, y = int(x), int(y)
            percentage = round((x/y)*100)
            if percentage <= 100:
                break
        except (ValueError, ZeroDivisionError):
            pass
    return percentage

def gauge(p):
    if p <= 1:
        return "E"
    elif p >= 99:
        return "F"
    else:
        return f"{p}%"

if __name__ == "__main__":
    main()
