c, d = 1, 2.35
print("Before changes 1:", c, ",", d)
s = c
c = d
d = s
print("After changes 1:", c, ",", d)

a, b = 'c', 3
print("Before changes 2:", a, ",", b)
a, b = b, a
print("After changes 2:", a, ",", b)

e, f = 23, 48
print("Before changes 3:", e, ",", f)
e = e + f
f = e - f
e = e - f
print("After changes 3:", e, ",", f)
