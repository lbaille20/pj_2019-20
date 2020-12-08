#!/usr/bin/env python
# coding: utf-8

# ## Fonctions

# In[13]:


def download_txt_csv_straight(src_url, src_encoding = 'utf-8', dst_encoding = 'utf-8', rep_dst = 'Telechargements'):
    import os
    filename = os.path.basename(src_url)
    if rep_dst not in os.listdir() or not os.path.isdir(rep_dst):
        os.mkdir(rep_dst)
    from urllib.request import urlopen
    f = urlopen(src_url)
    contenu = f.read().decode(src_encoding)
    with open(os.path.join(rep_dst, filename), 'wb') as f1:
        f1.write(contenu.encode(dst_encoding))
    #print("Fichier {} téléchargé dans le dossier {}".format(filename, rep_dst))


# In[14]:


import os


# ### Téléchargement du fichier

# In[15]:


##Téléchargement du fichier dont l'url est indiquée 
##dans le dossier "Telechargements"
src_url = "https://capytale.ac-paris.fr/pj/75/luc.baille/PCSI_TP_14_table_pays__csv_utf-8__semi_colon_.csv"
download_txt_csv_straight(src_url)


# ### Ouverture du fichier

# In[16]:


rep_src = "Telechargements"
filename = "PCSI_TP_14_table_pays__csv_utf-8__semi_colon_.csv"
path_to_file = os.path.join(rep_src, filename)


# In[17]:


import csv
with open(path_to_file) as csvfile:
    reader = csv.DictReader(csvfile, delimiter = ";")
    data = [row for row in reader]


# In[18]:


import pandas as pd
data_panda = pd.read_csv(path_to_file, delimiter = ";")
#data_panda


# In[19]:


"""## column names
## https://www.geeksforgeeks.org/how-to-get-column-names-in-pandas-dataframe
for index, row in data_panda.iterrows():
    print([ row[a] for a in data_panda.head() ])
    print(row.values)
    """


# ## Création de la base .db

# In[22]:


try:
    import sqlite3
    conn = sqlite3.connect('TP_14_BD_pays.db')
    c = conn.cursor()
    # Create table https://www.sqlite.org/lang_createtable.html
    c.execute('''CREATE TABLE pays
             (nom text, continent text, superficie integer, population integer, pib integer)''')
    # Insert a row of data
    for index, row in data_panda.iterrows():
        c.execute("INSERT INTO pays VALUES (?, ?, ?, ?, ?)", row.values)
    # Save (commit) the changes
    conn.commit()
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()
    print("base créée")
except:
    print("base déjà créée")


# ## Exécution d'une requête

# In[20]:


## fonction pour exécuter une requête SQL
def execute_requete(dbname, req):
    import sqlite3
    conn = sqlite3.connect(dbname+'.db')
    c = conn.cursor()
    res = c.execute(req)
    header = [att7[0] for att7 in c.description]
    tab = []
    for row in res:
        tab.append(row)
    conn.close()
    return header, tab


# In[23]:


"""dbname = 'TP_14_BD_pays'
r = 'SELECT * FROM pays ORDER BY nom'
execute_requete(dbname, r)
"""


# ### Avec magics

# In[26]:


## fonction pour exécuter une requête SQL
def requete_panda(dbname, req):
    import sqlite3
    conn = sqlite3.connect(dbname+'.db')
    c = conn.cursor()
    res = c.execute(req)
    header = [att7[0] for att7 in c.description]
    tab = []
    for row in res:
        tab.append(row)
    conn.close()
    return header, tab


# In[28]:


from IPython.core import magic_arguments
from IPython.core.magic import line_magic, cell_magic, line_cell_magic, Magics, magics_class
 
@magics_class
class TestMagics(Magics):
    @cell_magic
    def sql(self, line='', cell=None):
        h, t  =requete_panda(dbname, cell)
        import pandas as pd
        df = pd.DataFrame.from_records(t,index = None, columns= h)
        return df
 
    @line_magic
    def load_db(self, line):
        global dbname
        dbname = line
        print("Nom de la base \""+line+"\" enregistré.")
 
ip = get_ipython()
ip.register_magics(TestMagics)


# In[24]:


"""
%load_db TP_14_BD_pays
"""


# In[25]:


"""%%sql
SELECT * FROM pays ORDER BY population DESC
"""

