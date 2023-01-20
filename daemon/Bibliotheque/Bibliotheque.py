import requests
import time 
from lxml import etree 
import json

def requestsParking(x):
    response=requests.get(f'https://data.montpellier3m.fr/sites/default/files/ressources/{x}.xml')
    return response.text

def requestsVelo():
    f1=open("velo.json","w",encoding="utf8")
    response=requests.get("https://montpellier-fr-smoove.klervi.net/gbfs/en/station_status.json")
    f1.write(response.text)
    f1.close()

def placePasLibre():
    """Cette fonction prend la liste des parking de Montpellier, il vous est demander de rentrer un temps de fin 
    pour pouvoir éffectuer une batterie de test durant toutes cette dure à une fréquence qui vous ai demander 
    de choisir. Il fait la différence entre les place libre et total pour avoir les places occupé
    bibliothèque obligatoire: request, lxml (fonction etree) et time 
    """
    tpsFin,tpsIntervall=int(input("choisir temps de fin ")),int(input("choisir un intevalle "))
    parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH', 
    'FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT',
    'FR_MTP_PITO','FR_MTP_CIRCE','FR_MTP_SABI','FR_MTP_GARC','FR_MTP_SABL'
    ,'FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_CAS_VICA',
    'FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY'] 
    for i in parkings:
        temps_ini=int(time.time()) 
        temps=[float(temps_ini+i) for i in range(0,tpsFin+1,tpsIntervall)]
        tps=int(time.time())
        f1=open(f"{i}_place.txt","w", encoding='utf8')  
        maxi=max(temps)
        while maxi >=tps:
            if tps in temps: 
                    print(i)
                    response=requests.get(f"https://data.montpellier3m.fr/sites/default/files/ressources/{i}.xml")
                    f2=open(f"{i}.txt","w", encoding='utf8')
                    f2.write(response.text)
                    f2.close()
                    tree = etree.parse(f"{i}.txt")
                    for user in tree.xpath("Free") :
                        libre=int(user.text)
                    for user in tree.xpath("Total") :
                        total=int(user.text)
                    place=total-libre
                    f1.write(f'Le Parking:{i} à Nombre de places occupé :{place}     à un temps de {tps}\n') 
                    temps.remove(tps)
                    tps=int(time.time())
            else:
                    tps=int(time.time())

    f1.close() 
        
def placeLibreP():
    """
    Cette fonction prend la liste des parking de Montpellier, il vous est demander de rentrer un temps de fin 
    pour pouvoir éffectuer une batterie de test durant toutes cette periode à une fréquence qui vous ai demander 
    de choisir. Il dis combien il y a de place libre dans chaque parking.
    bibliothèque obligatoire: request, lxml (fonction etree) et time
    """
    tpsFin,tpsIntervall=int(input("choisir temps de fin ")),int(input("choisir un intevalle "))
    parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH', 
    'FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT',
    'FR_MTP_PITO','FR_MTP_CIRCE','FR_MTP_SABI','FR_MTP_GARC','FR_MTP_SABL'
    ,'FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_CAS_VICA',
    'FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY'] 

    for i in parkings:
        temps_ini=int(time.time()) 
        temps=[float(temps_ini+i) for i in range(0,tpsFin+1,tpsIntervall)]
        tps=int(time.time())
        f1=open(f"{i}_place.txt","w", encoding='utf8') 
        maxi=max(temps)
        while maxi >=tps:
            if tps in temps: 
                    response=requestsParking(i)
                    f2=open(f"{i}.txt","w", encoding='utf8')
                    f2.write(response.text)
                    f2.close()
                    tree = etree.parse(f"{i}.txt") 
                    for user in tree.xpath("Free") : 
                        f1.write(f'Le Parking:{i} à Nombre de places libres :{user.text}     à un temps de {tps}\n')  
                    temps.remove(tps)
                    tps=int(time.time())
            else:
                    tps=int(time.time())
    f1.close()

def placeLibreV():
    """
    Cette fonction prend la liste des parking de Montpellier, il vous est demander de rentrer un temps de fin 
    pour pouvoir éffectuer une batterie de test durant toutes cette periode à une fréquence qui vous ai demander 
    de choisir. Il dis combien il y a de place libre dans chaque parking.
    bibliothèque obligatoire: request, lxml (fonction etree) et time
    """
    tpsFin,tpsIntervall=int(input("choisir temps de fin ")),int(input("choisir un intevalle "))
    parkings=['Providence-Ovalie', 'PÃ©rols', 'EuromÃ©decine', 'Malbosc', 'HÃ´tel du DÃ©partement', 'Celleneuve', 'Tonnelles', 'Occitanie', 
    'Fac des Sciences', 'Vert Bois', 'Fac de Lettres', 'Boutonnet', 'Charles Flahault', 'Place Viala', 'PÃ¨re Soulas', 'Aiguelongue', 
    'Marie Caizergues', 'Jeu de Mail des AbbÃ©s', 'Les Aubes', 'Louis Blanc', 'Emile Combes', 'Corum', 'Beaux-Arts', 'Les Arceaux', 'Foch', 
    'Plan Cabanes', 'Gambetta', 'Renouvier', 'ClÃ©menceau', 'Halles Castellane', 'Esplanade', 'ComÃ©die', 'Observatoire', 'Rue Jules Ferry',
    'Saint-Denis', 'Parvis Jules Ferry', 'Nouveau Saint-Roch', 'CitÃ© Mion', 'Voltaire', "Nombre d'Or", 'Antigone Centre', 'MÃ©diathÃ¨que Emile Zola',
    'HÃ´tel de Ville', 'Port Marianne', 'Richter', 'Jardin de la Lironde', 'Odysseum', 'Garcia Lorca', "PrÃ¨s d'ArÃ¨nes", 'Sabines', 'Rondelet',
    'Place Albert 1er - St-Charles', 'Montpellier Sud de France', ' Deux Ponts - Gare Saint-Roch', 'Albert 1er - Cathedrale', 
    'Pont de Lattes - Gare St-Roch', 'Saint-Guilhem - Courreau'] 
    temps_initial=int(time.time()) 
    for i in parkings:
        temps_ini=int(time.time()) 
        temps=[float(temps_ini+i) for i in range(0,tpsFin+1,tpsIntervall)]
        tps=int(time.time())
        f1=open(f"{i}_place.txt","w", encoding='utf8') 
        maxi=max(temps)
        while maxi >=tps:
            if tps in temps: 
                    f2=open(f"{i}.json","w", encoding='utf8')
                    response=requestsVelo() 
                    print("prut")

                    resp=parseJson(response)  
                    print("prout")
                    f2.write(resp)
                    print("prt")
                    f2.close()
                    parse=parseJson(f"{i}.json")
                    for d in parse['data']  : 
                        f1.write(f'Le Parking à vélo:{parse["stations"]["name"]} à Nombre de places libres :{parse["installati"]}   à un temps de {tps}\n')  
                    temps.remove(tps)
                    tps=int(time.time())
            else:
                    tps=int(time.time())
    f1.close()

def parseJson ():
    requestsVelo()
    f1=open("velo.txt",'w',encoding='utf8')
    f2=open("velo.json",'r',encoding='utf8')
    content=json.load(f2)
    content=content['data']['stations']  #liste de dict , 1 dict =  station
    f1.write(str(content))
    f1.close()
    f2.close()
    print(content)
    
parseJson()
