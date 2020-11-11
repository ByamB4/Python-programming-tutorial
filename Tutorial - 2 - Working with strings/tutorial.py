tutorial = 'Python programming anyway'

print(tutorial.upper())                      # Тэмдэгт мөрийг том болгож байна
# Тэмдэгт мөрийг жижиг болгож байна
print(tutorial.lower())
print(tutorial.count('programming'))         # 'Programming' үгийг тоолж байна
# 'Python' үгийг 'Java' аар сольж байна
print(tutorial.replace('Python', 'Java'))
# 'Python' үгийн index ийг хайж байна
print(tutorial.index('Python'))

name = 'Byambadalai'
age = 20
utube = 'ByamB4'

print(f'{name} is {age} old.')
