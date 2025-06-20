from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money = MoneyMachine()
coffee = CoffeeMaker()
menu = Menu()



while True:
    options = menu.get_items()
    choice = input(f"What would you like ({options}): ").lower().strip()
    if choice == "off":
        break
    elif choice == "report":
        coffee.report()
        money.report()
    else:
        drink = menu.find_drink(choice)

        if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee.make_coffee(drink)