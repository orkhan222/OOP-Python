# 1-ci 3 urun bilgisini (id,ad,soyad) kullanicidan aldiginiz bilgilerle dictionary icinde saklayiniz.
urunler = {
    '1': {'ad': 'Orkhan', 'soyad': 'Mustafayev'}, 
    '2': {'ad': 'Salman', 'soyad': 'Mustafayev'}, 
    '3': {'ad': 'Orxan', 'soyad': 'Mustafayev'}
}

id = input('id: ')
ad = input('ad: ')
soyad = input('soyad: ')

urunler[id] ={
    'ad':ad,
    'soyad':soyad
}

id = input('id: ')
ad = input('ad: ')
soyad = input('soyad: ')

urunler[id] ={
    'ad':ad,
    'soyad':soyad
}


id = input('id: ')
ad = input('ad: ')
soyad = input('soyad: ')

urunler[id] ={
    'ad':ad,
    'soyad':soyad
}



# 2-ci Uruun id bilgisini kullanicidan alip ilgili urun bilgisini gosterin.
id = input('aramak istediginiz urun id: ')
urun = urunler[id]
print(urun)


print(urunler)
