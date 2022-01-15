# s = {2,3}
# print(s*3)-----------eror

# c= 4//5*5
# for i in range(3):
#     for j in range(i):
#         if i == j:
#             c = c+1
        
# print(c)---------------------0

# l = [1,2,3,4]
# l.remove(1)
# print(l) ----------------[2,3,4]

# fruits = ['a','b','c']
# fruits.clear(1)
# print(fruits) --------------eror

# aList = [5,10,15,25]
# print(aList[::-2]) ---------------[25, 10]

# L = [2,3,4,5]
# L = list(filter(lambda x:x%2, L))
# print(L)----------[3, 5]

# n1, n2 =15, 20
# if (n1> n2):
#     max = n1
# else:
#     max = n2
# while(True):
#     if(max % n1 == 0 and max % n2 ==  0):
#         break;
#     max = max + 1
# print(max)------------------60


# def x(val):
#     val[0] = 45
# val = [2,4,6]
# x(val)
# print(val)----------------[45, 4, 6]

# print('python dot hub'.title())--------------------Python Dot Hub

# a=1
# b=0
# print(any(a,b))---------------eror


# print('{1} loves {2}'.format('everyone','python.hub'))----------------eror



# mylist = (1,2,3)
# if type(mylist) is list:
#     print(1==1)
# print(mylist)----------------------------------(1, 2, 3)

# c=0
# for i in range(3):
#     for j in range(3):
#         if i !=j:
#             c = c + 1
#             c = c - 3 + 1
# print(c)------------------------------------(-6)




# l1 = [4,3,2,1]
# my_one = l1.pop(1)
# print(my_one)--------------------------------------3


# a= 16//5
# b = 16//5
# print(a+b)----------------------6

# x = [1,2,3]
# y = [2,3,4]
# print(len(set(x)) + len(set(y)))---------------------------------------6

# d= {0:'a',1:'b',2:'c'}
# for i in d.keys:
#     print(i)
# print(d)---------------------------------------------eror


# a = ('p' * 2) *3
# b = ('p' * 3) *2
# print(a==b)-----------------------------------True

# def unpack(p,q,r,s):
#     print(p+s)
# a = [2,3,4,5]
# unpack(*a)----------------------------------7



# l=[7,8,9,10]
# a=0
# for i in l:
#     if a<i:
#         a=i
# print(a)


# def fun():
#     x = 100
#     print(x)

# x=+1
# fun()

b = 30
def fun(a,b=b):
    return a+b
print(fun(1))