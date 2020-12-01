## Файлтай ажиллах, хийгдэх үйлдлүүд

```python
# Файлаас уншиж байна
with open('lorem.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        print(f'Line: {line}')

# Файлруу бичиж байна
with open('out.txt', 'w') as f:
    for i in range(10):
        f.write(f'Line: {i}: some text\n')
```
