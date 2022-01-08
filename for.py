# name = 'asrakadabra'

# for i in range(len(name)):
#     if name[i] == 'a':
#         name = name[i:] + '+' + name[i:]
        
# print(name)


num1 = int(input('num1: '))

new = []

while num1 > 0:
    new.append(input('reqem: '))
    num1 -=1

myMax = new[0]

for i in new:
    if i > myMax:
        myMax = i
        
        
print(myMax)