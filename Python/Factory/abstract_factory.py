class Frog():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print(f"{self} the Frog encounters {obstacle} and {obstacle.action()}")


class Bug():
    def __str__(self):
        return f"a bug"

    def action(self):
        return f"eats it"


class FrogWorld():
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return f"\n\n\t------ Frog World ------"

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


class Wizard(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print(f"{self} the Wizard encounters {obstacle} and {obstacle.action()}"
              )


class Ork():
    def __str__(self):
        return f"an ork"

    def action(self):
        return f"beats it"


class WizardWorld():
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return f"\n\n\t------ Wizard World ------"

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork()


class GameEnvironment():
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


def validate_age(age):
    return False if age < 18 else True


if __name__ == "__main__":
    age = input("What is your age?")
    name = input("What is your name?")
    game = FrogWorld if not validate_age(age) else WizardWorld
    environment = GameEnvironment(game(name))
    environment.play()
