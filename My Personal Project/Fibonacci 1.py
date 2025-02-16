a = 1
b = 0

print(b)
print(a)


for i in range(0,5):
    c = b
    b = a
    a = c+b
    print(a)
