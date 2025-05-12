from PIL import Image #A partir de la librairie PIL on importe le module Image

image = Image.open("NYC.jpg") #On importe l'image
largeur, hauteur = image.size #On crée un tuple contenant les composantes largeur hauteur

def reduire_image(image, f_reduction):
    """Création d'une nouvelle image réduite"""
    nouvelle_largeur = largeur // f_reduction
    nouvelle_hauteur = hauteur // f_reduction
    nouvelle_image = Image.new("RGB", (nouvelle_largeur, nouvelle_hauteur))

    for y in range(0,hauteur,f_reduction):
        for x in range(0,largeur,f_reduction):
            pixel = image.getpixel((x,y))
            nouvelle_image.putpixel((x//f_reduction, y//f_reduction), pixel)

    nouvelle_image.save("img_reduite.jpg") #sauvegarde

reduire_image(image, 3) 