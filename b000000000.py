# -*- coding: utf-8 -*-
"""

@author: Raissa111
"""
eleves = {}
eleves["Boris"]=["Amir","Franck","Nathalie","Bertrand"]
eleves["Amir"]=[]
eleves["Franck"]=[]
eleves["Nathalie"]=[]
eleves["Bertrand"]=["Erna","Hassana","Abdelkrim"]
eleves["Erna"]=[]
eleves["Hassana"]=[]
eleves["Zoureni"]=["Sekou","Auriane","Corlings"]
eleves["Sekou"]=[]
eleves["Auriane"]=[]
eleves["Corlings"]=[]
eleves["Abdelkrim"]=["Souleyman","Zack","Zoureni"]
eleves["Souleyman"]=[]
eleves["Zack"]=[]

from collections import deque
def personne_elue(name):
    return name == 'Zoureni'

def search(name):
   search_queue = deque()
   search_queue += eleves[name]
   print( len(search_queue) )
   return False

if __name__== "__main__":
   search("Boris")
