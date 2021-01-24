class PotentialMatch(object):
    
    # Initialize Potential Match object 
    def __init__(self, mentor, matchRate, matchPercents):

        # Save a copy of the original image
        self.mentor = mentor
        
        self.matchRate = matchRate

        self.matchPercents = matchPercents


    def printAll(self):
        print("[matchRate = " + str(self.matchRate)  + "; matchPercents = " + str(self.matchPercents) +"]")