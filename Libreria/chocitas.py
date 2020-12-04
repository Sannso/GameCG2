import pygame
import Libreria.constantes as cnt

def getChocitas(listachocitas):
	#Posicion enemigos chocita1
	poschoci1 = [35, 170]
	listachocitas.append(poschoci1)
	pe1 = [53,  246]

	#Posicion enemigos chocita2
	poschoci2 = [380, 1065]
	listachocitas.append(poschoci2)
	pe2 = [405,  1143]

	#Posicion enemigos chocita3
	poschoci3 = [1245, 25]
	listachocitas.append(poschoci3)
	pe2 = [1264,  108]

	#Posicion enemigos chocita4
	poschoci4 = [1402, 500]
	listachocitas.append(poschoci4)
	pe2 = [1430,  582]

	#Posicion enemigos chocita5
	poschoci5 = [1569, 16]
	listachocitas.append(poschoci5)
	pe2 = [1590,  107]

	#Posicion enemigos chocita6
	poschoci6 = [2136, 280]
	listachocitas.append(poschoci6)
	pe2 = [2162,  372]

	#Posicion enemigos chocita7
	poschoci7 = [1788, 1200]
	listachocitas.append(poschoci7)
	pe2 = [1812,  1277]

	return listachocitas


def getPosPE(listaPE):
	#Posicion enemigos chocita1
	pe1 = [53,  246]
	listaPE.append(pe1)
	
	#Posicion enemigos chocita2
	pe2 = [405,  1143]
	listaPE.append(pe2)
	
	#Posicion enemigos chocita3
	pe3 = [1264,  108]
	listaPE.append(pe3)

	#Posicion enemigos chocita4
	pe4 = [1430,  582]
	listaPE.append(pe4)

	#Posicion enemigos chocita5
	pe5 = [1590,  107]
	listaPE.append(pe4)

	#Posicion enemigos chocita6
	pe6 = [2162,  372]
	listaPE.append(pe5)

	#Posicion enemigos chocita7
	pe7 = [1812,  1277]
	listaPE.append(pe6)
	

	return listaPE


def generateCantPE(listaPE):

	for i in range(7):
		listaPE.append(2)
	
	return listaPE