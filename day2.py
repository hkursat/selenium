# Tip dönüşümleri
# faiz = 1.59
# vade = 36
# krediAdi = "ihtiyaç kredisi"

# print(type(faiz))
# print(type(vade))
# print(type(krediAdi))

# print(int(vade)+12)
# vade = vade+12

# vade = int(input("Vade giriniz :"))
# print(type(vade))


# String İnterpolation
# hesaplanan vade


# print("Vade {vade}".format(vade=vade))
# print(f"Vade :{vade}")  # f string


# Listeler

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "konut Kredisi"]

print(type(krediler))

print(krediler[0])

print(len(krediler))


# diziye eleman ekleme
krediler.append("Bireysel kredi")
print(krediler)

krediler.append("x kredisi")
print(krediler)
krediler.pop(0)  # son indexi siler
print(krediler)
krediler.remove("x kredisi")
krediler.extend(["1", "2", "3", "1"])
krediler.sort()
print(krediler.count("1"))
print(krediler)


# Döngüler

for i in range(1, 10):
    if i % 2 == 0:
        print(f"Sayı çift {i}")
    else:
        print(f"sayi tek {i}")


# for kredi in krediler:
#     print(kredi)


# while
# a = 0
# while a < 10:
#     a += 1
#     if a == 5:
#         break
#     print(a)
krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "konut Kredisi"]
i=0
while i < len(krediler):
    print(krediler[i])
    i+=1


# Fonksiyonlar
