Home_town_of_my_family = 'Batticalo'  # Static variable

class Grandparent:
    # Encapsulation with private variable
    def __init__(self, name, birth_year, occupation, relation, number_of_children):
        self.__name = name  # Private instance variable
        self.birth_year = birth_year
        self.occupation = occupation
        self.relation = relation
        self.number_of_children = number_of_children        

    def intro(self):  # Method overriding will happen in child classes
        if self.relation.lower() == "grand father":
            return f"{self.__name} is my {self.relation}. He was born in {self.birth_year}."
        elif self.relation.lower() == "grand mother":
            return f"{self.__name} is my {self.relation}. She was born in {self.birth_year}."

    def tell_story(self):
        if self.relation.lower() == "grand father":
            return f"He worked as {self.occupation} and he has {self.number_of_children} children."
        elif self.relation.lower() == "grand mother":
            return f"She worked as {self.occupation} and she has {self.number_of_children} children."

    # Getter for encapsulation
    def get_name(self):
        return self.__name


# Multi-level inheritance: Parent inherits from Grandparent
class Parent(Grandparent):
    def __init__(self, name, birth_year, occupation, education, hobby):
        super().__init__(name, birth_year, occupation, "Parent", 0)  
        self.education = education
        self.hobby = hobby  

    # Method overriding
    def intro(self):
        return f"{self.get_name()} is my parent with a {self.education} background."

    def give_advice(self):
        return f"Focus on {self.hobby} to relax!"


# Hierarchical inheritance: Child inherits from Parent
class Child(Parent):
    # Local variable used in method
    def __init__(self, name, birth_year, school, hobby, favorite_game):
        local_status = "Initializing child"  # Local variable
        print(local_status)
        super().__init__(name, birth_year, "Student", "High School", hobby)
        self.school = school
        self.favorite_game = favorite_game

    # Method overriding (polymorphism)
    def intro(self):
        if self.get_name().lower() == "musharraf":  
            return f"Hi, I’m {self.get_name()}, studying at {self.school}, and I love {self.favorite_game}!"
        else:
            return f"{self.get_name()} is my brother, studying at {self.school}, and he loves {self.favorite_game}!"

    def play_game(self):
        return f"Playing {self.favorite_game} now!"


# Multiple inheritance: Sibling inherits from Child and another class
class Talent:
    def __init__(self, skill):
        self.skill = skill

    def show_talent(self):
        return f"His talent is {self.skill}."


class Sibling(Child, Talent):
    def __init__(self, name, birth_year, school, hobby, favorite_game, skill):
        Child.__init__(self, name, birth_year, school, hobby, favorite_game)
        Talent.__init__(self, skill)

    # Method overloading simulation (Python doesn’t support true overloading, so we use default arguments)
    def play_game(self, hours=1):
        return f"Playing {self.favorite_game} for {hours} hour(s)!"


# Creating family tree instances
grandpa1 = Grandparent("Shaheed", "1939", "Business man", "grand father", 3)
grandpa2 = Grandparent("Fakeer", "1949", "Business man", "grand father", 2)
grandma1 = Grandparent("Aysha", "1936", "Teacher", "grand mother", 3)
grandma2 = Grandparent("Saleema", "1956", "Business woman", "grand mother", 2)
mother = Parent("Mufeetha", 45, "House wife", "GCE(A/L)", "Sewing")
father = Parent("Rauf", 56, "Officer", "SLAS", "Gardening")
me = Child("Musharraf", 24, "Horizon Campus", "Coding", "Call of Duty")
sibling = Sibling("Munsif", 20, "Colombo University", "Reading", "Halo", "Singing")

# Displaying family tree
print(f"All my family members' hometown is: {Home_town_of_my_family}")
# Displaying 1st grandparents
print(grandpa1.intro())
print(grandpa1.tell_story())
print(grandma1.intro())
print(grandma1.tell_story())
# Displaying 2nd grandparents
print(grandpa2.intro())
print(grandpa2.tell_story())
print(grandma2.intro())
print(grandma2.tell_story())
# Displaying my parents
print(father.intro())
print(father.give_advice())
print(mother.intro())
print(mother.give_advice())
# Displaying me and my sibling
print(me.intro())
print(me.play_game())
print(sibling.intro())
print(sibling.play_game(2))  # Polymorphism with method overloading
print(sibling.show_talent())  # Multiple inheritance
