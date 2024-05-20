class YayinEvleri:
    def __init__(self,baglanti):
        self.baglanti = baglanti
        
    def ekle(self,yayinevi_adi):
        if self.baglanti:
            try:
                cursor = self.baglanti.cursor()
                cursor.execute("INSERT INTO yayinEvleri (yayinevi_adi) VALUES (?)",
                               (yayinevi_adi,))
                self.baglanti.commit()
                print("Yayınevi eklendi.")
            except Exception as e:
                print("Yayınevi eklenemedi:", e)
        else:
            print("Veritabanı bağlantısı yok.")
            
    def sil(self, id):
        if self.baglanti:
            try:
                cursor = self.baglanti.cursor()
                cursor.execute("DELETE FROM yayinEvleri WHERE yayinevi_id=?", (id,))
                self.baglanti.commit()
                print("Yayınevi silindi.")
            except Exception as e:
                print("Yayınevi silinemedi:", e)
        else:
            print("Veritabanı bağlantısı yok.")
            
    def listele(self):
        if self.baglanti:
            try:
                cursor = self.baglanti.cursor()
                cursor.execute("SELECT * FROM yayinEvleri")
                yayin_evleri = cursor.fetchall()
                for yayinevi in yayin_evleri:
                    print(yayinevi)
            except Exception as e:
                print("Yayın evleri listelenemedi:", e)
        else:
            print("Veritabanı bağlantısı yok.")
            
            
    def guncelle(self, id, yayinevi_adi):
        if self.baglanti:
            try:
                cursor = self.baglanti.cursor()
                cursor.execute("UPDATE yayinEvleri SET yayinevi_adi=? WHERE yayinevi_id=?",
                               (yayinevi_adi, id))
                self.baglanti.commit()
                print("Yayınevi güncellendi.")
            except Exception as e:
                print("Yayınevi güncellenemedi:", e)
        else:
            print("Veritabanı bağlantısı yok.")