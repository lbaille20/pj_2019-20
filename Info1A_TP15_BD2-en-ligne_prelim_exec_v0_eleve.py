#!/usr/bin/env python
# coding: utf-8

# ## Fonctions

# ### Fonction de téléchargement du fichier

# In[1]:


def download_db(src_url, rep_dst = 'Sqlite_databases'):
    import os
    filename = os.path.basename(src_url)
    if rep_dst not in os.listdir() or not os.path.isdir(rep_dst):
        os.mkdir(rep_dst)
    from urllib.request import urlopen
    f = urlopen(src_url)
    contenu = f.read()
    with open(os.path.join(rep_dst, filename), 'wb') as f1:
        f1.write(contenu)
    print("Fichier {} téléchargé dans le dossier {}".format(filename, rep_dst))


# ### Fonction pour exécuter une requête

# In[2]:


## fonction pour exécuter une requête SQL
def execute_requete(dbname, req, rep_db = 'Sqlite_databases'):
    import os
    import sqlite3
    conn = sqlite3.connect(os.path.join(rep_db, dbname+'.db'))
    c = conn.cursor()
    res = c.execute(req)
    header = [att7[0] for att7 in c.description]
    tab = []
    for row in res:
        tab.append(row)
    conn.close()
    return header, tab


# ### Requête pour afficher toutes les tables de la base
# 
# https://likegeeks.com/python-sqlite3-tutorial/

# In[3]:


def show_tables1():
    req = 'SELECT name from sqlite_master where type= "table"'
    execute_requete(dbname, req)
    
def show_tables(rep_db = 'Sqlite_databases'):
    import sqlite3, os
    conn = sqlite3.connect(os.path.join(rep_db, dbname+'.db'))
    c = conn.cursor()
    req = 'SELECT name from sqlite_master where type= "table"'
    res = c.execute(req)
    tables = [row[0] for row in res]
    conn.close()
    return tables


# ### Magic functions

# In[4]:


from IPython.core import magic_arguments
from IPython.core.magic import line_magic, cell_magic, line_cell_magic, Magics, magics_class
 
@magics_class
class TestMagics(Magics):
    @cell_magic
    def sql(self, line='', cell=None, nmaxrows = 999):
        h, t  = execute_requete(dbname, cell)
        import pandas as pd
        pd.options.display.max_rows = nmaxrows
        df = pd.DataFrame.from_records(t,index = None, columns= h)
        return df
 
    @line_magic
    def load_db(self, line):
        global dbname
        dbname = line
        print("Nom de la base \""+line+"\" enregistré.")
 
ip = get_ipython()
ip.register_magics(TestMagics)


# ## Téléchargement de la base

# In[5]:


src_url = 'https://capytale.ac-paris.fr/pj/75/luc.baille/TP_15_BD_films.db'


# In[6]:


download_db(src_url)

