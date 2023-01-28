import requests
import json
import datetime
def getRequest(UrlSite:str,nomFic:str): # je fais cette fonction afin de moins écrire aux autres fonctions et grâce à cette fonction on pourra parser les données json des 3 sites
	res=requests.get(UrlSite)
	f1=open(nomFic+".json",'w',encoding='utf-8')
	f1.write(res.text)
	f1.close()

	f2= open(nomFic+".json",'r',encoding='utf-8')
	example=f2.read()
	f2.close()

	stat=json.loads(example)
	return stat

def getRequest2(UrlSite:str,nomFic:str): # avoir le json en .txt
	res=requests.get(UrlSite)
	f1=open(nomFic+".json",'w',encoding='utf-8')
	f1.write(res.text)
	f1.close()
	with open(nomFic+".json") as mon_fichier:
		da=json.load(mon_fichier)
	return da
	
# ~ er=getRequest2("https://montpellier-fr-smoove.klervi.net/gbfs/en/station_information.json","ficjson")
# ~ print(er)
ss=getRequest("https://montpellier-fr-smoove.klervi.net/gbfs/en/station_status.json","ficjson")
so=getRequest("https://montpellier-fr-smoove.klervi.net/gbfs/en/station_information.json","ficS")

def getIndice(idp:str,ficjson):# nous donne l'indice a partir de l'id du parking
	station=ficjson['data']['stations']
	for i in range(len(station)):
		indice=station[i]['station_id']
		
		if indice==idp:
			return i

# ~ st=getIndice('038',ss)


	

# ~ print(st)
def getName(ficjson,idp:str): #Donnera les noms des parkings a partir de leurs id et du coup les paramètres prennent la variable dans laquelle il y a le json parsé et l'id du parking en string
	station=ficjson['data']['stations']
	for i in range(len(station)):
		indice=station[i]['station_id']
		
		if indice==idp:
			nom=station[i]['name']
			return nom

# ~ se=getName(er,'003')
# ~ print(se)
def getId(ficjson,name:str):
	station=ficjson['data']['stations']
	for i in range(len(station)):
		nom=station[i]['name']
		
		if nom==name:
			ids=station[i]['station_id']
			return ids
# ~ oi=getId(so,'Corum')
# ~ print("jason:"+oi)

def getCapacity(ficjson,idp:str):
	i=getIndice(idp,ficjson)
	station=ficjson['data']['stations']
	res=station[1]['capacity']
	return res
# ~ op=getCapacity(so,'006')
# ~ print(op)

def getVeloDisponible(idP:str,ficjson):
	indice=getIndice(idP,ficjson)
	station=ficjson['data']['stations']
	return station[indice]['num_bikes_available']



def getVeloCasse(idp:str,ficjson):
	indice=getIndice(idp,ficjson)
	station=ficjson['data']['stations']
	return station[indice]['num_bikes_disabled']
	
# ~ op=getVeloCasse('005',ss)
# ~ print(op)
def getVeloQuaiDisponible(idp:str,ficjson):
	indice=getIndice(idp,ficjson)
	
	station=ficjson['data']['stations']
	return station[indice]['num_docks_available'] 
	
# ~ op=getVeloQuaiDisponible('005',ss)
# ~ print(op)
def getDernierMaj(idp:str,ficjson):
	i=getIndice(idp,ficjson)
	return ficjson['data']['stations'][i]['last_reported']
# ~ st=getDernierMaj('005',ss)
# ~ print(st)
def getDateVelo(secondes):
	return datetime.datetime.fromtimestamp(secondes).strftime('%H:%M:%S')

# ~ da=getDate(st)
# ~ print(da)
def getpourcentageVelo(idp:str,ficjson1,ficjson2):
	station=ficjson2['data']['stations']
	dern=ficjson2['last_updated']
	dern2=getDateVelo(dern)
	#for i in range(0,9):
	#indice=getIndice(idp,ficjson1)

	#idp=station[indice]['station_id']
	total=getCapacity(ficjson2,idp)
	free=getVeloQuaiDisponible(idp,ficjson1)
		
	
	pourcentage=(free/total)*100
	f2=open(idp+".txt",'a',encoding='utf-8')
	f2.write(idp+","+format(pourcentage,'.2f')+","+str(dern2))
	f2.write("\n")
	f2.close()
	
	print (str(dern)+','+str(dern2))

pl=getpourcentageVelo('045',ss,so)
print(pl)
# faire un json pour la partie parking voitures et velos aussi pour stocké
