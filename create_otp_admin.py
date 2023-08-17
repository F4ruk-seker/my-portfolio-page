import pyotp


import qrcode
from io import BytesIO
import base64

hash = pyotp.random_base32()

print(hash)
hash_gen = pyotp.TOTP(hash).provisioning_uri(name="f4rukseker@gmail.com", issuer_name="pars")
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(hash_gen)
qr.make(fit=True)
img = qr.make_image(fill_color='black', back_color='white')
buffered = BytesIO()
# img.save(buffered, format="PNG")
img.save(buffered)
encoded = base64.b64encode(buffered.getvalue()).decode()

print(f'<img width="200px" height="200px" src="data:image/png;base64,{encoded}">')