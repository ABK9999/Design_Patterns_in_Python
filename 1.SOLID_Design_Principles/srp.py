#This code is an example of Sigle responsibiliti principle: 

"""
In this example, the Journal class has a single responsibility, which is to store 
and manage journal entries.

The PersistenceManager class, on the other hand, has a single responsibility, which is to persist 
the Journal to different storage mediums (file, web, etc.).

This separation of responsibilities makes the code more maintainable 
and easier to understand, as changes to one class won't affect the other.
"""
class Journal:
    def __init__(self) -> None:
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append(f"{self.count},{text}")
        self.count += 1

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)
    
    # Break SRP
    def save(self, filename):
        file = open(filename,  'w')
        file.write(str(self))
        file.close()

    def load(self, filename):
        pass

    def load_from_web(slef, uri):
        pass

class PersistenceManager:
    def save(Journal, filename):
        file = open(filename,  'w')
        file.write(str(Journal))
        file.close()

j = Journal
j.add_entry("I Practiced Python Today.")
j.add_entry("I ate a bug.")
print(f"Journal entries:\n{j}\n")

p = PersistenceManager
file = r'c:\temp\journal.txt'
p.save_to_file(j, file)

# Verify
with open(file) as fh:
    print(fh.read())


    
    