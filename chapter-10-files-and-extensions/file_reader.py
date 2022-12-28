# with closes file once it's not longer in use
print('reading the whole file')
with open('pi_digits.txt') as file_object:
  contents = file_object.read()
# read adds a trailing line. rstrip to clean it up
print(contents.rstrip())

# reading line by line
print('\nreading line by line')
with open('pi_digits.txt') as file_object:
  for line in file_object:
    print(line.rstrip())

print('\nstoring lines for later use after the file is closed:')
with open('pi_digits.txt') as file_object:
  lines = file_object.readlines()

for line in lines:
  print(line.rstrip())

# Writing to a creates and clears it
with open('programming.txt', 'w') as file_object:
  file_object.write('I love programming.\n')
  file_object.write('Here is a second line.\n')

with open('programming.txt', 'a') as file_object:
  file_object.write('Here is line 3!!\n')

# Exceptions
try:
  print(5/0)
except ZeroDivisionError:
  print('you cannot divide by zero')


print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
  first_number = input("\nFirst number: ")
  if first_number == 'q':
    break
  second_number = input("Second number: ")
  if second_number == 'q':
    break
  try:
    answer = int(first_number) / int(second_number)
  except ZeroDivisionError:
    print('cannot divide by zero')
  else:
    print(answer)
