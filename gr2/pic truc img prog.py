"""from PIL import Image"""

def arrond_coul(nb) :
    palier = [31,63,95,127,159,191,223,255]
    
    for i in palier :
        if nb <= i  :
            return i
    return 255
"""
def dim_coul():
    img = Image.open("images/logo_NSI_mechain.jpg").convert('RGB')
    w,h = img.size
    pic= Image.new('RGB',(w,h))
    
    
    for i in range(w):
        for j in range(h):
            r, g, b = img.getpixel((i, j))
            r = arrond_coul(r)
            g = arrond_coul(g)
            b = arrond_coul(b)
            pic.putpixel((i,j),(r,g,b))
            
    pic.save("result.jpg")
    print("FINI")
    pic.show()

dim_coul()"""
    