from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
money = MoneyMachine()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    user_input = input(f"What would you like? ({options}):").lower()

    if user_input == "off":
        is_on = False
    elif user_input == "report":
        machine.report()
        money.report()
    else:
        drink = menu.find_drink(user_input)
        if machine.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                machine.make_coffee(drink)