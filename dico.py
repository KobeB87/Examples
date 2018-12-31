#coding:utf-8
"""
Dictionnaire
"""

dico = {
	"firstname" : "John",
	"lastname" : "Wick"
}

print("Dictionnaire : ", dico)
print("The first name is", dico["firstname"], "and the last name is", dico["lastname"])

dico ["firstname"] = "Jack"
print("The new first name is", dico["firstname"], "and the last name is", dico["lastname"])

value = dico.pop("firstname")
print("Value deleted", value)
#del dico["firstname"]
print("Display dico", dico)

dico ["age"] = 30
print("Display dico", dico)

print("Does the key 'age' exist ?", "age" in dico)
print("Does the key 'firstname' exist ?", "firstname" in dico)
print()
for key in dico:
	print("Key", key, "with the value", dico[key])
print()
print("Other way to display dico")
for (key, value) in dico.items():
	print("Key", key, "with the value", value)

#Coy a dictionnary dico.copy()

def dictionnary(**parameters):
	print(parameters)
	
dictionnary(firstname="John", lastname="Wick", country="France", age=31)

