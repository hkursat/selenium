import time


class Sicil():
    def __init__(self, name, surname, id, birthday, isaktif):
        self.name = name
        self.surname = surname
        self.id = id
        self.birthday = birthday
        self.isaktif = isaktif


class Kitap(Sicil):
    def __init__(self, id, kitapadi, sayfa, basimyili, yayinevi):
        self.id = id
        self.kitapadi = kitapadi
        self.sayfa = sayfa
        self.basimyili = basimyili
        self.yayinevi = yayinevi
    

        

    def kitapekle(self, id, kitapadi, yayinevi):
        pass

    def kitapsil(self):
        pass

    def kitapadiguncelle(self):
        pass


class Uye(Sicil):
    pass


class User(Sicil):
    pass


class Yazar(Sicil):
    pass


class Yayinevi(Sicil):
    pass


