from FormBehandler_Prosjekt.former.to_dimensjonell_form import to_dimensjonell_form

class Firkant(to_dimensjonell_form):
    """
    En firkant med like sider.
    """
    def __init__(self, side):
        super().__init__("Firkant")
        self.side = side

    def areal(self):
        return self.side ** 2

    def __str__(self):
        return f"Firkant | {super().__str__()}"