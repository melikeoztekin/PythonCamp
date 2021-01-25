istenenKredi=100000
hesap=15000
minOlmasiGerekenHesap=10000
if hesap>=minOlmasiGerekenHesap:
    print(str(istenenKredi)+" TL kredi çekebilirsiniz")
    print("Ödemeler hesaplandı")
elif hesap>=9000 and hesap<=9500:
    print("müdüre sorulacak")
elif hesap>=9501 and hesap<=9999:
    print("müdür zorlanacak")
else:
    print("mevcut bakiyeniz krediye uygun değildir")
print("İşlem sonu")