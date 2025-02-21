**Blackjack** of **21'en** is een <a href="https://nl.wikipedia.org/wiki/Eenentwintigen" target="_blank">populair kaartspel</a> waarbij de speler telkens een kaart kan vragen. Hoe dichter de speler bij het getal 21 komt, hoe beter. Komt de speler boven 21 uit, dan verliest deze zijn inzet.

![Blackjack, speel het juist!](media/blackjack.gif "Blackjack, speel het juist!"){:data-caption="Blackjack, speel het juist!" width="300px"}

## Opgave

Schrijf een programma dat de gebruiker **twee** willekeurige kaarten van 1 tot en met 10 geeft. Toon deze kaarten op het scherm.

* Het programma vraagt nu telkens of de gebruiker nog kaarten wil; 
* Dit doet het programma totdat de gebruiker geen kaarten meer wil **of** totdat de som van alle kaarten groter wordt dan 21;

Als de som:
* gelijk is aan 19 dan wint de gebruiker € 2;
* gelijk is aan 20 dan wint de gebruiker € 5;
* gelijk is aan 21 dan wint de gebruiker € 10;
* groter is dan 21 of te vroeg gestopt dan verliest de gebruiker!

#### Voorbeeld1
Stel bijvoorbeeld dat de gebruiker de willekeurige kaarten `5` en `6` kreeg.

```
Je kreeg kaarten 5 en 6
```

Op de vraag of de gebruiker nog een kaart wilt, antwoord deze `ja`. Vervolgens verschijnt er:

```
Wil je nog een kaart? ja
De nieuwe kaart is: 3
De som bedraagt nu: 14
```

De gebruik antwoordt opnieuw `ja` op een nieuw kaart, er verschijnt:

```
Wil je nog een kaart? ja
De nieuwe kaart is: 10
De som bedraagt nu: 24
Je verliest!
```#### Voorbeeld1
Stel bijvoorbeeld dat de gebruiker de willekeurige kaarten `5` en `6` kreeg.

```
Je kreeg kaarten 5 en 6
```

Op de vraag of de gebruiker nog een kaart wilt, antwoord deze `ja`. Vervolgens verschijnt er:

```
Wil je nog een kaart? ja
De nieuwe kaart is: 3
De som bedraagt nu: 14
```

De gebruik antwoordt opnieuw `ja` op een nieuw kaart, er verschijnt:

```
Wil je nog een kaart? ja
De nieuwe kaart is: 10
De som bedraagt nu: 24
Je verliest!

#### Voorbeeld2
Stel bijvoorbeeld dat de gebruiker de willekeurige kaarten `5` en `6` kreeg.

```
Je kreeg kaarten 6 en 6
```

Op de vraag of de gebruiker nog een kaart wilt, antwoord deze `ja`. Vervolgens verschijnt er:

```
Wil je nog een kaart? ja
De nieuwe kaart is: 6
De som bedraagt nu: 18
```

De gebruik antwoordt opnieuw `ja` op een nieuw kaart, er verschijnt:

```
Wil je nog een kaart? ja
De nieuwe kaart is: 3
De som bedraagt nu: 21
Je wint 10 euro!
