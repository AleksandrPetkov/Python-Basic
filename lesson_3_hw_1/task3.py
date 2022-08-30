print("Write something on a 'snake_case'")
a = input()
b = ''.join(a.capitalize() for a in a.split('_'))
print("On 'Capitalized camelCase' your text will be", b)
