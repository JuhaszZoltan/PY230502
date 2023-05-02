# "végjelig" történő adatbekérés

nevek:list[str] = []

beirt_nev = '-'
while len(nevek) < 10 and beirt_nev != '':
    beirt_nev = input('írj be egy nevet: ')
    if beirt_nev != '': nevek.append(beirt_nev)

nevek.sort()

for nev in nevek:
    print(nev, end=' ')
