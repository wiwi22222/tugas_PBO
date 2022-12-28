
# Nama   : Wiwi Lestiani
# Kelas  : INF G

import math 
class BangunRuang :
    def luas(self):
        pass

    def volume(self):
        pass

    def printLuas(self):
        print(self.luas())

    def printVolume(self):
        print(self.volume())

    
class Balok(BangunRuang):
    def __init__(self):
        self.panjang1 = 0
        self.lebar1 = 0
        self.tinggi1 = 0

    def luas(self):
        luas = 2 * (self.panjang1 * self.lebar1 + self.lebar1 * self.tinggi1 + self.panjang1 * self.tinggi1)
        return luas

    def volume(self):
        volume = self.panjang1 * self.lebar1 * self.tinggi1
        return volume

class Tabung(BangunRuang) :
    def __init__(self):
        self.jari_jari = 0
        self.tinggi = 0

    def luas(self):
        luas = 2 * math.pi * self.jari-jari * (self.jarijari + self.tinggi1)
        return round(luas,2)

    def volume(self):
        v = math.pi * (self.jari-jari ** 2) * self.tinggi1
        return round(v,2)

class Kubus(BangunRuang):
    def __init__(self):
        self.sisi = 0

    def luas(self):
        luas = 6 * (self.sisi**2)
        return luas

def ulang():
    print("Ingin menghitung lagi? (y/n)")
    inp = input("=>").lower()
    return True if inp == "y" else False

#panggil class

kubus = Kubus()
balok = Balok()
tabung = Tabung()

while True:
    print("""\nPilih Bangun Ruang
1. Balok
2. Tabung
3. Kubus
4. Berhenti""")
    pilihan = input("=>")

    if pilihan == "1":
        while True :
            print("""\n1. Luas
                       2. Volume
                       3. Keluar""")
            pilihan1 = input("->")

            if pilihan1 == "1":
                while True :
                    balok.panjang1 = float(input("Masukkaan Panjang :"))
                    balok.lebar1 = float(input("Masukkaan lebar :"))
                    balok.tinggi1 = float(input("Masukkaan tinggi :"))
                    print("luas dari balok adalah :")
                    balok.printLuas()
                    

                    if ulang() != True:
                        break
            elif pilihan1 == "2":
                while True :
                    balok.panjang1 = float(input("Masukkan panjang :"))
                    balok.lebar1 = float(input("Masukkan lebar :"))
                    balok.tinggi1 = float(input("Masukkan tinggi :"))
                    print("Luas dari volume adalah :")
                    balok.printVolume()
                   
                    if ulang() != True:
                        break
            elif pilihan1 == "3":
                break
            else :
                print("Masukkan pilihan yang benar!")

    if pilihan == "2":
        while True :
            print("""\n1. Luas
                       2. Volume
                       3. Keluar""")
            pilihan1 = input("=>")

            if pilihan1 == "1":
                while True :
                    balok.jari_jari = float(input("Masukkan jarijari :"))
                    balok.tinggi1 = float(input("Masukkan tinggi :"))
                    print("luas dari luas adalah : ")
                    balok.printLuas()
                    
                    if ulang() != True :
                        break
            elif pilihan1 == "2":
                while True:
                    balok.panjang1 = float(input("Masukkan panjang :"))
                    balok.tinggi1 = float(input("Masukkan tinggi :"))
                    print("luas dari volume adalah :")
                    balok.printVolume()
                    if ulang() != True :
                        break
            elif pilihan1 == "3":
                break
            else:
                print("Masukkan pilihan yang benar!")
    
    if pilihan == 3:
        while True:
            print("""\n1. Luas
                       2. Volume
                       3. Keluar""")
            pilihan1 = input("=>")

            if pilihan1 == "1":
                while True :
                    kubus.sisi = float(input("Masukkan siis :"))
                    print("luas dari luas adalah :")
                    balok.printLuas()
                    
                    if ulang() != True :
                        break
            elif pilihan1 == "2":
                while True:
                    kubus.sisi = float(input("Masukkan sisi :"))
                    balok.printVolume()
                    if ulang() != True :
                        break
            elif pilihan1 == "3":
                break
            else:
                print("Masukkan pilihan yang benar!")
print("Program berhenti. Selamat tinggal. ")

