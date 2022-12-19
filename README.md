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
