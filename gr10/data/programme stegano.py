from PIL import Image
from glob import glob

fichiers_dispo = glob("*.png")

#Fonction étape 1
def preparer_receptacle(nom_du_fichier):
    ''' Met à 0 les 4 LSB de chaque nuance de chaque pixel de l'image.
    Argument :
    - nom_du_fichier (str) : nom du fichier image avec extension .png.
    
    Renvoie :
    - image (PIL.PngImagePlugin.PngImageFile) : fichier image exploitable par chiffrer().
    
    '''
    image = Image.open(nom_du_fichier)
    resolution = image.size
    
    for h in range(resolution[1]):
        for w in range(resolution[0]):
            r = image.getpixel((w,h))[0] - image.getpixel((w,h))[0]%16
            g = image.getpixel((w,h))[1] - image.getpixel((w,h))[1]%16
            b = image.getpixel((w,h))[2] - image.getpixel((w,h))[2]%16
            
            image.putpixel((w,h),(r,g,b))
    
    return image


def chiffrer(nom_receptacle,nom_image_a_cacher,save=False):
    ''' Cache une image à cacher dans une image servant de réceptacle de même résolution et l'affiche (et sauvegarde si save == True).
    Arguments :
    - nom_receptacle (str) : nom avec .png de l'image réceptacle où vont être ajoutés les 4 LSB de l'image à cacher pour chaque couleur primaire
    de chaque pixel. Le réceptacle est modifié et on utilise .show() voire .save() sur cette variable.
    - nom_image_a_cacher (str) : nom avec .png de l'image allant être cachée dans l'image réceptacle.
    - save (bool) : renseigne si l'image doit être sauvegardée (mis par défaut à False).
    
    Renvoie :
    - None (NoneType)
    '''
    receptacle = preparer_receptacle(nom_receptacle) #Etape 1
    image_a_cacher = Image.open(nom_image_a_cacher)
    resolution_image_a_cacher = image_a_cacher.size 
    
    
    
    for h in range(resolution_image_a_cacher[1]):
        for w in range(resolution_image_a_cacher[0]):
            
            #Etape 2
            r = image_a_cacher.getpixel((w,h))[0] - image_a_cacher.getpixel((w,h))[0]%16
            g = image_a_cacher.getpixel((w,h))[1] - image_a_cacher.getpixel((w,h))[1]%16
            b = image_a_cacher.getpixel((w,h))[2] - image_a_cacher.getpixel((w,h))[2]%16
            
            #Etape 3
            receptacle.putpixel((w,h),(receptacle.getpixel((w,h))[0]+r//16,receptacle.getpixel((w,h))[1]+g//16,receptacle.getpixel((w,h))[2]+b//16)) # Ajout des 4 MSB de chaque couleur de chaque pixel de l'image à cacher  transformés en LSB aux 4 MSB de l'image réceptacle
    
    if save:
        receptacle.save(f"{nom_receptacle[:-4]} avec {nom_image_a_cacher[:-4]} caché.png")
    
    receptacle.show("Image chiffrée")


def dechiffrer(nom_image_chiffree,save=False):
    '''Déchiffre une image chiffrée grâce à chiffre et affiche l'image réceptacle et l'image cachée (inverse de la fonction précédente).
    Arguments :
    - nom_image_chiffree (str) : nom du fichier image avec extension .png contenant un récptacle et une image cachée grâce à la
    méthode utilisée par chiffrer().
    - save (bool) : renseigne si l'image doit être sauvegardée (mis par défaut à False).
    
    Renvoie :
    - None (NoneType)
    '''
    image_chiffree = Image.open(nom_image_chiffree)
    resolution_image_chiffree = image_chiffree.size
    image_dechiffree = Image.new("RGB", (resolution_image_chiffree[0],resolution_image_chiffree[1]))
    
    for h in range(resolution_image_chiffree[1]):
        for w in range(resolution_image_chiffree[0]):
            LSB_r = image_chiffree.getpixel((w,h))[0]%16
            LSB_g = image_chiffree.getpixel((w,h))[1]%16
            LSB_b = image_chiffree.getpixel((w,h))[2]%16
            
            image_dechiffree.putpixel((w,h),(LSB_r*16,LSB_g*16,LSB_b*16))
            
    if save:
        image_dechiffree.save("Image déchiffrée.png")
        
    image_dechiffree.show("Image dechiffrée")