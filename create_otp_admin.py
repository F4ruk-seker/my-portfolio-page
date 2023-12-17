import pyotp
import qrcode
from io import BytesIO
import base64
import environ

if input('otp task Create/use').lower() == 'u':
    totp_hash = input('entry hash : ')
else:
    totp_hash = pyotp.random_base32()

totp_gen = pyotp.TOTP(totp_hash)
hash_gen = totp_gen.provisioning_uri(name=input('email : '), issuer_name=input('user name : '))
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(hash_gen)
qr.make(fit=True)
img = qr.make_image(fill_color='black', back_color='white')
buffered = BytesIO()
# img.save(buffered, format="PNG")
img.save(buffered)
encoded = base64.b64encode(buffered.getvalue()).decode()


message = f"""
OTP code {totp_gen.now()}
Secret {totp_hash}
TOTP hash {hash_gen}
html qr code <img width="200px" height="200px" src="data:image/png;base64,{encoded}">
"""


print(message)
# print(f'<img width="200px" height="200px" src="data:image/png;base64,{encoded}">')

