# 1-ci Girilen 2 sayindan hangisi buyuktur?
sayi1 = int(input('sayi 1: '))
sayi2 = int(input('sayi 2: '))
sonuc = (sayi1 > sayi2)
print(f"{sayi1} {sayi2} den boyukdur: {sonuc}")

# 2-ci Girilen bir sayinin tek mi cift mi oldugunu yazdirin.
sayi = int(input('sayi: '))
sonuc = (sayi % 2 == 0)
print(sonuc)

# 3-cu Girilen bir sayinin negatif pozitif durumunu yazdirin.
sayi = int(input('sayi: '))
sonuc = (sayi>0)
print(sonuc)

# 4-cu Kullanicidan 2 vize (%60) ve final (%40) notunu alip ortalama hesaplayiniz.
    # Eger ortalama 50 ve ustundeyse gecti degilse kaldi yazdirin.
vize1 = float(input('vize1: '))
vize2 = float(input('vize2: '))
final = float(input('final: '))

ortalama = (((vize1+vize2) / 2) * 0.6) + (final * 0.4)
print(ortalama)
    
# 5-ci Parola ve email bilgisini isteyip dogrulugunu kontrol ediniz.
    # (email:orxanmustafayev072@gmail.com parol:12345)
_email = 'orxanmustafayev072@gmail.com' 
_password = '12345'

email = input('email: ')
password = input('password: ')

isEmail = (email.lower().strip() == _email)
isPassword = (password.lower().strip() ==_password)

print(f'email dogrulugu: {isEmail} ve parola dogrulugu : {isPassword}')
    
    
