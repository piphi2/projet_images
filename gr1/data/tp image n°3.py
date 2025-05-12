# Créé par lbrule1, le 06/05/2025 en Python 3.7
from PIL import Image

#charger les 2 images
image1 = Image.open("raspberry.png")
image2 = Image.open("python.png")

# créer une nouvelle image vide
largeur,hauteur = image1.size
image_resultat=Image.new("RGB",(largeur,hauteur))

# Copier la moitié gauche de image1
for x in range(largeur // 2):
    for y in range(hauteur):
        pixel = image1.getpixel((x, y))
        image_resultat.putpixel((x, y), pixel)

# Copier la moitié droite de image2
for x in range(largeur // 2, largeur):
    for y in range(hauteur):
        pixel = image2.getpixel((x, y))
        image_resultat.putpixel((x, y), pixel)


#sauvegarde + afficher
image_resultat.save("image_fusion3.png")
image_resultat.show()


