ids= {1524, 1144, 6945, 1524, 8897, 6945}
print(ids)

try:
    print(ids[2])
except TypeError:
    print('Items in a set are not ordered! So you cannot use index')

print(len(ids))
    
for item in ids:
    print(item)

duplicates = [6, 88, 15, 96, 6, 88, 15, 96]
print(duplicates)

print(set(duplicates))
print(sorted(set(duplicates)))

bools = {True, 1, False, 0}
print(bools)
