## Функц гэж юу вэ ? Хэрхэн ажиллах талаар

```python
def sum_of_numbers(*args, **kwargs):
    """Will return sum of numbers"""
    print(kwargs['name'])
    return sum(args)


teacher = {
    'name': 'Byambadalai',
    'more': 'https://facebook.com/ByamB4'
}

print(sum_of_numbers(6, 2, 3, 4, 5, **teacher))
```
