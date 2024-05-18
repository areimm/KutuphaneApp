import pyodbc

class VeritabaniBaglantisi:
    def __init__(self, server, database):
        # Bağlantı için gerekli bilgileri saklamak üzere özellikler oluşturur.
        self.server = server
        self.database = database
        # Bağlantıyı tutacak bir özellik oluşturur ve __baglan() metodunu kullanarak başlatır.
        self.conn = self.baglan()

    def baglan(self):
        try:
            # Bağlantı dizesini oluşturur.
            conn_str = f'DRIVER={{SQL Server}};SERVER={self.server};DATABASE={self.database};Trusted_Connection=yes;'
            # SQL Server veritabanına bağlanır.
            conn = pyodbc.connect(conn_str)
            # Bağlantının başarılı olduğunu kullanıcıya bildirir.
            print("Bağlantı başarılı.")
            return conn
        except Exception as e:
            # Bağlantı hatası durumunda hata mesajını kullanıcıya bildirir.
            print("Bağlantı hatası:", e)
            return None

    def baglantiyi_kapat(self):
        # Bağlantı mevcutsa işleme devam eder.
        if self.conn:
            # Bağlantıyı kapatır.
            self.conn.close()
            # Bağlantının başarıyla kapatıldığını kullanıcıya bildirir.
            print("Bağlantı kapandı.")
