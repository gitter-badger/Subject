#Clase que abstrae la informacion de un pais
class Pais(object):

	def __init__(self,id,pais,nacionalidad):
		self.id = id
		self.__pais = pais
		self.__nacionalidad = nacionalidad
	
	def __str__(self):
	   return self.__pais

	def get_pais(self):
		return self.__pais

	def get_nacionalidad(self):
		return self.nacionalidad
