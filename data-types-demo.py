# Daire Alani : pi r kvaritarti
# Daire Cevre : 2 pi r
#  Yari capi verilen bir dairenin alan ve ceversini hesaplayiniz. (pi: 3.14)


r = float(input('radius: '))

pi = 3.14

dairelani= pi * (r **2)
Dairecevre = 2 * pi * r
print(Dairecevre)


# Bir aracin km cinsinden gittigi yol bilgisini mil olarak yazdiriniz.
# mil = km / 1.6093444
mesafeKm = input()
mesafeMil = float(mesafeKm) / 1.6093444

result = str(mesafeKm) + ' km =  ' + str(mesafeMil) + ' mil'
print(result)