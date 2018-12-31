#coding:utf-8
"""
Manage exceptions : try/except wuth else, finally
Exceptions types : 
ValueError
NameError
ZeroDivisionError
OSError
AssertionError
"""

a = input("Enter a number :")
try:
	a = int(a)
	assert(a > 10) 
	print("The result is {}".format(100/a))
except ZeroDivisionError:
	print("Cannot divide by zero")
except ValueError:
	print("Must enter a number")
except AssertionError:
	print("The number is lower than 10")
except:
	print("Incorrect number")
else:
	print("Yes ! You succeed !!")
finally:
	print("End of program")