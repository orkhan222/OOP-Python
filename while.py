# num1 = int(input('Num1: '))
# # new = []
# num2 = 0

# while num1> 0:
#     num2 = num1%10
#     new.append(num2)
#     num1//=10
# print(max(new))

# while num1> 0:
#     num2 = num1%10
#     new.append(num2)
#     num1//=10
# print(new)


# while num1>0:
#     num2 = (num2*10) + (num1%10)
#     num1//=10
# print(num2)


# num1 = 12
# name = 'orkhan'
# liste = [1,'2',3,4,5,6,'orkhan',['orkhan']]
# index = 0

# while len(liste) > index:
#     print(liste[index])
#     index+=1
    
    
    
    
adlar = ['orkhan','eli','veli','salman','muxtar']
index = 0
yadda = ''
while len(adlar) > index:
    if index != len(adlar)-1:
        yadda = adlar[index]
        adlar[index] = adlar[index+1]
        adlar[index+1] = yadda
    index+=1
    
print(adlar)
    