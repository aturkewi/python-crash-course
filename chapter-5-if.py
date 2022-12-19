# If Statements

# Empty lists are falsey
# Else if is -> elif

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
  if car == 'bmw':
    print(car.upper())
  else:
    print(car)

# Cannot use & or &&
print(1 == 1 and 2 == 2)

# Cannot use ||
print(1 == 2 or 2 == 2)

# Item in list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
item = 'mushrooms'
print(f"{item.capitalize()} in list: {item in requested_toppings}")
item = 'peperoni'
print(f"{item.capitalize()} in list: {item in requested_toppings}")
# 'not' to negate
print(f"{item.capitalize()} not in list: {item not in requested_toppings}")

print('\n')

# elif for else if
# note scoping. vars are NOT scoped inside if blocks
age = 12

if age < 4:
  price = 0
  # print("Your admission cost is $0")
elif age < 18:
  price = 25
  # print("Your admission cost is $25")
else:
  price = 40
  # print("Your admission cost is $40")

print(f"Your admission cost is ${price}")

# EMPTY LISTS ARE FALSEY!
print(f"Empty lists are considered: {not not []}")
list = []
if list:
  print("This list has something in it")
else:
  print("This list is empty")


