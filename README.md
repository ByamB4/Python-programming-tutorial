## Алдааны мессежтэй ажиллах, Exception handler

```python
try:
    print(1 / 0)

    f = open('not_found.txt')

except ZeroDivisionError:
    print('Toog 0t huvaaj bolohgui')

except FileNotFoundError:
    print('File oldsongui')

else:
    print(f.read())

finally:
    print('Exiting...')
```
