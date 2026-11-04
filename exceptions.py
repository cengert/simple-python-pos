class NegativerWertFehler(Exception):
    """In diesem Programm sollten negative Werte keine Rolle spielen,
        je nach Anwendungszweck kann es Ausnahmen geben wie Umtauschware und Pfand."""

    def __init__(self, message="Bitte keine negativen Werte verwenden!"):
        super().__init__(message)