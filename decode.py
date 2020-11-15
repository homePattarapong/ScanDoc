from PIL import Image
from pyzbar.pyzbar import decode
data = decode(Image.open('.\\output\\1605458731\\output1.jpg'))
print(data)
for i in data:
    print(i.data.decode("utf-8"))
