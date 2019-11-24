

import math
import json
import itertools
from operator import itemgetter






projet = [
    {
        "niveau":0,
        "num_tache":1,
        "name":"A",
        "predecess":[],
        "pred":[],
        "succ":[],
        "duree":3,
        "date_debut_pluto": 0,
        "date_fin_pluto": 0,
        "date_debut_tard": 0,
        "date_fin_tard": 0,
        "marge_libre":0,
        "marge_totale":0
    },
    {
        "niveau":0,
        "num_tache":2,
        "name":"B",
        "predecess":[],
        "pred":[],
        "succ":[],
        "duree":12,
        "date_debut_pluto": 0,
        "date_fin_pluto": 0,
        "date_debut_tard": 0,
        "date_fin_tard": 0,
        "marge_libre":0,
        "marge_totale":0
    },
    {
        "niveau":0,
        "num_tache":3,
        "name":"C",
        "predecess":[1,2],
        "pred":[1,2],
        "succ":[],
        "duree":1,
        "date_debut_pluto": 0,
        "date_fin_pluto": 0,
        "date_debut_tard": 0,
        "date_fin_tard": 0,
        "marge_libre":0,
        "marge_totale":0
    },
    {
        "niveau":0,
        "num_tache":4,
        "name":"D",
        "predecess":[2],
        "pred":[2],
        "succ":[],
        "duree":6,
        "date_debut_pluto": 0,
        "date_fin_pluto": 0,
        "date_debut_tard": 0,
        "date_fin_tard": 0,
        "marge_libre":0,
        "marge_totale":0
    },
    {
        "niveau":0,
        "num_tache":5,
        "name":"E",
        "predecess":[3],
        "pred":[3],
        "succ":[],
        "duree":7,
        "date_debut_pluto": 0,
        "date_fin_pluto": 0,
        "date_debut_tard": 0,
        "date_fin_tard": 0,
        "marge_libre":0,
        "marge_totale":0
    },
    {
        "niveau":0,
        "num_tache":6,
        "name":"F",
        "predecess":[3,4],
        "pred":[3,4],
        "succ":[],
        "duree":3,
        "date_debut_pluto": 0,
        "date_fin_pluto": 0,
        "date_debut_tard": 0,
        "date_fin_tard": 0,
        "marge_libre":0,
        "marge_totale":0
    },
    {
        "niveau":0,
        "num_tache":7,
        "name":"G",
        "predecess":[6],
        "pred":[6],
        "succ":[],
        "duree":3,
        "date_debut_pluto": 0,
        "date_fin_pluto": 0,
        "date_debut_tard": 0,
        "date_fin_tard": 0,
        "marge_libre":0,
        "marge_totale":0
    },
    
]

######## Calcul niveau
dicspred = []
tacheinit = []
niv = 0
continues = True

################################# Ordonner le projet ###############################


while continues: 
    niv += 1
    comptoui = 0
    comptnon = 0
    for i, tache in enumerate(projet):
        
        nb_predecessuer = len(tache['predecess'])
        # print(i, nb_predecessuer)
        if nb_predecessuer == 0:
            tacheinit.append(tache['num_tache'])
            if  projet[i]['niveau'] == 0  :
                projet[i]['niveau'] = niv
                
            comptnon += 1 
        else:
            comptoui += 1

    for k , taches in enumerate(projet):
        # print(tacheinit, projet[k]['predecess'])
        for t in tacheinit:
            if t in projet[k]['predecess']:
                projet[k]['predecess'].remove(t)

    if comptoui != 0:
        continues = True
    else:
        continues = False

    # print('yes')



projetfilter = sorted(projet, key=itemgetter('niveau'))
#myprojet = json.loads(projet)

