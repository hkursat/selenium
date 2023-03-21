# Classlar
# moduls
# paket yönetimi

# import day2 # moduls import edilmesi


class Human:
   # built in
    def __init__(self, ad) -> None:
        self.ad = ad
        # self.soyad = soyad

    def __str__(self) -> str:
        return "Değer string"

    def talk(self, sentence):
        print(f"Talking {self.ad} {sentence}")

    def walk(self):
        print(f"Walking {self.ad}")


# instance- Örnek
# human1 = Human("Mirza")

# human1.talk("Merhaba")



