# python-resources

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
