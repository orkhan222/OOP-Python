# BankAccount isminde bir sinif tanimlayiniz.
# Urentilen her bir nesne owner isminde  bir ozellige sahip olmalidir. BankAccount('Orkhan Mustafayev')
# Urentilen her bir nesne balance isminde bir ozellige sahip olup baslangicta 0.0 degerinde olmalidir.
# Urentilen her bir nesne icin deposit metodu olusturun ve disarindan yatirilcak miktir bilgisini  alip balance
# uzerine ekleyin  ve balance miktarini geriye dondurun.
# Urentilen her bir nesne icin withdraw metodu olusturun ve disarindan cekilecek miktar bilgisini alip balance degerinde cikarip geriye dondurun

# hesap = BankAccount('Orkhan Mustafayev)
# hesap.owner = Orkhan Mustafayev
# hesap.balance = 0.0
# hesap.deposit(1000) = 1000.0
# hesap.withdraw(500) = 500.0

class BankAccount:
    def __init__(self,name):
        self.owner = name
        self.balance = 0.0
        
    def getBalance(self):
        return self.balance
        
    def deposit(self,amount):
        self.balance += amount
        return self.balance

    def withdraw(self,amount):
        self.balance -= amount
        return self.balance
    
hesap = BankAccount('Orkhan Mustafayev')


print(hesap.getBalance())
hesap.deposit(1000)
print(hesap.getBalance())
hesap.withdraw(500)
print(hesap.getBalance())