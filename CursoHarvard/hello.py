def main():
    # Perguntar nome do usuario
    name = input("Qual o seu nome? ")

    #Tira o espaco(whitespace) do str e captalize
    name = name.strip().title()

# Mostrar nome do usuarip 
    hello()
    hello(name)



def hello(to ="word"):
    print("Hello", to)

main()
