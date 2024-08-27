#STAP 1 vraag naar DNA-sequentie
dna_sequentie = \
input("Geef DNA-sequentie(enkel A, C, G of T gebruiken:\n")

#STAP 2: definieer teller en stel alles op 0
a_aantal = 0; c_aantal = 0; g_aantal = 0; t_aantal = 0

#STAP 3: doorloop DNA-sequentie en verhoog juiste tellers
for base in dna_sequentie:
    if base == "A":
        a_aantal +=1
    elif base == "C":
        c_aantal +=1
    elif base == "G":
        g_aantal +=1
    elif base == "T":
        t_aantal +=1
    else:
        print(base, "is niet toegelaten!")

#STAP4: toon de aantallen
print("Aantal A:", a_aantal)
print("Aantal C:", c_aantal)
print("Aantal G:", g_aantal)
print("Aantal T:", t_aantal)

print("Programme stopt")

