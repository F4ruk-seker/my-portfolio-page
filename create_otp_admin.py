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
hash_gen = hash_gen.provisioning_uri(name="f4rukseker@gmail.com", issuer_name="pars")
# hash_gen = hash_gen.provisioning_uri(name="", issuer_name="pars")
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

"""
EXF2AMNBAJDIHX6NTWQ6IJ2DNSHS7RT3
320077
has
otpauth://totp/pars:Secret?secret=F3EZXKEF7TREYQ3JDOHIDMMJC7SVLSEV&issuer=pars
<img width="200px" height="200px" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAdYAAAHWAQAAAADiYZX3AAADeElEQVR4nO2dTW7jMAyFH8cGupRvkKMoNyt6M/soPUABeRnABmdBUVLdNE7boNNm3lsE8c8HJcADSVGKI4rPav3zaRQgS5YsWbJkyZIlS5bsB6SqqjqWwzGoAujsvL2zq2Hxm4Kqqi6/8fuS/V42WwXALAKEk2AaAEQ9iRwBqKatCf/1Zyb7C9hVRIb8Xsf5QeUxAcD8oIipU7PZJCK3HZfsXbL99kTU1c7pJIBiBjANHSSm9Ybjkr1v9o2vpmOngpDMYYJwEgVW0Wl4ueG4ZO+b9ZLJ6yvV1OXDsdZcdt+yufk3fl+y38vOIiLSA9PhJADW/DINgI5hAaYBEBGxMv5W45K9TzaHoEYJQEyATfuiNRsAnzJWMV6RfV81tfmZTnUMOech1tzoF9i/Irsvb0l1arEpFjcVc9VeKWKCxTD6iuxFta3OrZFc0Ut2C1Ws28nuqqmqgM6cg7x602levQnVV8yDZK9RkwcBwFOgWs6r3YV8NeUlRPqK7EVVX3nrygv1bKkFto4TmQfJXi8vqHK6M+WwtDS3eIKsnQn6iuz7Ki4BcoshzwdzGZUAj1ILcneLviK7p+qrthEaFnh9lSstsM9A9gPSRql0Pku59brmql6jr8heVJMHc1iCFermsFiqL3sHzgfJXqNtvHpdo7+q5ZkHyX6UnXtgGlaR49xD9bn3cqvJjavo02F5y35lXLL3ybZbquwFpRua0LauGocxD5Ldke8XnftFAAGiAgIAgqC2Bdm1igKdShy/Pi7Z+2ab+sojknr7XXO1bhfyZhnW7WSvUS3Z/UxpjiZfd45ltmg2Y91Odk9eXy2oi4R+wS1lGx38t6rsX5HdV/ZVaaajpkBffM7rOEBujrJuJ7urc/NBu1C6odbOir7Uw3hFdl+Nr7TsPs7hq2vc1IrxiuyedKMR7aQw35KAmgzpK7LXspNkAVhFHtMqiPYCyBGAjlilbnS40bhk75Q9nwdVy95QAHm5sMYwxiuyOyrPZ1h7IOQnMAjCS2/nYhqQO1uzAAjpNuOS/d/YuQfic583uT8dFtgP7G3rVVrFf7zzgz4z2Z/GnnlOEYDpsFi8Usw9FPMgOg3dIggpP23mi+OSvW/2zPNkUPZabbZjddrMDFlfkb0k7y744fYRRUHV13a6tgtBX5G9IOH/TZAlS5YsWbJkyZIl++PZv0+3K2Z6AW5EAAAAAElFTkSuQmCC">
"""