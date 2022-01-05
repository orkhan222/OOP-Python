# 1-ci 'Samsung S5, Samsung S6 ,Samsung S7,Samsung S8' elemanlarina shaip bir liste olusturunuz.
telefonlar = ['Samsung S5', 'Samsung S6' ,'Samsung S7','Samsung S8' ]
print(telefonlar)

# 2-ci Liste Kac elemanlidir?
sonuc = len(telefonlar)

# 3-cu List ilk ve son elemani nedir?
sonuc = telefonlar[0]
sonuc = telefonlar[-1]

# 4-cu 'Samsung S5' degerini 'Samsung S9' ile degistirin.
telefonlar[0] = 'Samsung S9'
sonuc = telefonlar

# 5-ci 'Samsung S6' listenin bir elamani midir?
if 'Samsung S6' in telefonlar:
    print('Samsung S6 liste icinde var.')

# 6-ci Listenin -3 indexdeki deger nedir?
sonuc = telefonlar[-3]

# 7-ci Listenin ilk 2 elemanini alin?
sonuc = telefonlar[:2]

# 8-ci Listenin son 2 elemanini yerine 'Samsung S9' ve 'Samsung S10' degerlerini ekliyin.
sonuc = telefonlar[2:] = ['Samsung S9','Samsung S10']
sonuc = telefonlar

# 9-cu Listenin uzerine 'IPhone X' ve 'IPhone XR' degerlerini ekliyin.
sonuc = telefonlar + ['IPhone X','IPhone XR']

# 10-cu Listenin son elamani silin.
del telefonlar[-1]
sonuc = telefonlar

# 11-ci Liste elamanlarini tersten yazdiriniz.
sonuc = telefonlar[::-1]

# 12-ci Liste elamalarini ekrana yazdiriniz.
for a in telefonlar:
    print(a)



print(sonuc)