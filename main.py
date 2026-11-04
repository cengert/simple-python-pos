from artikel import artikel_anlegen
from kasse import kassiervorgang


def main():
    '''
    Hauptfunktion des Programmes.
    Darstellung eines einfachen Auswahlmenus
    '''
    while True:
        try:
            auswahl = int(input("Hauptmenü. Bitten wählen:\n(1) Artikel anlegen\n(2) Kassiervorgang starten\n(0) Programm beenden\n"))
            if auswahl == 1:
                artikel_anlegen()
            elif auswahl == 2:
                kassiervorgang()
            elif auswahl == 0:
                break
            else:
                print("Menüpunkt nicht vorhanden!")
        except ValueError:
            print("Bitte eine Zahl eingeben!")


main()