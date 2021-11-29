from _typeshed import Self


class Bumedli(Self):



    def marcipontszamado(szam):
        with open('marcipont.txt','r') as file:
            intek = file.read()
            file.close()

    kivett_szam = [int(i) for i in intek.split() if i.isdigit()]
    sima_szam = kivett_szam[0]
    osszeadott_szam = sima_szam + szam
    vegleges_szam = str(osszeadott_szam)

    with open('marcipont.txt', 'w') as file:
        file.write(vegleges_szam)
        file.close()
        pass

def zozipontszamado(self, szam):
    with open('zozipont.txt','r') as file:
        intek = file.read()

    kivett_szam = [int(i) for i in intek.split() if i.isdigit()]
    sima_szam = kivett_szam[0]
    osszeadott_szam = sima_szam + szam
    vegleges_szam = str(osszeadott_szam)

    with open('zozipont.txt', 'w') as file:
        file.write(vegleges_szam)
        file.close()
        pass

def marcipontok(self):
    with open('marcipont.txt', 'r') as file:
        pontok = file.read()
        file.close()
    print(f"Márton pontjai: {pontok}")
    pass

def zozipontok(self):
    with open('zozipont.txt', 'r') as file:
        pontok = file.read()
        file.close()
    print(f'Zoltán pontjai: {pontok}')
    pass

marci = Bumedli()
zozi = Bumedli()

print(zozi.zozipontok())

