from operator import and_
import random
import string


class Restaurant () :
    def __init__(self, admin, password):
        self.admin = admin
        self.password = password
        self.admin_psd = []
    
    def admin_rights(self):
        characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
        ## shuffling the characters
        random.shuffle(characters)
        if len(self.password) < 8:
            return f"Weak password"
        
        elif self.password == characters and len(self.password) == 8:
            for i in range(self.password):
                self.admin_psd.append(random.choice(characters[i]))
        
            random.shuffle(self.admin_psd)
            print ("".join(self.admin_psd))
            return f"Strong password"
        else:
            return f"Invalid password"