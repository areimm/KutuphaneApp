class KitapBilgileri:
    def __init__(self,baglanti):
        self.baglanti = baglanti
        
    def ekle(self, ISBN_No, kitap_adi, kitap_yazari, basimYili,  tur_id, yayinevi_id):
        if self.baglanti:
            try:
                cursor = self.baglanti.cursor()
                cursor.execute("INSERT INTO kitapBilgileri (ISBN_No, kitap_adi, kitap_yazari, basimYili, tur_id, yayinevi_id) VALUES (?,?,?,?,?,?)",
                               (ISBN_No, kitap_adi, kitap_yazari, basimYili, tur_id, yayinevi_id))
                self.baglanti.commit()
                print("Kitap bilgileri eklendi.")
            except Exception as e:
                print("Kitap bilgileri eklenemedi:", e)
        else:
            print("Veritabanı bağlantısı yok.")
            
    def listele(self):
        
        if self.baglanti:
            try:
                cursor = self.baglanti.cursor()
                cursor.execute("SELECT kb.id,kb .ISBN_No,kb.kitap_adi,kb.kitap_yazari,kb.basimYili,kt.tur_adi,ye.yayinevi_adi FROM kitapBilgileri kb INNER JOIN kitapTurleri kt ON kb.tur_id=kt.tur_id INNER JOIN yayinEvleri ye ON kb.yayinevi_id=ye.yayinevi_id")
                kitaplar = cursor.fetchall()
                for kitap in kitaplar:
                    print(kitap)
            except Exception as e:
                print("Kitaplar listelenemedi:", e)
        else:
            print("Veritabanı bağlantısı yok.")
            
    def sil(self, id):
        if self.baglanti:
            try:
                cursor = self.baglanti.cursor()
                cursor.execute("DELETE FROM kitapBilgileri WHERE id=?", (id,))
                self.baglanti.commit()
                print("Kitap bilgileri silindi.")
            except Exception as e:
                print("Kitap bilgileri silinemedi:", e)
        else:
            print("Veritabanı bağlantısı yok.")
            
            
    def guncelle(self, ISBN_No, yeni_kitap_adi, yeni_kitap_yazari, yeni_basimYili, yeni_tur_id, yeni_yayinevi_id):
        if self.baglanti:
            try:
                cursor = self.baglanti.cursor()
                cursor.execute("UPDATE kitapBilgileri SET kitap_adi = ?, kitap_yazari = ?, basimYili = ?, tur_id = ?, yayinevi_id = ? WHERE ISBN_No = ?",
                               ( yeni_kitap_adi, yeni_kitap_yazari, yeni_basimYili, yeni_tur_id,yeni_yayinevi_id,ISBN_No))
                self.baglanti.commit()
                print("Kitap bilgileri güncellendi.")
            except Exception as e:
                print("Kitap bilgileri güncellenemedi:", e)
        else:
            print("Veritabanı bağlantısı yok.")