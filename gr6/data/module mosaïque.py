#Alexis LECOCQ
from PIL import Image

def appliquer_mosaique(image, taille_pixel):
    img = Image.open(image)
    largeur, hauteur = img.size
    img_mosaique = img.copy()
    for i in range(0, largeur, taille_pixel):
        for j in range(0, hauteur, taille_pixel):
            pixels = [img.getpixel((x, y)) for x in range(i, min(i + taille_pixel, largeur)) for y in range(j, min(j + taille_pixel, hauteur))]
            if pixels:
                couleur_moyenne = tuple(
                    sum(val) // len(pixels) for val in zip(*pixels)
                )
                for x in range(i, min(i + taille_pixel, largeur)):
                    for y in range(j, min(j + taille_pixel, hauteur)):
                        img_mosaique.putpixel((x, y), couleur_moyenne)
    return img_mosaique

image = 'mona.jpg'
taille_pixel = 10

img_mosaique = appliquer_mosaique(image, taille_pixel)
img_mosaique.show()
img_mosaique.save('image_mosaique.jpg')
