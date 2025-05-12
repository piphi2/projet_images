from PIL import Image

def retourner(image, choix):
    largeur, hauteur = image.size

    if choix == 1:
        image_tournee = Image.new("RGB", (hauteur, largeur))
        for x in range(largeur):
            for y in range(hauteur):
                pixel = image.getpixel((x, y))
                image_tournee.putpixel((hauteur - 1 - y, x), pixel)
        return image_tournee

    elif choix == 2:
        image_tournee = Image.new("RGB", (largeur, hauteur))
        for x in range(largeur):
            for y in range(hauteur):
                pixel = image.getpixel((x, y))
                image_tournee.putpixel((largeur - 1 - x, hauteur - 1 - y), pixel)
        return image_tournee

    elif choix == 3:
        image_tournee = Image.new("RGB", (hauteur, largeur))
        for x in range(largeur):
            for y in range(hauteur):
                pixel = image.getpixel((x, y))
                image_tournee.putpixel((y, largeur - 1 - x), pixel)
        return image_tournee

    else:
        return None

image = Image.open("VACHE.jpg")

image_tournee = retourner(image, choix)

if image_tournee:
    image_tournee.save("image_tournee.jpg")
    image_tournee.show()
    print("L'image a été tournée et enregistrée sous le nom 'image_tournee.jpg' !")
else:
    print("Erreur sur le nombre de quart de tour !")