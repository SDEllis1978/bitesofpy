from datetime import datetime

NOW = datetime.now()
name = ''
expires = datetime.second


class Promo:
    def __init__(self, name, expires):
        self.Promo = str(name)
        self.expires = datetime.second
        self.expired = False

        if expires < NOW:
            self.expired = True
        else:
            self.expired = False
