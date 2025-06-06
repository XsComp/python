class Form:
    """
    Base klasse for alle former.
    Holder følge med hvor mange former laget.
    Gir oss standard areal og volum metoder.
    """
    _count = 0

    def __init__(self, beskrivelse="Generisk Form"):
        self.beskrivelse = beskrivelse
        Form._count += 1

    def areal(self):
        return 0

    def volum(self):
        return 0

    def __str__(self):
        return f"Beskrivelse: {self.beskrivelse}, Areal: {self.areal()}, Volum: {self.volum()}"

    @classmethod
    def count(cls):
        return cls._count