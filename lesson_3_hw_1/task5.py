print("Write the number:")
a = input()
print("The first variant:", sum(map(int, str(a))))

b = int(a[0])
c = int(a[1])
d = int(a[2])
print("The second variant:", b+c+d)
