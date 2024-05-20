
class KitapOdunc:
    def __init__(self, baglanti):
        self.baglanti = baglanti

    def ekle(self, uye_id, ISBN_No, odunc_tarihi, geri_verme_tarihi):
     if self.baglanti:
        try:
            cursor = self.baglanti.cursor()
            # Kitabın ödünç verilmiş olup olmadığını kontrol eden sorgu
            cursor.execute("SELECT COUNT(*) FROM kitapOdunc WHERE ISBN_No = ?", (ISBN_No,))
            count = cursor.fetchone()[0]

            if count > 0:
                print("Kitap zaten ödünç verilmiş.")
            else:
                cursor.execute("INSERT INTO kitapOdunc (uye_id, ISBN_No, odunc_alma_tarihi, geri_verme_tarihi) VALUES (?,?,?,?)",
                               (uye_id, ISBN_No, odunc_tarihi, geri_verme_tarihi))
                self.baglanti.commit()
                print("Kitap ödünç eklendi.")
        except Exception as e:
            print("Kitap ödünç eklenemedi:", e)
     else:
        print("Veritabanı bağlantısı yok.")
            
    def sil(self, id):
        if self.baglanti:
            try:
                cursor = self.baglanti.cursor()
                cursor.execute("DELETE FROM kitapOdunc WHERE odunc_id=?", (id,))
                self.baglanti.commit()
                print("Kitap ödünç silindi.")
            except Exception as e:
                print("Kitap ödünç silinemedi:", e)
        else:
            print("Veritabanı bağlantısı yok.")
            
    def listele(self):
        if self.baglanti:
            try:
                cursor = self.baglanti.cursor()
                cursor.execute("SELECT ko.odunc_id, u.uye_ad, u.uye_soyad , kb.kitap_adi, ko.odunc_alma_tarihi, ko.geri_verme_tarihi FROM kitapOdunc ko INNER JOIN kitapBilgileri kb ON ko.ISBN_No = kb.ISBN_No  INNER JOIN uye u ON ko.uye_id = u.uye_id;")
                odunc_listesi = cursor.fetchall()
                for odunc in odunc_listesi:
                    print(odunc)
            except Exception as e:
                print("Ödünçler listelenemedi:", e)
        else:
            print("Veritabanı bağlantısı yok.")
            
    def guncelle(self, id, uye_id, ISBN_No, odunc_tarihi, geri_verme_tarihi):
        if self.baglanti:
            try:
                cursor = self.baglanti.cursor()
                cursor.execute("UPDATE kitapOdunc SET uye_id=?, ISBN_No=?, odunc_alma_tarihi=?, geri_verme_tarihi=? WHERE odunc_id=?",
                               (uye_id, ISBN_No, odunc_tarihi, geri_verme_tarihi, id))
                self.baglanti.commit()
                print("Kitap ödünç güncellendi.")
            except Exception as e:
                print("Kitap ödünç güncellenemedi:", e)
        else:
            print("Veritabanı bağlantısı yok.")        


# class KitapOdunc:
    # def __init__(self,baglanti):
    #     self.baglanti = baglanti
        
    # def ekle(self, uye_id, ISBN_No, odunc_tarihi, geri_verme_tarihi):
    #     if self.baglanti:
    #         try:
    #             cursor = self.baglanti.cursor()
    #             cursor.execute("INSERT INTO kitapOdunc (uye_id, ISBN_No, odunc_tarihi, geri_verme_tarihi) VALUES (?,?,?,?)",
    #                            (uye_id, ISBN_No, odunc_tarihi, geri_verme_tarihi))
    #             self.baglanti.commit()
    #             print("Kitap ödünç eklendi.")
    #         except Exception as e:
    #             print("Kitap ödünç eklenemedi:", e)
    #     else:
    #         print("Veritabanı bağlantısı yok.")
    