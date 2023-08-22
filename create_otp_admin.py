import pyotp


import qrcode
from io import BytesIO
import base64
import environ

from config.settings.base import env

# hash = env('TEMP_OTP_HASH')

hash = pyotp.random_base32()

print(hash)


# hash_gen = pyotp.TOTP(hash).provisioning_uri(name="f4rukseker@gmail.com", issuer_name="pars")
hash_gen = pyotp.TOTP('F3EZXKEF7TREYQ3JDOHIDMMJC7SVLSEV')
print(hash_gen.now())
# hash_gen = hash_gen.provisioning_uri(name="f4rukseker@gmail.com", issuer_name="pars")
hash_gen = hash_gen.provisioning_uri(name="", issuer_name="pars")
print('has')

print(hash_gen)
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(hash_gen)
qr.make(fit=True)
img = qr.make_image(fill_color='black', back_color='white')
buffered = BytesIO()
# img.save(buffered, format="PNG")
img.save(buffered)
encoded = base64.b64encode(buffered.getvalue()).decode()


print(f'<img width="200px" height="200px" src="data:image/png;base64,{encoded}">')