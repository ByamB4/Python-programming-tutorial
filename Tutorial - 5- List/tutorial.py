names = ['ByamBa', 'David', 'John', 'Alice']

names.append('Jack')                          # Jack утгийг List лүү оруулж байна
names.count('ByamBa')                         # ByamBa утгийг хэд байгааг тоолж байна
names.index('David')                          # David хэд дэхь индекс болохыг олно. Хэрэв элемент байхгүй тохиолдолд -1 ирнэ
names.insert(3, 'Hako')                       # Hako нэрийг 3 дахь индекс дээр оруулж байна
names.sort()                                  # Эрэмбэлж байна
names.clear()                                 # List утгуудыг устгаж байна
