# mymodules.py

import time                                 # For håndtering av tid
import random                               # For generering av tilfeldige tall

def create_time():
    return time.time()                      # Returnerer nåværende tidspunkt (epoch time)

def output_local_time(time_obj):
    lokal_tid = time.ctime(time_obj)        # Konverterer epoch time til lokal tid som streng
    print(f"Lokal tid: {lokal_tid}")

def calculate_difference(start, end):
    return end - start                      # Returnerer forskjellen i sekunder mellom to tidspunkt

def generate_random(max_tall):
    return random.randint(0, max_tall)      # Returnerer et tilfeldig heltall mellom 0 og max_tall (inkludert)