from PIL import Image

image = Image.open("VACHE.jpg")

largeur, hauteur = image.size

choix = int(input("Combien de quart de tour (1, 2 ou 3) : "))

if choix == 1:
    image_tournee = Image.new("RGB", (hauteur, largeur))
    for x in range(largeur):
        for y in range(hauteur):
            pixel = image.getpixel((x, y))
            image_tournee.putpixel((hauteur - 1 - y, x), pixel)

    
elif choix == 2:
    image_tournee = Image.new("RGB", (largeur, hauteur))
    for x in range(largeur):
        for y in range(hauteur):
            pixel = image.getpixel((x, y))
            image_tournee.putpixel((largeur - 1 - x, hauteur - 1 - y), pixel)


elif choix == 3:
    image_tournee = Image.new("RGB", (hauteur, largeur))
    for x in range(largeur):
        for y in range(hauteur):
            pixel = image.getpixel((x, y))
            image_tournee.putpixel((y, largeur - 1 - x), pixel)

elif choix < 1 or choix > 3:
    print('Erreur sur le nombre de quart de tour !')

image_tournee.save("image_tournee.jpg")
image_tournee.show()
print("L'image a été tournée et enregistrée sous le nom 'image_tournee.jpg' !")


