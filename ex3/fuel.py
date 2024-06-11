def main():
    print_percentage()

def print_percentage():
    while True:
        try:
            x, y = input("What's x/y: ").split("/")
        except ValueError:
            print("x and y must be integers")
            continue

        try:
            x, y = int(x), int(y)
        except ValueError:
            print("x and y must be integers")
            continue
        
        if x > y:
            print("y must be greater than x")
            continue

        try:
           percentage = round((x/y)*100)
        except ZeroDivisionError:
            print("You can't divide by zero!")
        else: 
            break

    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print ("F")
    else:
        print (f"{percentage}%")

if __name__ == "__main__":
    main()