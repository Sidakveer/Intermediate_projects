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

profit = 0
resources = {
    "water": 0,
    "milk": 200,
    "coffee": 100,
}



def report():

    """ prints the report of the available resources present in the coffee machine"""
    
    for key, value in resources.items():
        print(f"{key}: {value}")
    # print(f"Money: {money}")


def check_resources():
    """
    checks the resources dict whether the coffee machine has enough resources or not
        based onn the user input
    :return: returns a tuple with boolean value at index 0.
    """
    for key in resources:
        if (MENU[choice]["ingredients"][key]) > resources[key]:
            return False, (f"Sorry there is not enough {key}")
    else:
        return True,


choice = None
while choice != "off":
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        quit()
    elif choice == "report":
        print(report())
    else:
        # print(check_resources())
        if not check_resources()[0]:
            print(check_resources()[1])
            break
        else:
            print("ho")
