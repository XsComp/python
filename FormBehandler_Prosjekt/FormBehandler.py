from FormBehandler_Prosjekt.former.firkant import Firkant
from FormBehandler_Prosjekt.former.rektangel import Rektangel
from FormBehandler_Prosjekt.former.kube import Kube
from FormBehandler_Prosjekt.former.boks import Boks

if __name__ == "__main__":
    former = [
        Firkant(5),
        Rektangel(4, 6),
        Kube(3),
        Boks(2, 4, 6)
    ]

    for former in former:
        print(former)

    print("\nTotallt antall former laget:", Firkant.count())


'''

Denne må kjøres fra din "working folder" med kommandoen:

python3 -m FormBehandler_Prosjekt.FormBehandler

Firkant | Two-dimensional shape | Beskrivelse: Firkant, Areal: 25, Volum: 0
Rektangel | Two-dimensional shape | Beskrivelse: Rektangel, Areal: 24, Volum: 0
Kube | Tre-dimensjonell form | Beskrivelse: Kube, Areal: 54, Volum: 27
Boks | Tre-dimensjonell form | Beskrivelse: Boks, Areal: 88, Volum: 48

Totallt antall former laget: 4

'''