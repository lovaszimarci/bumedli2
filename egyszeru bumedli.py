with open('marcipont.txt','r') as file:
    intek = file.read()

kivett_szam = [int(i) for i in intek.split() if i.isdigit()]
sima_szam = kivett_szam[0]
osszeadott_szam = sima_szam + 3
vegleges_szam = str(osszeadott_szam)

with open('marcipont.txt', 'w') as file:
    file.write(vegleges_szam)
    file.close()


# def pontszam(pont):
#     with open('marcipont.txt', 'r') as file:
#         alapszam = file.read()
#         fil
#
#         total = sum(alapszam.split(',') + list((pont)))
#         print(total)
#     #     pass
#     # file2 = int(alapszam) + int(pont)
#     # with open('marcipont.txt', 'w') as file:
#     #     file.write(str(file2))
#     #     return file.read()
#
# pontszam(2)
#
# # itt az a gond hogy ez csak at irja nem pedig osszeadja oket
# # de a write es a read def alapja mar megvan
#
#
# # read from file --> aztan egy varieblehez hozza adni egy szamot --> osszeadni aztan writeolni a filet miutan string