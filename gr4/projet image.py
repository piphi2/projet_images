#On importe les modules exterieur:
from PIL import Image
from random import random

#fonction qui modifiant une image donnée a partir d'un filtre
def filtre(image,filtre):
    img=Image.open(image)
    print(img.size)
    for i in range (img.size[0]):
        for j in range (img.size[1]):
            (r,v,b)=img.getpixel((i, j))
            r1=int(r*filtre[0][0]+v*filtre[0][1]+b*filtre[0][2])
            v1=int(r*filtre[1][0]+v*filtre[1][1]+b*filtre[1][2])
            b1=int(r*filtre[2][0]+v*filtre[2][1]+b*filtre[2][2])
            img.putpixel((i,j),((r1,v1,b1)))
    img.show()


#Programme principal:Banque de filtre sous forme de matrice de coefficient
niveau_de_gris=[[0.2126,0.7152,0.0722],[0.2126,0.7152,0.0722],[0.2126,0.7152,0.0722]]
sepia=[[0.393,0.769,0.189],[0.349,0.686,0.168],[0.272,0.534,0.131]]
normal=[[1,0,0],[0,1,0],[0,0,1]]
rouge=[[1,0,0],[0,0,0],[0,0,0]]
bleu=[[0,0,0,],[0,0,0],[0,0,1]]
cuba=[[1,0,0],[0,1,0],[0,0,0,]]
eclaircir=[[1.5,0,0],[0,1.5,0],[0,0,1.5]]
assombrir=[[0.5,0,0],[0,0.5,0],[0,0,0.5]]
negatif=[[0,1,1],[1,0,1],[1,1,0]]
random=[[random() for i in range (3)]for j in range (3)]

filtre("./data/Arbre.jfif",random)