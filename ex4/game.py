from random import randint

def main():
    while True:
        try: 
            level = int(input("Level: "))
        except:
            pass
        else:
            if level > 0:
                break
    random = randint(1,level)
    while True:
        try: 
            guess = int(input("Guess: "))
        except:
            pass
        else:
            if guess > random:
                print("Too large!")
            elif guess < random:
                print("Too small!")
            else: 
                print("Just right!")
                break

if __name__ == "__main__":
    main()