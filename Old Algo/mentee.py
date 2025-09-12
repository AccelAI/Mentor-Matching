# Quick instantiation of a mentee as an object (dict/k:v)
class Mentee(object):    
    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)

    def printAll(self):
        print(self.__dict__)
