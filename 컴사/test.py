a = {"a":1,"b":2}

b = {"a":1,"b":3}


max = 0
key = ""
for i in b:
    if b[i] >= max:
        max = b[i]
        key = i

if key in a:
    a[key] += 1

print(a)
