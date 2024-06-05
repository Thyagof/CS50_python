def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
    print(evaluate(answer))

def evaluate(answer):
    if answer == "42" or answer == "forty-two" or answer == "forty two":
        return "Yes"
    else:
        return "No"
    
if __name__ == "__main__":
    main()