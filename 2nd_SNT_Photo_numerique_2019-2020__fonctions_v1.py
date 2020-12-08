#!/usr/bin/env python
# coding: utf-8

# ## S.N.T. 2019-2020 - Photographie numérique - Traitement d'image

# Source : https://pixees.fr/informatiquelycee/n_site/snt_photo_transImg.html  
# 
# Url d'origine de l'image de pomme : https://pixees.fr/informatiquelycee/n_site/img/pomme.jpg

# Références diverses (prof) :   
#     https://wprock.fr/blog/emoji-smiley-copier-coller/#Emoji-Smiley-Personnes-et-emotions  
#     https://pixabay.com/fr/illustrations/thumbs-up-visage-souriant-emoji-4007573/  
#     https://www.w3schools.com/charsets/ref_emoji_smileys.asp  
# Markdown :  
# https://wordpress.com/support/markdown-quick-reference/  
# Agrandissement fenêtre matplotlib :
# http://www.learningaboutelectronics.com/Articles/How-to-set-the-size-of-a-figure-in-matplotlib-with-Python.php  
# Taille de la figure (matplotlib) :
# https://stackoverflow.com/questions/29702424/how-to-get-matplotlib-figure-size  

# ### Préliminaires sur Capytale

# ### > Exécuter la cellule suivante pour charger les fonctions utiles au TP

# In[15]:


def telecharger_image(url_image, rep_dst = '.'):
    import os
    filename = os.path.basename(url_image)
    import requests
    with open(filename, 'wb') as f:
        f.write(requests.get(url_image).content)
    return filename

def taille_fichier(path_to_file):
    import os
    return str(os.stat(path_to_file).st_size)+ " octets"

def charger_image(fichier_image, ext = "default"):
    from skimage import io
    im = io.imread(fichier_image)
    return im

def taille_image(im):
    return im.shape[:2][::-1]

def get_pixel(im, coords):
    x, y = coords
    r, v, b = list(map(int, im[y, x]))
    return r, v, b

def put_pixel(im, coords, niveaux):
    x, y = coords
    r, v, b = niveaux
    im[y, x] = (r, v, b)

def get_ligne(im, no_ligne):
    return im[no_ligne, :]

def get_colonne(im, no_colonne):
    return im[:,no_colonne]

def afficher_image(im):
    import matplotlib.pyplot as plt
    plt.imshow(im)
    
def creer_image_couleur(largeur, hauteur):
    import numpy as np
    im = np.zeros((hauteur, largeur, 3), dtype = 'uint8')
    return im

def creer_image_noir_et_blanc(largeur, hauteur):
    import numpy as np
    im = np.zeros((hauteur, largeur), dtype = 'uint8')
    return im
    
def creer_image_depuis_tableau(tableau):
    import numpy as np
    return np.array(tableau)


# In[42]:


def montrer_couleur(couleur):
    import numpy as np
    hauteur, largeur = 2, 8
    im = creer_image_couleur(largeur, hauteur)
    im[:,:] = couleur
    import matplotlib.pyplot as plt
    h, w = 2, 8
    plt.figure(figsize=(h, w))
    plt.imshow(im)


# In[44]:


##%matplotlib inline
##couleur = (125, 200, 10)
##montrer_couleur(couleur)


# In[ ]:


def liste_couleur(array):
    import numpy as np
    hauteur, largeur = 2, 8
    im = creer_image_couleur(largeur, hauteur)
    im[:,:] = couleur
    import matplotlib.pyplot as plt
    h, w = 2, 8
    plt.figure(figsize=(h, w))
    plt.imshow(im)


# In[1]:


## Métadonnées Exif


# In[2]:


import PIL


# In[3]:


def get_exifdata(filename):
    import PIL.Image
    img = PIL.Image.open('filename')
    exif_data = img._getexif()
    return exif_data


# In[ ]:




