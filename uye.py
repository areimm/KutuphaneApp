class Uye:
    def __init__(self,baglanti):
       # Veritabanı bağlantısını saklamak için bir özellik oluşturur.
        self.baglanti = baglanti
    
    def ekle(self, ad, soyad, email, telefon):
        if self.baglanti:
            try:
                cursor = self.baglanti.cursor()
                cursor.execute("INSERT INTO uye (uye_ad, uye_soyad, uye_email, uye_telefon) VALUES (?, ?, ?, ?)",
                               (ad, soyad, email, telefon))
                self.baglanti.commit()
                print("Üye eklendi.")
            except Exception as e:
                print("Üye eklenemedi:", e)
        else:
            print("Veritabanı bağlantısı yok.")
            
    def sil(self, uye_id):
        if self.baglanti:
            try:
                cursor = self.baglanti.cursor()
                cursor.execute("DELETE FROM uye WHERE uye_id = ?", (uye_id,))
                self.baglanti.commit()
                print("Üye silindi.")
            except Exception as e:
                print("Üye silinemedi:", e)
        else:
            print("Veritabanı bağlantısı yok.")
            
    def listele(self):
        if self.baglanti:
            try:
                cursor = self.baglanti.cursor()
                cursor.execute("SELECT * FROM uye")
                uyeler = cursor.fetchall()
                for uye in uyeler:
                    print(uye)
            except Exception as e:
                print("Üyeler listelenemedi:", e)
        else:
            print("Veritabanı bağlantısı yok.")
            
    def guncelle(self, uye_id, yeni_ad, yeni_soyad, yeni_email, yeni_telefon):
        if self.baglanti:
            try:
                cursor = self.baglanti.cursor()
                cursor.execute("UPDATE uye SET uye_ad = ?, uye_soyad = ?, uye_email = ?, uye_telefon = ? WHERE uye_id = ?",
                               (yeni_ad, yeni_soyad, yeni_email, yeni_telefon, uye_id))
                self.baglanti.commit()
                print("Üye güncellendi.")
            except Exception as e:
                print("Üye güncellenemedi:", e)
        else:
            print("Veritabanı bağlantısı yok.")
        
            
        
        