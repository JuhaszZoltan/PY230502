from random import randint, seed

# seed(1986)

szamok:list[int] = []

for _ in range(20):
    szam:int = randint(50, 150)
    szamok.append(szam)

szamok.sort()

for n in szamok:
    print(n, end=' ')
print(end='\n')

osszeg:int = sum(szamok)
print(f'lista elemeinek összege: {osszeg}')

atlag:float = osszeg / len(szamok)
print(f'lista elemeinek átlaga: {atlag}')

szamlalo:int = 0
for n in szamok:
    if n % 10 == 0:
        szamlalo += 1
print(f'a listában a 0-ra végződő elemek száma: {szamlalo}')

osszeg:int = 0
for n in szamok:
    osszeg += n
print(f'elemek összege, csak progtétellel: {osszeg}')

szamlalo:int = 0
for n in szamok:
    if n > atlag:
        szamlalo += 1
print(f'átlagnál nagypobb elemek száma: {szamlalo}')

szamlalo:int = 0
for n in szamok:
    if n >= 60 and n < 70:
        szamlalo += 1
print(f'6-ossal kezdődő elemek száma: {szamlalo}')

# általánosan: "megszámlálás tétele":
# számláló:int = 0
# for <elem> in <lista>:
#   if <feltétel az elemre vonatkozóan>:
#       számláló += 1