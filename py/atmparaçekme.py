
class ATM:
    def __init__(self, hesap_bakiyesi):
        self.hesap_bakiyesi = hesap_bakiyesi
    
    def para_yatir(self, miktar):
        self.hesap_bakiyesi += miktar
        print("Yeni hesap bakiyeniz:", self.hesap_bakiyesi)
    
    def para_cek(self, miktar):
        if miktar > self.hesap_bakiyesi:
            print("Hesabinizda yeterli bakiye yok!")
        else:
            self.hesap_bakiyesi -= miktar
            print("Yeni hesap bakiyeniz:", self.hesap_bakiyesi)
    
    def bakiye_sorgula(self):
        print("Hesap bakiyeniz:", self.hesap_bakiyesi)

atm = ATM(1000)

while True:
    print("1-Para yatirma\n2-Para çekme\n3-Bakiye sorgulama\n4-Çikiş")
    secim = int(input("Seçiminiz: "))
    if secim == 1:
        miktar = float(input("Yatirmak istediğiniz miktar: "))
        atm.para_yatir(miktar)
    elif secim == 2:
        miktar = float(input("Çekmek istediğiniz miktar: "))
        atm.para_cek(miktar)
    elif secim == 3:
        atm.bakiye_sorgula()
    elif secim == 4:
        break
    else:
        print("Geçersiz seçim!")
