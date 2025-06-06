from FormBehandler_Prosjekt.former.form import Form

class tre_dimensjonell_form(Form):
    """
    Representerer en 3-dimensjonell form, arver fra Shape.
    """
    def __str__(self):
        return f"Tre-dimensjonell form | {super().__str__()}"