# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = "May"
my_age = 22
my_bio = "Cheeky"
myself = Person(my_name, my_bio, my_age)

def introduction():
    print("Hello, %s. Welcome to our portal." % myself.name)

def options():
    # your code goes here!
    user_input = ""
    while user_input != "-1":
        user_input = input("Would you like to: \n1) Create a new club. \nor: \n2) Browse and join clubs. \nor: \n3) View existing clubs. \nor: \n4) Display members of a club. \nor: \n-1) Close application. \n>")
        if user_input == "1": 
            create_club()
        elif user_input == "2": 
            join_clubs()
            break
        elif user_input == "3": 
            view_clubs()
        elif user_input == "4": 
            view_club_members()
        elif user_input == "-1": 
            break
        else:
            print("This option does not exist")


def create_club():
    # your code goes here!
    name = input("Pick a name for your awesome new club: ")
    description = input("What is your club about? ")
    new_club = Club(name, description)

    print("Enter the numbers of the people you would like to recruit to your new club (-1 to stop):")
    
    count = 1
    for member in population: 
        print("[%s] %s" %(count, member.name))
        count += 1
    
    recruit_people = 0
    new_club.recruit_member(myself)
    new_club.assign_president(myself)
    while True:
        recruit_people = input("")
        if recruit_people == "-1":
            break
        elif recruit_people.isdigit() and int(recruit_people) <= len(population):
            person = population[int(recruit_people)-1]
            new_club.recruit_member(person)
        else:
            print("Invalid input please try again")

    print("Here's your club: ")
    print (new_club.name)
    print (new_club.description)
    print("Members:")  
    new_club.print_member_list()
    clubs.append(new_club)

def join_clubs():
    # your code goes here!
    for club in clubs:
        print("NAME: %s \nDESCRIPTION: %s \nMEMBERS: %s " % (club.name, club.description, len(club.club_members)))

    #while True:
    club_to_join = input("Enter the name of the club you'd like to join: ")
    for club in clubs:
        if club_to_join == club.name:
            print("%s just joined %s \n---------" % (myself.name,club_to_join))
            club.recruit_member(myself)
            break
        else:
            print("This club doesn't exist, try again")

def view_clubs():
    # your code goes here!
    for club in clubs:
        print("NAME: %s \nDESCRIPTION: %s \nMEMBERS: %s " % (club.name, club.description, len(club.club_members)))
    

def view_club_members():
    # your code goes here!
    for club in clubs:
        print("NAME: %s \nDESCRIPTION: %s \nMEMBERS: %s " % (club.name, club.description, len(club.club_members)))

    club_to_join = input("Enter the name of the club whose members you'd like to see: ")
    for club in clubs:
        if club_to_join == club.name:
            club.print_member_list()

def application():
    introduction()
    # your code goes here!
    options()