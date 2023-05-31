from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
machine_off = False


while not machine_off:
    option = menu.get_items()
    order_drink = input(f"What would you like? ({option}): ")
    if order_drink == "off":
        machine_off = True
    elif order_drink == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order_drink)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
