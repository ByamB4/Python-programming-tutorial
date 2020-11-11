student = {
    'name': 'Byamba',
    'age': 20,
    'courses': [
        'C',
        'Java',
        'Python'
    ],
    2: 'test'
}        # Dictionary үүсгэж байна

print(student['name'])                          # Нэрийг хэвлэж байна
print(student.keys())                           # Бүх 'key' ийг хэвлэж байна
# Бүх 'value' утгийг хэвлэж байна
print(student.values())
print(student.items())                          # 'key', 'value'-г хэвлэж байна

student['address'] = 'Darkhan'                  # Шинэ утга оруулж байна
