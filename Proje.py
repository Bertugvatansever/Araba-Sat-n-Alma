import sqlite3 as sql
import random
vt=sql.connect('uye.db')
imlec=vt.cursor()
imlec.execute("Create Table IF NOT EXISTS Uyelık(kullanıcıadı,sifre)")
Dolar=8
Tl=1
Euro=10
girisdurumu="fsdsads"
istekmodel={"Marka":[],"Model":[]}

# Giriş Ekranı
def girisyap():
   kadı=input("Kullanıcı adınızı giriniz.: ")
   ksifre=input("Sifrenizi giriniz : ")
   sorgu="select kullanıcıadı from Uyelık where kullanıcıadı='{adı}' and sifre='{sifre}'".format(adı=kadı,sifre=ksifre)
   imlec.execute(sorgu)
   sonuc=imlec.fetchall()
   if len(sonuc)>0:
       globaldegisken=globals()
       globaldegisken["girisdurumu"]="s"
   else:
       globaldegisken=globals()
       globaldegisken["girisdurumu"]="f"
# Kayıt ekranı
def kayıtyap():
    kullanıcıadı=input("Kullanıcı adı giriniz.")
    sifre=input("Sifre giriniz.")
    imlec.execute("insert into Uyelık values (?,?)",(kullanıcıadı,sifre))
    print("Sayın {adı}, Kayıt işleminiz başarıyla tamamlanmıştır. Giriş için yönlendiriliyorsunuz...".format(adı=kullanıcıadı))
    vt.commit()
def paraHesapla():
    odemesekli=input("Para biriminizi yazınız.(Dolar,Tl,Euro)")
    para=int(input("Bakiyenizi giriniz."))
    if odemesekli =="Dolar":
        totalpara=para*Dolar
        print(totalpara)
        return totalpara    
    elif odemesekli =="Tl":
        totalpara=para*Tl
        return totalpara
    elif odemesekli =="Euro":
        totalpara=para*Euro
        return totalpara
# Araba Bilgileri      
def arababilgileri():
    Honda=["Civic"]
    Kia=["Rio HB"]
    Bmw=["BMW1 serisi"]   
    Renault=["Clio"]
    Audi=["A3"]
    Mercedes=["A serisi"]
    Nissan=["Micra"]
    Ford=["Fiesta"]
    Volkswagen=["Polo"]
    Jeep=["Gladiator"]
    while True:    
        model=input("Öğrenmek istediğiniz modelin ismini yazınız.")
        if model == "Honda":
            print(Honda)
        elif model =="Kia":
            print(Kia)
        elif model =="Bmw":
            print(Bmw)
        elif model=="Renault":
            print(Renault)
        elif model=="Audi":
            print(Audi)
        elif model=="Mercedes":
            print(Mercedes)
        elif model=="Nissan":
            print(Nissan)
        elif model=="Ford":
            print(Ford)
        elif model=="Volkswagen":
            print(Volkswagen)
        elif model=="Jeep":
            print(Jeep)
        else:
            print("Böyle bir model uygulamada mevcut değil.")
        cıkıs=input("Menüden çıkmak isterseniz 1 e diğer modeller hakkında bilgi almak için 2 ye basınız.")
        if cıkıs=="1":
            break
def İstekmodeller():
    while True:
        marka=input("Uygulamaya eklenmesini istediğiniz markayı yazınız.")
        model=input("Markanın modelini yazınız.")
        istekmodel["Marka"].append(marka)
        istekmodel["Model"].append(model)
        secenek=input("Başka bir marka ve model eklemek ister misiniz evet veya hayır yazınız")    
        if secenek == "hayır":
            break
    print("Teşekkürler,isteğiniz sisteme eklenmiştir.")            
class Car:
    def __init__(self,Marka,Model,Fiyat,Renk,Yakıtturu,Vitestipi):
        self.Marka=Marka
        self.Model=Model
        self.Fiyat=Fiyat
        self.Yakıtturu=Yakıtturu
        self.Renk=Renk
        self.Vitestipi=Vitestipi
