name = 'asrakadabra'

for i in range(len(name)):
    if name[i] == 'a':
        name = name[i:] + '+' + name[i:]
        
print(name)