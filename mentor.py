# Quick instantiation of a mentor as an object (dict/k:v)
class Mentor(object):    
    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)

    def printAll(self):
        print(self.__dict__)
