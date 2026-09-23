jmeno = input("Jak se jmenujete?")
while True:
    style = input("Formální [F] nebo neformální [N] pozdrav?")
    if style == "F" or "f":
        print("Dobrý den " + jmeno)
    elif style == "N" or "n":
        print("Brý jitro " + jmeno)