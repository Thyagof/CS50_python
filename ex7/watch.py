import re
import sys

def main():
    print(parse(input("HTML: ").strip()))

def parse(s):
    if matches := re.search(r'^<iframe.* src="https?:\/\/(?:www\.)?youtube\.com\/embed\/([A-Za-z0-9]+)".*><\/iframe>$', s):
        return f"https://youtu.be/{matches.group(1)}"
    else:
        return None

if __name__ == "__main__":
    main()