MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def checkResources(menuChoice):
    """ Takes in the order and outputs if their are enough resources to make the order"""
    if menuChoice in MENU:
        ingredients = MENU[menuChoice]['ingredients']
        # Checks to see if you didn't order espresso
        if menuChoice != "espresso":
            if resources['water'] < ingredients['water']:
                print("Sorry there is not enough water")
                return False
            elif resources["milk"] < ingredients["milk"]:
                print("Sorry there is not enough milk")
                return False
            elif resources["coffee"] < ingredients["coffee"]:
                print("Sorry there is not enough coffee")
                return False
            else:
                return True
        # It deals with espresso's order
        else:
            if resources['water'] < ingredients['water']:
                print("Sorry there is not enough water")
                return False
            elif resources["coffee"] < ingredients["coffee"]:
                print("Sorry there is not enough coffee")
                return False
            else:
                return True

    else:
        return False

def checkTransaction(menuChoice):
    if menuChoice == "espresso":
        resources["water"] -= 50
        resources["coffee"] -= 18
    elif menuChoice == "latte":
        resources["water"] -= 200
        resources["milk"] -= 150
        resources["coffee"] -= 24
    else:
        resources["water"] -= 250
        resources["milk"] -= 100
        resources["coffee"] -= 24
    resources["money"] += MENU[menuChoice]['cost']

def processCoins(moneyGiven):
    totalSum = 0
    for money in moneyGiven:
        if money == "quarters":
            totalSum += moneyGiven[money] * 0.25
        elif money == "dimes":
            totalSum += moneyGiven[money] * 0.10
        elif money == "nickles":
            totalSum += moneyGiven[money] * 0.05
        elif money == "pennies":
            totalSum += moneyGiven[money] * 0.05
    return totalSum

def printReport():
    for resource in resources:
        if resource == "water" or resource == "milk":
            print(f"{resource.capitalize()}: {resources[resource]}ml")
        elif resource == "coffee":
            print(f"{resource.capitalize()}: {resources[resource]}g")
        else:
            print(f"{resource.capitalize()}: ${resources[resource]}")

def makeCoffe(choice):
    # TODO: 2. Check resources sufficient
    sufficientResources = checkResources(choice)
    # TODO: 3. Process coins
    if sufficientResources:
        print("Please insert coins.")
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))
        moneyEntered = {"quarters": quarters, "dimes": dimes, "nickles": nickles, "pennies": pennies}
        finalSum = processCoins(moneyEntered)
        if finalSum >= MENU[choice]["cost"]:
            finalSum = finalSum - MENU[choice]['cost']
            print(f"Here is ${round(finalSum, 2)} in change")
            print(f"Here is your {choice} ☕️. Enjoy!")
            # TODO: 4. Check transaction successful
            checkTransaction(choice)
        else:
            print("Sorry that's not enough money. Money refunded.")

def choiceGiven(inputedChoice):
    # TODO: 1. Print report
    if inputedChoice == "report":
        printReport()
        return True
    # TODO: 5. Make coffee
    elif inputedChoice in MENU:
        makeCoffe(inputedChoice)
        return True
    # TODO: 6. Turn off
    elif inputedChoice == "off":
        print("Good bye.")
        return False
    # TODO: 7. Ask again
    else:
        print("I didn't get that.")
        return True

keepMakingIt = True
while keepMakingIt:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    keepMakingIt = choiceGiven(choice)