website = 'http://www.github.com/orkhan222'
kursAdi = 'Python Dersleri: Sifirdan ileri seviye Python Programlama.'

# 1-ci 'Hello World' karakert dizisinin bas ve sondaki bosluk karakterlerini silin?
# sonuc = 'Hello World'.strip()
# sonuc = 'Hello World'.lstrip()
# sonuc = 'Hello World'.rstrip()
# sonuc = website.lstrip('/:pthw.')

# 2-ci 'www.github.com.com' icindeki github bilgisi haricindeki her karakteri silin?
# sonuc = 'www.github.com'.strip('w.moc')

# 3-ci 'kursAdi' karakter dizisinin tum krakterini kucuk harf yapin?
# sonuc = kursAdi.lower()

# 4-cu 'website' icinde kac tane a karakteri vardir? (count('a))
# sonuc = website.count('a')
# sonuc = website.count('www')
# sonuc = website.count('www',9,15)

# 5-ci 'website' "www" ile baslayip com ile bitiyor mu?
# sonuc = website.startswith('www')
# sonuc = website.startswith('com')

# 6-ci 'website' icinde '.com' ifadesi var mi?
# sonuc = website.find('.com')
# sonuc = website.find('.com',0,10)
# sonuc = website.find('Python')

# 7-ci 'kursAdi' icindeki karakterlerin hepsi alfabetik mi? (isalpha,isdigit)
# sonuc = 'abc1'.isalpha()
sonuc = '123'.isdigit()

# 8-ci 'Contents' ifadesini satirda 50 karakter icine yerlestirip sag ve soluna * ekleyiniz.
# sonuc = 'Contents'.center(50,'*')
# sonuc = 'Contents'.ljust(50,'*')
# sonuc = 'Contents'.rjust(50,'*')

# 9-ci 'kursAdi' karakter dizisinindeki tum bosluk krakterini '-' ile degistirin?
# sonuc = kursAdi.replace(' ','-')

# 10-cu 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak degistirin
# sonuc = 'Hello World'.replace('World','There')

# 11-ci 'kursAdi' karakter dizisini bosluk karakterlerinden ayirin.
# kursAdi = kursAdi.lower().replace(':','')
# sonuc = kursAdi.split()



print(sonuc)