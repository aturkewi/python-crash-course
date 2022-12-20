# Dictionaries
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# Removing a key/value pair
del alien_0['points']
# Note: `del` must be at the start of the line and has no return val
print(alien_0)

# Can define multiline:
favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'ruby',
  'phil': 'python'
}

print(favorite_languages.get('susan'))
# Returns `None`

# Iterating through dict
for name, language in favorite_languages.items():
  print(f"{name} prefers {language}")
# Note the .items() call

# Iterating through keys in a dict:
for name in favorite_languages.keys():
  print(f"Name: {name}")

# Looping through keys is default behavior and doesn't need the .keys() call
for name in favorite_languages:
  print(f"Name: {name}")

if 'erin' not in favorite_languages.keys():
  print("Erin does not have a favorite language")


