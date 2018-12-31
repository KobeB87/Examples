#coding:utf-8
"""
Human class
"""
class Human:
	#Defines a human being
	total_humans = 0
	somewhere = "Earth"
	
	def __init__(self, firstname="John", lastname="Wick", age=1):
		print("Creates an human")
		self._firstname = firstname
		self._lastname = lastname
		self._age = age
		Human.total_humans += 1
		
	def _getAge(self):
		try:
			return self._age
		except AttributeError:
			print("The age was deleted")
		
	def _setAge(self, age):
		if age <= 0:
			age = 0
		self._age = age
		
	def _delAge(self):
		del self._age
		
	age = property(_getAge, _setAge, _delAge, "Representing the age of the human being")
	
	def speak(self, message="No comment"):
		print("{} says '{}'".format(self.firstname, message))
		
	def planet(cls, new_planet):
		Human.somewhere = new_planet
		
	updatePlanet = classmethod(planet)
	
	def definition():
		print("I am a human")

	definition = staticmethod(definition)
		
print("Starting program")
Human.definition()
h1 = Human("John", "Doe", 31)
help(Human.age)
print("Firstname : {}, Lastname : {}, Age : {}".format(h1._firstname, h1._lastname, h1._age))
h1._setAge(20)
h1._delAge()
print("Changing age with : {}".format(h1.age))
