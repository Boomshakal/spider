key=''
k=2
key="&#x{}".format(k)
print(key)

key2=eval("u'\\u{}".format(k) + "'")
print(key2)