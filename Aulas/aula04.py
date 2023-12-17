# Trabalhando com Listas, Tuplas e Sets

# Coleções mutaveis e ordenadas de qualquer tipo de dado
bands = ['Metallica', 'Angra', 'Pantera', 'Megadeth']

print(bands[1])
print(bands[-2])
print(bands[4])
print(bands[1:-2])
print(bands[4])

# Modificando as listas

bands.append('Disturbed')

bands2 = ['AC/DC', 'Avenged Sevenfold']
bands.insert(0, bands2)
bands.extend(bands2)

# Adding Elements:
# append(): Add an element to the end.
# insert(): Insert an element at a specific position.

# Removing Elements:
# remove('Angra'): Remove a specific element.
# pop(): Remove and return an element by index.
popped = bands.pop()
print(popped)
# clear(): Remove all elements.

# Other Modifications:
# .extend(): Add elements from another list.
# .reverse() .sort() .sort(reverse=True)
# sorted = sorted(list)
# min(list) max(list) sum(list)
# bands.index('Banda')
# 'in' operator - print('Pantera' in bands)


