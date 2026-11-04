import sqlite3


class Datenbank:

    def __init__(self, datenbankname):
        self.datenbankname = datenbankname

    def artikeldb_erzeugen(self):
        '''
        Erzeugt die Artikel-Tabelle in der Datenbank,
        sollte für alle Kassen gleich bleiben.
        '''
        conn = None
        try:
            conn = sqlite3.connect(self.datenbankname)
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS artikel(
                                artikelnummer INTEGER PRIMARY KEY,
                                artikelname TEXT NOT NULL,
                                preis FLOAT NOT NULL);''')
            conn.commit()
        except sqlite3.Error:
            print("Datenbankfehler!")
        finally:
            if conn:
                conn.close()

    def kassendb_erzeugen(self):
        '''
        Initialisiert die Kasenbon-Tabelle in der Datenbank,
        kann durch kopieren der Funktion und
        ändern des Tabellennamen für mehrere Kassen verwendet werden.
        '''
        conn = None
        try:
            conn = sqlite3.connect(self.datenbankname)
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS kasse1(
                                  bonnummer INTEGER PRIMARY KEY AUTOINCREMENT,
                                  datum TEXT NOT NULL,
                                  gesamtpreis FLOAT NOT NULL);''')
            conn.commit()
        except sqlite3.Error:
            print("Datenbankfehler!")
        finally:
            if conn:
                conn.close()

    def artikel_in_db(self, artikelnummer, artikelname, preis):
        '''
        Speichert einen Artikel in der Datenbank,
        Exception bei Verletzung der Integritätsbedingungen und andere Datenbankfehler.
        :param artikelnummer: Artikelnummer als Integer
        :param artikelname: Artikelname als String
        :param preis: Preis
        '''
        conn = None
        try:
            conn = sqlite3.connect(self.datenbankname)
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO artikel (artikelnummer, artikelname, preis) VALUES (?, ?, ?)''',(artikelnummer, artikelname, preis))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            print("Artikelnummer bereits vorhanden!")
            return False
        except sqlite3.Error as e:
            print(f"Datenbankfehler!:{e}")
        finally:
            if conn:
                conn.close()

    def artikelpreis_aus_db(self, artikelnummer):
        '''
        Holt den Artikelpreis zu einer Artikelnummer aus der Datenbank,
        Exception bei Datenbankfehler
        :param artikelnummer: Artikelnummer als Integer
        :return: Preis als float
        '''
        conn = None
        try:
            conn = sqlite3.connect(self.datenbankname)
            cursor = conn.cursor()
            ergebnis = cursor.execute('''SELECT preis FROM artikel WHERE artikelnummer=?''',(artikelnummer,)).fetchone()
            if ergebnis is None:
                return None
            return ergebnis[0]
        except sqlite3.Error:
            print("Datenbankfehler!")
        finally:
            if conn:
                conn.close()

    def kassiervorgang_in_db(self, datum, gesamtpreis):
        '''
        Speichert einen Kassenbon in die Datenbank,
        Exception bei Datenbankfehler
        :param datum: Datum als String
        :param gesamtpreis: Gesamtpreis als Float
        '''
        conn = None
        try:
            conn = sqlite3.connect(self.datenbankname)
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO kasse1 (datum, gesamtpreis) VALUES (?, ?)''',(datum, gesamtpreis))
            conn.commit()
        except sqlite3.Error:
            print("Datenbankfehler!")
        finally:
            if conn:
                conn.close()
