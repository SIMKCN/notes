
import random
import csv
import time
import os.path
import itertools
import os
notes = ['A1', 'A#1', 'B1', 'C1', 'C#1', 'D1', 'D#1', 'E1', 'F1', 'F#1', 'G1', 'G#1', 'A2', 'A#2', 'B2', 'C2', 'C#2', 'D2', 'D#2', 'E2', 'F2', 'F#2', 'G2', 'G#2']

mellist = []
mellist = set(mellist)


def purge():
    os.remove("melody.csv")
def new_set():
    counter = 0
    while True:
        melody1 = random.choices(notes, k=6)
        melody1 = tuple(melody1)
        if melody1 in mellist:
            print("Alert--- ", counter)
            
        elif melody1 not in mellist:
            print("is not in")
            mellist.add(melody1)

            datei = open("melody.csv", "a")

            datei.write("\n" + str(melody1))

            datei.close()
            counter += 1


            sz = os.path.getsize("melody.csv")
            speicher = (sz/1024)/1000
            print("Index:", counter, "Status of list: ", "is not in", "Filesize: ", speicher, "Melody: ", melody1)


        if counter == (1/24) ** 6:
            break
        else:
            continue

while True:
    a = input("::")
    if a == ("!newset"):
        new_set()
    elif a == ("!purge"):
        purge()