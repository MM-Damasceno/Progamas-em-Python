def main():
    x = int(input("What's the number? "))
    print("The squere of the number = ", square(x))

def square(n):
    return pow(n, 2)

main()