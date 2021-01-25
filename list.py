urunler=["Laptop","Mouse","Keyboard"]
print(urunler)
print(type(urunler))
urunler.append("Phone")
print(urunler)

ogrenciler1 =["Melike","Kadriye","Ceylan"]
ogrenciler2 =["Ali","Veli","Ahmet"]
ogrenciler1=ogrenciler2
ogrenciler2[0]="Melek"
print(ogrenciler1)
print(ogrenciler2)


sayi1=10
sayi2=20
sayi1=sayi2
sayi2=30
print(sayi1)
print(sayi2)


#list --> referans tip
#int --> değer tip


isim="Melike" #string ifadelerde aslında listelerdir
print(isim[0])