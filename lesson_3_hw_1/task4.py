print("Write the data:")
a = input()
b = a.split('*')
c = list(map(int, b[1].split('-')))
d = list(map(int, b[2].split('-')))
print("Name:", b[0])
print("Age:", d[0]-c[0], "years")
