def get_guess():
    guess = int(input("Digite um numero "))
    return guess

def main():
    guess = get_guess()
    if guess == 20:
        print("Correto! ")
    else:
        print("Errado!")
    print(guess)

main()
