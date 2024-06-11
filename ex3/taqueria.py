def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    place_order(menu)

def place_order(m):
    total = 0
    while True:
        try:
            item = input("Item: ").title()
        except EOFError:
            break
        
        if item in m:
            try:
                total += m[item]
            except KeyError:
                pass
            else:
                print(f"Total: ${total:.2f}")
        else: 
            continue

if __name__ == "__main__":
    main()