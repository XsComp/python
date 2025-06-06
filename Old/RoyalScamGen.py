#RoyalScamGen.py

# Vi genererer en (litt for mistenkelig) e-post fra en "prins"

# Trinn 1 – Vi lager malen med plassholdere
mal = (
    "Kjære {tittel} {etternavn},\n\n"
    "Mitt navn er {prinsenavn}, og jeg er den {rolle} i {land}. "
    "Jeg skriver til deg med en spesiell mulighet som gjelder en utestående arv på hele {beløp}.\n\n"
    "Alt jeg trenger fra deg er din {nøkkelinfo} for å overføre pengene.\n"
    "Dette haster. Vennligst svar innen {dager} dager.\n\n"
    "Med vennlig hilsen,\n"
    "Prins {prinsenavn}"
)

# Trinn 2 – Vi ber brukeren fylle ut hullene i den mistenkelige meldingen
tittel = input("Tittel (f.eks. Hr., Fr., Dr.): ")
etternavn = input("Etternavn: ")
prinsenavn = input("Navnet på prinsen: ")
rolle = input("Rolle (f.eks. arving, skatteansvarlig): ")
land = input("Land: ")
beløp = input("Beløp (f.eks. 14 millioner euro): ")
nøkkelinfo = input("Hva trenger du fra offeret? (f.eks. bankinfo): ")
dager = input("Antall dager til svarfrist: ")

# Trinn 3 – Vi fyller inn plassholderne med brukerens input
fiksferdig_epost = mal.format(
    tittel=tittel,
    etternavn=etternavn,
    prinsenavn=prinsenavn,
    rolle=rolle,
    land=land,
    beløp=beløp,
    nøkkelinfo=nøkkelinfo,
    dager=dager
)

# Trinn 4 – Vi skriver ut det (mistenkelig) ferdige resultatet
print("\n📨 Her er e-posten som ble generert:\n")
print(fiksferdig_epost)