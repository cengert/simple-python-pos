from datenbank import Datenbank
from exceptions import NegativerWertFehler
from datetime import datetime


def artikelnummer_abfragen():
    '''
    Abfragen der Artikelnummer beim User, Wiederholung bei ungültiger Eingabe
    :return: Artikelnummer als Integer
    '''
    while True:
        try:
            artikelnummer = int(input("Bitte Artikelnummer eingeben: "))
            if artikelnummer < 0:
                raise NegativerWertFehler()
            else:
                return artikelnummer
        except NegativerWertFehler as e:
            print(e)
        except ValueError:
            print("Bitte Artikelnummer als Zahl angeben!")

def menge_abfragen():
    '''
    Abfragen der Menge beim User, Wiederholung bei ungültiger Eingabe
    :return: Menge als Integer
    '''
    while True:
        try:
            menge = int(input("Bitte Menge eingeben: "))
            if menge < 0:
                raise NegativerWertFehler()
            return menge
        except NegativerWertFehler as e:
            print(e)
        except ValueError:
            print("Bitte Menge als Zahl eingeben!")

def bon_speichern(db, kassenbon):
    '''
    Speichert die übergebenen Werte in die Datenbank, Positivmeldung bei Erfolg
    :param db: Datenbank, in die gespeichert werden soll als String
    :param kassenbon: Wert des gesamten Kassenbons als Float
    '''
    datum = datetime.now().strftime("%d.%m.%Y")
    db.kassiervorgang_in_db(datum, kassenbon)
    print(f"Kassiervorgang erfolgreich beendet. Gesamtbetrag: {kassenbon:.2f}€")


def kassiervorgang():
    '''
    Funktion berechnet aus Artikelnummern und Menge den Gesamtpreis eines Kassenbons
    und speichert diesen in der Datenbank
    '''
    db = Datenbank("datenbank.db")
    db.kassendb_erzeugen()
    kassiermenu = 1
    kassenbon = 0
    while kassiermenu == 1:

        artikelnummer = artikelnummer_abfragen()
        artikelpreis = db.artikelpreis_aus_db(artikelnummer)

        if artikelpreis is None:
            print("Artikelnummer nicht in Datenbank vorhanden!")
            continue

        menge = menge_abfragen()

        kassenbon += (artikelpreis * menge)

        while True:
            try:
                kassiermenu = int(input("(1) Weiteren Artikel scannen\n(0) Bon beenden, zurück ins Hauptmenü\n"))
                if kassiermenu in (0, 1):
                    break
                else:
                    print("Menüpunkt nicht vorhanden!")
            except ValueError:
                print("Bitte eine Zahl eingeben!")

        if kassiermenu == 0:
            break

    bon_speichern(db, kassenbon)

