print("Write the number:")
a = input()
print("The first variant:", sum(map(int, str(a))))

print("Write another number:")
b = int(input())
c = b % 10
d = (b % 100)//10
e = b // 100
print("The second variant:", c+d+e)
