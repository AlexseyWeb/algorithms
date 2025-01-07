# Принцип  единой отвественности SRP
class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)
    # Нарушение принципа

    # def save_entry(self, filename):
    #     with open(filename, "w+") as file:
    #         file.write(f"{str(self)}")

    # def load(self, filename):
    #     pass

    # def low_from_web(self, uri):
    #     pass

# Лучше создать другой класс


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, "w+") as file:
            file.write(f"{str(journal)}")


j = Journal()
j.add_entry("I cried today.")
j.add_entry("I ate a bug")
print(f"Journal entries:\n{j}")
print("-" * 30)
file = r'journal.txt'
PersistenceManager.save_to_file(j, file)
with open(file) as file:
    print(file.read())

#LSP
class Rectangle:
	def __init__(self, width, height):
		self._height = height
		self._width = width

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, value):
		self._height = value

	@property
	def width(self):
		return self._width

	@width.setter
	def width(self, value):
		self._width = value

	@property
	def area(self):
		return self._width * self._height

	def __str__(self):
		return f'Width: {self.width} Height: {self.height}'


def use_it(rc):
	w = rc.width 
	rc.height = 10
	expected = int(w * 10)
	print(f'Expected an area of {expected} got {rc.area}')

rc = Rectangle(2, 3)
use_it(rc)

	
