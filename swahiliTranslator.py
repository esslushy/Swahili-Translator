quit = False
#AddTense
def addTense(suffix, verb):
	tense = input("What tense? (past/present/future): ")
	if(tense.lower() == "past"):
		print(suffix + "li" + verb)
		return
	elif(tense.lower() == "present"):
		print(suffix + "na" + verb)
		return
	elif(tense.lower() == "future"):
		print(suffix + "ta" + verb)
		return
	else:
		print("invalid")
		return
#Hello Conjugation
def conjugateHello():
	place =  input("Enter the English person(I/you/he/we/yall/they: ")
	if(place.lower() == "i"):
		print("sijambo")
		return
	elif(place.lower() == "you"):
		print("hujambo")
		return
	elif(place.lower() == "he"):
		print("hajambo")
		return
	elif(place.lower() == "we"):
		print("hatujambo")
		return
	elif(place.lower() == "yall"):
		print("hamjambo")
		return
	elif(place.lower() == "they"):
		print("hawajambo")
		return
	else:
		print("invalid")
		return
#conjugateToBe
def conjugateToBe():
	place =  input("Enter the English person(I/you/he/we/yall/they: ")
	if(place.lower() == "i"):
		addTense("ni", "kuwa")
		return
	elif(place.lower() == "you"):
		addTense("u", "kuwa")
		return
	elif(place.lower() == "he"):
		addTense("a", "kuwa")
		return
	elif(place.lower() == "we"):
		addTense("tu", "kuwa")
		return
	elif(place.lower() == "yall"):
		addTense("m", "kuwa")
		return
	elif(place.lower() == "they"):
		addTense("wa", "kuwa")
		return
	else:
		print("invalid")
		return
#conjugateVerb
def conjugateVerb():
	verb = input("Enter the verb you want to conjugate: ")
	place =  input("Enter the English person(I/you/he/we/yall/they: ")
	if(place.lower() == "i"):
		addTense("ni", verb)
		return
	elif(place.lower() == "you"):
		addTense("u", verb)
		return
	elif(place.lower() == "he"):
		addTense("a", verb)
		return
	elif(place.lower() == "we"):
		addTense("tu", verb)
		return
	elif(place.lower() == "yall"):
		addTense("m", verb)
		return
	elif(place.lower() == "they"):
		addTense("wa", verb)
		return
	else:
		print("invalid")
		return
while(not quit):
	choice = input("Would you like to:\n1) Say Hello\n2) Conjugate 'to be'\n3) Conjugate another verb\n4) Quit\n")
	if(choice == "1"):
		conjugateHello()
	elif(choice == "2"):
		conjugateToBe()
	elif(choice == "3"):
		conjugateVerb()
	elif(choice == "4"):
		quit=True
