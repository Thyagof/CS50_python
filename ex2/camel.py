def main():
    camel = input("camelCase: ").strip()
    camel_to_snake(camel)

def camel_to_snake(s):
    print("snake_case: ", end="")
    for c in s:
        if c.isupper():
            print("_" + c.lower(), end="")
        else:
            print(c, end="")

if __name__ == "__main__":
    main()