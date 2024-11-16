import keyboard
import time
import os

plansza = [['                    ' for _ in range(3)] for _ in range(3)]

def drukuj_plansze():
    os.system('clear') 
    sciana = [
        " | ", " | ", " | ", " | ", " | ", " | ", " | ", " | "
    ]
    for i, row in enumerate(plansza):
        for linia in sciana:
            print(linia.join(row))
        if i < 2:
            print('------------------------------------------------------------------')
drukuj_plansze()
while True:
    key = keyboard.read_key()
    if key == 12:
        print("nacisnales q")
        break
    time.sleep(0.1)
        