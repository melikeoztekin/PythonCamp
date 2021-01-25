class Matematik:
    def __init__(self, sayi1,sayi2): #constructor-yapıcı
        self.s1=sayi1
        self.s2=sayi2
        print("Matematik başladı (referansı oluştu)")

    def topla(self):
        return self.s1+self.s2

    def cikar(self):
        return self.s1-self.s2
   
    def bol(self):
        return self.s1/self.s2

    def carp(self):
        return self.s1*self.s2

matematik = Matematik(8,2)
sonuc=matematik.topla()
print("Sonuc = "+str(sonuc))
sonuc2=matematik.cikar()
print("Sonuc = "+str(sonuc2))
sonuc3=matematik.bol()
print("Sonuc = "+str(sonuc3))
sonuc4=matematik.carp()
print("Sonuc = "+str(sonuc4))

#inheritance
class Istatistik(Matematik):
    def __init__(self,sayi1,sayi2):
        super().__init__(sayi1,sayi2)
    def varyansHesapla(self):
        return self.s1 * self.s2
    

istatistik=Istatistik(3,8)
sonuc5=istatistik.varyansHesapla()
print("Varyans Hesabı yaptık varsay = ",sonuc5)