from FormBehandler_Prosjekt.former.to_dimensjonell_form import to_dimensjonell_form

class Rektangel(to_dimensjonell_form):
    """
    Et rektangel definert med bredde og høyde.
    """
    def __init__(self, bredde, hoyde):
        super().__init__("Rektangel")
        self.bredde = bredde
        self.hoyde = hoyde

    def areal(self):
        return self.bredde * self.hoyde

    def __str__(self):
        return f"Rektangel | {super().__str__()}"