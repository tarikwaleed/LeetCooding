# Some cool hacks tricks i learned during my competitive programming journey

### if you want to iterate n times and you don't want to use the iteration variable

```python
for _ in '-' * n:
    print('a')
```

will print the letter 'a' n times , as well as

```python
for _ in range(n):
    print('a')
```

### to take n line of input as list of lists

```python
list_of_lists = [input().split() for _ in '_' * n]
print(list_of_lists)
```

```
Output:
[[..,..],[..,..,..,..],[..,..]]
```

### to unpack the list

```python
print(*list_of_lists)
```

```python
Output:
[..,..], [..,.., .., ..], [..,..]
```