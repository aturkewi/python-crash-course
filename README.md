# Python Crash Course

Following along with the Python Crash Course book here: https://learning.oreilly.com/library/view/python-crash-course/

## Personal Python Notes

### Strings

Interpolation
```python
name = "Dumbledore"
print(f"My name is {name}")
```

### Lists

Empty lists `[]` are considered 'falesy'

Iterating:
```python
for num in range(1,5):
  print(num)
```

Comprehension (like a map?):
```python
squares = [value**2 for value in range(1, 11)]
# >>> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

Watch out for some of the list functions as they mutate the list:
- `list.sort()` - mutates / `sorted(list)` - no mutate
- `list.remove(item)` - removes FIRST occurrence of item from list
- `list.insert(index, item)` - mutates

### If Statements

if, else if, else:
```python
num = 1
if num == 1 or num ==2:
  string = "The number is 1 or 2"
elif num == 3:
  string = "The number is 3"
else:
  string = "The number isn't 1, 2, or 3"

print(string)
```
Scoping: Vars are not scoped inside if block:

### Dictionaries

Python 3.7+ dictionaries retain order when iterating.

Deleting from a list: `del alien_0['points']`
`del` must be at the beginning of the line.

Key error if key is missing:
```python
dict = {}
dict['horse']
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'horse'
```
`.get()` returns `None` if it's not there and can take a default:
```python
dict.get('horse')
# None
dict.get('horse', 'big')
# 'big'
```

Looping through a list:
```python
for name, language in favorite_languages.items():
  print(f"{name} prefers {language}")
```

`.keys()` returns a list of the dict keys.
`.values()` returns a list of dict values.

### While loop

```python
active = True
while active:
  if condition:
    # Fully break out of the loop
    break
  if condition_2:
    # Restart the loop block
    continue
  print('something cool')
```

### Functions

```python
def function_name(arg_1, arg_2='default value'):
  """
  Docstring - Used to define function
  Python looks for this when auto-generating docs
  """
  return {arg_1: arg_1, arg_2: arg_2}
```

This can be called multiple ways:
Args in order: `function_name('apple', 'candy')`
Keyword args: `function_name(arg_1='apply', arg_2='candy')`

Seems a little dangerous? Now _any_ arg names cannot be changed without risking breaking current implementations. **All arg names must be treated as keyword args.**

Note: If data is passed into a function (e.g. a list) it is modified outside of the func because it is the same instance of data (similar to Ruby).

`def func(*any_number_of_args):` - Returns a tuple of args.
`def func(**any_number_of_args)` - Returns a dict of args

### Importing

Importing a class:
```python
from car import Car
```

Importing function(s)

```python
# pizza.py
def make_pizza(some_args):

```

#### Option 1: Import everything in a module scope

```python
import pizza
# aliasing
import pizza_two as p2

# Need to specify module
pizza.make_pizza(16, 'pineapple', 'ham')
```

#### Option 2: Only import some functions

```python
from pizza import make_pizza, func2
# Aliasing...
from pizza_two import make_pizza as make_pizza_two

# No need to specify module
make_pizza(16, 'pineapple', 'ham')
```

#### Option 3: Import all functions to new module

```python
from pizza import *

make_pizza(16, 'pineapple', 'ham')
```

**Careful with this one. This could cause unintended collisions of duplicate names.**

### Classes

Classes are CamelCase
Every class should have a doc string immediately following class def
Import from standard libs first, then a blank line, then import from custom libs

```python
class Dog:
  """Dog class"""
  def __init__(self, name, age):
    """
    Init, a special method name used when creating a new instance
    `self` is automatically passed in by Python, this is not an arg that we need to pass
    """
    self.name = name
    self.age = age

  def sit(self):
    """
    Same note, `self` is auto passed in by Python so we can access the instance
    """
    print(f"{self.name} is now sitting.")
```

Attrs can always be directly accessed (e.g. `dog.name = "new name"`). Programers need to know not to use these if there is a method like `def update_name(new_name):` or something like that. 

Inheritance:
```python
# Car must already be defined (in the same file?)
class ElectricCar(Car):
  """ElectricCar inherits from Car"""
  def __init__(self, make, model, year):
    # Calling Car's `__init__` method. Note, still don't need to pass in `self`
    super().__init__(make, model, year)
```

#### Importing - Same as for functions...

Importing a class `from car import Car`

Multiple classes can be in a single module: `from car import Car, ElectricCar, Battery`

Can also add aliases: `from car import ElectricCar as EC`

Importing all classes from a module:
```python
import car

my_car = car.Car('volkswagen', 'beetle', 1999)
my_electric_car = car.ElectricCar('speedy', 'golf cart', 2010)
```

All classes can be imported directly with `from car import *`, but it's not recommended (name collisions again).
