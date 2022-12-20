# Functions
# https://learning.oreilly.com/library/view/python-crash-course/9781492071266/xhtml/ch08.xhtml

def greet_user():
  # Docstring - Defines the function and Python uses it to auto-gen docs
  """
  Display simple greeting
  This can be multiple lines?
  """
  print('hello!')

greet_user()

def pets(pet_name, kind_of_pet):
  print(f"I have a {kind_of_pet} named {pet_name}")

# Ordered args
pets('Boo', 'dog')
# Keyword args
pets(kind_of_pet='dog', pet_name='Boo')

# Passing in a copy of a list to a function
unverified_names = ['boo', 'fraya', 'coco']
verified_names = []

def verify_names(unverified_names, verified_names):
  while unverified_names:
    name = unverified_names.pop()
    verified_names.append(name)

  print('done!')

# Using [:] to slice the list and make a duplicate:
verify_names(unverified_names[:], verified_names)

print(f"Original unverified_names: {unverified_names}")
print(f"Original verified_names: {verified_names}")

# Unspecified number of args
def list_toppings(*toppings):
  for topping in toppings:
    print(topping)

list_toppings('peperoni', 'cheese', 'mushroom')
