import random

soru = int(raw_input("kac karakterli parola istiyorsun\n"))
Bharf = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
Kharf = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
Sayi = ["0","1","2","3","4","5","6","7","8","9"]
OzelKarakter = [".",",",":",";","+","-","%","&","/","(",")","=","?","-"]

sifre = ""

while soru >= 0:
    if len(sifre)>=soru:
        break
    else:
        karekterSecenSayi = random.randint(1,25)
        sifre += Bharf[karekterSecenSayi]

    if len(sifre)>=soru:
        break
    else:
        karekterSecenSayi = random.randint(1,25)
        sifre += Kharf[karekterSecenSayi]

    if len(sifre)>=soru:
        break
    else:
        karekterSecenSayi = random.randint(1,9)
        sifre += Sayi[karekterSecenSayi]
    if len(sifre)>=soru:
        break
    else:
        karekterSecenSayi = random.randint(1,13)
        sifre += OzelKarakter[karekterSecenSayi]





print "sifreniz:", sifre
