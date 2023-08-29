#modus ponens
premisa1=True #si llueve, entonces la calle estara mojada
premisa2=True #la calle no esta mojada
conclusion = premisa1 and premisa2 #No esta lloviendo
if conclusion:
	print("la calle estara mojada")
else:
        print("la conclusion no es valida")
