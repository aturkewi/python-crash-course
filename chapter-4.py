# working with lists
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
  print(magician)

# make a list with range()
# this goes from 1-4 (non inclusive end)
for num in range(1,5):
    print(num)

# making a list from a range
numbers = list(range(1,5))
print(numbers)

# other list operators
min(numbers)
max(numbers)
sum(numbers)

# list comprehension
# (works like map)
squares = [value**2 for value in range(1, 11)]
print(squares)
# >>> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# slice
# list[start_of_slice:end_of_slice]
print(squares[2:3])
# >> [9]

# copy a list
new_squares = squares[:]

# tuples - immutable lists
dimensions = (200,50)
