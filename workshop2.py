sayi = int(input("Hangi sayının faktöriyeli hesaplansın ="))
#KENDI YAPTIGIM---------
# hesapla=1
# if sayi>=0:
#     for sayi in range(sayi):
#         hesapla= hesapla*(sayi+1)
#         print("Faktöriyel sonucu =" +str(hesapla))
#     print("işlem tamamlandı")
# else:
#     print("negatif sayıların faktöriyeli hesaplanamaz")
#     print("işlem tamamlanamadı")


#HOCANIN YAPTIGI----------
faktoriyel=1
if sayi<0:
    print("negatif sayıların faktöriyeli hesaplanamaz")
elif sayi==0:
    print("Faktöriyel sonucu = 1")
else:
    for i in range(1,sayi+1):
        faktoriyel= faktoriyel*i
    print("Faktöriyel sonucu = ",faktoriyel)