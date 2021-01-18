# TODO 1: Import the menu
from coffee_menu import MENU, resources

machine_is_on = True

machine_money = {
    "cash": 0
}

# TODO 4: Print report


def report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    machine_cash = machine_money["cash"]
    print(f"Water: {water}ml,\n Milk: {milk}ml,\n Coffee: {coffee}ml,\n Money ${machine_cash}")


# TODO 5: Check resources sufficient?


def check_resources(order_ingredients):
    """Take a drink and return whether or not the drink can be made given the resources"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


# TODO 7: Check transaction successful?


def insert_money():
    """Asks the user for coins and returns the total amount given"""
    print("Please insert coins")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickels?: "))
    pennies = float(input("How many pennies?: "))

    total_money = round(((0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)), 2)

    return total_money


def transaction_successful(coins, drink):
    """Take the coins given and the drink and check if there is enough coins
    if there is more coins, return change"""
    drink_cost = MENU[drink]["cost"]

    if drink_cost > coins:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    elif coins > drink_cost:
        coin_change = coins - drink_cost
        machine_money["cash"] += drink_cost
        print(f"Here is ${round(coin_change, 2)} dollars in change.")
        return True
    elif drink_cost == coins:
        machine_money["cash"] += drink_cost
        return True


# TODO 8: Make coffee
# TODO 6: Reduce resources if a drink was made


def make_coffee(drink, order_ingredients):
    """Take a drink and extract the given resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    return f"Here is your {drink} ☕ Enjoy!"




# TODO 2: Prompt user by asking “What would you like? (espresso/latte/cappuccino): ”


while machine_is_on:

    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "report":
        report()
    elif user_input == "off":
        machine_is_on = False
    else:
        user_drink = MENU[user_input]
        if check_resources(user_drink["ingredients"]):
            money = insert_money()
            process_transaction = transaction_successful(money, user_input)
            if process_transaction:
                print(make_coffee(user_input, user_drink["ingredients"]))
                extract_resources(user_input)

