# ==========================================
# Voorbeeld Opdracht
#
# Maak een dictionary genaamd 'fruit' met daarin de sleutels 'appel' en 'banaan'.
# Geef 'appel' de value 'rood' en 'banaan' de value 'geel'.
# Print vervolgens de kleur van de banaan door de naam 'banaan' te gebruiken.
#
# Verwachte uitkomst:  geel
# ==========================================

# dictionary met kleuren als values
fruit = {'appel': 'rood', 'banaan': 'geel'}

# print de kleur van de banaan
print(fruit['banaan'])  # Het resultaat is: geel


# ==========================================
# Opdracht 1:
# Gegeven is de dictionary 'boodschappen' met daarin de keys 'Appels' en 'Brood'.
# Maak de volgende deelopdrachten. Print de uitkomst van elke opdracht om te zien of je het juiste resultaat krijgt.
#
# Opdracht 1a:
# Roep de waarde aan die hoort bij de naam 'Brood'
# Verwachte uitkomst: 2
#
# Opdracht 1b:
# Gebruik de get() methode op de waarde 'Appels' en 'Bananen'. Zorg dat als de naam niet bestaat, de tekst 'Niet gevonden' wordt geprint.
# ==========================================

boodschappen = {'Appels': 6, 'Brood': 2}


# ==========================================
# Opdracht 2:
# Gegeven zijn vier boodschappenlijstjes als dictionary. Je kan een if statement gebruiken en de == operator om te vergelijken.
#
# Opdracht 2a:
# Vergelijk de boodschappenlijstjes van Marie en Raj. Als de lijstjes gelijk zijn, print 'De boodschappenlijstjes zijn gelijk.'.
#
# Opdracht 2b:
# Vergelijk de boodschappenlijstjes (Marie, Raj en Jan). Als de lijstjes gelijk zijn, print 'De boodschappenlijstjes zijn gelijk.'.
# Waarom worden deze lijstjes wel/niet als gelijk beschouwd?
#
# Opdracht 2c:
# Vergelijk nu op dezelfde manier alle lijstjes. Zijn ze gelijk? Waarom wel/niet?
# ==========================================

boodschappenlijst_marie = {'Brood': 1, 'Appels': 6}
boodschappenlijst_raj = {'Brood': 1, 'Appels': 6}
boodschappenlijst_jan = {'Appels': 6, 'Brood': 1}
boodschappenlijst_karel = {'Appels': 6, 'Brood': 25}


# ==========================================
# Opdracht 2:
# De voorraad van meubelwinkel 'Op Eigen Houtje' is als volgt:
# Gegeven is de dictionary 'meubels' met daarin de keys 'banken' en 'stoelen'.
# Maak de volgende deelopdrachten. Print de uitkomst van elke opdracht om te zien of je het juiste resultaat krijgt.
#
# Opdracht 2a:
# Er worden 6 banken verkocht. Pas de waarde van de naam 'banken' aan en print de aangepaste dictionary
# Verwachte uitkomst: {'banken': 4, 'stoelen': 20}

# Opdracht 2b:
# Er komen klachten dat klanten door eerder gekochte stoelen zijn gezakt. De winkel besluit om de stoelen uit het assortiment te halen.
# Verwijder de naam 'stoelen' (en daarmee ook de bijbehorende value) uit de dictionary en print de aangepaste dictionary.
# Verwachte uitkomst: {'banken': 4}

# Opdracht 2c:
# De winkel gaat tafels verkopen en koopt er gelijk 15 in. Voeg de naam 'tafels' toe met een waarde van 15 en print de aangepaste dictionary.
# Verwachte uitkomst: {'banken': 4, 'tafels': 15}
# ==========================================

meubels = {'banken': 10, 'stoelen': 20}


# ==========================================
# Opdracht 3:
# Docent Erik heeft proefwerken van studenten nagekeken en de cijfers in een dictionary opgeslagen.
# Erik komt erachter dat hij een fout heeft gemaakt en moet de cijfers met een factor 1,5 vermenigvuldigen.
# Met als enige uitzondering dat een cijfer nooit hoger mag zijn dan een 10.
# Print de uitkomst om te zien of je het juiste resultaat krijgt.

# Gegeven is de dictionary 'cijfers' met daarin de keys 'Jaap', 'Winnie', 'Jeroen' en 'Lana' en hun cijfers.
# Verwachte uitkomst: {'Jaap': 4.5, 'Winnie': 6.0, 'Jeroen': 10, 'Lana': 10}
# ==========================================

cijfers = {'Jaap': 3, 'Winnie': 4, 'Jeroen': 9, 'Lana': 10}


# ==========================================
# Opdracht 4:
# De eigenaar van dierentuin 'Het Zootje' heeft een lijst met dieren en hun aantallen. De dieren en hun aantallen zijn opgeslagen in een dictionary.
# Maak onderstaande deelopdrachten.
#
# Opdracht 4a:
# De eigenaar wil de dieren op alfabetische volgorde zien. Sorteer de dieren op naam en print de dictionary uit.
# Verwachte uitkomst: {'Aap': 5, 'Giraffe': 2, 'Leeuw': 3, 'Olifant': 4, 'Zebra': 1}
#
# Opdracht 4b:
# Nu wil de eigenaar in een oogopslag wat het hoogste aantal is en het laagste. Sorteer nu de aantallen van hoog naar laag en print de dictionary uit. (De keys hoef je niet te printen)
# ==========================================

dieren = {'Olifant': 5, 'Zebra': 8, 'Aap': 12, 'Giraffe': 3, 'Neushoorn': 7}
