"""
Author: Jacob Blazina
Date: 6/21/2021
File: People.py
Title: Lab 7
"""

# A human has an age, emotions, and hobbies
class Human :

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Prints this human's hobby
    def hobby(self):
        print("Likes watching Netflix")

    # Prints the info about this human
    def info(self):
        print(self.name, " is ", self.age, " years old.")

# A really cool hiker person. Is like a human, but better
class Hiker(Human):

    # Prints the hikers hobby, overrides the human class
    def hobby(self):
        print("Likes going on hikes")


# A fancy scientist. Is like a human but smarter
class Scientist(Human):
    def __init__(self, name, age, lab):
        self.lab = lab
        Human.__init__(self, name, age)

    # Scientists have hobbies too. Overrides the human class
    def hobby(self):
        print("Likes to play with science")

    # Gets the name of the lab
    def labName(self):
        print("Works at the ", self.lab, " laboratory")

# A strong swimmer, look a human but swims a lot
class Swimmer(Human):
    def __init__(self, name, age, hours):
        self.hours = hours
        super().__init__(name, age)

    def hobby(self):
        print("Likes swimming in the lake")

    def hoursSwimming(self):
        print("Swims ", self.hours, " hours per week")


# A smart fish guy
class ScientificSwimmer(Scientist, Swimmer):
    def __init__(self, name, age, hours, lab):
        Scientist.__init__(self, name, age, lab)
        Swimmer.__init__(self, name, age, hours)


# Demo with sample inputs
human = Human("Megan", 20)
hiker = Hiker("Jack", 43)
scientist = Scientist("Mike Flex", 27, "research")
swimmer = Swimmer("Tom Accer", 23, 15)
scienceSwimmer = ScientificSwimmer("John Smith", 30, 100, "nuclear")

human.info()
human.hobby()

print()

hiker.info()
hiker.hobby()

print()

scientist.info()
scientist.hobby()
scientist.labName()

print()

swimmer.info()
swimmer.hobby()
swimmer.hoursSwimming()

print()

scienceSwimmer.info()
scienceSwimmer.hobby()
scienceSwimmer.labName()
scienceSwimmer.hoursSwimming()

