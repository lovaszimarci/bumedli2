def pontszam(szam):
    with open('marcipont.txt','r') as file:
        intek = file.read()

    kivett_szam = [int(i) for i in intek.split() if i.isdigit()]
    sima_szam = kivett_szam[0]
    osszeadott_szam = sima_szam + szam
    vegleges_szam = str(osszeadott_szam)

    with open('marcipont.txt', 'w') as file:
        file.write(vegleges_szam)
        file.close()
        pass

pontszam(10)

# lepesek: 1 beolvassa a txt
# 2 egy for loopal kiszedi egy listaba a szamjegyeket
# 3 a kiszedet szamjegyet atteszi a listabol egy sima int varieableba
# 4 az int variablet es def ben megadott numot ossze adja
# a vegleges_szam pedig at konvertalja az ossze adott intet strbe mert csak azt tudja writeolni
# a vegleges szammra kicserelni a txtben az alap szamot es bezarul