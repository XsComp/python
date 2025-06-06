# GenerateLetter.py


def generer_bokstav():
    bokstaver = ["a", "b", "c", "d", "e"]
    indeks = 0
    while True:
        yield bokstaver[indeks]
        indeks = (indeks + 1) % len(bokstaver)

# Vi tester at det funker
if __name__ == "__main__":
    bokstav_gen = generer_bokstav()
    for _ in range(10):                             # Vi skriver ut a til e to ganger
        print(next(bokstav_gen), end=" ")
