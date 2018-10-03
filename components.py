# CLASSES AND METHODS
class Person():
    def __init__(self, name, bio, age):
        # your code goes here!
        self.name = name
        self.bio = bio
        self.age = age


class Club():
    def __init__(self, name, description):
        # your code goes here!
        self.name = name
        self.description = description
        self.club_members = []
        self.President = ""


    def assign_president(self, person):
        # your code goes here!
        self.President = person.name
        #self.club_members.append(person)


    def recruit_member(self, person):
        # your code goes here!
        self.club_members.append(person)


    def print_member_list(self):
        # your code goes here!
        Total_age = 0
        for Person in self.club_members:
            if Person.name == self.President:
                print("- %s (%s years old, President) - %s" % (Person.name, Person.age, Person.bio))
                Total_age += Person.age
            else:    
                print("- %s (%s years old) - %s" % (Person.name, Person.age, Person.bio))
                Total_age += Person.age
        average_age = Total_age / len(self.club_members) + 0.0
        print("Average age in this club: %s years old" % (average_age))
