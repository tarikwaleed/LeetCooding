**Some cool hacks tricks i learned during my competitive programming journey**

- if you want to iterate n times and you don't want to use the iteration variable

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
[..,..] [..,.., .., ..] [..,..]
```

**Trick from CF268-D2-A**

suppose you have the followint input:

3

1 2

3 4

5 6

the first line of input is n .

the following line of code takes the input as rows and then convert them to colums using zip():

```python
a, b = zip(*(input().split() for _ in '_' * n))
```

a=[1,3,5]

b=[2,4,6]


