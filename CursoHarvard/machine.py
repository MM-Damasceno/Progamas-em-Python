emotion = "w.w"

def main():
    global emotion
    say(input("Qual foi? "))
    emotion = "=D"
    say(input("Tudo Bem? "))

def say(frase):
    print(frase + " " + emotion)

main()