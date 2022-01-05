# User
# Moderator

class User:
    active_users = 0
    
    @classmethod
    def display_active_users(cls):
        return f'su anda aktif {cls.active_users} user var.'
    
    
    def __init__(self,firstname,lastname) :
        self.firstname = firstname
        self.lastname = lastname
        User.active_users +=1
        
    def fullname(self):
        return f'{self.firstname} -{self.lastname}'
        
class Moderator(User):
    active_modertors = 0
    
    @classmethod
    def display_active_users(cls):
        return f'su anda aktif {cls.active_modertors} Moderator var.'
    
    def __init__(self,firstname,lastname,community):
        super().__init__(firstname,lastname)
        self.community = community
        Moderator.active_modertors +=1
        
    def remove_post(self):
        return f'{self.fullname()} {self.community} grubundan bir post sildi.'
        
    def update_post(self):
        return f'{self.fullname()} {self.community} grubundan bir post guncelledi.'
        
print(Moderator.display_active_users()) 
print(User.display_active_users())   


u1 = User('Ali','Korkmaz')
m1 = Moderator('Yagmur','Korkmaz','yazilim')


print(m1.remove_post())
print(m1.update_post())
print(Moderator.display_active_users())
print(User.display_active_users()) 

# print(u1.fullname())
# print(m1.fullname())




        
# print(isinstance(u1, User))
# print(isinstance(u1, Moderator))
# print(isinstance(m1, Moderator))
        