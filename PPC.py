class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def __repr__(self):
        return 'This is a car'

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name

    def read_odometer(self):
        print(f'This car has {self.odometer_reading} miles on it')

    def update_odometer(self, mileage):
        if self.odometer_reading >= mileage:
            self.odometer_reading = mileage
        else:
            print('Invalid mileage number')

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f'This car has a {self.battery_size} -kWh battery.')

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = f'This car can go approximately {range} miles on a full charge.'
        return message


def main():
    newcar = Car('Audi', 'A4', 2016)
    print(newcar.get_descriptive_name() + ' with odometer reading at ' + str(newcar.odometer_reading))
    newcar.increment_odometer(500)
    newcar.read_odometer()
    my_teslar = ElectricCar('Tesla', 'Model S', 2018)
    print(my_teslar.get_descriptive_name())
    my_teslar.read_odometer()
    my_teslar.battery.describe_battery()
    my_teslar.battery.get_range()


if __name__ == '__main__':
    main()

