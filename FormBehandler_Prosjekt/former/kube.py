from FormBehandler_Prosjekt.former.tre_dimensjonell_form import tre_dimensjonell_form

class Kube(tre_dimensjonell_form):
    """
    En kube med alle sider like lange.
    """
    def __init__(self, side):
        super().__init__("Kube")
        self.side = side

    def areal(self):
        return 6 * (self.side ** 2)

    def volum(self):
        return self.side ** 3

    def __str__(self):
        return f"Kube | {super().__str__()}"