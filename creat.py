# for i in range(24+1):
#     print(f"{i}:0,",end='')
#
#
#March
import pyotp
import qrcode

gen = pyotp.random_base32()

code = pyotp.TOTP("").provisioning_uri(name="f4rukseker@gmail.com",issuer_name="pars")
print(code)
qrcode.make(code).save("qr_auth.png")

print(code)


# gen = pyotp.TOTP("")
#
# gen.verify(input(": "))