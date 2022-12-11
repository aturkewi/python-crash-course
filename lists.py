bikes = ['honda']
bikes.append('yamaha')

bikes.insert(1, 'suzuki')
print(bikes)
# >>> ['honda', 'suzuki', 'yamaha']

del bikes[1]
print(bikes)
# >>> ['honda', 'yamaha']
# order of opps seems different than expected.
# del isn't a normal function?

# pop can be passed an arg (works like delete then)
# without an arg, it pops the last one
popped_bike = bikes.pop(0)
print(popped_bike)
# >>> honda
print(bikes)
# >>> ['yamaha']

# delete by value
bikes.remove('yamaha')
# note: only deletes first occurrence, not all

# SORT
cars = ['bmw', 'audi', 'toyota', 'subaru']

# sorting and creating a new list with sorted()
sorted_cars = sorted(cars)
print(cars)
# >>> ['bmw', 'audi', 'toyota', 'subaru']
print(sorted_cars)
# >>> ['audi', 'bmw', 'subaru', 'toyota']

# sort () is destructive
# sort can take options like (reverse=True)
cars.sort()
print(cars)
# >>> ['audi', 'bmw', 'subaru', 'toyota']

# other functions
cars.revers()
len(cars)
