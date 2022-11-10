class Transport:
    """
    Creating master class of Transport
    """
    def __init__(self, number_of_transport, number_of_wheels, power_of_engine, max_speed):
        """
        Initialization attributes:
        :param number_of_transport:
        :param number_of_wheels:
        :param power_of_engine:
        :param max_speed:
        """
        self.number_of_transport = number_of_transport
        self.number_of_wheels = number_of_wheels
        self.power_of_engine = power_of_engine
        self.max_speed = max_speed

    def __str__(self):
        """
        Function returned string with attributes for object
        """
        return f'Number of transport: {self.number_of_transport}, Number of wheels: {self.number_of_wheels}, ' \
               f'Power of engine: {self.power_of_engine} HP, Max speed: {self.max_speed} Km/h'


class Bicycle(Transport):
    """
    Creating slave class Bicycle from master class Transport
    """
    def __init__(self, number_of_transport, number_of_wheels, power_of_engine, max_speed, bicycle_brand):
        """
        Initialization attributes:
        :param number_of_transport:
        :param number_of_wheels:
        :param power_of_engine:
        :param max_speed:
        :param bicycle_brand:
        """
        super().__init__(number_of_transport, number_of_wheels, power_of_engine, max_speed)
        self.bicycle_brand = bicycle_brand

    def __str__(self):
        """
        Function returned string with attributes for object
        """
        return f'Number of wheels: {self.number_of_wheels}, Max speed: {self.max_speed} Km/h, ' \
               f'Bicycle Brand: {self.bicycle_brand}'


class Car(Transport):
    """
    Creating slave class Car from master class Transport
    """
    def __init__(self, number_of_transport, number_of_wheels, power_of_engine, max_speed, car_brand):
        """
        Initialization attributes:
        :param number_of_transport:
        :param number_of_wheels:
        :param power_of_engine:
        :param max_speed:
        :param car_brand:
        """
        super().__init__(number_of_transport, number_of_wheels, power_of_engine, max_speed)
        self.car_brand = car_brand

    def __str__(self):
        """
        Function returned string with attributes for object
        """
        main = super().__str__()
        return main + f', Car Brand: {self.car_brand}'


class Bus(Transport):
    """
    Creating slave class Bus from master class Transport
    """
    def __init__(self, number_of_transport, number_of_wheels, power_of_engine, max_speed, bus_brand):
        """
        Initialization attributes:
        :param number_of_transport:
        :param number_of_wheels:
        :param power_of_engine:
        :param max_speed:
        :param bus_brand:
        """
        super().__init__(number_of_transport, number_of_wheels, power_of_engine, max_speed)
        self.bus_brand = bus_brand

    def __str__(self):
        """
        Function returned string with attributes for object
        """
        main = super().__str__()
        return main + f', Bus Brand: {self.bus_brand}'


class Motorbike(Bicycle):
    """
    Creating slave class Motorbike from class Bicycle
    """
    def __init__(self, number_of_transport, number_of_wheels, power_of_engine, max_speed, motorbike_brand):
        """
        Initialization attributes:
        :param number_of_transport:
        :param number_of_wheels:
        :param power_of_engine:
        :param max_speed:
        :param motorbike_brand:
        """
        super().__init__(number_of_transport, number_of_wheels, power_of_engine, max_speed, None)
        self.motorbike_brand = motorbike_brand

    def __str__(self):
        """
        Function returned string with attributes for object
        """
        return f'Number of transport: {self.number_of_transport}, Number of wheels: {self.number_of_wheels}, Max speed: {self.max_speed} Km/h' \
               f', Motorbike Brand: {self.motorbike_brand}'


class Truck(Car):
    """
    Creating slave class Truck from master class Car
    """
    def __init__(self, number_of_transport, number_of_wheels, power_of_engine, max_speed, truck_brand):
        """
        Initialization attributes:
        :param number_of_transport:
        :param number_of_wheels:
        :param power_of_engine:
        :param max_speed:
        :param truck_brand:
        """
        super().__init__(number_of_transport, number_of_wheels, power_of_engine, max_speed, None)
        self.truck_brand = truck_brand

    def __str__(self):
        """
        Function returned string with attributes for object
        """
        return f'Number of transport: {self.number_of_transport}, Number of wheels: {self.number_of_wheels}, ' \
               f'Power of engine: {self.power_of_engine} HP, Max speed: {self.max_speed} Km/h, ' \
               f'Truck brand: {self.truck_brand}'


bicycle = Bicycle(None, 2, None, 40, "BMW")
print(bicycle)

motorbike = Motorbike("AA7356DY", 2, 98, 280, "Yamaha")
print(motorbike)

car = Car("BH71316OI", 4, 231, 280, "BMW")
print(car)

bus = Bus("AI7635BT", 4, 134, 220, "Ford")
print(bus)

truck = Truck("BH6936AE", 4, 480, 120, "MAN")
print(truck)