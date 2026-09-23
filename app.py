jmeno = input("Jak se jmenujete?")
while True:
    style = input("Formální [F] nebo neformální [N] pozdrav?")
    if style == "F" or style == "f":
        print("Dobrý den " + jmeno)
        break
    elif style == "N" or style == "n":
        print("Brý jitro " + jmeno)
        break
    else:
        print("Neplatný vstup")