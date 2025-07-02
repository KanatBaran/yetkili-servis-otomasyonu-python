###---------- BILGILER (START) ----------###
# Ogrenci Numarasi: 22100011013
# Ad: BARAN
# Soyad: KANAT
###---------- BILGILER (END) ----------###


def yetkili_servis_otomasyon():
    ###---------- HATA FONKSIYONU (START) ----------###
    def hata_mesaji_dosya():
        print("\n")
        print("***HATA***")
        print("Bu hata mesajinin almis olmanin birden fazla sebebi olabilir."
              "\nEndiselenme elimden geldigi kadar yardimci olacagim."
              "\nIlk basta en uste '-->' ok ile gosterilen hatanin ne oldugunu ogren."
              "\nHangi hatayi aldigini bulduysan alttaki talimatlari okuyabilirsin.")

        print("\n1) 'Kayit dosyasi bulunamadi.'"
              "\nBu hatanin sebebi girilen kayitlarin depolandigi dosya bulunamamasidir."
              "\nDosyanin yerinde olup olmadigini kontrol etmek icin programin"
              "\n\tbulundugu klasore bakmalisin."
              "\nBurada '22100011013.txt' adinda bir dosya olmasi gerekmektedir. "
              "\nDosyayi goremiyorsan manuel bir sekilde '22100011013.txt' adinda bir dosya olustur."
              "\nBundan sonra yuksek ihtimalle hataniz cozulecektir."
              "\nBu adimi yapmakta zorluk cekiyorsan bir Uzmandan yardim almalisin.")

        print("\n2) 'Kayit dosyasina islem yapilamiyor.'"
              "\nBu hatanin sebebi bilgilerin depolandigi dosya uzerinde islem yapilamamasidir."
              "\nOncelikle programin bulundugu klasore gitmelisin."
              "\nKlasorde '22100011013.txt' adinda bir dosya olacaktir. "
              "\nBu dosyayi silmeli ve tekrardan ayni isimle bir dosya olusturmalisin."
              "\n!!!UYARI!!!Dosyayi silersen programdaki kayitli bilgileride tamamini silersin."
              "\nBu adimi yapmakta zorluk cekiyorsan bir Uzmandan yardim almalisin.")

        print("\n3) 'Genel bir hata olustu.' "
              "\nBu hata mesaj genel bir mesajdir."
              "\nYani bircok hataya karsilik gelebilir."
              "\nBu hatayi aldiysan bir Uzmandan yardim almalisin.")

        exit()

    ###---------- HATA FONKSIYONU (END) ----------###



    ###---------- YARDIMCI FONKSIYONLAR (START) ----------###

    # -- kayitli araba (start) --#
    def kayit_sayi(dosya):
        uzunluk = ""
        try:
            with open(dosya, "r", encoding="utf-8") as f:
                araclar = f.readlines()
            uzunluk = len(araclar)
        except FileNotFoundError:
            print("--> kayit dosyasi bulunamadi.")
            hata_mesaji_dosya()
        except IOError:
            print("--> Kayit dosyasina islem yapilamiyor.")
            hata_mesaji_dosya()
        except:
            print("--> Genel bir hata olustu.")
            hata_mesaji_dosya()

        return uzunluk

    # -- kayitli araba (end) --#

    # -- kapanis (start) --#F
    def kapanis():
        print("\nOtomasyon kapatiliyor, Iyi gunler...")
        exit()

    # -- kapanis (end) --#

    # -- alt menu (start) --#
    def alt_menu():
        while True:
            alt_secenek = ""

            print("\n(1) Islemi Tekrarla (1)")
            print("(2) Ana Menuye Don  (2)")
            print("(3) Cikis Yap!      (3)")
            alt_sec = input("Secim Yapin:  ")

            try:
                alt_secenek = int(alt_sec)
                if alt_secenek > 3 or alt_secenek < 1:
                    print("\nLutfen gecerli bir secenek secin. (1,2 veya 3)")
                    continue
                break
            except ValueError:
                print("\nLutfen gecerli bir secenek secin. (1,2 veya 3)")
                continue
            except:
                print("\nLutfen gecerli bir secenek secin. (1,2 veya 3)")
                continue

        return alt_secenek

    # -- alt menu (end) --#

    # -- arabalari listeleme (start) --#
    def arac_listesi(dosya):
        try:
            with open(dosya, "r", encoding="utf-8") as f:
                Arabalar = f.readlines()
        except FileNotFoundError:
            print("--> Kayit dosyasi bulunamadi.")
            hata_mesaji_dosya()
        except IOError:
            print("--> Kayit dosyasina islem yapilamiyor.")
            hata_mesaji_dosya()
        except:
            print("--> Genel bir hata olustu.")
            hata_mesaji_dosya()
        return Arabalar

    # -- arabalari listeleme (end) --#

    ###---------- YARDIMCI FONKSIYONLAR (END) ----------###



    ###---------- ARAC LISTELEME (START) ----------###
    def araba_listele():
        Arabalar = arac_listesi("22100011013.txt")

        print("\n\t~~~~~~ARABA LISTESI~~~~~~")
        print("NO\tPLAKA\t\tTARIH\t\tSAHIP")

        syc = 1
        for araba in Arabalar:
            bilgiler = araba.split("|")
            araba_plaka = bilgiler[1]
            araba_sahip = bilgiler[2]
            araba_tarih = bilgiler[3]
            araba_islem = bilgiler[4]
            print(f"{syc}) | {araba_plaka} | {araba_tarih} | {araba_sahip}")

            for islemler in bilgiler[5:]:
                islem = islemler.split("/")
                islem_aciklama = islem[0]
                islem_gideri = islem[1]
                if islem[2][-1] == "\n":
                    islem_geliri = islem[2][:-1]
                else:
                    islem_geliri = islem[2]

                print(f"\t --> {islem_aciklama} Gider:{islem_gideri}TL, Gelir:{islem_geliri}TL")

            print("\n", end="")
            syc += 1

    ###---------- ARAC LISTELEME (END) ----------###



    ###---------- ARAC EKLEME (START) ----------###
    def araba_ekle():
        Arabalar = {}
        print("\n\t+++++ YENI ARABA EKLE +++++")

        while True:
            try:
                adet = int(input("Kaç adet araç eklemek istersiniz? "))
                break
            except ValueError:
                print("Lutfen gecerli bir sayi degeri girin.\n")
            except:
                print("Lutfen gecerli bir sayi degeri girin.\n")

        if adet <= 0:
            return False

        son_id = kayit_sayi("22100011013.txt")

        id = son_id + 1
        for i in range(adet):
            gecici_liste = []

            araba_plakasi = input(f"\n{i + 1}.Arabanin plaka numarasini girin: ")
            araba_sahibi = input(f'\t--> "{araba_plakasi}" Arabanin sahibini girin: ')
            araba_tarihi = input(f'\t--> "{araba_plakasi}" Arabanin islem tarihini girin: ')
            try:
                araba_islemi = int(input(f'\t--> "{araba_plakasi}" Arabaya uygulanan islem sayisini girin: '))
            except:
                araba_islemi = 1

            gecici_liste.append(araba_plakasi)
            gecici_liste.append(araba_sahibi)
            gecici_liste.append(araba_tarihi)
            gecici_liste.append(araba_islemi)

            for i in range(araba_islemi):

                islem_ismi = input(f"\n\t{i + 1}.Islemin aciklamasini girin: ")

                try:
                    islem_gideri = int(input(f"\t-->'{islem_ismi}' Giderini girin: "))
                except:
                    islem_gideri = "0"

                try:
                    islem_geliri = int(input(f"\t-->'{islem_ismi}' Gelirini girin: "))
                except:
                    islem_geliri = "0"

                eleman = islem_ismi + "/" + str(islem_gideri) + "/" + str(islem_geliri)
                gecici_liste.append(eleman)

            Arabalar[id] = gecici_liste
            id += 1

        # "kayit_olusturma" fonksiyonu kayıt dosyasina eklenecek satirin son halini duzenlemektedir.
        def kayit_olustuma(el):
            for anahtar, degerler in Arabalar.items():
                ekle = str(anahtar) + "|"

                for deger in degerler:
                    ekle += str(deger) + "|"
                el.append(ekle)

        el = []
        kayit_olustuma(el)

        try:
            with open("22100011013.txt", "a", encoding="utf-8") as dosya:
                for araba in el:
                    dosya.write(araba[:-1] + "\n")
        except FileNotFoundError:
            print("Kayit dosyasi bulunamadi.")
        except IOError:
            print("dosya islemede bir hata olustu.")
            print("Kayit dosyasini kontrol edin")
        except:
            print("Genel bir hata meydana geldi.")

    ###---------- ARAC EKLEME (END) ----------###



    ###---------- ARAC DUZENLE (START) ----------###
    def araba_duzenle():
        yeni_araba = ""
        Arabalar = arac_listesi("22100011013.txt")
        uzunluk = kayit_sayi("22100011013.txt")

        print("\n\t::::: ARABA DUZENLE :::::")

        while True:
            while True:
                try:
                    eleman = int(input("Duzenlemek istediginiz kayit hangisi? "))
                    break
                except ValueError:
                    print("Lutfen gecerli bir sayi degeri girin.\n")
                except:
                    print("Lutfen gecerli bir sayi degeri girin.\n")
            if 0 <= eleman <= uzunluk:
                break
            else:
                print("lutfen gecerli bir kayit girin.")

        if eleman == 0:
            return False

        # kayitli aracin id degeri aliyoruz
        def araba_id(eleman):
            indis = ""
            syc = 1
            for araba in Arabalar:
                if syc == eleman:
                    indis = Arabalar.index(araba)
                    break
                syc += 1
            return int(indis)

        index = araba_id(eleman)
        araba = Arabalar[index].split("|")

        id = araba[0]
        plaka = araba[1]
        sahip = araba[2]
        tarih = araba[3]
        islem = araba[4]

        guncel_plaka = input(f"Onceki plaka: {plaka} | Guncel plakayi girin: ")
        guncel_sahip = input(f"Onceki sahip: {sahip} | Guncel sahibi girin: ")
        guncel_tarih = input(f"Onceki tarih: {tarih} | Guncel tarihi girin: ")

        yeni_araba = id + "|" + guncel_plaka + "|" + guncel_sahip + "|" + guncel_tarih + "|" + islem + "|"

        islem_sayisi = 1
        print(f"\nIslemler ({islem})")
        while islem_sayisi <= int(islem):
            yeni_islem = ""
            islem_listesi = araba[4 + islem_sayisi].split("/")
            islem_ismi = islem_listesi[0]
            islem_gideri = islem_listesi[1]
            islem_geliri = islem_listesi[2]

            print(f"\t{islem_sayisi}.Islem")
            guncel_isim = input(f"\t--> Onceki aciklama: {islem_ismi} | Guncel aciklama girin: ")

            try:
                guncel_gider = int(input(f"\t--> Onceki gider: {islem_gideri} | Guncel gider girin: "))
            except ValueError:
                guncel_gider = "0"
            except:
                guncel_gider = "0"

            try:
                guncel_gelir = int(input(f"\t--> Onceki gelir: {int(islem_geliri)} | Guncel gelir girin: "))
            except ValueError:
                guncel_gelir = "0"
            except:
                guncel_gelir = "0"

            yeni_islem = guncel_isim + "/" + str(guncel_gider) + "/" + str(guncel_gelir)
            yeni_araba += yeni_islem + "|"

            islem_sayisi += 1

        Arabalar[index] = yeni_araba[:-1] + "\n"

        try:
            with open("22100011013.txt", "w", encoding="utf-8") as yeni_dosya:
                yeni_dosya.writelines(Arabalar)
        except FileNotFoundError:
            print("Kayit dosyasi bulunamadi.")
        except IOError:
            print("dosya islemede bir hata olustu.")
            print("Kayit dosyasini kontrol edin")
        except:
            print("Genel bir hata meydana geldi.")

    ###---------- ARAC DUZENLE (END) ----------###



    ###---------- ARAC SIL (START) ----------###
    def araba_sil():
        Arabalar = arac_listesi("22100011013.txt")
        uzunluk = kayit_sayi("22100011013.txt")

        print("\n\t----- ARABA SIL -----")

        while True:
            while True:
                try:
                    eleman = int(input("Silmek istediginiz kayit hangisi? "))
                    break
                except ValueError:
                    print("Lutfen gecerli bir sayi degeri girin.\n")
                except:
                    print("Lutfen gecerli bir sayi degeri girin.\n")
            if 0 <= eleman <= uzunluk:
                break
            else:
                print("lutfen gecerli bir kayit girin.")

        if eleman == 0:
            return False

        # kayitli aracin id degeri aliyoruz
        def araba_id(eleman):
            indis = ""
            syc = 1
            for araba in Arabalar:
                if syc == eleman:
                    indis = Arabalar.index(araba)
                    break
                syc += 1
            return int(indis)

        araba_id = araba_id(eleman)
        del Arabalar[araba_id]

        try:
            with open("22100011013.txt", "w", encoding="utf-8") as yeni_dosya:
                yeni_dosya.writelines(Arabalar)
        except FileNotFoundError:
            print("Kayit dosyasi bulunamadi.")
        except IOError:
            print("dosya islemede bir hata olustu.")
            print("Kayit dosyasini kontrol edin")
        except:
            print("Genel bir hata meydana geldi.")

    ###---------- ARAC SIL (END) ----------###



    ###---------- KAR-ZARAR HESAPLA (START) ----------###
    def araba_hesapla():
        Arabalar = arac_listesi("22100011013.txt")

        print("\n ***** KAR-ZARAR HESAPLA ***** \n")

        tarih = input("Kar-Zarar'i Hesaplamak Istediginiz Tarih? ")

        print("\nNO\tPLAKA\t\tTARIH\t\tSAHIP")

        syc = 1
        net_kazanc = 0
        deger = 0
        for araba in Arabalar:
            araba_veri = araba.split("|")
            araba_plaka = araba_veri[1]
            araba_sahip = araba_veri[2]
            araba_tarih = araba_veri[3]
            araba_islem = araba_veri[4]

            if tarih == araba_tarih:
                deger += 1
                print(f"{syc}) | {araba_plaka} | {araba_tarih} | {araba_sahip}")
                syc += 1

                islemler_net = 0
                for islemler in araba_veri[5:]:
                    islem = islemler.split("/")
                    islem_aciklama = islem[0]
                    islem_gideri = islem[1]
                    if islem[2][-1] == "\n":
                        islem_geliri = islem[2][:-1]
                    else:
                        islem_geliri = islem[2]

                    print(f"\t --> {islem_aciklama} Gider:{islem_gideri}TL, Gelir:{islem_geliri}TL")
                    net_islem = int(islem_geliri) - int(islem_gideri)

                    islemler_net += net_islem
                print(f"\tArabanin net kazanci: {islemler_net}TL")
                net_kazanc += islemler_net
                print("\n", end="")

        if deger == 0:
            print(f"\n{tarih} Gun icin kayit bulunamadi.")
            return False

        print(f"==> {tarih} Günün Kazanci: {net_kazanc}TL <==")

    ###---------- KAR-ZARAR HESAPLA (END) ----------###



    ###---------- FILITRELI ARAMA (START) ----------###
    def araba_arama():
        Arabalar = arac_listesi("22100011013.txt")

        print("\n ***** FILTRELI ARAMA *****")

        plaka = input("Aranacak plakayi girin: ")
        tarih = input("Aranacak tarihi girin: ")

        print("\nNO\tPLAKA\t\tTARIH\t\tSAHIP")

        syc = 1
        deger = 0
        for araba in Arabalar:
            araba_veri = araba.split("|")
            araba_plaka = araba_veri[1]
            araba_sahip = araba_veri[2]
            araba_tarih = araba_veri[3]
            araba_islem = araba_veri[4]

            if plaka == araba_plaka and tarih == araba_tarih:
                deger += 1
                print(f"{syc}) | {araba_plaka} | {araba_tarih} | {araba_sahip}")
                syc += 1

                for islemler in araba_veri[5:]:
                    islem = islemler.split("/")
                    islem_aciklama = islem[0]
                    islem_gideri = islem[1]
                    if islem[2][-1] == "\n":
                        islem_geliri = islem[2][:-1]
                    else:
                        islem_geliri = islem[2]

                    print(f"\t --> {islem_aciklama} Gider:{islem_gideri}TL, Gelir:{islem_geliri}TL")

                print("\n", end="")

        if deger == 0:
            print(f"\n{tarih} ve {plaka} icin herhangi bir esleme yok.")
            return False

    ###---------- FILITRELI ARAMA (END) ----------###

    ###---------- OTOMASYON MENU (START) ----------###
    while True:

        son_durum = 0
        print("\n*******************************")
        print("*  YETKILI SERVIS OTOMASYONU  *")
        print("*******************************")
        print(" ISLEMLER                   SEC")
        print("_______________________________")
        print("* Araclari Listele          (1)")
        print("* Yeni Arac Ekle            (2)")
        print("* Araclari Duzenle          (3)")
        print("* Arac Sil                  (4)")
        print("* Kar-Zarar Belirle         (5)")
        print("* Filtreli Arama            (6)")
        print("* Cikis Yap!                (7)")
        print("_______________________________")

        sec = input("\nLutfen bir islem secin: ")

        try:
            secenek = int(sec)
        except ValueError:
            print("Lutfen gecerli bir deger girin!")
            continue
        except:
            print("Lutfen gecerli bir deger girin!")
            continue

        if secenek == 1:
            # --- Arac Listeleme (Start) ---#
            while True:
                if kayit_sayi("22100011013.txt") > 0:
                    araba_listele()
                else:
                    print("\nListelenecek Araba yok.\n")

                alt_secenek = alt_menu()

                if alt_secenek == 1:
                    continue
                elif alt_secenek == 2:
                    break
                elif alt_secenek == 3:
                    son_durum = 1
                    break
                else:
                    print("\nMenuler icin gecerli degerleri girmelisiniz!\n")
                    break
        # --- Arac Listeleme (end) ---#

        elif secenek == 2:
            # --- Arac ekleme (start) ---#
            while True:
                sonuc = araba_ekle()

                if sonuc != False:
                    print("\nAraba ekleme islemi basarili bir sekilde gerceklesti.\n")
                else:
                    print("\nAraba ekeleme islemi iptal edildi.\n")

                alt_secenek = alt_menu()

                if alt_secenek == 1:
                    continue
                elif alt_secenek == 2:
                    break
                elif alt_secenek == 3:
                    son_durum = 1
                    break
                else:
                    print("\nMenuler icin gecerli degerleri girmelisiniz!\n")
                    break
        # --- Arac ekleme (end) ---#

        elif secenek == 3:
            # --- Arac Duzenle (Start) --- #
            while True:
                if kayit_sayi("22100011013.txt") > 0:
                    araba_listele()
                    sonuc = araba_duzenle()

                    if sonuc != False:
                        print("\nSecilen kayit basarili bir sekilde duzenlendi.\n")
                    else:
                        print("\nDuzenleme islemi iptal edildi.\n")
                else:
                    print("\nKayitli Araba yok.\n")

                alt_secenek = alt_menu()

                if alt_secenek == 1:
                    continue
                elif alt_secenek == 2:
                    break
                elif alt_secenek == 3:
                    son_durum = 1
                    break
                else:
                    print("\nMenuler icin gecerli degerleri girmelisiniz!\n")
                    break
        # --- Arac Duzenle (End) ---#

        elif secenek == 4:
            # --- Arac sil (start) ---#
            while True:
                if kayit_sayi("22100011013.txt") > 0:
                    araba_listele()
                    sonuc = araba_sil()

                    if sonuc != False:
                        print("\nSecilen kayit basarili bir sekilde silindi.\n")
                    else:
                        print("\nSilme islemi iptal edildi.\n")
                else:
                    print("\nSilinecek Araba yok.\n")

                alt_secenek = alt_menu()

                if alt_secenek == 1:
                    continue
                elif alt_secenek == 2:
                    break
                elif alt_secenek == 3:
                    son_durum = 1
                    break
                else:
                    print("\nMenuler icin gecerli degerleri girmelisiniz!\n")
                    break
        # --- Arac sil (end) ---#

        elif secenek == 5:
            # --- kar-zarar hesapla (start) ---#
            while True:
                if kayit_sayi("22100011013.txt") > 0:
                    araba_hesapla()
                else:
                    print("\nListelenecek Araba yok.\n")

                alt_secenek = alt_menu()

                if alt_secenek == 1:
                    continue
                elif alt_secenek == 2:
                    break
                elif alt_secenek == 3:
                    son_durum = 1
                    break
                else:
                    print("\nMenuler icin gecerli degerleri girmelisiniz!\n")
                    break
        # --- kar-zarar hesapla (end) ---#

        elif secenek == 6:
            # --- araba arama (start) --- #
            while True:
                if kayit_sayi("22100011013.txt") > 0:
                    araba_arama()
                else:
                    print("\nListelenecek Araba yok.\n")

                alt_secenek = alt_menu()

                if alt_secenek == 1:
                    continue
                elif alt_secenek == 2:
                    break
                elif alt_secenek == 3:
                    son_durum = 1
                    break
                else:
                    print("\nMenuler icin gecerli degerleri girmelisiniz!\n")
                    break
        # --- araba arama (end) --- #

        elif secenek == 7:
            # -- kapanis (start) -- #
            kapanis()
        # -- kapanis (end) -- #
        else:
            print("Gecerli bir secenek girin!")

        if son_durum == 1:
            kapanis()
    ###---------- OTOMASYON MENU (END) ----------###

yetkili_servis_otomasyon()