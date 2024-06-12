def main():
    fraction = input("What's x/y: ").strip()
    p = convert(fraction)
    print(gauge(p))

def convert(f):
    x, y = f.split("/")
    x, y = int(x), int(y)
    
    if y == 0:
        raise ZeroDivisionError("y can't be zero")
    
    if x > y:
        raise ValueError("y must be greater than x")

    percentage = round((x/y)*100)
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