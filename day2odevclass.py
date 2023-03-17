
import day2odev


class Banka():
    def krediBasvur(self):
        print("Kredi Başvur")

    def krediHesapla(self):
        print("Hesaplar Yapıldı")


banka = Banka()
banka.krediBasvur()


class Matematik:

    # constructor (Yapıcı) metot
    def __init__(self, sayi1, sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2

    def topla(self):
        
        return self.sayi1+self.sayi2

    def cikar(self):
        return self.sayi1-self.sayi2

    def bol(self):
        return self.sayi1/self.sayi2

    def carp(self):
        return self.sayi1*self.sayi2



matematik = Matematik(3, 5)
sonuc = matematik.topla()
