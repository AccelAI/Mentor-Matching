class PotentialMatch(object):
    
    # Initialize Potential Match object 
    def __init__(self, mentee, mentor, matchRate, matchPercents):

        # Save a copy of the original image
        self.mentee = mentee 
        
        self.mentor = mentor
        
        self.matchRate = matchRate

        self.matchPercents = matchPercents


    def printAll(self):
        print("[matchRate = " + str(self.matchRate)  + "; matchPercents = " + str(self.matchPercents) +"]")