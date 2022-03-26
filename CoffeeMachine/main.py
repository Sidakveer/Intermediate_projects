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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



def report():

    """ prints the report of the available resources present in the coffee machine"""

    for key, value in resources.items():
        print(f"{key}: {value}")
    return (f"Money: {profit}")


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


def insert_coins():
    
    """
        uses profit variable from outer scope and asks the user to input the 
        number of coins as payment
        checks if added funds are sufficient or not and calls another function
        make coffee if funds added are enough
    """
    
    global profit
    print("Please enter coins")
    quarters = int(input("How many quaters: "))
    dimes = int(input("How many dimes: "))
    nickels = int(input("How many nickels: "))
    pennies = int(input("How many pennies: "))
    money_inserted = 0.25 * quarters + 0.10 * dimes + 0.05 * nickels + 0.01 * pennies
    cost1 = MENU[choice]["cost"]
    if money_inserted < cost1:
        print("Sorry that's not enough money. Money refunded.")
    elif money_inserted >= cost1:
        profit += cost1
        change = money_inserted - cost1
        print(f"Here is a ${round(change, 2)} dollars in change")
        print(make_coffee())


def make_coffee():
    
    """
        deducts the amount of resources used based on the type of coffee selected by 
        the user
    """
    for key in resources:
        resources[key] -= MENU[choice]["ingredients"][key]
    return f"Here is you {choice}. Enjoy!"


choice = None
while choice != "off":
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        quit()
    elif choice == "report":
        print(report())
    else:
        if not check_resources()[0]:
            print(check_resources()[1])
            continue
        else:
            insert_coins()
            