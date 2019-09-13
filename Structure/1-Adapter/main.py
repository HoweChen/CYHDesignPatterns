class Synthesizer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'the {self.name} synthesizer'

    def play(self):
        return f'is playing an electronic song'


class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name} the human'

    def speak(self):
        return 'says hello'


class Computer:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'the {self.name} computer'

    def execute(self):
        return 'executes a program'


class Adapter:
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.name = obj.name  # 这里的做法让注入的obj的name暴露出来给外部使用者
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)


def main():
    objects = [Computer("Asus")]
    synth = Synthesizer("moog")
    # 注入的是类的方法
    objects.append(Adapter(synth, dict(execute=synth.play)))
    human = Human("Bob")
    objects.append(Adapter(human, dict(execute=human.speak)))

    for i in objects:
        print(i.name)
        print(f'{str(i)} {i.execute()}')


if __name__ == "__main__":
    main()
