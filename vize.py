'''
???
'''
from datetime import datetime

y = datetime.strptime(input("Sınav tarihini ve saatini giriniz (YYYY-AA-GG SS:DD): "), "%Y-%m-%d %H:%M")
z = datetime.now()

x = y - z
print(x.days, "gün", x.seconds // 3600, "saat", (x.seconds // 60) % 60, "dakika", x.seconds % 60, "saniye kaldı")