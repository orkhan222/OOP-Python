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
    
    
    
    
# adlar = ['orkhan','eli','veli','salman','muxtar']
# index = 0
# yadda = ''
# while len(adlar) > index:
#     if index != len(adlar)-1:
#         yadda = adlar[index]
#         adlar[index] = adlar[index+1]
#         adlar[index+1] = yadda
#     index+=1
    
# print(adlar)
    
    
# name = 'abrakadabra'
# name2 = name
# index = 0

# while len(name) > index:
#     if name[index] =='a':
#         name2 = name2[:index] + "+" + name2[index+1:]
#     index +=1
    
# print(name2)


# nums = 23556
# test = True

# while nums > 0:
#     if (nums%10)%2 !=0:
#         test = False
#         break
#     nums//=10
    
# if test:
#     print('yes')
# else:
#     print('no')

num1 = int(input('num1: '))
num2 = 0    
while num1 > 0:
    num3 = int(input('reqem: '))
    num2 = num2*10+num3
    num1 -=1
    
print(num2 )
