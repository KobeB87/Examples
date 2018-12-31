#coding:utf-8
"""
(!) Tuple : conteneur immuable dont on ne peut pas modifier les valeurs
"""

def getPosition():
	posX = 10
	posY = 20
	
	return (posX, posY)

#Main
coordX = 100
coordY = 30
print("Initialize position : {}/{}".format(coordX, coordY))
(coordX, coordY) = getPosition()
print("Get position : {}/{}".format(coordX, coordY))