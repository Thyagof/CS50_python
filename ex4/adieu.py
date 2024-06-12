def main():
    get_items()

def get_items():
    list = []
    while True:
        try:
            item = input("Name: ").strip()
        except EOFError:
            adieu_names(list)
            break
        except KeyError:
            continue

        list.append(item)

def adieu_names(l):
    if len(l) == 1:
        print ("Adieu, adieu, to " + l[0])
    elif len(l) == 2:
        print ("Adieu, adieu, to " + l[0] + " and " + l[1])
    else:
        print ("Adieu, adieu, to ", end="")
        for i in l:
            if len(l)-1 == l.index(i):
                print("and " + i)
            else:    
                print(i + ", ", end="")

if __name__ == "__main__":
    main()