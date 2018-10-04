a = [1,2,4,5,6,2,5,2]
b = []
for x in a:
    if x not in b:
        b.append(x)
c = []
for i in a:
    if a.count(i) == 1:
        c.append(i)
print("All elements used once:",b)
print("Unique elements not been repeated:",c)