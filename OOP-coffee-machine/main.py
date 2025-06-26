
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu=Menu()
coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()

game_over=False

while not game_over:
    option=menu.get_items()
    choice=input(f"what coffee do you want? {menu.get_items()}: ").lower()
    if choice=="off":
        break
    elif choice=="report":
        print(coffee_maker.report(),money_machine.report())
    else:
        drink=menu.find_drink(choice)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
