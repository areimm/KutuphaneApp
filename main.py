import config

from kitap_bilgileri import KitapBilgileri
from kitap_odunc import KitapOdunc
from kitap_turleri import KitapTurleri
from veritabani_baglantisi import VeritabaniBaglantisi
from yayin_evleri import YayinEvleri
from uye import Uye

server = config.SERVER
database = config.DATABASE

baglanti = VeritabaniBaglantisi(server, database).baglan()

kitap_bilgileri = KitapBilgileri(baglanti)
kitap_odunc = KitapOdunc(baglanti)
kitap_turleri = KitapTurleri(baglanti)
yayin_evleri = YayinEvleri(baglanti)
uye = Uye(baglanti)

def ana_menu():
     print('\n Ana Menü')
     print('1. Kitap Bilgileri İşlemleri')
     print('2. Kitap Türleri İşlemleri')
     print('3. Yayın Evleri İşlemleri')
     print('4. Üye İşlemleri')
     print('5. Kitap Ödünç İşlemleri')
     print('6. Çıkış Yap')
     
     
def kitapturleri_menu():
        print('\n Kitap Türleri Menüsü')
        print('1. Kitap Türü Ekle')
        print('2. Kitap Türü Güncelle')
        print('3. Kitap Türü Sil')
        print('4. Kitap Türlerini Listele')
        secim = input('Seçiminizi yapınız (1-5): ')
        
        if secim == '1':
            kitap_turleri.ekle(input('Kitap Türü Adı '))
        elif secim == '2':
            kitap_turleri.guncelle(input('Kitap Türü ID '), input('Kitap Türü Adı '))  
        elif secim == '3':
            kitap_turleri.sil(input('Kitap Türü ID '))
        elif secim == '4':
            kitap_turleri.listele()
        else:
            print('Geçersiz seçim')
      
      
def yayinevleri_menu():
        print('\n Yayın Evleri Menüsü')
        print('1. Yayın Evi Ekle')
        print('2. Yayın Evi Güncelle')
        print('3. Yayın Evi Sil')
        print('4. Yayın Evlerini Listele')
        secim = input('Seçiminizi yapınız (1-5): ')
        
        if secim == '1':
            yayin_evleri.ekle(input('Yayın Evi Adı '))
        elif secim == '2':
            yayin_evleri.guncelle(input('Yayın Evi ID '), input('Yayın Evi Adı '))  
        elif secim == '3':
            yayin_evleri.sil(input('Yayın Evi ID '))
        elif secim == '4':
            yayin_evleri.listele()
        else:
            print('Geçersiz seçim')
            
            
            
def uye_menu():
        print('\n Üye Menüsü')
        print('1. Üye Ekle')
        print('2. Üye Güncelle')
        print('3. Üye Sil')
        print('4. Üyeleri Listele')
        secim = input('Seçiminizi yapınız (1-4): ')
        
        if secim == '1':
            uye.ekle(input('Üye Adı: '), input('Üye Soyadı: '),input('Üye Email: ') ,input('Üye Telefon: '))
        elif secim == '2':
            uye.guncelle(input('Üye Yeni  ID '), input('Üye Yeni  Adı '), input('Üye Yeni  Soyadı '), input('Üye Yeni Email '), input('Üye Yeni  Telefon '))  
        elif secim == '3':
            uye.sil(input('Üye ID '))
        elif secim == '4':
            uye.listele()
        else:
            print('Geçersiz seçim')
            
            
def kitapodunc_menu():
        print('\n Kitap Ödünç Menüsü')
        print('1. Kitap Ödünç Ver')
        print('2. Kitap Ödünç İade')
        print('3. Ödünç Kitapları Listele')
        secim = input('Seçiminizi yapınız (1-3): ')
        
        if secim == '1':
            kitap_odunc.odunc_ver(input('Kitap ID '), input('Üye ID '), input('Ödünç Tarihi '), input('Teslim Tarihi '))
        elif secim == '2':
            kitap_odunc.iade(input('Kitap ID '), input('Üye ID '))
        elif secim == '3':
            kitap_odunc.listele()
        else:
            print('Geçersiz seçim')
            
            
def kitap_bilgileri_menu():
        print('\n Kitap Bilgileri Menüsü')
        print('1. Kitap Ekle')
        print('2. Kitap Güncelle')
        print('3. Kitap Sil')
        print('4. Kitapları Listele')
        secim = input('Seçiminizi yapınız (1-4): ')
        
        if secim == '1':
            kitap_bilgileri.ekle(input('ISBN No: '),input('Kitap Adı '), input('Yazar Adı '),input('Kitap Basım Yılı '),input('Kitap Türü ID '), input('Yayın Evi ID '))
        elif secim == '2':
            kitap_bilgileri.guncelle(input('Kitap ISBN_No '), input('Kitap Adı '), input('Yazar Adı '), input('Kitap Basım Yılı '), input('Kitap Türü ID '), input('Yayın Evi ID '))
        elif secim == '3':
            kitap_bilgileri.sil(input('Kitap ID '))
        elif secim == '4':
            kitap_bilgileri.listele()
        else:
            print('Geçersiz seçim')
        
            
            
            
while True:
    ana_menu()
    secim = input('Seçiminizi yapınız (1-6): ')
    if secim == '1':
        kitap_bilgileri_menu()
    elif secim == '2':
        kitapturleri_menu()
    elif secim == '3':
        yayinevleri_menu()
    elif secim == '4':
        uye_menu()
    elif secim == '5':
        kitapodunc_menu()
    elif secim == '6':
        break
    else:
        print('Geçersiz seçim')
        




def kitapbilgileri_menu():
     print('\n Kitap Bilgileri Menüsü')
     print('1. Kitap Ekle')
     print('2. Kitap Güncelle')
     print('3. Kitap Sil')
     print('4. Kitapları Listele')
     print('5. Ana Menü')
     secim = input('Seçiminizi yapınız (1-5): ')
     
     
