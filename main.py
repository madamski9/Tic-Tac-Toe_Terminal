import keyboard
import time
import os

def drukuj_plansze():
    os.system('clear') 
    plansza = [[" " * 20 for _ in range(3)] for _ in range(3)]
    sciana = [ " | " for _ in range(7) ]
    poziom = [ "-" for _ in range(66) ]
    for i, row in enumerate(plansza):
        for linia in sciana:
            print(linia.join(row))
        if i < 2:
            print("".join(poziom))
drukuj_plansze()
def on_key_event(event):
    if event.event_type == keyboard.KEY_DOWN:
        if event.name == "right":
            print("Naciśnięto strzałkę w prawo")
        else:
            print(f"Naciśnięto klawisz: {event.name}")

keyboard.hook(on_key_event)

while True:
    time.sleep(0.1)

        