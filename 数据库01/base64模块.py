import base64

data = '嗨'

data_encode = base64.urlsafe_b64encode(data.encode())

print(data_encode)

result = base64.urlsafe_b64decode(data_encode)
print(result.decode())