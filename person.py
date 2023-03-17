class Person:
    def __init__(self, name, lastname) -> None:
        self.name = name
        self.lastname = lastname


class Memur(Person):
    def __init__(self, name, lastname) -> None:
        self.name = name
        self.lastname = lastname

    def add(self, name, lastname):
        print("Ad soyad eklendi{name}{lastname}".format(
            name=name, lastname=lastname))


class Isci(Person):
    def __init__(self, name, lastname) -> None:
        super().__init__(name, lastname)


class Binted(Person):
    def __init__(self, name, lastname) -> None:
        super().__init__(name, lastname)


memur = Memur("deneme", "deneme")


ad = input("Adı gir :")
soyad = input("SOyad :")

memur.add(ad, soyad)

# musteri = Person("ahmet", "sert")
# print(musteri.name)
# print(musteri.lastname)
