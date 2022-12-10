name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = 'ada'
last_name = 'lovelace'
# f strings - interpolation
full_name = f"{first_name} {last_name}"
print(full_name)

first_name = 'ada    '
# Strip (also, rstrip and lstrip for left and right only)
print(f"{first_name.strip()} {last_name}")

# Constants are a convention, not a hard rule:
NAME = 'ada lovelace'
NAME = 'something else'
print(NAME)
