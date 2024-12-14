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
