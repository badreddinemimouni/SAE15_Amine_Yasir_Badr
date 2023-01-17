import requests
from lxml import etree

parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT',
'FR_MTP_PITO','FR_MTP_CIRCE','FR_MTP_SABI','FR_MTP_GARC','FR_MTP_SABL','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_CAS_VICA','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY']

def DonnéesParking(parking): 
	for i in range(0,len(parking)):
		response=requests.get("https://data.montpellier3m.fr/sites/default/files/ressources/"+parking[i]+".xml")
		print(response.text)

# ~ ss=DonnéesParking(parkings)
# ~ print(ss)

def infosParking(nomP):
	response=requests.get("https://data.montpellier3m.fr/sites/default/files/ressources/"+nomP+".xml")
	f1=open(nomP+".txt","w", encoding='utf8')
	f1.write(response.text)
	f1.close()
	tree = etree.parse(nomP+".txt")
	for user in tree.xpath("Name"):
		print('Nom du parking :',user.text)
	for user in tree.xpath("Total"):
		print('Nombre total de places :',user.text)
	for user in tree.xpath("Free"):
		print('Nombre de places libres :',user.text) 
# ~ ss=infosParking("FR_MTP_FOCH")
# ~ print(ss)

def nbrPlaces(parking):
	f3=open("parkingPlacesLibre.txt","w",encoding='utf-8') 
	f3.write(" ")
	f3.close()
	for i in range (0,len(parking)): 
		res=requests.get("https://data.montpellier3m.fr/sites/default/files/ressources/"+parking[i]+".xml")
		f2=open(parking[i]+".txt","w",encoding='utf-8')
		f2.write(res.text)
		f2.close()
		tree = etree.parse(parking[i]+".txt") 
	
		f3=open("parkingPlacesLibre.txt","a",encoding='utf-8')  
	
		for us in tree.xpath("Free"): 
			print('Nombre de places libres :',us.text) 
			free=us.text 
			f3.write('Nombre de places libres :'+free+"\n") 
		for us in tree.xpath("Status"): 
			if us.text == "Open": 
				f3.write('parking ouvert') 
				f3.write('\n') 
				print("open")
			else:
				f3.write("parking ferme")
				print("ferme")
			f3.write("---------------------------------------------------------------------------------------------")
			f3.write('\n')

# ~ ss=nbrPlaces(parkings)
# ~ print(ss)


def pourcentagePlacesLibres(parking):
	f3=open("pourcentagePlacesLi.txt","w",encoding='utf-8') # ce sera dans ce fichier que je stockerai toutes les données des places libres
	f3.write(" ") # je le vide comme ca si je re-execute le programme je n'ai pas le meme resultat plusieurs fois
	f3.close()
	nbFree1=0
	nbTotal1=0
	for i in range (0,len(parkings)): 
		res=requests.get("https://data.montpellier3m.fr/sites/default/files/ressources/"+parking[i]+".xml")
		f2=open(parking[i]+".txt","w",encoding='utf-8')
		f2.write(res.text)
		f2.close()
		tree = etree.parse(parking[i]+".txt") 
	
		f3=open("pourcentagePlacesLi.txt","a",encoding='utf-8') # j'ai mis "a" qui veut dire append comme ca il n'ecrase pas les données a chaque tour 
		for us in tree.xpath("Free"): # on parcours ce qu'il y a dans la balise Free  
		
			nbFree=int(us.text) #J'attribue a la variable free le nombre de places libres	
			nbFree1=nbFree1+int(us.text)
		for us in tree.xpath("Total"):
		
			nbTotal=int(us.text)
			nbTotal1=nbTotal1+int(us.text)
		pourcentage=(nbFree/nbTotal)*100	
		print("pourcentage : de places dans le parking: ",format(pourcentage,'.2f'))
		f3.write('Pourcentage de places libres dans le parking: '+format(pourcentage,'.2f')+"%"+"\n")
		print("-----------------------------------------------------------------------")
		f3.write("---------------------------------------------------------------------------------------------")
		f3.write('\n')
	pourcentagePlaces=(nbFree1/nbTotal1)*100
	f3.write("pourcentage de places libre dans toute la ville est de: "+format(pourcentagePlaces,'.2f')+"%")

# ~ ss=pourcentagePlacesLibres(parkings)
# ~ print(ss)

def placesLibresEtNoms(parking):
	f3=open("parkingPlacesLibresEtNom.txt","w",encoding='utf-8') # ce sera dans ce fichier que je stockerai toutes les données des places libres
	f3.write(" ") # je le vide comme ca si je re-execute le programme je n'ai pas le meme resultat plusieurs fois
	f3.close()
	for i in range (0,len(parking)): 
		res=requests.get("https://data.montpellier3m.fr/sites/default/files/ressources/"+parking[i]+".xml")
		f2=open(parking[i]+".txt","w",encoding='utf-8')
		f2.write(res.text)
		f2.close()
		tree = etree.parse(parking[i]+".txt") 
	
		f3=open("parkingPlacesLibresEtNom.txt","a",encoding='utf-8') # j'ai mis "a" qui veut dire append comme ca il n'ecrase pas les données a chaque tour 
		for us in tree.xpath("Name"):  # parcourir ce qu'il y a dans la balise de  name 
			print('Nom du parking :',us.text) # afficher ce qu'il y a dedans (user c'est comme un indice dans ce cas la) et on l'affiche en format texte
			name=us.text # j'attribu le resultat de la donnée dans la balise name dans la variable name
			f3.write('Nom du parking :'+name+"\n") # je l'ecris dans le fichier dans lequel il y aura toutes les données
		for us in tree.xpath("Free"): # on parcours ce qu'il y a dans la balise Free 
			print('Nombre de places libres :',us.text) # J'affiche les places libres 
			free=us.text #J'attribue a la variable free le nombre de places libres
			f3.write('Nombre de places libres :'+free+"\n") # j'ecris cette donnée dans le fichier parkingPlacesLibres
		for us in tree.xpath("Status"): 
			if us.text == "Open": # si le resultat de la donnée dans la balise status est open
				f3.write('parking ouvert') # j'ecris parking ouvert
				f3.write('\n') # je saute de ligne
				print("open")
			else:
				f3.write("parking ferme") # sinon parking ferme
				print("ferme")
			f3.write("---------------------------------------------------------------------------------------------")
			f3.write('\n')	
# ~ ss=placesLibresEtNoms(parkings)
# ~ print(ss)
	
                                                                                                                                                         