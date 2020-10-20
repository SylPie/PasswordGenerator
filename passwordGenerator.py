from random import randint, choices
from time import sleep

EXIT = "y"

while True:
    A = "QWERTYUIOPASDFGHJKLZXCVBNM"
    a = "qwertyuiopasdfghjklzxcvbnm"
    numbers = "0123456789"
    characters_type = [A, a, numbers]
    password = ""

    number_of_characters = int(input("How many characters should the password contain. \n"))

    for _ in range(number_of_characters):
        charactersType = characters_type[randint(0,2)]
        i = len(charactersType)
        password = password + charactersType[randint(0,i-1)]

    print(password)

    EXIT = input("Draw another password?(y/n)")
    if EXIT == "y":
        continue
    else:
        print("Bye!")
        sleep(2)
        break
