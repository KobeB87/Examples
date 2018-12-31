class Vehicule:
	def __init__(self, marque, quantite):
		self.marque=marque
		self.quantite=quantite
		
	def move(self):
		print("The vehicule {} is moving".format(self.marque))

#Class fille
class Voiture(Vehicule):
	def __init__(self, marque, quantite, modele):
		Vehicule.__init__(self, marque, quantite)
		self.modele = modele
		
	def move(self):
		print("The car {} is driving".format(self.marque))
		
class Avion(Vehicule):
	def __init__(self, marque, quantite, merchandise):
		Vehicule.__init__(self, marque, quantite)
		self.merchandise = merchandise
		
	def move(self):
		print("The plane {} is flying".format(self.marque))


print("Is Voiture a subclass of Vehicule : {}".format(issubclass(Voiture, Vehicule)))
print("Is Avion a subclass of Vehicule : {}".format(issubclass(Avion, Vehicule)))
print("Is Avion a subclass of Voiture : {}".format(issubclass(Avion, Voiture)))
print("Is Voiture a subclass of Avion : {}".format(issubclass(Voiture, Avion)))

vehicule = Vehicule("Toyota", 3000)
vehicule.move()

voiture = Voiture("Peugeot", 30, "208")
voiture.move()
print("Is a car an instance of Vehicule : {}".format(isinstance(voiture, Vehicule)))
print("Is a car an instance of Voiture : {}".format(isinstance(voiture, Voiture)))
print("Is a car an instance of Avion : {}".format(isinstance(voiture, Avion)))

avion = Avion("Boeing", 3000000, "Missile")
avion.move()
print("Is a plane an instance of Vehicule : {}".format(isinstance(avion, Vehicule)))
print("Is a plane an instance of Voiture : {}".format(isinstance(avion, Voiture)))
print("Is a plane an instance of Avion : {}".format(isinstance(avion, Avion)))