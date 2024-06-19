import re

def main():
    print(count(input("Text: ")))

def count(s):
    matches = re.findall(r"(\b\W*um\W*\b|\b\W*um\W)", s, re.IGNORECASE)
    return len(matches)

if __name__ == "__main__":
    main()