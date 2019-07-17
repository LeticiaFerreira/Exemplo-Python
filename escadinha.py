degraus = int(input("Quantos degraus tem a escada"))
material = input("Qual o material da escada")
a = "@"
i = 0

while (i < degraus):
    print(material)
    material = a + material
    i=i+1