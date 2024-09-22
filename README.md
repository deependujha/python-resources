# python-resources

## Basic Python

<details>
  <summary>Iterators</summary>

- When we write `for` loop, it internally calls **`iter()`** on the container object.
- The **`iter()`** function returns an **`iterator`** object.
- The **`iterator`** object has a **`__next__()`** method that returns the next item in the container.
- The **`__next__()`** method is called repeatedly until it raises **`StopIteration`** exception, which tells the **`for`** loop to stop iterating.

```python
>>> s = 'abc'
>>> it = iter(s)
>>> it
<str_iterator object at 0x10c90e650>
>>> next(it)
'a'
>>> next(it)
'b'
>>> next(it)
'c'
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(it)
StopIteration
```

- To add `iterator` behaviour to a class, refer to [the sample code](./01_iterator.py)

</details>

<details>
  <summary>Generators</summary>

- **`Generators`** are a simple and powerful tool for creating `iterators`.
- They are written like regular functions but use the **`yield`** statement whenever they want to return data.
- Each time **`next()`** is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed).
- When it terminates, it raises **`StopIteration`** exception.

```python
>>> def reverse(data):
...    for index in range(len(data)-1, -1, -1):
...        yield data[index]
>>>
>>> for char in reverse('golf'):
...    print(char)
f
l
o
g
```

> Anything that can be done with generators can also be done with class-based iterators as described in the previous section. 
>
> What makes generators so compact is that the `__iter__()` and `__next__()` methods are created automatically.

- [sample generator code](./02_generator.py)

- List comprehension:

```python
>>> [x**2 for x in range(10)] # list comprehension
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> (x**2 for x in range(10)) # list comprehension
<generator object <genexpr> at 0x10c90e650>
```

- To convert a generator to a list, use the `list()` function.
- `all()` and `any()` functions can be used to check if all or any of the elements in a generator are true.

```python
>>> list((x**2 for x in range(10)))
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> all((x**2>0 for x in range(10)))
True
```

- `all((...generator))` and `any((...generator))` can also be used with `all([...list])` and `any([...list])`.

- But, generators will be more efficient than lists when the condition is more complex and the list is very long.

</details>

