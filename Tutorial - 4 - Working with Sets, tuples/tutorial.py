tutorials = ('C', 'C++', 'Java', 'Python')                  # Энэ бол tuple
# 'C' гэх утга хэд байгааг тоолж байна
tutorials.count('C')
# 'C++' хэд дэхь индекс болохыг олж байна
tutorials.index('C++')
# ---------------------------------------------------------------------------------------------------

# Set үүсгэж байна хэрвээ давхардсан элемент байвал оруулахгүй
nums_a = {1, 2, 3, 4, 5}
nums_b = {4, 5, 6, 7, 8}
# Нэгдлийг хэвлэнэ 'union'
print(nums_a | nums_b)
# Огтлолцлыг хэвлэнэ 'intersection'
print(nums_a & nums_b)
# nums_b байгаа элементүүдийг nums_a ээс хасна
print(nums_a - nums_b)
# nums_a байгаа элементүүдийг nums_b ээс хасна
print(nums_b - nums_a)
# Union - Intersection буюу нэгдлээс огтлолцлыг хасна
print(nums_a ^ nums_b)
