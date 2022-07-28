from operator import and_
import random
import string


class Restaurant () :
    def __init__(self, admin, password):
        self.admin = admin
        self.password = password
        self.admin_psd = []
        self.addWaiter = [] 
    
    def admin_rights(self):
        characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
        ## shuffling the characters
        random.shuffle(characters)
        if len(self.password) < 8 and self.password != characters:
            return f"Weak password"
        elif len(self.password) >= 8 :
            return f"Strong password"
        else:
            return f"Invalid password"
    
    def add_waiter(self, nametag, name, tables):
        self.addWaiter.append({
            'tag': {nametag},
            'name': {name},
            'tables': {tables},
        })

        return self.addWaiter
    

    def view_waiter(self):
        for waiter in self.addWaiter:
            return waiter.lamda()