import requests
import json
import datetime
def getRequest(UrlSite:str,nomFic:str): # je fais cette fonction afin de moins écrire aux autres fonctions et grâce à cette fonction on pourra parser les données json des 3 sites
	res=requests.get(UrlSite)
	f1=open(nomFic+".txt",'w',encoding='utf-8')
	f1.write(res.text)
	f1.close()

	f2= open(nomFic+".txt",'r',encoding='utf-8')
	example=f2.read()
	f2.close()

	stat=json.loads(example)
	return stat

#ss=getRequest("https://montpellier-fr-smoove.klervi.net/gbfs/en/station_status.json","ficjson")
#so=getRequest("https://montpellier-fr-smoove.klervi.net/gbfs/en/station_information.json","ficS")

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

# ~ se=getName(so,'003')
# ~ print(se)
def getId(ficjson,name:str):
	station=ficjson['data']['stations']
	for i in range(len(station)):
		nom=station[i]['name']
		
		if nom==name:
			ids=station[i]['station_id']
			return ids
# ~ oi=getId(so,'Corum')
# ~ print(oi)

def getCapacity(ficjson,idp:str):
	indice=getIndice(idp,ficjson)
	station=ficjson['data']['stations']
	return station[indice]['capacity']
# ~ op=getCapacity(so,'005')

# ~ print(op)

def getVeloDisponible(idP:str,ficjson):
	indice=getIndice(idP,ficjson)
	station=ficjson['data']['stations']
	return station[indice]['num_bikes_available']
#rt=getVeloDisponible('005',ss)
#print(rt)

def getVeloCasse(idp:str,ficjson):
	indice=getIndice(idp,ficjson)
	station=ficjson['data']['stations']
	return station[indice]['num_bikes_disabled']
	
# ~ op=getVeloCasse('005',ss)
# ~ print(op)
def getVeloQuaiDisponible(idp:str,ficjson):
	indice=getIndice(idp,ficjson)
	
	station=ficjson['data']['stations']
	return station[indice]['num_docks_available'] , "à", 
	
# ~ op=getVeloQuaiDisponible('005',ss)
# ~ print(op)
def getDernierMaj(idp:str,ficjson):
	i=getIndice(idp,ficjson)
	return ficjson['data']['stations'][i]['last_reported']
st=getDernierMaj('005',ss)
# ~ print(st)
def getDate(secondes):
	return datetime.datetime.fromtimestamp(secondes).strftime('%Y-%m-%d %H:%M:%S')
#da=getDate(st)
#print(da)
