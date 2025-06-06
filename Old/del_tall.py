# # Script: del_tall.py
# # Beskrivelse: Viser tre måter å hente ut heltalls- og desimaldel fra et flyttall

# import math  # For metode 2

# # Vi starter med en flyttallsverdi
# a = 30.675

# print("Originalverdi:", a)
# print("-" * 40)

# # 📌 Metode 1: Lagre original verdi i egen variabel
# print("Metode 1: Bruke en ekstra variabel")
# original_value = a
# heltall_1 = int(a)
# desimal_1 = original_value - heltall_1
# print("Heltallsdel:", heltall_1)
# print("Desimaldel: ", desimal_1)
# print("-" * 40)

# # 📌 Metode 2: Bruke math.modf()
# print("Metode 2: Bruke math.modf()")
# desimal_2, heltall_2 = math.modf(a)
# print("Heltallsdel:", int(heltall_2))
# print("Desimaldel: ", desimal_2)
# print("-" * 40)

# # 📌 Metode 3: Egendefinert funksjon
# print("Metode 3: Bruke funksjon")
# def splitt_tall(verdi):
#     heltall = int(verdi)
#     desimal = verdi - heltall
#     return heltall, desimal

# heltall_3, desimal_3 = splitt_tall(a)
# print("Heltallsdel:", heltall_3)
# print("Desimaldel: ", desimal_3)
# print("-" * 40)

# # Ekstra: Vis at a fortsatt er uendret
# print("Flyttallsverdien a er fortsatt:", a, "(float)")