list=[]                    
list.append(Car("Honda","Civic",240000,"Siyah,gri,beyaz Renk","LPG","Otomatik Vites"))
list.append(Car("Kia","Riohb",180000,"Gri,Kırmızı Renk","Benzin","Manuel Vites"))
list.append(Car("BMW","BMW1",520000,"Kırmızı Renk","Dizel","Otomatik Vites"))
list.append(Car("Renault","Clio",140000,"Beyaz Renk","Benzin","Manuel Vites"))
list.append(Car("Audi","A3",400000,"Beyaz Renk","Benzin","Otomatik Vites"))
list.append(Car("Mercedes","A Serisi",575000,"Siyah Renk","Benzinli","Otomatik Vites"))
list.append(Car("Nissan","Micra",140000,"Kırmızı Renk","Benzinli","Manuel Vites"))
list.append(Car("Ford","Fiesta",100000,"Beyaz Renk","Dizel","Otomatik Vites"))
list.append(Car("Volkswagen","Polo",50000,"Beyaz Renk","LPG","Manuel Vites"))
list.append(Car("Jeep","Gladiator",1600000,"Siyah Renk","Benzinli","Otomatik Vites"))
#Satın alma işlemleri
def Satınal(money):
    yazı=open("Odemesonucu.txt","w",encoding="utf-8")
    satın=input("Satın almak istediğiniz arabanın modelini yazınız.")
    if satın == "Civic":
        if sanslıkisi == "1":
            if money<list[0].Fiyat-list[0].Fiyat*(20/100):
                print("Yetersiz Bakiye")
            else:
                print("Satın alımınız başarıyla gerçekleştirilmiştir.")
                bilgimesaji="{marka} markalı {model} modelli araba satın alınmıştır.".format(marka="Honda",model="Civic")
                print(bilgimesaji)
                yazı.write(bilgimesaji)
                kalanpara=money-list[0].Fiyat
                yazı.close()
                return kalanpara
        else:
            if money<list[0].Fiyat:
                print("Yetersiz Bakiye ")
            else:
                print("Satın alımınız başarıyla gerçekleştirilmiştir.")
                bilgimesaji="{marka} markalı {model} modelli araba satın alınmıştır.".format(marka="Honda",model="Civic")
                print(bilgimesaji)
                yazı.write(bilgimesaji)
                kalanpara=money-list[0].Fiyat
                yazı.close()
                return kalanpara    

        
        
    if satın=="RioHb":
        if sanslıkisi =="1":
            if money<list[1].Fiyat-list[1].Fiyat*(20/100):
                print("Yetersiz Bakiye")
            else:
                print("Satın alımınız başarıyla gerçekleştirilmiştir.")
                bilgimesaji="{marka} markalı {model} modelli araba satın alınmıştır.".format(marka="Kia",model="RioHb")
                print(bilgimesaji)
                yazı.write(bilgimesaji)
                kalanpara=money-list[1].Fiyat
                yazı.close()
                return kalanpara
        else:
            if money<list[1].Fiyat:
                print("Yetersiz Bakiye ")
            else:
                print("Satın alımınız başarıyla gerçekleştirilmiştir.")
                bilgimesaji="{marka} markalı {model} modelli araba satın alınmıştır.".format(marka="Kia",model="RioHb")
                print(bilgimesaji)
                yazı.write(bilgimesaji)
                kalanpara=money-list[1].Fiyat
                yazı.close()
                return kalanpara
    
    if satın == "Bmw1":
        if sanslıkisi == "1":
            if money<list[2].Fiyat-list[2].Fiyat*(20/100):
                print("Yetersiz Bakiye")
            else:
                print("Satın alımınız başarıyla gerçekleştirilmiştir.")
                bilgimesaji="{marka} markalı {model} modelli araba satın alınmıştır.".format(marka="Bmw",model="Bmw1")
                print(bilgimesaji)
                yazı.write(bilgimesaji)
                kalanpara=money-list[2].Fiyat
                yazı.close()
                return kalanpara
        else:
            if money<list[2].Fiyat:
                print("Yetersiz Bakiye ")
            else:
                print("Satın alımınız başarıyla gerçekleştirilmiştir.")
                bilgimesaji="{marka} markalı {model} modelli araba satın alınmıştır.".format(marka="Bmw",model="Bmw1")
                print(bilgimesaji)
                yazı.write(bilgimesaji)
                kalanpara=money-list[2].Fiyat
                yazı.close()
                return kalanpara    
    
    if satın == "Clio":
        if sanslıkisi == "1":
            if money<list[3].Fiyat-list[3].Fiyat*(20/100):
                print("Yetersiz Bakiye")
            else:
                print("Satın alımınız başarıyla gerçekleştirilmiştir.")
                bilgimesaji="{marka} markalı {model} modelli araba satın alınmıştır.".format(marka="Renault",model="Clio")
                print(bilgimesaji)
                yazı.write(bilgimesaji)
                kalanpara=money-list[3].Fiyat
                yazı.close()
                return kalanpara
        else:
            if money<list[3].Fiyat: 
                print("Yetersiz Bakiye ")
            else:
                print("Satın alımınız başarıyla gerçekleştirilmiştir.")
                bilgimesaji="{marka} markalı {model} modelli araba satın alınmıştır.".format(marka="Renault",model="Clio")
                print(bilgimesaji)
                yazı.write(bilgimesaji)
                kalanpara=money-list[3].Fiyat
                yazı.close()
                return kalanpara
    
    if satın == "A3":
        if sanslıkisi == "1":
            if money<list[4].Fiyat-list[4].Fiyat*(20/100):
                print("Yetersiz Bakiye")
            else:
                print("Satın alımınız başarıyla gerçekleştirilmiştir.")
                bilgimesaji="{marka} markalı {model} modelli araba satın alınmıştır.".format(marka="Audi",model="A3")
                print(bilgimesaji)
                yazı.write(bilgimesaji)
                kalanpara=money-list[4].Fiyat
                yazı.close()
                return kalanpara
        else:
            if money<list[4].Fiyat:
                print("Yetersiz Bakiye ")
            else:
                print("Satın alımınız başarıyla gerçekleştirilmiştir.")
                bilgimesaji="{marka} markalı {model} modelli araba satın alınmıştır.".format(marka="Audi",model="A3")
                print(bilgimesaji)
                yazı.write(bilgimesaji)
                kalanpara=money-list[4].Fiyat
                yazı.close()
                return kalanpara        
    
    if satın == "A serisi":
        if sanslıkisi == "1":
            if money<list[5].Fiyat-list[5].Fiyat*(20/100):
                print("Yetersiz Bakiye")
            else:
                print("Satın alımınız başarıyla gerçekleştirilmiştir.")
                bilgimesaji="{marka} markalı {model} modelli araba satın alınmıştır.".format(marka="Mercedes",model="A serisi")
                print(bilgimesaji)
                yazı.write(bilgimesaji)
                kalanpara=money-list[5].Fiyat
                yazı.close()
                return kalanpara
        else:
            if money<list[5].Fiyat:
                print("Yetersiz Bakiye ")
            else:
                print("Satın alımınız başarıyla gerçekleştirilmiştir.")
                bilgimesaji="{marka} markalı {model} modelli araba satın alınmıştır.".format(marka="Mercedes",model="A serisi")
                print(bilgimesaji)
                yazı.write(bilgimesaji)
                kalanpara=money-list[5].Fiyat
                yazı.close()
                return kalanpara

    if satın == "Micra":
        if sanslıkisi == "1":
            if money<list[6].Fiyat-list[6].Fiyat*(20/100):
                print("Yetersiz Bakiye")
            else:
                print("Satın alımınız başarıyla gerçekleştirilmiştir.")
                bilgimesaji="{marka} markalı {model} modelli araba satın alınmıştır.".format(marka="Nissan",model="Micra")
                print(bilgimesaji)
                yazı.write(bilgimesaji)
                kalanpara=money-list[6].Fiyat
                yazı.close()
                return kalanpara
        else:
            if money<list[6].Fiyat:
                print("Yetersiz Bakiye ")
            else:
                print("Satın alımınız başarıyla gerçekleştirilmiştir.")
                bilgimesaji="{marka} markalı {model} modelli araba satın alınmıştır.".format(marka="Nissan",model="Micra")
                print(bilgimesaji)
                yazı.write(bilgimesaji)
                kalanpara=money-list[6].Fiyat
                yazı.close()
                return kalanpara
    
    if satın == "Fiesta":
        if sanslıkisi == "1":
            if money<list[7].Fiyat-list[7].Fiyat*(20/100):
                print("Yetersiz Bakiye")
            else:
                print("Satın alımınız başarıyla gerçekleştirilmiştir.")
                bilgimesaji="{marka} markalı {model} modelli araba satın alınmıştır.".format(marka="Ford",model="Fiesta")
                print(bilgimesaji)
                yazı.write(bilgimesaji)
                kalanpara=money-list[7].Fiyat
                yazı.close()
                return kalanpara
        else:
            if money<list[7].Fiyat:
                print("Yetersiz Bakiye ")
            else:
                print("Satın alımınız başarıyla gerçekleştirilmiştir.")
                bilgimesaji="{marka} markalı {model} modelli araba satın alınmıştır.".format(marka="Ford",model="Fiesta")
                print(bilgimesaji)
                yazı.write(bilgimesaji)
                kalanpara=money-list[7].Fiyat
                yazı.close()
                return kalanpara
    
    if satın == "Polo":
        if sanslıkisi == "1":
            if money<list[8].Fiyat-list[8].Fiyat*(20/100):
                print("Yetersiz Bakiye")
            else:
                print("Satın alımınız başarıyla gerçekleştirilmiştir.")
                bilgimesaji="{marka} markalı {model} modelli araba satın alınmıştır.".format(marka="Volskwagen",model="Polo")
                print(bilgimesaji)
                yazı.write(bilgimesaji)
                kalanpara=money-list[8].Fiyat
                yazı.close()
                return kalanpara
        else:
            if money<list[8].Fiyat:
                print("Yetersiz Bakiye ")
            else:
                print("Satın alımınız başarıyla gerçekleştirilmiştir.")
                bilgimesaji="{marka} markalı {model} modelli araba satın alınmıştır.".format(marka="Volkswagen",model="Polo")
                print(bilgimesaji)
                yazı.write(bilgimesaji)
                kalanpara=money-list[8].Fiyat
                yazı.close()
                return kalanpara                
    
    if satın == "Gladiator":
        if sanslıkisi == "1":
            if money<list[9].Fiyat-list[9].Fiyat*(20/100):
                print("Yetersiz Bakiye")
            else:
                print("Satın alımınız başarıyla gerçekleştirilmiştir.")
                bilgimesaji="{marka} markalı {model} modelli araba satın alınmıştır.".format(marka="Jeep",model="Gladiator")
                print(bilgimesaji)
                yazı.write(bilgimesaji)
                kalanpara=money-list[9].Fiyat
                yazı.close()
                return kalanpara
        else:
            if money<list[9].Fiyat:
                print("Yetersiz Bakiye ")
            else:
                print("Satın alımınız başarıyla gerçekleştirilmiştir.")
                bilgimesaji="{marka} markalı {model} modelli araba satın alınmıştır.".format(marka="Jeep",model="Gladiator")
                print(bilgimesaji)
                yazı.write(bilgimesaji)
                kalanpara=money-list[9].Fiyat
                yazı.close()
                return kalanpara    

