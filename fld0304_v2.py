nevek:list[str] = []

for _ in range(10):
    nev:str = input('írj be egy nevet: ')
    if nev == '': break
    else: nevek.append(nev)

nevek.sort()
for nev in nevek:
    print(f'\t{nev}')