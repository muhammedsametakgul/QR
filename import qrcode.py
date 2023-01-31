import qrcode
import image
import random

qr=qrcode.QRCode(
    version= 15,
    box_size=8,
    border= 5
)
name=random.randint(0,100000)
data =input()

qr.add_data(data)
qr.make(fit=True)
img =qr.make_image(fill="black",back_color="white")
img.save(str(name) +".png")