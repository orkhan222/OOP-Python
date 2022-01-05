# 1-ci Kullancidan isim, yas ve egitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz.
# Ehliyet alma kosulu en az 18 ve egitim durumu lise ya da unversite olmalidir.

isim = input('isim: ')
yas = int(input('yas: '))
egitim = input('egitim: ')

if (yas >= 18):
    if egitim == 'liste' or egitim == 'universite':
        print('ehliyet alabilirsiniz.')
    else:
        print(f'{isim} ehliyet alamazsiniz cunki egitim durumu yetersiz.')
        
else:
    print(f'{isim} ehliyet alamazsiniz cunki yasiniz tutmuyor.')

# 2-ci Bir oyrencinin 2 yazili bir sozlu notunu alip hesaplanan ortalamaya gore not araligina karsilik gelen not bilgisini yazdiriniz.
#   0-24  --------0
#   25-44 --------1
#   45-54 --------2
#   55-69 --------3
#   70-84 --------4
#   85-100 -------5

yazili1 = float(input('1.yazili: '))
yazili2 = float(input('2.yazili: '))
sozlu = float(input('sozlu: '))

ortalama = (yazili1 + yazili2 + sozlu) / 3

if (ortalama >=0 and ortalama < 25):
    print(f'ortalamaniz: {ortalama} ve notunuz: 0')
elif (ortalama >=25 and ortalama < 45):
    print(f'ortalamaniz: {ortalama} ve notunuz: 1')
elif (ortalama >=45 and ortalama < 55):
    print(f'ortalamaniz: {ortalama} ve notunuz: 2')
elif (ortalama >=55 and ortalama < 70):
    print(f'ortalamaniz: {ortalama} ve notunuz: 3')
elif (ortalama >=70 and ortalama < 86):
    print(f'ortalamaniz: {ortalama} ve notunuz: 4')
elif (ortalama >=86 and ortalama < 101):
    print(f'ortalamaniz: {ortalama} ve notunuz: 5')
else:
    print('yanlis bilgi girdiniz.')
    

# 3-cu Trafige cikis tarihi alinan bir aracin servis zamanini asagidaki bilgilere gore hesaplayiniz.
    # 1. Bakim --1. yil
    # 2. Bakim --2. yil
    # 3. Bakim --3. yil
#   ** Sure hesabini alinan gun, ay ,yil bilgisine gore gun bazli hesaplayiniz..
#   *** datatime modulunu kullanmaniz gerekiyor.
#   (simdi) - (2018/8/1) -- gun


import datetime

tarih = input('araciniz hangi tarihte traffige cikti (2019/7/11): ')
tarih = tarih.split('/')

simdi = datetime.datetime.now()
trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))

fark = simdi - trafigeCikis
gun = fark.days

print(gun)

if (gun<=365):
    print('1.servis bakimi.')
elif (gun<=365) and (gun<=365*2):
    print('2.servis bakimi.')
elif (gun<=365*2) and (gun<=365*3):
    print('3.servis bakimi.')
else:
    print('hatali bilgi girdiniz.')
    