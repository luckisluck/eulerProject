#problem 2
i = 0
j = 2
k = 0
multiple=[1,2]

while k <= 4000000:
    k = multiple[j-1] + multiple[j-2] 
    multiple.append(k)
    j = j + 1

for items in range(len(multiple)):
    if(multiple[items] % 2 == 0):
        i = i + multiple[items]

print(i)