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
    "money": 0.0
}


# Prompt user by asking “What would you like? (espresso/latte/cappuccino):
def get_prompt():
    inp = input('What would you like? (espresso/latte/cappuccino): ').lower()
    while inp not in ['espresso', 'latte', 'cappuccino', 'off', 'report']:
        inp = input('What would you like? (espresso/latte/cappuccino): ').lower()
    return inp


def print_report(res):
    print(f'Water: {res["water"]}ml\n'
          f'Milk: {res["milk"]}ml\n'
          f'Coffee: {res["coffee"]}g\n'
          f'Money: ${res["money"]}\n')


def check_insufficient_resource(res, drink):
    for ingredient, amount in MENU[drink]["ingredients"].items():
        if res[ingredient] < amount:
            return ingredient
    return ''


def process_coins():
    quarters = int(input("Insert quarters: ") or 0) * 0.25
    dimes = int(input("Insert dimes: ") or 0) * 0.1
    nickles = int(input("Insert nickles: ") or 0) * 0.05
    pennies = int(input("Insert pennies: ") or 0) * 0.01
    return quarters + dimes + nickles + pennies


def check_transaction_success(drink, money):
    if MENU[drink]["cost"] <= money:
        return True
    return False


def get_change(drink, money):
    return money - MENU[drink]["cost"]


def make_coffee(drink, res):
    for ingredient, amount in MENU[drink]["ingredients"].items():
        res[ingredient] -= amount


def main():
    inp = get_prompt()
    first_run = True
    # Turn off the Coffee Machine by entering “off” to the prompt.
    while inp != 'off':
        if not first_run:
            inp = get_prompt()
        first_run = False
        if inp == 'report':
            print_report(resources)
            continue
        insufficient_res = check_insufficient_resource(resources, inp)
        if insufficient_res != '':
            print(f"Sorry there is not enough {insufficient_res}")
            continue
        money = process_coins()
        if not check_transaction_success(inp, money):
            print('Sorry that\'s not enough money. Money refunded.')
            money = 0
            continue
        change = get_change(inp, money)
        if change > 0:
            print(f'Here\'s your change: ${change}')
        resources["money"] += money - change
        make_coffee(inp, resources)
        print(f'Here\'s your {inp}! Enjoy!')

    print('Turning coffee machine down...')
    return 0


if __name__ == "__main__":
    main()