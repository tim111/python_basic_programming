import random

inzet = int(input("Geef jouw inzet:"))

getal1computer1 = random.randint(1,5)
getal1computer2 = random.randint(1,5)
getal1computer3 = random.randint(1,5)


print(f"De 3 willekeurige getallen zijn {getal1computer1} | {getal1computer2} | {getal1computer3}")
if getal1computer1 == getal1computer2 and getal1computer2 == getal1computer3:
    score = 3 * inzet
    print(f"Proficiat, je verdient 3 * jouw inzet namelijk {score} euro.")
elif getal1computer1 == getal1computer2 or getal1computer2 == getal1computer3 or getal1computer1 == getal1computer3:
    score = 2 * inzet
    print(f"Proficiat, je verdient 2 x jouw inzet: {score} euro.")
else:
    score = -inzet
    print(f"Helaas je verliest jouw inzet!")