#Uygulama giriş
print("""
**** Uygulamaya Hoşgeldiniz ****
Lütfen uygulamaya giriş yapınız.
Kayıt olmak  için 1 e basınız.
Giriş yapmak için 2 e basınız.
""")
secenek=input("")
if secenek == "1":
    kayıtyap()
    girisyap()
if secenek== "2":
    girisyap()    

globaldegisken=globals()
if globaldegisken["girisdurumu"]=="s":
  #şanslı kişiye %20 indirim
  #şanslı kişi olma ihtimali %10
    sanslıkisi=random.randint(0,9)
    if sanslıkisi == "1":
        print("******************** Tebrikler alacağınız araba için %20 indirim kazandınız.(Bütün arabalar dahil)********************")
    else:
        secenek=input("Uygulamada Mevcut Satılık araçları görmek isterseniz 1 e basınız")
        if secenek == "1":
            arababilgileri()
        bilgi=input("Araçlar Hakkında Fiyat ve diğer bilgileri öğrenmek için 1 e basınız.")
        if bilgi == "1":
            for a in list:
                print("{marka} - {model} - {fiyat} -  {renk} - {yakıtturu} - {vitestipi}".format(marka=a.Marka,model=a.Model,fiyat=a.Fiyat,renk=a.Renk,yakıtturu=a.Yakıtturu,vitestipi=a.Vitestipi))

            paramiktarı=paraHesapla()
            Satınal(paramiktarı)
            İstekmodeller()
            kalanpara=Satınal(paramiktarı)
            print("Kalan para",kalanpara)
            
else:
    while True:
        print("Kullanıcı adı veya şifre yanlış")
        print("giris basarisiz")
        break




   
                                                                                                                                                                                                                                                                                                                                                                                                                                        