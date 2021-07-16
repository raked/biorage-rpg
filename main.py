# encoding: utf8
import time
import sys
import random
printf = sys.stdout.write

starter1 = {
    "name": "Devil Summoner",
    "damage": 3,
    "health": 1,
    "stamina": 2
}

starter2 = {
    "name": "Doctor Electric",
    "damage": 1,
    "health": 3,
    "stamina": 2
}

starter3 = {
    "name": "Scooter from boderlands",
    "damage": 2,
    "health": 1,
    "stamina": 3
}

enemy1 = {
    "name": "Radioactive Waste",
    "image": "     _.-^^---....,,--       \n _--                  --_  \n<                        >)\n|                         | \n \._                   _./  \n    ```--. . , ; .--'''       \n          | |   |             \n       .-=||  | |=-.   \n       `-=#$%&%$#=-'   \n          | ;  :|     \n _____.,-#%&$@%#&#~,._____",
    "catchphrase1": "Don't stand too close!",
    "catchphrase2": "Make sure to be equipped with proper PPE!",
    "catchphrase3": "Why are you itchy?",
    "damage": 3,
    "health": 1,
    "stamina": 2
}

enemy2 = {
    "name": "The Troll",
    "image": "░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░\n░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░\n░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░\n░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░\n░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░\n█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█\n█░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█\n░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░\n░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░\n░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░\n░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░\n░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░\n░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░\n░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░\n░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░",
    "catchphrase1": "Step 1: Oil floats on water.",
    "catchphrase2": "problem?",
    "catchphrase3": ":D",
    "damage": 1,
    "health": 3,
    "stamina": 2
}

enemy3 = {
    "name": "marco from BorderLands 3",
    "image": "#############\n##         ##\n#  ~~   ~~  #\n#  ()   ()  #\n(     ^     )\n |         | \n |  {===}  | \n  \       /  \n /  -----  \ ",
    "catchphrase1": "Welcome to my shop!",
    "catchphrase2": "A day without slaughter is like a day without sunshine.",
    "catchphrase3": "No no no, slag him first!",
    "damage": 2,
    "health": 2,
    "stamina": 1
}


def printText(text, speed=.05):  # text defined as variable, speed in seconds per character
    for i in range(len(text)):
        printf(text[i])
        time.sleep(speed)
        sys.stdout.flush()
    print()


def fightSequence(enemy):
    printText(enemy["image"] + " " + random.choice([enemy["catchphrase1"],
              enemy["catchphrase2"], enemy["catchphrase3"]]), .005)
    printText("A random '" + enemy["name"] + "' has appeared!")
    printText("It doesn't look very friendly.")


def main():
    printText("Welcome to Biorage RPG!", .05)

    name = ""

    while (name == ""):
        printText("Please enter a name for your character below", .05)
        name = input()
        if (name == ""):
            printText("Name invalid. Please enter at least 1 character.", .05)

    printText("----------------------------------------------------", .01)
    printText("\t\tChoose your starter", .01)
    printText("\tStarter 1\tStarter 2\tStarter 3", .01)
    printText("Name:\t" + starter1["name"] + "\t" +
              starter2["name"] + "\t" + starter3["name"], .01)
    printText("Damage:\t" + str(starter1["damage"]) + "\t\t" +
              str(starter2["damage"]) + "\t\t" + str(starter3["damage"]), .01)
    printText("Health:\t" + str(starter1["health"]) + "\t\t" +
              str(starter2["health"]) + "\t\t" + str(starter3["health"]), .01)
    printText("Stamina:" + str(starter1["stamina"]) + "\t\t" +
              str(starter2["stamina"]) + "\t\t" + str(starter3["stamina"]), .01)
    printText("----------------------------------------------------", .01)
    starterChoice = printText("Enter your starter choice (1, 2, 3) below", .01)
    starterChoice = input()
    if (starterChoice == "1" or starterChoice == "2" or starterChoice == "3"):
        if (starterChoice == "1"):
            starter = starter1
        if (starterChoice == "2"):
            starter = starter2
        if (starterChoice == "3"):
            starter = starter3
    else:
        printText(
            "Please make a valid selection. Restart your application to retry.", .01)
    playerinfo = {
        "name": name,
        "starter": starter
    }
    print("Name:", playerinfo["name"], "\n" +
          "Starter:", playerinfo["starter"]["name"])

    fightSequence(random.choice([enemy1, enemy2, enemy3]))


main()
