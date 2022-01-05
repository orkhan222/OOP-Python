website = 'https://www.github.com/orkhan222'
kursAdi = 'Python Dersleri: Sifirdan ileri seviye Python Programlama.'

# 1-ci 'kursAdi' karater dizisiinde kac karater bulunmaktadir?
sonuc = len(kursAdi)
sonuc = len(website)


# 2-ci 'website' icinden www karakerti alin?
sonuc = website[8:11]

# 3-ci 'website' icinde com karakerti alin?
sonuc = website[19:22]

# 4-cu 'kursAdi' icinde ilk 15 ve son 15 karakterini alin?
sonuc = kursAdi[:15]
sonuc = kursAdi[-15:]

# 5-ci 'kursAdi' ifadesindeki karekterleri tersten yazdirin?
sonuc = kursAdi[::-1]

# 6-ci 'Hello World' ifadesindeki w harifini 'W' ile deyisdirin?

a = 'Hello world'
a = a[0:6] + 'W' + a[-4:0]
print(a)

# 7-ci 'abc' ifadesini yan yana 3 defe yazdirin?
sonuc = 'abc' *3


name, surname, age, job = 'Orkhan', 'Mustafayev' , 20 , 'student'
# 8-ci Yukarida verilen degiskenler ile ekrana asagidaki ifadeyi yazdirin.
#           'Benim adim Orkhan Mustafayev, Yasim 20 ve meslegim student'

sonuc = 'Benim adim {0} {1}, Yasim {2} ve meslegim {3}'.format(name,surname,age,job)
sonuc = f"Benim adim {name} {surname}, Yasim {age} ve meslegim {job}"


print(sonuc)