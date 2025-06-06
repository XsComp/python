# rektangel_modul.py

class Rektangel:
    def __init__(self, lengde, bredde, vis_karakter):
        self.lengde = lengde                  # Instansvariabel for lengde – målt i tegn
        self.bredde = bredde                  # Instansvariabel for bredde – også i tegn
        self.vis_karakter = vis_karakter      # Hvilket tegn skal brukes til å "tegne" rektangelet

    def kalkuler_område(self):
        return self.lengde * self.bredde      # Standard formel for areal (lengde * bredde)

    def display(self):
        # Skriver ut informasjon om rektangelet
        print(f"Lengde: {self.lengde}, Bredde: {self.bredde}, Areal: {self.kalkuler_område()}")
        
        # Tegner rektangelet linje for linje med valgt tegn
        for _ in range(self.bredde):
            print(self.vis_karakter * self.lengde)  # Én linje av rektangelet