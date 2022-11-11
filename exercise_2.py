class Animals:
    """
    Creating master class of Animals
    """

    def __init__(self, name_of_animals, weight_of_animal, speed_of_animals):
        """
        Initialization attributes of parameters:
        -name_of_animals:
        -weight_of_animal:
        -speed_of_animals:
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
        Initialization attributes of parameters:
        -name_of_animals:
        -weight_of_animal:
        -speed_of_animals:
        -color:
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

    def __init__(self, name_of_animals, weight_of_animal, speed_of_animals, color, color_of_neb):
        """
        Initialization attributes of parameters:
        -name_of_animals:
        -weight_of_animal:
        -speed_of_animals:
        -color:
        -color_of_neb:
        """
        super().__init__(name_of_animals, weight_of_animal, speed_of_animals, color)
        self.color_of_neb = color_of_neb

    def __str__(self):
        """
        Function returned string with attributes for object
        """
        main = super().__str__()
        return main + f', Color of neb: {self.color_of_neb}'

    def say(self):
        """
        Creating function "say" for Musophagidae
        """
        print("Voise: сch cch cch")


class Phoenicopteridae(Bird):
    """
    Creating slave class Phoenicopteridae from class Bird
    """

    def __init__(self, name_of_animals, weight_of_animal, speed_of_animals, color, length_of_legs):
        """
        Initialization attributes of parameters:
        -name_of_animals:
        -weight_of_animal:
        -speed_of_animals:
        -color:
        -length_of_legs:
        """
        super().__init__(name_of_animals, weight_of_animal, speed_of_animals, color)
        self.length_of_legs = length_of_legs

    def __str__(self):
        """
        Function returned string with attributes for object
        """
        main = super().__str__()
        return main + f', Length of legs: {self.length_of_legs} cm'

    def say(self):
        """
        Creating function "say" for Phoenicopteridae
        """
        print("Voise: cke cke cke")


class Reptile(Animals):
    """
    Creating slave class Reptile from master class Animals
    """

    def __init__(self, name_of_animals, weight_of_animal, speed_of_animals, color):
        """
        Initialization attributes of parameters:
        -name_of_animals:
        -weight_of_animal:
        -speed_of_animals:
        -color:
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

    def __init__(self, name_of_animals, weight_of_animal, speed_of_animals, color, temp_of_body):
        """
        Initialization attributes of parameters:
        -name_of_animals:
        -weight_of_animal:
        -speed_of_animals:
        -color:
        -temp_of_body:
        """
        super().__init__(name_of_animals, weight_of_animal, speed_of_animals, color)
        self.temp_of_body = temp_of_body

    def __str__(self):
        """
        Function returned string with attributes for object
        """
        main = super().__str__()
        return main + f', Temperature of body: {self.temp_of_body} °C'

    def say(self):
        """
        Creating function "say" for Agamidae
        """
        print("Voise: ghh ghh ghh")


class Testudinidae(Reptile):
    """
    Creating slave class Testudinidae from class Reptile
    """

    def __init__(self, name_of_animals, weight_of_animal, speed_of_animals, color, life_expectancy):
        """
        Initialization attributes of parameters:
        -name_of_animals:
        -weight_of_animal:
        -speed_of_animals:
        -color:
        -life_expectancy:
        """
        super().__init__(name_of_animals, weight_of_animal, speed_of_animals, color)
        self.life_expectancy = life_expectancy

    def __str__(self):
        """
        Function returned string with attributes for object
        """
        main = super().__str__()
        return main + f', Life expectancy: {self.life_expectancy} years'

    def say(self):
        """
        Creating function "say" for Testudinidae
        """
        print("Voise: ech ech ech")


class Mammal(Animals):
    """
    Creating slave class Mammal from master class Animal
    """

    def __init__(self, name_of_animals, weight_of_animal, speed_of_animals, color):
        """
        Initialization attributes of parameters:
        -name_of_animals:
        -weight_of_animal:
        -speed_of_animals:
        -color:
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

    def __init__(self, name_of_animals, weight_of_animal, speed_of_animals, color, length_of_tail):
        """
        Initialization attributes of parameters:
        -name_of_animals:
        -weight_of_animal:
        -speed_of_animals:
        -color:
        -length_of_tail:
        """
        super().__init__(name_of_animals, weight_of_animal, speed_of_animals, color)
        self.length_of_tail = length_of_tail

    def __str__(self):
        """
        Function returned string with attributes for object
        """
        main = super().__str__()
        return main + f', Length of tail: {self.length_of_tail} cm'

    def say(self):
        """
        Creating function "say" for Sciuridae
        """
        print("Voise: hrrr chi chi")


class Ursidae(Mammal):
    """
    Creating slave class Ursidae from class Mammal
    """

    def __init__(self, name_of_animals, weight_of_animal, speed_of_animals, color, length_of_wool):
        """
        Initialization attributes of parameters:
        -name_of_animals:
        -weight_of_animal:
        -speed_of_animals:
        -color:
        -length_of_wool:
        """
        super().__init__(name_of_animals, weight_of_animal, speed_of_animals, color)
        self.length_of_wool = length_of_wool

    def __str__(self):
        """
        Function returned string with attributes for object
        """
        main = super().__str__()
        return main + f', Length of wool: {self.length_of_wool} cm'

    def say(self):
        """
        Creating function "say" for Ursidae
        """
        print("Voise: ckeeey ckeeey ")


turaco = Musophagidae("Red-crested turaco", 0.3, 30, "green-red", "yellow")
print(turaco)
turaco.say()

flamingo = Phoenicopteridae("American flamingo", 3, 20, "purple", 52)
print(flamingo)
flamingo.say()

amaga = Agamidae("Sinai agama", 0.1, 15, "blue", 42)
print(amaga)
amaga.say()

turtle = Testudinidae("Floreana giant tortoise", 7, 0.001, "grey", 200)
print(turtle)
turtle.say()

squirrel = Sciuridae("Fox squirrel", 0.15, 35, "orange-grey", 30)
print(squirrel)
squirrel.say()

panda = Ursidae("Giant panda", 60, 45, "black-white", 8)
print(panda)
panda.say()