compt = 0
t0 = 1
######################################### calcule des date au plus tot ####################################
for key ,item in enumerate(projetfilter):
    if compt == 0:
        if item['niveau'] == 1:
            # print([0],  " " * (item['niveau']), "Tache ", item['name'] )
            projetfilter[key]['date_debut_pluto'] = t0
            projetfilter[key]['date_fin_pluto'] = t0 + item['duree'] - 1

        else:
            tach = projetfilter[key]
            tab_duree = []
            pdces = []
            # print(tach['pred'])
            
            for ids,data in enumerate(projetfilter[:key]):
                if data['num_tache'] in tach['pred']:
                    
                    # print(data['num_tache'])
                    tab_duree.append(data['date_fin_pluto'])
                    pdces.append(data['name'])
        
            # print(pdces, "." * item['niveau']**3, "Tache ", item['name'] )
            projetfilter[key]['date_debut_pluto'] = max(tab_duree) + 1
            projetfilter[key]['date_fin_pluto'] = max(tab_duree) + 1 + item['duree'] - 1


            # print(tach)



########################################### Calcul des date au plus tard #####################################

for key, taches in enumerate(projetfilter):
    for item in projetfilter:
        if taches['num_tache'] in item['pred']:
            projetfilter[key]['succ'].append(item['num_tache'])

iscontune = 0
jecontinue = True
projetfilter = sorted(projet, key=itemgetter('niveau'), reverse=True)

# while jecontinue:
max_duree = max(projetfilter, key=lambda item:item['date_fin_pluto'])
#print(max_duree)

for key , tachess in enumerate(projetfilter):

    if len(tachess['succ']) == 0:
        # print("fin", tachess['name'])
        projetfilter[key]['date_fin_tard'] = max_duree['date_fin_pluto']
        projetfilter[key]['date_debut_tard'] = max_duree['date_fin_pluto'] - tachess['duree'] + 1
    else:
        tach = projetfilter[key]
        tab_duree = []
        succ = []
        # print(tach['pred'])
        for ids,data in enumerate(projetfilter):
            if data['num_tache'] in tach['succ']:
                
                # print(data['num_tache'],  tach['succ'])
                # print(tach['date_debut_tard'])
                tab_duree.append(data['date_debut_tard'])
        # print(tab_duree, tachess['name'])

        projetfilter[key]['date_fin_tard'] = min(tab_duree) - 1
        projetfilter[key]['date_debut_tard'] = min(tab_duree) - tachess['duree']


# 

#################################  Calcule de marge totale

for key, item in enumerate(projetfilter):
    projetfilter[key]['marge_totale'] = item['date_debut_tard'] - item['date_debut_pluto']


for key , tachess in enumerate(projetfilter):

    if len(tachess['succ']) == 0:
        # print("fin", tachess['name'])
        projetfilter[key]['marge_libre'] = tachess['marge_totale']
    else:
        tach = projetfilter[key]
        tab_duree = []
        for ids,data in enumerate(projetfilter):
            if data['num_tache'] in tach['succ']:
                

                tab_duree.append(data['date_debut_pluto'])

        projetfilter[key]['marge_libre'] = (min(tab_duree) - 1) - projetfilter[key]['date_fin_pluto']
        


"""""""""""""""""""""

N*    Tache    Duree    Succ    DePTot   FinPt






"""""""""""""""""""""
esp = " "*4
print("\n")
# print("N*", esp ,"Tache",esp ,"Duree", esp ,"Succ", esp ,"DePTot", esp ,"FinPt")
projetfilter = sorted(projet, key=itemgetter('num_tache'))

for item in projetfilter:
    print(item['num_tache'], esp ,item['name'],esp ,item['duree'], esp  ,item['date_debut_pluto'], esp ,item['date_fin_pluto'], esp ,item['marge_totale'],esp, item['marge_libre'])
    

######### Chemin Critique
chemcritiq = []
dureeprojet = 0
for item in projetfilter:
    if item['marge_totale'] == 0 :
        chemcritiq.append(item['name'])
        dureeprojet += item['duree']

print('Chemin critique :', chemcritiq, '\n Duree :', dureeprojet)