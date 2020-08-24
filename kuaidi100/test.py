data = [1,2,3,4,5]

for i in data:
    if i%2==1:
        # data.__delitem__(i)
        del data[i]

print(data)