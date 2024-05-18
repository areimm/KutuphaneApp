class YayinEvleri:
    def __init__(self,baglanti):
        self.baglanti = baglanti
        
    def ekle(self,yayinevi_ad):
        if self.baglanti:
            try:
                cursor = self.baglanti.cursor()
                cursor.execute("INSERT INTO yayinEvleri (yayinevi_ad) VALUES (?)",
                               (yayinevi_ad,))
                self.baglanti.commit()
                print("Yayınevi eklendi.")
            except Exception as e:
                print("Yayınevi eklenemedi:", e)
        else:
            print("Veritabanı bağlantısı yok.")