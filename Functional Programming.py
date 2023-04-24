# Contoh FP: fungsi filter dan map
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter mengembalikan list baru dengan elemen yang memenuhi kondisi
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# map mengembalikan list baru dengan elemen yang telah diubah
squared_numbers = list(map(lambda x: x**2, numbers))

print(even_numbers) # [2, 4, 6, 8, 10]
print(squared_numbers) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
