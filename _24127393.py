#24127393
print("i'm a student")

x=1/7
print("gia tri cua 1/7 la: {:.5f}".format(x))

a= 3
b=5
print("gia tri cua {} + {} la: {}".format(a,b,a+b))

from pyzbar.pyzbar import decode
from PIL import Image

img=Image.open(r"C:/Users/Huy/Documents/checkin_qr_12345.png")
data=decode(img)

if data:
    print("data tin the qrcode: ",data[0].data.decode("utf-8"))
else:
    print("data can't open")

