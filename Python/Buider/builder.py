from enum import Enum
import time

PizzaProgress = Enum("PizzaProgress", "queued preparation baking ready")
PizzaDough = Enum("PizzaDough", "thin thick")
PizzaSauce = Enum("PizzaSauce", "tomato creme_fraiche")
PizzaTopping = Enum(
    "PizzaTopping", "mozzarella double_mozzarella bacon ham mushrooms red_onion oregano")
STEP_DELAY = 3


class Pizza:
    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []

    def __str__(self):
        return self.name

    def prepare_dough(self, dough):
        self.dough = dough
        print(f"Preparing for the {self.dough.name} dough of your {self}")
        time.sleep(STEP_DELAY)


class MargaritaBuilder():
    def __init__(self):
        self.pizza = Pizza("Margarita")
        self.progress = PizzaProgress.queued
        self.baking_time = 5

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self):
        print(f"Adding tomato sauce onto the dough.")
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print("Done with the tomato sauce!")

    def add_topping(self):
        print("Adding the topping (double mozzarella, oregano) to your margarita.")
        self.pizza.topping.append(
            [PizzaTopping.double_mozzarella, PizzaTopping.oregano])
        self.progress = PizzaProgress.ready
        print("Done with adding toppings to your margartia.")

    def bake(self):
        print(
            f"Now we are baking your margarita for about {self.baking_time} minutes.")
        self.progress = PizzaProgress.baking
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print(f"Your margarita is ready!")


class CreamyBaconBuilder():
    def __init__(self):
        self.pizza = Pizza("creamy bacon")
        self.progress = PizzaProgress.queued
        self.baking_time = 7

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thick)

    def add_sauce(self):
        print("Adding the creme fraiche sauce to your creamy bacon.")
        self.pizza.sauce = PizzaSauce.creme_fraiche
        time.sleep(STEP_DELAY)
        print("Done with the creme fraiche sauce")

    def add_topping(self):
        print("Adding the topping(mozzarella, bacon, ham, mushrooms, red onion, oregano) to your creamy bacon")
        self.pizza.topping.append([PizzaTopping.mozzarella, PizzaTopping.bacon, PizzaTopping.ham,
                                   PizzaTopping.mushrooms, PizzaTopping.red_onion, PizzaTopping.oregano])
        print("Done with the topping(mozzarella, bacon, ham, mushrooms, red onion, oregano) to your creamy bacon")

    def bake(self):
        self.progress = PizzaProgress.baking
        print(f"Baking your creamy bacon for {self.baking_time}")
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print("Your creamy bacon is ready")


class Waiter():
    def __init__(self):
        self.builder = None

    def construct_pizza(self, builder):
        self.builder = builder
        [step() for step in (builder.prepare_dough,
                             builder.add_sauce, builder.add_topping, builder.bake)]

    @property
    def pizza(self):
        return self.builder.pizza


def validate_style(builders):
    try:
        pizza_style = input(
            "what pizza would you like, [m]argarita or [c]reamy bacon?")
        builder = builders[pizza_style]()
    except KeyError as err:
        print(err)
        print("Sorry, only margarita (key m ) and creamy bacon (key c) are available.")
        return (False, None)
    return (True, builder)


def main():
    builders = dict(m=MargaritaBuilder, c=CreamyBaconBuilder)
    valid_input = False
    while not valid_input:
        valid_input, builder = validate_style(builders)
    print()
    waiter = Waiter()
    waiter.construct_pizza(builder)
    pizza = waiter.pizza
    print()
    print(f"Enjoy your {pizza}!")


if __name__ == "__main__":
    main()
