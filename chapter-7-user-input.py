# User Inputs and While Loops
# https://learning.oreilly.com/library/view/python-crash-course/9781492071266/xhtml/ch07.xhtml

message = input("Tell me something to say:")
print(f"Ok, '{message}'")

age = input("How old are you?")
# Need to use `int()` to have the string treated as an int
if int(age) >= 18:
  print("Old enough to vote at least!")

# While loops
current_number = 1
while current_number < 5:
  print(f"Current number: {current_number}")
  current_number += 1
