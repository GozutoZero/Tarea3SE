#modus tollens
premisa1=True #si llueve, entonces la calle estara mojada
premisa2=False #la calle no esta mojada
conclusion = not premisa1 or premisa2 #No esta lloviendo
if conclusion:
	print("no esta lloviendo")
else:
        print("la conclusion no es valida")
