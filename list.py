#coding:utf-8

import copy

tab = ["item"] * 10
print(tab)

brands = ["Peugeot", "Renault", "Citroen", "Fiat", "Mini", "Porsche", "Ferrari" ]
for brand in brands:
	print("Marque", brand)

print("Affiche tous les elements :", brands[:])	
print("Affiche les 2 premiers elements :", brands[:2])
print("Affiche a partir du 2eme element :", brands[2:])
print("Affiche le 3e element a partir de la fin :", brands[-3])
print("Affiche les elements d'indice A à l'element d'indice B :", brands[2:5])

brands.append("Jeep")
print("Ajoute l'element 'Jeep' en fin de liste :", brands)
brands.remove("Jeep")
print("Supprime l'element 'Jeep' de la liste :", brands)
brands.pop()
print("Retire le dernier element de la liste :", brands)
brands.insert(2, "Jeep")
print("Insere 'Jeep' a l'indice 2 de la liste :", brands)
del brands[2]
print("Supprime l'element a l'indice 2 de la liste :", brands)
print("Affiche l'index de l'element 'Fiat' :", brands.index("Fiat"))

brands.sort()
print("Affiche la liste triee par ordre alpha :", brands)
brands.reverse()
print("Affiche la liste triee par ordre alpha :", brands)
brands.append("Fiat")
print("Compte le nombre d'occurence de 'Fiat' :", brands.count("Fiat"))
print("Compte le nombre d'occurence de 'Jeep' :", brands.count("Jeep"))
print("Compte le nombre d'occurence de 'Renault' :", brands.count("Renault"))

#brands.clear() #ou bien brands[:] = []
#print("Efface toute la liste :", brands)

print("Joindre tous les elements separes par une virgule :", ":".join(brands))

brands2 = copy.deepcopy(brands)
print("Affiche la copie de la liste :", brands2)
brands2.pop()
print("Supprime le dernier element de la liste copiee :", brands2, brands)

#Concatener 2 liste
color1 = [ "Blue", "White", "Red" ]
print("Affiche la liste des couleurs :", color1)
color2 = [ "Green", "Yellow", "Black" ]
color1.extend(color2) #color1 += color2 
print("Affiche la liste concatenee des couleurs :", color1)

for idx, value in enumerate(color1):
	print("Index : {} et valeur : {}".format(idx, value))


