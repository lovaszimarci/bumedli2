class Marci():
    def __init__(self, név):
     self.név = név


     def marcipontszamado(self,szam):
        with open('marcipont.txt', 'r') as file:
            intek = file.read()

        kivett_szam = [int(i) for i in intek.split() if i.isdigit()]
        sima_szam = kivett_szam[0]
        osszeadott_szam = sima_szam + szam
        vegleges_szam = str(osszeadott_szam)

        with open('marcipont.txt', 'w') as file:
            file.write(vegleges_szam)
            file.close()
            pass
    def pontok_(self):
        with open('marcipont.txt', 'r') as file:
            pontjaim = file.read()
            print(pontjaim)
            pass




marci = Marci('marci')



