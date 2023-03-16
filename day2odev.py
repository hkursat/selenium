from datetime import time
import time
"""
Öğrenci Kayıt sistemi

"""
deger = 0
ogrenciListesi = []
islem = ""
adsoyad = ""
templist = []
devammi = ""

# Öğrenci ekleyen fonksiyon


def ogrenciekle(adsoyad):
    print("Öğrenci listeye ekleniyor ....")
    time.sleep(1)
    ogrenciListesi.append(adsoyad)
    print("Öğrenci sisteme başarı ile eklenmiştir....")


# Öğrenci bilgilerini silen fonksiyon.
def ogrencisil():
    if len(ogrenciListesi)<=0:
        time.sleep(1)
        print("Hiç öğrenci yok")
    else:
        adsoyad = input("Silinecek öğrenci bilgilerini giriniz :")
        if adsoyad in ogrenciListesi:
            print(f"{adsoyad} isimli ö1ğrenci bilgileri siliniyor...")
            time.sleep(1)
            ogrenciListesi.remove(adsoyad)
            print("Öğrenci Silindi.")
        elif len(ogrenciListesi) == 0:
            print("Lİstede hiç öğrenci yok")
        else:
            print("Belirttiğiniz isimde öğrenci bulunamadı.")


# Listedeki öğrencileri bu fonksiyon yazdırır.
def ogrenciyazdir():
    print("Öğrenci Listesi yazdırılıyor...")
    time.sleep(1)
    for ogrenci in ogrenciListesi:
        print(ogrenci)
    
    if len(ogrenciListesi) == 0:
        print("Listede öğrenci yoktur")
    else:
        print(f"Listede toplam {len(ogrenciListesi)} öğrenci olmuştur...")


def cokluekle():
    while True:
        adsoyad = input(" İsim giriniz :")
        templist.append(adsoyad)
        # for ogrenci in templist:
        #     ogrenciListesi.append(togrenci)
        print(f"Güncel liste {templist}")
        devammi = input("Devammı ? E/ H :")
        if devammi == "e":
            continue
        else:
            for ogrenci in templist:
                ogrenciListesi.append(ogrenci)
            break


def coklusil():
    while len(ogrenciListesi)!=0:
        print(ogrenciListesi)
        adsoyad = input("Silinecek isim yazınız :")
        templist.append(adsoyad)
        
        devammi = input("Devammı ? E/ H :")
        if devammi == "e":
            continue
        elif devammi=="h":
            for ogrenci in templist:
                if ogrenci in ogrenciListesi:
                    ogrenciListesi.remove(ogrenci)
                    print(f"{ogrenci} isimli 1ogrenci silindi")
                    if len(ogrenciListesi)==0:
                        print("listede öğprenci bilgisi kalmamıştır.")
                        break
                
       
                
        
                
                
        
                
                


def indexbul():
    while True:
        adsoyad=input("Numarasını öğreneceğiniz Öğenci adı giriniz : ")
        if adsoyad in ogrenciListesi:
            index=ogrenciListesi.index(adsoyad)
            index+=1
            print(f"Öğrenci numarası {index} tir.")
        else:
            print(f"{adsoyad} adında bir öğrenci bulunamadı !!!! ")
        break

while True:
    # Menü gösterimi burada.
    print("""                
    *********** Öğrenci Kayıt Sistemi *************
    Lütfen Yapmak istediğiniz işlemi seçiniz. 
    1- Öğrenci Ekle
    2- Öğrenci Yazdır
    3- Öğrenci Sil
    4- Çoklu Öğrenci Ekle
    5- Çoklu Öğrenci Sil 
    6- Öğrenci Numarası bul
    7- Çıkış
    *********** Öğrenci Kayıt Sistemi *************
    """)

    # İşlem seçimi buradan yapılıyor.
    islem = input("İşlem Seçiniz : ")
    if islem == "1":
        adsoyad = input("İsim giriniz :").lower()
        if adsoyad in ogrenciListesi:
            print("Bu öğrenci zaten eklenmiş")
        else:
            ogrenciekle(adsoyad)
    elif islem == "2":
        ogrenciyazdir()
    elif islem == "3":
        ogrencisil()
    elif islem == "4":
        cokluekle()

    elif islem == "5":
        coklusil()
    elif islem == "6":
        indexbul()
    elif islem == "7":
        print("Çıkış yapılıyor...")
        time.sleep(1)
        print("Çıkış yapılmıştır...")
        break
