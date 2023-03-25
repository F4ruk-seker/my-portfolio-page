# # for i in range(24+1):
# #     print(f"{i}:0,",end='')
# #
# #
# #March
# import pyotp
# import qrcode
#
# gen = pyotp.random_base32()
#
# code = pyotp.TOTP("").provisioning_uri(name="f4rukseker@gmail.com",issuer_name="pars")
# print(code)
# qrcode.make(code).save("qr_auth.png")
#
# print(code)
#
#
# # gen = pyotp.TOTP("")
# #
# # gen.verify(input(": "))


import matplotlib.pyplot as plt

# Market verileri
market_data = [
    {
        "name": "erzurum çağ kebab",
        "results": [
            {"name": "sincere", "result": 20},
            {"name": "reputable", "result": 10},
            {"name": "strong", "result": 20},
            {"name": "competence", "result": 20},
            {"name": "excitement", "result": 20},
        ]
    },
    # Diğer market verileri
]

# Tüm verilerin toplamı
total_results = sum([sum([x['result'] for x in market['results']]) for market in market_data])

# Pasta grafiği verileri
labels = ["arf"]
sizes = [sum([result['result'] for result in market['results']]) / total_results for market in market_data]

# Pasta grafiği oluşturma
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')

plt.show()