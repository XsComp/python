from FormBehandler_Prosjekt.former.tre_dimensjonell_form import tre_dimensjonell_form

class Boks(tre_dimensjonell_form):
    """
    En boks med bredde, høyde, og dybde.
    """
    def __init__(self, bredde, hoyde, dybde):
        super().__init__("Boks")
        self.bredde = bredde
        self.hoyde = hoyde
        self.dybde = dybde

    def areal(self):
        return 2 * (self.bredde * self.hoyde + self.bredde * self.dybde + self.hoyde * self.dybde)

    def volum(self):
        return self.bredde * self.hoyde * self.dybde

    def __str__(self):
        return f"Boks | {super().__str__()}"