def main():
    text = input()
    text = convert(text)
    print(text)

def convert(text):
    text = text.replace(":)", "🙂").replace(":(", "🙁")
    return text

if __name__ == "__main__":
    main()