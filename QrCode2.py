import qrcode

data = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=50,
    border=2
)
data.add_data('Hello world')
data.make(fit=True)

image = data.make_image(fill_color="red",back_color="black")
image.save('vol2.png')