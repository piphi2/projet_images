from PIL import Image,ImageTk
import tkinter
from tkinter import filedialog

#----------
#Fonction
#----------

def colorise(main_img, h_cible, marge):
    
    result = Image.new("RGB", main_img.size, "white")
    
    # ----------Modificiation d'image----------
    for y in range(main_img.height):
        for x in range(main_img.width):
            r, g, b = main_img.getpixel((x, y))
            h, s, l = RGB_to_HSL((r, g, b))

            # marge de valeur
            delta = abs(h - h_cible)
            if delta < marge or abs(delta - 360) < marge:
                result.putpixel((x, y), (r, g, b))
            else:
                gray = int((r+g+b) / 3)
                result.putpixel((x, y), (gray,gray,gray))
    #------------------------------------------
                
    result.save("image_filtree.png")
    result.show()
    

def RGB_to_HSL(RGB_tuple):
    r,g,b = RGB_tuple[0],RGB_tuple[1],RGB_tuple[2]
    
    
    #Normalise les couleurs en les ramenant entre 0 et 1 
    r /= 255
    g /= 255
    b /= 255
    
    
    max_c = max(r, g, b)
    min_c = min(r, g, b)
    
    # l est la moyenne de la valeur minimal et maximal
    l = (max_c + min_c) / 2

    if max_c == min_c:
        #max_c == min_c -> gris
        h = 0
        s = 0
        
    else:
        d = max_c - min_c
        s = d / (2 - max_c - min_c) if l > 0.5 else d / (max_c + min_c)
        if max_c == r:
            h = ((g - b) / d) % 6
        elif max_c == g:
            h = ((b - r) / d) + 2
        else:
            h = ((r - g) / d) + 4
        h *= 60
    return (h, s, l)

def get_color_HSL(event):
    '''affiche la couleur du pixel cliqué au format HSL'''
    #à compléter
    r,g,b = main_img.getpixel((event.x,event.y))
    h_cible=RGB_to_HSL((r,g,b))[0]
    
    
    print(h_cible)
    print(RGB_to_HSL((r,g,b)))
    
    
    colorise(main_img, h_cible, 20)
    
    return(RGB_to_HSL((r,g,b)))

def get_color_RGB(event):
    '''affiche la couleur du pixel cliqué au format RGB'''
    r,g,b = main_img.getpixel((event.x,event.y))
    print((r,g,b))
    
    colorise(main_img, RGB_to_HSL((r,g,b))[0], 20)
        
    return((r,g,b))
#----------
    
    

#----------
#Main
#----------

link = filedialog.askopenfilename()

main_img = Image.open(link).convert("RGB")

w,h=main_img.size
fenetre = tkinter.Tk()
fenetre.resizable(width=False, height=False)
fenetre.minsize(400,400)
fenetre.title('Cliquer sur un pixel pour connaitre sa couleur')
photo = ImageTk.PhotoImage(main_img)
label=tkinter.Label(fenetre,image=photo)
label.bind("<Button-1>", get_color_RGB) # clic gauche pour RGB
label.bind("<Button-3>", get_color_HSL) # clic droit pour HSL
label.pack()
fenetre.mainloop()
main_img.close()
