# Classes
# https://learning.oreilly.com/library/view/python-crash-course/9781492071266/xhtml/ch09.xhtml

class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def sit(self):
    print(f"{self.name} is now sitting.")

  def roll_over(self):
    print(f"{self.name} is rolling over")

my_dog = Dog('Boo', 10)

print(f"My dogs name is {my_dog.name}")
print(f"My dogs age is {my_dog.age}")
my_dog.sit()
my_dog.roll_over()

my_dog.name = "Scooby"
my_dog.sit()

from car import Car
my_new_car = Car('audi', 'b5', 1999)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
