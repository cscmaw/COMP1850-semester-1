# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self,name,dob):
        self.name = name
        self.dob = dob

    def is_birthday(self):
        if date.today() == self.dob:
            return True
        else:
            return False

today = date.today()
p=Person("Mark",today)

print(p.is_birthday())

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
