from FormBehandler_Prosjekt.former.form import Form

class to_dimensjonell_form(Form):
    """
    Represents a 2D shape, inherits from Shape.
    """
    def __str__(self):
        return f"Two-dimensional shape | {super().__str__()}"