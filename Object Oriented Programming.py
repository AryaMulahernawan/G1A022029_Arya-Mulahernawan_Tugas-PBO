# Contoh OOP: kelas mobil
class Car:
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0

  def get_descriptive_name(self):
    long_name = f"{self.year} {self.make} {self.model}"
    return long_name.title()

  def read_odometer(self):
    print(f"This car has {self.odometer_reading} miles on it.")

  def update_odometer(self, mileage):
    if mileage >= self.odometer_reading:
      self.odometer_reading = mileage
    else:
      print("You can't roll back an odometer!")

  def increment_odometer(self, miles):
    self.odometer_reading += miles

my_car = Car('toyota', 'avanza', 2022)
print(my_car.get_descriptive_name()) # Toyota Avanza 2022
my_car.update_odometer(500)
my_car.read_odometer() # This car has 500 miles on it.
