import random
def tas_kagit_makas_ugurhan_dasdemir():
    print("TAŞ KAĞIT MAKAS OYUNU")
    print("---------------------")
    print("Kurallar: ")
    print("1-) Taş, Kağıt, Makas durumlarından birini seçiniz.")
    print("2-) Taş makası yener")
    print("3-) Makas kağıtı yener")
    print("4-) Kağıt taşı yener")
    print("5-) 1 Oyun 3 turdan oluşur. 3 Turdan 2'sini kazanan oyunu kazanır")
    print("Çıkmak için 0 seciniz\n")

    oyuncu_kazanma = 0
    pc_kazanma = 0
    tur_sayisi = 0


    while True:
        while tur_sayisi<3:

            print("Lütfen birini seçiniz.")
            secim = int(input(print("1-)Makas \n2-)Taş \n3-)Kağıt")))
            if(secim < 0 or secim >3):
                print("Lütfen 1 ve 3 arasında bir değer seciniz")
                continue



            if secim == 1:
                print("Oyuncu makas seçti\n")
            elif secim == 2:
                print("Oyuncu taş seçti\n")
            elif secim == 0:
                break
            else:
                print("Oyuncu kağıt seçti\n")


            pc_secim = random.randint(1, 3)
            if pc_secim == 1:
                print("Bilgisayar makas seçti\n")
            elif pc_secim == 2:
                print("Bilgisayar taş seçti\n")
            else:
                print("Bilgisayar kağıt seçti\n")

            if(pc_secim == secim):
                print("Berabere\n")
            elif(secim==1 and pc_secim == 3 ) or (secim==2 and pc_secim == 1) or (secim==3 and pc_secim == 2):
                print("Kazandınız\n")
                oyuncu_kazanma += 1
            else:
                print("Bilgisayar Kazandı\n")
                pc_kazanma += 1

            tur_sayisi += 1

            if(tur_sayisi == 3):
                devam_secim = int(input(print("Başka bir oyun oynamak ister misiniz ?\n1-)Evet\n2-)Hayır")))
                if (devam_secim==1):
                    tur_sayisi=0

                elif(devam_secim==2):
                    print("Oyun sonlandırılıyor...")
                    break


                pc_devam_secim = random.randint(1, 2)
                if (pc_devam_secim == 1):
                    tur_sayisi = 0
                    print("Bilgisayarda devam etmek istiyor")
                elif (pc_devam_secim == 2):
                    print("Bilgisayar devam etmek istemiyor \nOyun sonlandırılıyor...")
                    break


        if(oyuncu_kazanma > pc_kazanma ):
            print("OYUNCU KAZANDI")
        elif(pc_kazanma > oyuncu_kazanma):
            print("BİLGİSAYAR KAZANDI")
        elif(oyuncu_kazanma == pc_kazanma):
            print("BERABERE")

        break


tas_kagit_makas_ugurhan_dasdemir()