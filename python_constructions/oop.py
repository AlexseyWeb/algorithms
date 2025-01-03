class Character():
	#Statics Attributes
	__LIFE_HP = 100
	def __init__(self, race, damage=10):
		self.__race = race 
		self.damage = damage 
		self._health = 100

	def __str__(self):
		return f'You race {self.__race} and your hp {Character.__LIFE_HP}'

	def hit(self, damage):
		return self._health - damage 

	@property
	def health(self):
		return self._health

	@health.setter
	def health(self, current_health):
		if current_health < 0:
			self._health = 0
			return "You dead!"
		else:
			self._health = current_health

	@property
	def race(self):
		return self.__race

class StrConveror():
	@staticmethod
	def display(msg):
		print(f'Your message: -> {msg}')



from abc import ABC 
from abc import abstractmethod


class Shape(ABC):
	def __init__(self):
		super().__init__()
	
	@abstractmethod
	def draw(self):
		pass


unit = Character('Elf', 30)
print(unit.health)
unit.health = -2
print(unit.health)
StrConveror.display('Hi google')
shape = Shape()
print(shape.draw())