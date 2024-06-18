from random import randint


def main():
    score = 0
    level = get_level()
    i = 0
    while i < 10:
        a = generate_integer(level)
        b = generate_integer(level)
        result = a + b
        x = 0
        while x < 3:
            try:
                answer = int(input(f"{str(a)} + {str(b)} = "))
            except:
                pass
            finally:
                if answer == result:
                    score += 1
                    break
                else:
                    x += 1
                    if x == 3:
                        print(f"{str(a)} + {str(b)} = {result}")
                    else:
                        print("EEE")
        i += 1
    print("Score: ", score)

def get_level():
    while True:
        try: 
            level = int(input("Level: "))
        except:
            pass
        else:
            if level > 0 and level < 4:
                break
    return level

def generate_integer(level):
    if level == 1:
        int = randint(0,9)
    elif level == 2:
        int = randint(10,99)
    else:
        int = randint(100,999)
    
    return int

if __name__ == "__main__":
    main()