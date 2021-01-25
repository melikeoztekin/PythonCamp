class Person:
    def __init__(self,name,lastName):
        self.name=name
        self.lastName=lastName



musteri1=Person("Ahmet","Kemal")
musteri2=Person("Veli","Kenmal")
musteri3=Person("Mehmet","Kenmal")

print(musteri1.name , musteri1.lastName)
print(musteri2.name , musteri2.lastName)
print(musteri3.name , musteri3.lastName)


class Istatistik(Matematik):
    def varyansHesapla(self):
        return self.s1 * self.s2