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
print(boodschappen['Brood'])

print(boodschappen.get('Appels', 'Niet gevonden'))
print(boodschappen.get('Bananen', 'Niet gevonden'))

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

if boodschappenlijst_marie == boodschappenlijst_raj :
    print('De boodschappenlijstjes zijn gelijk.')
else :
    print('De boodschappenlijstjes zijn niet gelijk.')

if boodschappenlijst_marie == boodschappenlijst_raj == boodschappenlijst_jan :
    print('De boodschappenlijstjes zijn gelijk.')
else :
    print('De boodschappenlijstjes zijn niet gelijk.')

# Ze worden als gelijk gezien bij 2B omdat de volgorde van de key-value pairs niet uitmaakt, maar ze wel gelijk zijn.

if boodschappenlijst_marie == boodschappenlijst_raj == boodschappenlijst_jan == boodschappenlijst_karel:
    print('De boodschappenlijstjes zijn gelijk.')
else :
    print('De boodschappenlijstjes zijn niet gelijk.')

# Ze worden niet als gelijk gezien omdat de key-value pairs niet gelijk zijn

# ==========================================
# Opdracht 3:
# De voorraad van meubelwinkel 'Op Eigen Houtje' is als volgt:
# Gegeven is de dictionary 'meubels' met daarin de keys 'banken' en 'stoelen'.
# Maak de volgende deelopdrachten. Print de uitkomst van elke opdracht om te zien of je het juiste resultaat krijgt.
#
# Opdracht 3a:
# Er worden 6 banken verkocht. Pas de waarde van de naam 'banken' aan en print de aangepaste dictionary
# Verwachte uitkomst: {'banken': 4, 'stoelen': 20}

# Opdracht 3b:
# Er komen klachten dat klanten door eerder gekochte stoelen zijn gezakt. De winkel besluit om de stoelen uit het assortiment te halen.
# Verwijder de naam 'stoelen' (en daarmee ook de bijbehorende value) uit de dictionary en print de aangepaste dictionary.
# Verwachte uitkomst: {'banken': 4}

# Opdracht 3c:
# De winkel gaat tafels verkopen en koopt er gelijk 15 in. Voeg de naam 'tafels' toe met een waarde van 15 en print de aangepaste dictionary.
# Verwachte uitkomst: {'banken': 4, 'tafels': 15}
# ==========================================

meubels = {'banken': 10, 'stoelen': 20}
#3a
meubels['banken'] = 4 #andere optie is: meubels['banken'] -= 6
print(meubels)

#3b
del meubels['stoelen']
print(meubels)

#3c
meubels.update(tafels = 15) #andere optie is: meubels['tafels'] = 15
print(meubels)
# ==========================================
# Opdracht 4:
# Docent Erik heeft proefwerken van studenten nagekeken en de cijfers in een dictionary opgeslagen.
# Erik komt erachter dat hij een fout heeft gemaakt en moet de cijfers met een factor 1,5 vermenigvuldigen.
# Met als enige uitzondering dat een cijfer nooit hoger mag zijn dan een 10.
# Print de uitkomst om te zien of je het juiste resultaat krijgt.

# Gegeven is de dictionary 'cijfers' met daarin de keys 'Jaap', 'Winnie', 'Jeroen' en 'Lana' en hun cijfers.
# Verwachte uitkomst: {'Jaap': 4.5, 'Winnie': 6.0, 'Jeroen': 10, 'Lana': 10}
# ==========================================

cijfers = {'Jaap': 3, 'Winnie': 4, 'Jeroen': 9, 'Lana': 10}

for naam, resultaat in cijfers.items():
    if resultaat * 1.5 >= 10:
        cijfers[naam] = 10
    else:
        cijfers[naam] = resultaat * 1.5

print(cijfers)

# ==========================================
# Opdracht 5:
# De eigenaar van dierentuin 'Het Zootje' heeft een lijst met dieren en hun aantallen. De dieren en hun aantallen zijn opgeslagen in een dictionary.
# Maak onderstaande deelopdrachten.
#
# Opdracht 5a:
# De eigenaar wil de dieren op alfabetische volgorde zien. Sorteer de dieren op naam en print de dictionary uit.
# Verwachte uitkomst: {'Aap': 5, 'Giraffe': 2, 'Leeuw': 3, 'Olifant': 4, 'Zebra': 1}
#
# Opdracht 5b:
# Nu wil de eigenaar in een oogopslag wat het hoogste aantal is en het laagste. Sorteer nu de aantallen van hoog naar laag en print de dictionary uit. (De keys hoef je niet te printen)
# ==========================================

dieren = {'Olifant': 5, 'Zebra': 8, 'Aap': 12, 'Giraffe': 3, 'Neushoorn': 7}

# alleen de gesorteerde namen printen, de dictionary blijft ongewijzigd:
for naam in sorted(dieren.keys()):
    print(naam, end=' ')
print()

# dieren = dict(sorted(dieren.items())) --> dit maakt een gesorteerde dictionary met key-value pairs
#NB: niet dieren = sorted(dieren) doen. Daarmee maak je van de dictionary
# een gesorteerde lijst met enkel de keys (dieren = ['Aap', 'Giraffe', 'Neushoorn', 'Olifant', 'Zebra']
# als je enkel de keys in volgorde wil printen:
# for naam in sorted(dieren.keys()):
#     print(naam, end=' ')

for aantal in sorted(dieren.values()):
    print(aantal, end=' ')
print()
# als je ook de namen erbij wilt, moet je een kleine functie gebruiken.
# met een for loop kan je door de dictionary items gaan. Je krijgt een tijdelijke view van de key-value pairs, waar je door kan itereren.
# sorted neemt het iterabele key-value pair en maakt er een lijst met twee tuples van: nu heb je dus een index die je kunt gebruiken.
# doordat je met lambda aanwijst dat sorted moet sorteren op de tweede index (plek 1). Met de for loop pak je elke tuple afzonderlijk als naam en aantal.
# met key=lambda item: item[1] geef je sorted een tijdelijke anonieme functie mee. Je maakt gebruik van de optionele key parameter van sorted().
# het tweede item van de tuple (index 1) maakt je de key waarop gesorteerd moet worden.

for naam, aantal in sorted(dieren.items(), key= lambda item: item[1]):
    print(naam, '-->', aantal, end=' / ')