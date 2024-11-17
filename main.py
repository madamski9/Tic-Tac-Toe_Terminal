import keyboard
import time
import os

# Inicjalizacja planszy
plansza = [[" " for _ in range(3)] for _ in range(3)]

# Wzory dla X i O
x_wzor = [
    "#@         @# ",
    "  @\     %$   ",
    "     #%#      ",
    "  %/     \$   ",
    "$#         %$ "
]
o_wzor = [
    "  /$#%#@$%@\  ",
    " #?        %$ ",
    "$#          ?@",
    " #%        $# ",
    "  \%#$@#%#@/  "
]

def drukuj_plansze(gracz):
    os.system('clear')
    sciana = " | "
    poziom = "-" * 66
    leftPadding = " " * 45
    topPadding = "\n" * 10

    print(topPadding, end="")
    print(" "*72 + f"RUCH: {gracz}")
    print("Nacisnij q zeby wyjsc\nNaciskaj odpowiednio:\n1 |2 |3 \n4 |5 |6 \n7 |8 |9 ")
    for i, row in enumerate(plansza):
        for j in range(5):  
            print(leftPadding + sciana.join([f"   {cell[j]}   " if isinstance(cell, list) else f" {cell} " + " " * 17 for cell in row]))
        if i < 2:
            print(leftPadding + poziom)

def aktualizuj_plansze(x, y, wzor):
    if plansza[x][y] == " ":
        plansza[x][y] = wzor

drukuj_plansze("GRACZ 1")

def key_engine(gracz):
    event = keyboard.read_event()
    if gracz % 2 == 0:
        wzor = x_wzor
    else:
        wzor = o_wzor
    if event.scan_code == 18:
        aktualizuj_plansze(0, 0, wzor)
    elif event.scan_code== 19:
        aktualizuj_plansze(0, 1, wzor)
    elif event.scan_code == 20:
        aktualizuj_plansze(0, 2, wzor)
    elif event.scan_code == 21:
        aktualizuj_plansze(1, 0, wzor)
    elif event.scan_code == 23:
        aktualizuj_plansze(1, 1, wzor)
    elif event.scan_code == 22:
        aktualizuj_plansze(1, 2, wzor)
    elif event.scan_code == 26:
        aktualizuj_plansze(2, 0, wzor)
    elif event.scan_code == 28:
        aktualizuj_plansze(2, 1, wzor)
    elif event.scan_code == 25:
        aktualizuj_plansze(2, 2, wzor)
    drukuj_plansze("GRACZ 1" if gracz % 2 != 0 else "GRACZ 2")

def test():
    event = keyboard.read_event()
    if event:
        print(event.name)

ktory_gracz = 0
while True:
    event = keyboard.read_event()
    if event.scan_code == 12:
        break
    if event.event_type == keyboard.KEY_DOWN:
        key_engine(ktory_gracz)
        print(ktory_gracz)
        ktory_gracz += 1
    time.sleep(0.1)