def pontszamiro(pont):
    with open('marcipont.txt', 'w') as file:
        file.write(pont)
        file.close()
        pass

def pontszamolvaso():
    with open('marcipont.txt', 'r') as file:
        return file.read()


pontszamiro(22)
print(pontszamolvaso())

# itt az a gond hogy ez csak at irja nem pedig osszeadja oket
# de a write es a read def alapja mar megvan


# read from file --> aztan egy varieblehez hozza adni egy szamot --> osszeadni aztan writeolni a filet miutan string 