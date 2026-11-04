from datenbank import Datenbank
from exceptions import NegativerWertFehler


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
            print("Artikelnummer muss eine Zahl sein!")

def artikelname_abfragen():
    '''
    Abfrage des Artikelnamen beim User, Wiederholung bei ungültiger Eingabe
    :return: Artikelname als String
    '''
    while True:
        artikelname = input("Bitte Artikelname eingeben: ")
        if artikelname:
            return artikelname
        else:
            print("Artikelname darf nicht leer sein!")

def preis_abfragen():
    '''
    Abfrage des Preises beim User, Wiederholung bei ungültiger Eingabe
    :return: Preis als Float
    '''
    while True:
        try:
            preis = float(input("Bitte Preis eingeben: "))
            if preis < 0:
                raise NegativerWertFehler()
            return preis
        except NegativerWertFehler as e:
            print(e)
        except ValueError:
            print("Preis muss eine Zahl sein!")

def artikel_speichern(db, artikelnummer, artikelname, preis):
    '''
    Speichert die übergebenen Werte in die Datenbank, Positivmeldung bei Erfolg
    :param db: Datenbank, in die gespeichert werden soll als String
    :param artikelnummer: Artikelnummer als Integer
    :param artikelname: Artikelname als String
    :param preis: Preis als Float
    '''
    if db.artikel_in_db(artikelnummer, artikelname, preis):
        print("Artikel erfolgreich gespeichert!")


def artikel_anlegen():
    '''
    Funktion zum Artikel anlegen
    '''
    db = Datenbank("datenbank.db")
    db.artikeldb_erzeugen()
    artikelmenu = 1
    while artikelmenu == 1:
        artikelnummer=artikelnummer_abfragen()
        artikelname=artikelname_abfragen()
        preis = preis_abfragen()
        artikel_speichern(db, artikelnummer, artikelname, preis)
        while True:
            try:
                artikelmenu = int(input("(1) Weiteren Artikel anlegen\n(0) Zurück ins Hauptmenü\n"))
                if artikelmenu == 1 or artikelmenu == 0:
                    break
                else:
                    print("Menüpunkt nicht vorhanden!")
            except ValueError:
                print("Bitte eine Zahl eingeben!")
        if artikelmenu == 0:
            break



