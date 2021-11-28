class Marci():
   pontszam = 0

   @classmethod
   def update(cls, value):
       cls.pontszam += value

   def __init__(self, value):
       self.value = value
       self.update(value)

marci = Marci(0)

Marci.update(5)
Marci.update(6)

print(Marci.pontszam)

