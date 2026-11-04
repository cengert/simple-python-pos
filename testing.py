import pytest
import sqlite3

from exceptions import NegativerWertFehler
from datenbank import Datenbank


def test_negativer_wert_fehler():
    fehler = NegativerWertFehler()
    assert str(fehler) == "Bitte keine negativen Werte verwenden!"


def test_artikel_anlegen_und_preis_auslesen(tmp_path):
    dbfile = tmp_path / "test.db"
    db = Datenbank(str(dbfile))
    db.artikeldb_erzeugen()
    assert db.artikel_in_db(1,"Hans Wurst", 2.99) is True
    assert db.artikelpreis_aus_db(1) == 2.99

def test_artikelpreis_nicht_vorhanden(tmp_path):
    dbfile = tmp_path / "test.db"
    db = Datenbank(str(dbfile))
    db.artikeldb_erzeugen()
    preis = db.artikelpreis_aus_db(99999999999)
    assert preis is None

def test_doppelte_artikelnummer(tmp_path):
    dbfile = tmp_path / "test.db"
    db = Datenbank(str(dbfile))
    db.artikeldb_erzeugen()
    ergebnis1 = db.artikel_in_db(1,"Hans Wurst", 2.99)
    assert ergebnis1 is True
    ergebnis2 = db.artikel_in_db(1,"Franz Käse", 1.99)
    assert ergebnis2 is False

def test_kassiervorgang_testbon(tmp_path):
    dbfile = tmp_path / "kasse.db"

    db = Datenbank(str(dbfile))
    db.artikeldb_erzeugen()
    db.kassendb_erzeugen()

    db.artikel_in_db(1, "Hans Wurst", 7.88)
    db.artikel_in_db(2, "Franz Käse", 1.99)

    bon = 0
    artikel1 = 1
    artikel2 = 2
    menge1 = 1
    menge2 = 2

    bon += (db.artikelpreis_aus_db(artikel1) * menge1)
    bon += (db.artikelpreis_aus_db(artikel2) * menge2)

    db.kassiervorgang_in_db("heute", bon)

    conn = sqlite3.connect(str(dbfile))
    cursor = conn.cursor()
    testbon = cursor.execute("SELECT gesamtpreis FROM kasse1").fetchone()[0]
    conn.close()

    assert testbon == bon == 11.86

