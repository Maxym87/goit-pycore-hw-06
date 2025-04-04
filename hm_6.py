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

        def add_phone(self, phone: str):
            self.phones.append(Phone(phone))

        def remove_phone(self, phone: str):
            self.phones = [p for p in self.phones if p.value != phone]

        def edit_phone(self, old_phone: str, new_phone: str):
            for phone in self.phones:
                if phone.value == old_phone:
                    phone.value = new_phone
                    return
            raise ValueError("Телефон не знайдений")
