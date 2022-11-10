class Animals:
    """
    Creating master class of Animals
    """
    def __init__(self, name_of_animals, weight_of_animal, speed_of_animals):
        """
        Initialization attributes:
        :param name_of_animals:
        :param weight_of_animal:
        :param speed_of_animals:
        """
        self.name_of_animals = name_of_animals
        self.weight_of_animal = weight_of_animal
        self.speed_of_animals = speed_of_animals

    def __str__(self):
        """
        Function returned string with attributes for object
        """
        return f'Name of Animal: {self.name_of_animals}, Weight of animal: {self.weight_of_animal} kg, ' \
               f'Speed of animal: {self.speed_of_animals} Km/h'


class Bird(Animals):
    """
    Creating slave class Bird from master class Animals
    """
    def __init__(self, name_of_animals, weight_of_animal, speed_of_animals, color):
        """
        Initialization attributes:
        :param name_of_animals:
        :param weight_of_animal:
        :param speed_of_animals:
        :param color:
        """
        super().__init__(name_of_animals, weight_of_animal, speed_of_animals)
        self.color = color

    def __str__(self):
        """
        Function returned string with attributes for object
        """
        main = super().__str__()
        return main + f', Color of bird: {self.color}'


class Musophagidae(Bird):
    """
    Creating slave class Musophagidae from class Bird
    """
    def __init__(self, name_of_animals, weight_of_animal, speed_of_animals, color):
        """
        Initialization attributes:
        :param name_of_animals:
        :param weight_of_animal:
        :param speed_of_animals:
        :param color:
        """
        super().__init__(name_of_animals, weight_of_animal, speed_of_animals, color)

    def __str__(self):
        """
        Function returned string with attributes for object
        """
        main = super().__str__()
        return main

    def say(self):
        """
        Creating function "say" for animal
        """
        print("Voise: сch cch cch")


class Phoenicopteridae(Bird):
    """
    Creating slave class Phoenicopteridae from class Bird
    """
    def __init__(self, name_of_animals, weight_of_animal, speed_of_animals, color):
        """
        Initialization attributes:
        :param name_of_animals:
        :param weight_of_animal:
        :param speed_of_animals:
        :param color:
        """
        super().__init__(name_of_animals, weight_of_animal, speed_of_animals, color)

    def __str__(self):
        """
        Function returned string with attributes for object
        """
        main = super().__str__()
        return main

    def say(self):
        """
        Creating function "say" for animal
        """
        print("Voise: cke cke cke")


class Reptile(Animals):
    """
    Creating slave class Reptile from master class Animals
    """
    def __init__(self, name_of_animals, weight_of_animal, speed_of_animals, color):
        """
        Initialization attributes:
        :param name_of_animals:
        :param weight_of_animal:
        :param speed_of_animals:
        :param color:
        """
        super().__init__(name_of_animals, weight_of_animal, speed_of_animals)
        self.color = color

    def __str__(self):
        """
        Function returned string with attributes for object
        """
        main = super().__str__()
        return main + f', Color of Reptile: {self.color}'


class Agamidae(Reptile):
    """
    Creating slave class Agamidae from class Reptile
    """
    def __init__(self, name_of_animals, weight_of_animal, speed_of_animals, color):
        """
        Initialization attributes:
        :param name_of_animals:
        :param weight_of_animal:
        :param speed_of_animals:
        :param color:
        """
        super().__init__(name_of_animals, weight_of_animal, speed_of_animals, color)

    def __str__(self):
        """
        Function returned string with attributes for object
        """
        main = super().__str__()
        return main

    def say(self):
        """
        Creating function "say" for animal
        """
        print("Voise: ghh ghh ghh")


class Testudinidae(Reptile):
    """
    Creating slave class Testudinidae from class Reptile
    """
    def __init__(self, name_of_animals, weight_of_animal, speed_of_animals, color):
        """
        Initialization attributes:
        :param name_of_animals:
        :param weight_of_animal:
        :param speed_of_animals:
        :param color:
        """
        super().__init__(name_of_animals, weight_of_animal, speed_of_animals, color)

    def __str__(self):
        """
        Function returned string with attributes for object
        """
        main = super().__str__()
        return main

    def say(self):
        """
        Creating function "say" for animal
        """
        print("Voise: ech ech ech")


class Mammal(Animals):
    """
    Creating slave class Mammal from master class Animal
    """
    def __init__(self, name_of_animals, weight_of_animal, speed_of_animals, color):
        """
        Initialization attributes:
        :param name_of_animals:
        :param weight_of_animal:
        :param speed_of_animals:
        :param color:
        """
        super().__init__(name_of_animals, weight_of_animal, speed_of_animals)
        self.color = color

    def __str__(self):
        """
        Function returned string with attributes for object
        """
        main = super().__str__()
        return main + f', Color of Mammal: {self.color}'


class Sciuridae(Mammal):
    """
    Creating slave class Sciuridae from class Mammal
    """
    def __init__(self, name_of_animals, weight_of_animal, speed_of_animals, color):
        """
        Initialization attributes:
        :param name_of_animals:
        :param weight_of_animal:
        :param speed_of_animals:
        :param color:
        """
        super().__init__(name_of_animals, weight_of_animal, speed_of_animals, color)

    def __str__(self):
        """
        Function returned string with attributes for object
        """
        main = super().__str__()
        return main

    def say(self):
        """
        Creating function "say" for animal
        """
        print("Voise: hrrr chi chi")


class Ursidae(Mammal):
    """
    Creating slave class Ursidae from class Mammal
    """
    def __init__(self, name_of_animals, weight_of_animal, speed_of_animals, color):
        """
        Initialization attributes:
        :param name_of_animals:
        :param weight_of_animal:
        :param speed_of_animals:
        :param color:
        """
        super().__init__(name_of_animals, weight_of_animal, speed_of_animals, color)

    def __str__(self):
        """
        Function returned string with attributes for object
        """
        main = super().__str__()
        return main

    def say(self):
        """
        Creating function "say" for animal
        """
        print("Voise: ckeeey ckeeey ")


turaco = Musophagidae("Red-crested turaco", 0.3, 30, "green-red")
print(turaco)
turaco.say()

flamingo = Phoenicopteridae("American flamingo", 3, 20, "purple")
print(flamingo)
flamingo.say()

amaga = Agamidae("Sinai agama", 0.1, 15, "blue")
print(amaga)
amaga.say()

turtle = Testudinidae("Floreana giant tortoise", 7, 0.001, "grey")
print(turtle)
turtle.say()

squirrel = Sciuridae("Fox squirrel", 0.15, 35, "orange-grey")
print(squirrel)
squirrel.say()

panda = Ursidae("Giant panda", 60, 45, "black-white")
print(panda)
panda.say()
