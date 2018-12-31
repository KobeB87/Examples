#coding:utf-8
"""
Les fichiers
Mode ouverture :
r : lecture seule
w : écriture avec remplacement
a : écriture avec ajout en fin de fichiers
x : lecture/écriture
r+: lecture/écriture dans un même fichier

Lecture 	: read(), readline(), readlines()
Ecriture	: write()
"""
import pickle

class Player:
	def __init__(self, name, number, age, team):
		self.name=name
		self.number=number
		self.age=age
		self.team=team
		
	def display(self):
		return "The player named {} with number '{}' has {} years old and plays for the team {}".format(self.name, self.number, self.age, self.team)


p1 = Player("Messi", 10, 31, "FC Barcelona")
p2 = Player("Henry", 14, 41, "Arsenal")
p3 = Player("Zidane", 10, 45, "Juventus")

players = [p1, p2, p3]

"""
with open("players.txt", "a") as txt:
	for player in players:
		txt.write("\n" + player.display())
"""

with open("players.data", "wb") as fic:
	record = pickle.Pickler(fic)
	record.dump(p1)

with open("players.data", "rb") as fic:
	record = pickle.Unpickler(fic)
	player1 = record.load()

print(player1.display())
print("End of the program")