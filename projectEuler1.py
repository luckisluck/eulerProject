#problem 1
i = 0
j = 0
multiple=[]
while i < 1000:
    if(i % 3 == 0 or i % 5 == 0 ):
        multiple.append(i)
        j = j + i
    i = i + 1

print(multiple,j)