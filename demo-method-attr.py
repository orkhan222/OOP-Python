class Pet:
    cinsler = ['kedi','kopek','kus']
    
    def __init__(self, isim,cins):
        if cins not in Pet.cinsler:
            raise ValueError(f'{cins} bir evcil heyvan deyildir.')
        self.isim = isim
        self.cins = cins
    
    def set_cins(self,cins):
        cinsler = ['kedi','kopek','kus']
        if cins not in Pet.cinsler:
            raise ValueError(f'{cins} bir evcil heyvan deyildir.')
        self.cins = cins
        
        
boncuk = Pet('Boncuk','kedi')
pasa = Pet('Pasa','kopek')
mavis = Pet('Mavis','kus')


mavis.set_cins('aslan')