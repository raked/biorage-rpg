import time
import sys
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


def printText(text, speed):  # text defined as variable, speed in seconds per character
    for i in range(len(text)):
        printf(text[i])
        time.sleep(speed)
        sys.stdout.flush()
    print()


def trollFace(text):
    print("░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░")
    print("░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░")
    print("░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░")
    print("░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░")
    print("░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░")
    print("█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█")
    print("█░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█")
    print("░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░")
    print("░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░")
    print("░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░")
    print("░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░")
    print("░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░")
    print("░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░")
    print("░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░")
    print("░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░", text)


def main():
    printText("Welcome to Biorage RPG!", .05)
    printText("Please enter a name for your character below", .05)
    name = input()
    print("----------------------------------------------------")
    printText("\t\tChoose your starter", .05)
    printText("\tStarter 1\tStarter 2\tStarter 3", .05)
    print("Name:\t" + starter1["name"] + "\t" +
          starter2["name"] + "\t" + starter3["name"])
    print("Damage:\t" + str(starter1["damage"]) + "\t\t" +
          str(starter2["damage"]) + "\t\t" + str(starter3["damage"]))
    print("Health:\t" + str(starter1["health"]) + "\t\t" +
          str(starter2["health"]) + "\t\t" + str(starter3["health"]))
    print("Stamina:" + str(starter1["stamina"]) + "\t\t" +
          str(starter2["stamina"]) + "\t\t" + str(starter3["stamina"]))
    print("----------------------------------------------------")
    starterChoice = printText("Enter your starter choice (1, 2, 3) below", .05)
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
            "Please make a valid selection. Restart your application to retry.", .05)
    playerinfo = {
        "name": name,
        "starter": starter
    }
    print("Name:", playerinfo["name"], "\n" +
          "Starter:", playerinfo["starter"]["name"])

    trollFace("get owned")


main()
