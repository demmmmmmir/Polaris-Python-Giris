import random

x = random.randint(1, 100)
y = 0
while y != x:
    try:
        y = int(input("1'den 100'e kadar bir sayı tahmin ediniz: "))
        if y < x:
            print("yukarı çık")
        elif y > x:
            print("aşağı in")
    except:
        print("Lütfen geçerli bir sayı giriniz")

print("sayıyı buldunuz")
