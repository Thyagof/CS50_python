import validators

def main():
    print(validate(input("What's your email address: ").strip()))

def validate(email):
    if validators.email(email):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()