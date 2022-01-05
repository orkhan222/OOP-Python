# isimler = ['Ada','Yigit','Hasan','Beril']
# yasler = [1998,2000,1998,1987]

# # 1-ci 'Cenk' ismini listenin sonuna ekleyiniz.
# isimler.append('Cenk')

# # 2-ci 'Sena' degerini listenin basina ekleyiniz.
# isimler.insert(0,'Sena')
# isimler.insert(-1,'Sena')
# isimler.insert(len(isimler),'Sena')

# # 3-cu 'Yigit' ismini listeden siliniz.
# isimler.remove('Yigit')
# isimler.pop()
# isimler.pop(0)

# # 4-cu 'Yigit' isminin index nedeir? 
# index = isimler.index('Yigit')
# print(index)

# # 5-ci  'Beril' listenin bir elemani nedir?
# sonuc = 'Beril' in isimler
# print(sonuc)

# # 6-ci Liste elemanlari ters cevirin.
# isimler.reverse()
# yasler.reverse()

# # 7-ci Liste elemanlarini alfabetik olarak siralayiniz.
# isimler.sort()

# # 8-ci yasler listenin rakamsal buyukluge gore siralayiniz.
# yasler.sort()

# # 9-cu str = 'IPhone X, IPhone XR' karakter dizisini listeye ceviriniz.
# a = 'IPhone X, IPhone XR'
# sonuc = a.split(',')
# print(sonuc)

# # 10-cu yaslar dizisinin en buyuk ve en kucuk elemani nedir?
# print(max(yasler))
# print(min(yasler))

# # 11-ci yaslar dizisinin kac tane 1998 deyeri vardir?
# print(yasler.count(1998))

# # 12-ci yaslar dizisinin tum elemanlarini siliniz.
# yasler.clear()

# # 13-cu Kullancidan alacaginiz 3 tane marka bilgisini bir listede saklayiniz.

# markalar = []

# marka =input('marka: ')
# markalar.append(marka)

# marka =input('marka: ')
# markalar.append(marka)

# marka =input('marka: ')
# markalar.append(marka)

# print(markalar)




# print(isimler)
# print(yasler)

adlar = ['orkhan','anar','salman','aydin','arzu','anar']
count = 0
index = 0

while len(adlar) > index:
    if adlar[index][0] =='a' and adlar[index][-1] == 'r':
        count +=1
    index+=1
    
print(count)