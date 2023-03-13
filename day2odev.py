from datetime import time
import time
"""
Öğrenci Kayıt sistemi

"""
deger = 0
ogrenciListesi = []
islem = ""
adsoyad = ""

#Öğrenci ekleyen fonksiyon
def ogrenciekle(adsoyad):
    print("Öğrenci listeye ekleniyor ....")
    time.sleep(1)
    ogrenciListesi.append(adsoyad)
    print("Öğrenci sisteme başarı ile eklenmiştir....")


#Öğrenci bilgilerini silen fonksiyon.
def ogrencisil():
    adsoyad = input("Silinecek öğrenci bilgilerini giriniz :")
   
    if adsoyad in ogrenciListesi:
        print(f"{adsoyad} isimli ö1ğrenci bilgileri siliniyor...")
        time.sleep(1)        
        ogrenciListesi.remove(adsoyad)
        print("Öğrenci Silindi.")
    elif len(ogrenciListesi)==0:
        print("Lİstede hiç öğrenci yok")
    else:
        print("Belirttiğiniz isimde öğrenci bulunmamadı.")


#Listedeki öğrencileri bu fonksiyon yazdırır.
def ogrenciyazdir():
    print("Öğrenci Listesi yazdırılıyor...")
    time.sleep(1)
    for ogrenci in ogrenciListesi:
        print(ogrenci)
    if len(ogrenciListesi) == 0:
        print("Listede öğrenci yoktur")
    else:
        print(f"Listede toplam {len(ogrenciListesi)} öğrenci olmuştur...")


def exit(islem):
    if islem == "x" or islem == "X":
        print("Çıkış yapılıyor....")
        time.sleep(1)
        print("Çıkış yapıldı")


while True:
    #Menü gösterimi burada.
    print("""                
    *********** Öğrenci Kayıt Sistemi *************
    Lütfen Yapmak istediğiniz işlemi seçiniz. 
    1- Öğrenci Ekle
    2- Öğrenci Yazdır
    3- Öğrenci Sil
    4- Çıkış   
    *********** Öğrenci Kayıt Sistemi *************
    """)
    
    #İşlem seçimi buradan yapılıyor.
    islem = input("İşlem Seçiniz : ")
    if islem == "1":
        adsoyad = input("İsim giriniz :").lower()
        ogrenciekle(adsoyad)
    elif islem == "2":
        ogrenciyazdir()
    elif islem == "3":
        ogrencisil()
    elif islem == "4":
        print("Çıkış yapılıyor...")
        time.sleep(1)
        print("Çıkış yapılmıştır...")
        break
