# 1-ci Girilen bir sayinin 50-100 arasinda olub olmadigini kontrol ediniz.
sayi = int(input('sayi: '))
sonuc = (sayi>50) and (sayi<=100)
print(sonuc)

# 2-ci Girilen bir sayinin pozitif tek sayi olub olmadigini kontrol ediniz.
sayi = int(input('sayi: '))
sonuc = (sayi>0) and (sayi % 2 ==1)
print(sonuc)

# 3-cu Username ve parola bilgileri ile giris kontrolu yapiniz.
_username = 'OrkhanMustafayev'
_password = '12345'

girilenUsername = input('username: ')
girilenPassword = input('parola: ')

sonuc = (girilenUsername==_username) and (girilenPassword == _password)
print(sonuc)

# 4-cu Girilen 3 sayiyi boyukluk olarak karsilastiriniz.
x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))

sonuc = (x>y) and (x>z)
print('x en boyuk sayi: ',sonuc)

sonuc = (y>x) and (y>z)
print('y en boyuk sayi: ',sonuc)

sonuc = (z>x) and (z>y)
print('z en boyuk sayi: ',sonuc)

# 5-ci Kullanicidan 2 vize (%60) ve final (%40) notunu alib ortalama hesablayiniz.
    # Eger ortalama 50 ve ustundeyse gecti degilse kaldi yazdirin.
    # a-) Ortamalama 50 olsa bile final notu en az 50 olmalidir.
    # b-) Finalden 70 alindiginda ortalamanin onemi olmasin.
    
vize1 = float(input('vize1: '))
vize2 = float(input('vize2: '))
final = float(input('final: '))

ortalama = (((vize1 + vize2) / 2) * 0.4) +(final * 0.6)

sonuc = (ortalama >= 50) and (final>=50)

sonuc = (ortalama >= 50) or (final>=70)

print(f'oyrencini not ortalamasi: {ortalama} ve gecme durumu: {sonuc}')
    
# 6-ci Kisinin ad, kilo ve boy bilgilerini alib kilo index hesablayaniz.
    # Formul: (Kilo / boy uzunlugunun karesi)
    # Asagidaki tabloya gore kisi hansi qrupa girmektedir.
    # 0-18.4 - zayif
    # 18.5-24.9 - normal
    # 25.0-29.9 - Fazla Kilolu
    # 30.0-34.9 - sisman
    
    
ad = input('adiniz: ')
kg = float(input('kilonuz: '))
hg = float(input('boyunuz: '))

kiloIndex = kg / (hg ** 2)

zaif = (kiloIndex >=0 ) and (kiloIndex<=18.4)
normal = (kiloIndex >=18.4 ) and (kiloIndex<=24.9)
kilolu = (kiloIndex >=25 ) and (kiloIndex<=29.9)
obez = (kiloIndex >=30 ) and (kiloIndex<=34.9)


print(f'{ad} kilo indexnin: {kiloIndex} ve kilo degerlendirmen zaif : {zaif}')
print(f'{ad} kilo indexnin: {kiloIndex} ve kilo degerlendirmen zaif : {normal}')
print(f'{ad} kilo indexnin: {kiloIndex} ve kilo degerlendirmen zaif : {kilolu}')
print(f'{ad} kilo indexnin: {kiloIndex} ve kilo degerlendirmen zaif : {obez}')