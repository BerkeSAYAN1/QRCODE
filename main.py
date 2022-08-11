import qrcode
data = qrcode.make("Hello world")
data.save("vol1.png")