import base64
import hashlib

data = [1,2,3,4,5]

for i in data:
    if i%2==1:
        # data.__delitem__(i)
        del data[i]

print(data)


str = '1111'
md5_str = hashlib.md5(str.encode('utf8')).hexdigest()
base_str = base64.b64encode(md5_str.encode('utf-8')).decode('utf-8')
print(md5_str,base_str)