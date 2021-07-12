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


def main():
    print("Welcome to Biorage RPG!")
    name = input("Please enter a name for your character: ")
    print("\t\tChoose your starter")
    print("\tStarter 1\tStarter 2\tStarter 3")
    print("Name:\t" + starter1["name"] + "\t" +
          starter2["name"] + "\t" + starter3["name"])
    print("Damage:\t" + str(starter1["damage"]) + "\t\t" +
          str(starter2["damage"]) + "\t\t" + str(starter3["damage"]))
    print("Health:\t" + str(starter1["health"]) + "\t\t" +
          str(starter2["health"]) + "\t\t" + str(starter3["health"]))
    print("Stamina:" + str(starter1["stamina"]) + "\t\t" +
          str(starter2["stamina"]) + "\t\t" + str(starter3["stamina"]))
    starterChoice = input("Enter your starter choice (1, 2, 3): ")
    if (starterChoice == "1" or starterChoice == "2" or starterChoice == "3"):
        if (starterChoice == "1"):
            starter = starter1
        if (starterChoice == "2"):
            starter = starter2
        if (starterChoice == "3"):
            starter = starter3
    else:
        print("Please make a valid selection. Restart your application to retry.")
    playerinfo = {
        "name": name,
        "starter": starter
    }
    print("Name:", playerinfo["name"], "\n" +
          "Starter:", playerinfo["starter"])


main()
