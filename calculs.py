tab=[]
for i in range(0,9):
  f1=open(str(i)+'heure.txt','r')
  lignes=f1.readlines()
  for ligne in lignes:
    ligne=ligne.replace('\n','')
    #print(ligne)
    donnees=ligne.split(',')
    tab.append(float(donnees[0]))
print(tab)









	for j in range(0,9):
		
		valeur=tab7[j]
		tab4.clear()
		tab4.append(valeur)
		#print("tabel")
		#print(tab7)
		if heure==0:
			for x in range(0,len(tab4)):

				tab10.append(tab4[x])
			#print(tab10)
		if heure==1:
			for x in range(0,len(tab4)):
				tab11.append(tab4[x])
		if heure==2:
			for x in range(0,len(tab4)):
				tab12.append(tab4[x])
		if heure==3:
			for x in range(0,len(tab4)):
				tab13.append(tab4[x])
		if heure==4:
			for x in range(0,len(tab4)):
				tab14.append(tab4[x])
		if heure==5:
			for x in range(0,len(tab4)):
				tab15.append(tab4[x])
		if heure==6:
			for x in range(0,len(tab4)):
				tab16.append(tab4[x])
		if heure==7:
			for x in range(0,len(tab4)):
				tab19.append(tab4[x])
		if heure==8:
			for x in range(0,len(tab4)):
				tab22.append(tab4[x])
		heure=heure+1