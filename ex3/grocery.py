def main():
    get_items()

def get_items():
    list = {}
    while True:
        try:
            item = input()
        except EOFError:
            sort_print_list(list)
            break
        except KeyError:
            continue
        if item in list:
            list[item] += 1
        else:
            list[item] = 1

def sort_print_list(l):
    sorted_list = sorted(l)
    for i in sorted_list:
        print(l[i], i.upper())

if __name__ == "__main__":
    main()