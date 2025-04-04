from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value
        def __str__(self):
            return str(self.value)
        
class Name(Field):
    pass

class Phone(Field):
    pass

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
