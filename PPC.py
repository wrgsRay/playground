class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name


newcar = Car('Audi', 'A4', 2016)
print(newcar.get_descriptive_name() + 'with odometer reading at ' + str(newcar.odometer_reading))

