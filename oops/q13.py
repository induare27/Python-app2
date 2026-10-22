#Q13: Demonstrate multiple inheritance using a Writer and Singer class, combined into MultiTalentedPerson.

class Writer:
    def write(self,book):
        self.book=book
        print("book name:",self.book)
class Singer:
    def sing(self,song):
        self.song=song
        print("song name:",self.song)
class Multitalented(Writer,Singer):
    def person(self):
        print("he is multitalented")
m=Multitalented()
m.person()
m.write("Twisted series")
m.sing("Fairy tale")