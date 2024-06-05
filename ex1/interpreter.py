def main():
    expression = input("Expression: ").strip()
    print(resolve(expression))

def resolve(expression):
    x, y, z = expression.split(" ")
    x = float(x)
    z = float(z)
    match y:
        case "+":
            return (f"{(x+z):.1f}")
        case "-":
            return (f"{(x-z):.1f}")
        case "*":
            return (f"{(x*z):.1f}")
        case "/":
            return (f"{(x/z):.1f}")

if __name__ == "__main__":
    main()