class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    def change_color(self, color):
        Animal.color = color


first_animal = Animal("Fox", 2)
first_animal.change_color("red")
second_animal = Animal("Fos_2", 5)
second_animal.change_color("red")
