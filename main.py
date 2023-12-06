import random

options = ("piedra", "papel", "tijera")

computer_wins = 0
user_wins = 0

rounds = 1

while True:

    print("*" * 10)
    print("ROUND", rounds)
    print("*" * 10)

    print("computer_wins", computer_wins)
    print("user_wins", user_wins)

    user_option = input("piedra, papel ó tijera --> ")
    user_option = user_option.lower()   #Estoy diciendo al sistema que me transcriba el texto que puso el usuario a minúscula

    rounds += 1 #para que le sume 1 al round

    if not user_option in options:
        print("Esa opción no es valida")
        continue

    computer_option = random.choice(options) #de forma aleatoria se va a escoger piedra, papel ó tijera.

    print("User option -->", user_option)
    print("Computer option -->", computer_option)

    if user_option == computer_option:
        print("Empate")
    elif user_option == "piedra":
        if computer_option == "tijera":
            print("Piedra gana a tijera")
            print("User gano!")
            user_wins += 1  #indicamos +1 cada vez que el usuario gane.
        else:
            print("Papel gana a piedra")
            print("Computer gano!")
            computer_wins += 1  #indicamos +1 cada vez que el computer gane.
    elif user_option == "papel":
        if computer_option == "piedra":
            print("Papel gana a piedra")
            print("User gano!")
            user_wins += 1  #indicamos +1 cada vez que el usuario gane.
        else:
            print("Tijera gana a papel")
            print("Computer gano!")
            computer_wins += 1  #indicamos +1 cada vez que el computer gane.
    elif user_option == "tijera":
        if computer_option == "papel":
            print("Tijera gana a papel")
            print("User gano!")
            user_wins += 1  #indicamos +1 cada vez que el usuario gane.
        else:
            print("Piedra gana a tijera")
            print("Computer gano!")
            computer_wins += 1  #indicamos +1 cada vez que el computer gane.
    else:
        print("Elige una opción correcta")
    
    if computer_wins == 2:
        print("El rotundo ganador es la computadora, porque llego a 2")
        break
    if user_wins == 2:
        print("El rotundo ganador es el usuario, porque llego a 2")
        break