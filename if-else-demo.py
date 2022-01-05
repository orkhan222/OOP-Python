# Bir aracin yakit tipine gore (benzin, dizel) belitilen bir mesafede ne qeder yakit masrafi oldugunu
# hesaplayan uygulamayi yapiniz

benzinFiyat = 1.3
dizelFiyat = 0.8
toplamYakitUcreti = 0

ortalama = float(input('100 km deki ortalama yakit tuketimi: '))
gidilecekYol = float(input('gidilecek yol kac km: '))
yakit = input('yakit tipiniz nedir: ')

toplamYakitTuketimi = gidilecekYol * (ortalama / 100)



if (yakit =='benzin'):
    toplamYakitUcreti = benzinFiyat * toplamYakitTuketimi
elif (yakit == 'dizel'):
    toplamYakitUcreti = benzinFiyat * toplamYakitTuketimi
else:
    print('yanlis yakit tipi girdiniz')
    
if (toplamYakitUcreti !=0):
    print(toplamYakitUcreti)

print(toplamYakitUcreti)