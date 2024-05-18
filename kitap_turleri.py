class KitapTurleri:
    def __init__(self,baglanti):
        self.baglanti = baglanti
        
    def ekle(self, tur_ad):
        if self.baglanti:
            try:
                cursor = self.baglanti.cursor()
                cursor.execute("INSERT INTO kitap_turleri (tur_ad) VALUES (?)",
                               (tur_ad,))
                self.baglanti.commit()
                print("Kitap türü eklendi.")
            except Exception as e:
                print("Kitap türü eklenemedi:", e)
        else:
            print("Veritabanı bağlantısı yok.")
            
            
    def sil(self, tur_id):
        if self.baglanti:
            try:
                cursor = self.baglanti.cursor()
                cursor.execute("DELETE FROM kitap_turleri WHERE tur_id = ?", (tur_id,))
                self.baglanti.commit()
                print("Kitap türü silindi.")
            except Exception as e:
                print("Kitap türü silinemedi:", e)
        else:
            print("Veritabanı bağlantısı yok.")
            
            
    def listele(self):
        if self.baglanti:
            try:
                cursor = self.baglanti.cursor()
                cursor.execute("SELECT * FROM kitap_turleri")
                kitap_turleri = cursor.fetchall()
                for kitap_turu in kitap_turleri:
                    print(kitap_turu)
            except Exception as e:
                print("Kitap türleri listelenemedi:", e)
        else:
            print("Veritabanı bağlantısı yok.")
            
    
    def guncelle(self, tur_id, yeni_ad):
        if self.baglanti:
            try:
                cursor = self.baglanti.cursor()
                cursor.execute("UPDATE kitap_turleri SET tur_ad = ? WHERE tur_id = ?",
                               (yeni_ad, tur_id))
                self.baglanti.commit()
                print("Kitap türü güncellendi.")
            except Exception as e:
                print("Kitap türü güncellenemedi:", e)
        else:
            print("Veritabanı bağlantısı yok.")
            