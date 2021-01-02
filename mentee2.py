class Mentee(object):

    #initialize Mentee object with all attributes from mentee responses
    def __init__(self, menteeId, email, firstName, lastName, 
                gender, isLatinx, originCountry, currentLocation, 
                affiliation, position, website, languages, 
                timezone, commsPreference, mentoringArea, motivationStatement, 
                preferredOutcomes, professionalCharacteristics, experienceStatement,
                careerGoals, impactDiscussion, mentoringSkills, researchAreas,
                careerAreas, leadAspiration, leadershipSkills):
    
        # save variables to self
        self.menteeId = menteeId
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.gender = gender
        self.isLatinx = isLatinx
        self.originCountry = originCountry
        self.currentLocation = currentLocation
        self.affiliation = affiliation
        self.position = position
        self.website = website
        self.languages = languages
        self.timezone = timezone
        self.commsPreference = commsPreference
        self.mentoringArea = mentoringArea
        self.motivationStatement = motivationStatement
        self.preferredOutcomes = preferredOutcomes
        self.professionalCharacteristics = professionalCharacteristics
        self.experienceStatement = experienceStatement
        self.careerGoals = careerGoals
        self.impactDiscussion = impactDiscussion
        self.mentoringSkills = mentoringSkills
        self.researchAreas = researchAreas
        self.careerAreas = careerAreas
        self.leadAspiration = leadAspiration
        self.leadershipSkills = leadershipSkills

    def printAll(self):
        print("menteeId" + self.menteeId + "; email" + self.email + "; firstName = " + self.firstName + "; lastName = " + self.lastName +
             "; gender = " + self.gender + "; isLatinx = " + self.isLatinx + "; originCountry = " + self.originCountry +
             "; currentLocation = " + self.currentLocation + "; affiliation = " + self.affiliation + "; position = " + self.position +
             "; website = " + self.website + "; languages = " + self.languages + "; timezone = " + self.timezone +
             "; commsPreference = " + self.commsPreference + "; mentoringArea = " + self.mentoringArea + "; motivationStatement = " + self.motivationStatement +
             "; preferredOutcomes = " + self.preferredOutcomes + "; professionalCharacteristics = " + self.professionalCharacteristics + "; experienceStatement = " + self.experienceStatement +
             "; careerGoals = " + self.careerGoals + "; impactDiscussion = " + self.impactDiscussion + "; mentoringSkills = " + self.mentoringSkills + "; researchAreas = " + self.researchAreas +
             "; careerAreas = " + self.careerAreas + "; leadAspiration = " + self.leadAspiration + "; leadershipSkills = " + self.leadershipSkills
            )

    
