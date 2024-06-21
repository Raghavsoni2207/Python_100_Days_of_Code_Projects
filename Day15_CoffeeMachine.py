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
    "money": 0,
}


def take_money():
    """Returns the total calculate money from coin inserted"""
    print("Please insert coins.")
    pennies = int(input("Pennies: "))
    nickles = int(input("Nickles: "))
    dimes = int(input("Dimes: "))
    quarters = int(input("Quarters: "))

    total_money = (pennies*0.01) + (nickles*0.05) + (dimes*0.10) + (quarters*0.25)

    return total_money


def if_resource_sufficient(order_ingredients):
    """Returns True if order can be maid or False if ingredients are in sufficient"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def update_resources(order_ingredients):
    """Update the resources left after making coffee"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]


machine_status = True

while machine_status:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input == "off":
        machine_status = False
    elif user_input == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    else:
        order = MENU[user_input]

        if if_resource_sufficient(order["ingredients"]):
            user_money = take_money()
            if user_money >= order["cost"]:
                left_money = round(user_money - order["cost"], 2)
                print(f"Here is ${left_money} dollars in change.")
                print(f"Here is your {user_input}. Enjoy!")
                resources["money"] += order["cost"]
                update_resources(order["ingredients"])
            else:
                print("Sorry that's not enough money. Money refunded.")
