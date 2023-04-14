from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def get_prompt():
    inp = input('What would you like? (espresso/latte/cappuccino): ').lower()
    while inp not in ['espresso', 'latte', 'cappuccino', 'off', 'report']:
        inp = input('What would you like? (espresso/latte/cappuccino): ').lower()
    return inp


def main():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    inp = get_prompt()
    first_run = True
    while True:
        if not first_run:
            inp = get_prompt()
        first_run = False
        if inp == 'off':
            break
        if inp == 'report':
            coffee_maker.report()
            money_machine.report()
            continue
        drink = menu.find_drink(inp)
        coffee_maker.is_resource_sufficient(drink)
        money_machine.process_coins()
        if not money_machine.make_payment(drink.cost):
            continue
        coffee_maker.make_coffee(drink)

    print('Turning machine down...')
    return 0

if __name__ == '__main__':
    main()