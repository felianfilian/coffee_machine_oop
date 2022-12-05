from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

def check_drink(drink, drink_item):
    print(drink.title())
    if coffee_maker.is_resource_sufficient(menu.find_drink(drink)):
        if money_machine.make_payment(drink_item.cost):
            coffee_maker.make_coffee(menu.find_drink(drink))

while is_on:
    choice = input("Espresso (a) Latte (b) Cappuccino (c):\n")
    if choice == "a":
        drink = menu.find_drink("espresso")
        check_drink("espresso", drink)
    elif choice == "b":
        drink = menu.find_drink("latte")
        check_drink("latte", drink)
    elif choice == "c":
        drink = menu.find_drink("cappuccino")
        check_drink("cappuccino", drink)
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        is_on = False



