
def processMentee(sheet, row):

    #Mentee Id
    menteeId = row
    
    #Email
    if sheet.cell(row=row, column=2).value == None:
        email = "" 
    else:
        email = sheet.cell(row=row, column=2).value.strip()

    #First Name
    firstName = sheet.cell(row=row, column=3).value
    #Last Name
    lastName = sheet.cell(row=row, column=4).value

    #Gender
    if sheet.cell(row=row, column=5).value == None:
        gender = ""
    else:
        gender = sheet.cell(row=row, column=5).value[0]

    #LatinX Identity
    menteeSelfIdentification = sheet.cell(row=row, column=6).value
    isLatinx = (True, False)[menteeSelfIdentification == "No"]
                #(if_test_is_false, if_test_is_true)[test]

    #Country of Origin
    originCountry = sheet.cell(row=row, column=7).value

    #Current Location
    currentLocation = sheet.cell(row=row, column=8).value

    #Affiliation
    affiliation = sheet.cell(row=row, column=9).value

    #Current Postition
    position = sheet.cell(row=row, column=10).value

    #Website
    website = sheet.cell(row=row, column=11).value

    #Languages
    menteeLanguages = sheet.cell(row=row, column=12).value
    if menteeLanguages is not None:
        if "," in menteeLanguages:
            languages = menteeLanguages.strip().split(",")
        else:
            languages = []
            languages.append(menteeLanguages.strip())
    else:
        languages = ['English']


    #Timezone
    if sheet.cell(row=row, column=13).value == None:
        timezone = ""
    else:
        timezone = sheet.cell(row=row, column=13).value

    #Communication Preferences
    menteeCommsPreference = sheet.cell(row=row, column=14).value
    if "," in menteeCommsPreference:
        commsPreference = menteeCommsPreference.strip().split(",")
    else:
        commsPreference = []
        commsPreference.append(menteeCommsPreference)

    #Mentoring Area
    menteeMentoringVerticals = sheet.cell(row=row, column=15).value
    if ' e.g., writing, communication,' in menteeMentoringVerticals:
        menteeMentoringVerticals = menteeMentoringVerticals.replace(' e.g., writing, communication,', '')
    if "," in menteeMentoringVerticals:
        mentoringVertical = menteeMentoringVerticals.strip().split(",")
    else:
        mentoringVertical = []
        mentoringVertical.append(menteeMentoringVerticals)

    #Motivation Statement
    motivationStatement = sheet.cell(row=row, column=16).value

    #Preffered Outcomes
    preferredOutcomes = sheet.cell(row=row, column=17).value

    #Professional Characteristics
    professionalCharacteristics = sheet.cell(row=row, column=18).value

    #Experience Statement
    experienceStatement = sheet.cell(row=row, column=19).value

    #Career Goals
    careerGoals = sheet.cell(row=row, column=20).value

    #Open to Impact Discussion?
    menteeImpactDiscussion = sheet.cell(row=row, column=21).value
    if menteeImpactDiscussion == "No":
        impactDiscussion = False
    else:
        impactDiscussion = True

    #Skills Needing Improvement
    menteeMentoringSkills = sheet.cell(row=row, column=22).value
    if menteeMentoringSkills == None:
        menteeMentoringSkills = ""
    if "," in menteeMentoringSkills:
        mentoringSkills = menteeMentoringSkills.strip().split(",")
    else:
        mentoringSkills = []
        mentoringSkills.append(menteeMentoringSkills)

    
    #Research Areas Needing Improvement
    menteeResearchAreas = sheet.cell(row=row, column=23).value
    if menteeResearchAreas == None:
        menteeResearchAreas = ""
    if "," in menteeResearchAreas:
        researchAreas = menteeResearchAreas.strip().split(",")
    else:
        researchAreas = []
        researchAreas.append(menteeResearchAreas)

    #Career Areas Needing Improvement
    menteeCareerAreas = sheet.cell(row=row, column=24).value
    if menteeCareerAreas == None:
        menteeCareerAreas = ""
    if "," in menteeCareerAreas:
        careerAreas = menteeCareerAreas.strip().split(",")
    else:
        careerAreas = []
        careerAreas.append(menteeCareerAreas)

    #Do they aspire to lead?
    menteeLeadAspiration = sheet.cell(row=row, column=25).value
    leadAspiration = (True, False)[menteeLeadAspiration == "No"]
                    #(if_test_is_false, if_test_is_true)[test]

    #Leadership Skills Needing Improvement
    menteeLeadershipSkills = sheet.cell(row=row, column=26).value
    if menteeLeadershipSkills == None:
        menteeLeadershipSkills = ""
    if "," in menteeLeadershipSkills:
        leadershipSkills = menteeLeadershipSkills.strip().split(",")
    else:
        leadershipSkills = []
        leadershipSkills.append(menteeLeadershipSkills)

    cleanRow = {"menteeId": menteeId, 
                "email": email, 
                "firstName": firstName, 
                "lastName": lastName, 
                "gender": gender, 
                "isLatinx": isLatinx, 
                "originCountry":originCountry, 
                "currentLocation": currentLocation, 
                "affiliation": affiliation, 
                "position": position, 
                "website": website, 
                "languages": set(languages), 
                "timezone": timezone, 
                "commsPreference": commsPreference, 
                "mentoringVertical": set(mentoringVertical),
                "motivationStatement": motivationStatement, 
                "preferredOutcomes": preferredOutcomes, 
                "professionalCharacteristics": professionalCharacteristics,
                "experienceStatement": experienceStatement, 
                "careerGoals": careerGoals, 
                "impactDiscussion": impactDiscussion, 
                "mentoringSkills": set(mentoringSkills),
                "researchAreas": set(researchAreas), 
                "careerAreas": set(careerAreas), 
                "leadAspiration": leadAspiration, 
                "leadershipSkills": set(leadershipSkills)
                }
    return cleanRow

def processMentor(sheet, row):
    """
    Function to take in mentor information from a spreadsheet
    row by row and to clean the data and store it as a dictionary
    to instantiate a mentor object
    """
    #mentor id
    mentorId = row

    #metor email address
    mentorEmailAddress = sheet.cell(row=row, column=2).value
    if mentorEmailAddress is not None:
        email = mentorEmailAddress.strip()
    else:
        email = ""

    #mentor firstname
    if sheet.cell(row=row, column=3).value is not None:
        firstName = sheet.cell(row=row, column=3).value
    else:
        firstName = ""

    #mentor lastname
    if sheet.cell(row=row, column=4).value is not None:
        lastName = sheet.cell(row=row, column=4).value
    else:
        lastName = ""

    #mentor gender
    if sheet.cell(row=row, column=5).value is not None:
        gender = sheet.cell(row=row, column=5).value
    else:
        gender = ""

    #mentor self-identified as LatinX
    isLatin = sheet.cell(row=row, column=6).value
    if isLatin == "Yes" or isLatin == "Maybe":
        isLatinx = True
    else:
        isLatinx = False

    #mentor country of origin
    if sheet.cell(row=row, column=7).value is not None:
        originCountry = sheet.cell(row=row, column=7).value
    else:
        originCountry = ""

    #mentor current location (city, state, country)
    if sheet.cell(row=row, column=8).value is not None:
        currentLocation = sheet.cell(row=row, column=8).value
    else:
       currentLocation = ""

    #mentor current position (career)
    if sheet.cell(row=row, column=9).value is not None:
        position = sheet.cell(row=row, column=9).value
    else:
        position = ""
    #mentor current organization (career)
    if sheet.cell(row=row, column=10).value is not None:
        affiliation = sheet.cell(row=row, column=10).value
    else:
        affiliation = ""
    
    #mentor seniority level
    if sheet.cell(row=row, column=11).value is not None:
        seniority = sheet.cell(row=row, column=11).value
    else:
        seniority = ""
 
    #mentor googles cholar or linkenin or personal site
    if sheet.cell(row=row, column=12).value is not None:
        website = sheet.cell(row=row, column=12).value.strip()
    else:
        website = ""

    #mentor preferred languages
    if sheet.cell(row=row, column=13).value is not None:
        if ',' in sheet.cell(row=row, column=13).value:
            languages = sheet.cell(row=row, column=13).value.split(',')
        else:
            languages = []
            languages.append(sheet.cell(row=row, column=13).value)
    else:
        languages = ['English']
 
    #mentor preferred timezone
    if sheet.cell(row=row, column=14).value is not None:
        timezone = sheet.cell(row=row, column=14).value
    else:
        timezone = ""
    #mentor preferred communication channel
    commsResponse = sheet.cell(row=row, column=15).value
    if commsResponse is not None:
        if ' (e.g., Zoom)' in commsResponse:
            commsResponse = commsResponse.replace(' (e.g., Zoom)', '')
        if ' (e.g., Slack)' in commsResponse:
            commsResponse = commsResponse.replace(' (e.g., Slack)', '')
        if ',' in commsResponse:
            commsPreference = commsResponse.split(',')
        else:
            commsPreference = []
            commsPreference.append(commsResponse)
    else:
        commsPreference =  []

    #mentor area of mentorship
    mentorAreas = sheet.cell(row=row, column=16).value
    if ' e.g., writing, communication,' in mentorAreas:
        mentorAreas = mentorAreas.replace(' e.g., writing, communication,', '')
    if ',' in mentorAreas:
        mentoringVertical = mentorAreas.split(',')
    else:
        mentoringVertical = []
        mentoringVertical.append(mentorAreas)
    
    #mentor weekly time commitment
    commitment = sheet.cell(row=row, column=17).value
    menteeLimit = int(list(filter(str.isdigit, commitment))[0])
    
    #mentor preferrence for characteristics in a mentee
    preferredMenteeChars = sheet.cell(row=row, column=18).value
    
    #mentor research tools available
    tools = sheet.cell(row=row, column=19).value
    if tools is not None:
        if ',' in tools:
            toolsAvailable = tools.split(',')
        else:
            toolsAvailable = []
            toolsAvailable.append(tools)
    else:
        toolsAvailable = []
    
    #mentor specific preferrences for accepting a mentee
    preferredMenteePrefs = sheet.cell(row=row, column=20).value
    
    #mentor choices for skills they would like to help a mentee improve
    skillz = sheet.cell(row=row, column=21).value
    if skillz is not None:
        if ',' in skillz:
            mentorSkills = skillz.split(',')
        else:
            mentorSkills = []
            mentorSkills.append(skillz)
    else:
        mentorSkills = []

    #mentor research areas that they could help mentee improve
    ra = sheet.cell(row=row, column=22).value
    mentoringResearchAreas = []
    if ra is not None:
        if ' (Javascript, React)' in ra:
            ra = ra.replace(' (Javascript, React)', '')
        if ',' in ra:
            mentoringResearchAreas = ra.split(',')
        else:
            mentoringResearchAreas.append(ra)

    #mentor forms of career advice
    ca = sheet.cell(row=row, column=23).value
    mentoringCareerAdvice = []
    if ca is not None:
        if ',' in ca:
            mentoringCareerAdvice = ca.split(',')
        else:
            mentoringCareerAdvice.append(ca)

    #does mentor currently lead a project
    leading = sheet.cell(row=row, column=24).value
    if leading is None:
        leading = "No"
    leadingProject = (True, False)[leading == "No"]
    #(if_test_is_false, if_test_is_true)[test]

    #mentor skills they would like to mentor
    ls = sheet.cell(row=row, column=25).value
    leadershipSkills = []
    if ls is not None:
        if ',' in ls:
            leadershipSkills = ls.split(',')
        else:
            leadershipSkills.append(ls)

    cleanRow = {"mentorId": mentorId, 
                "email": email, 
                "firstName": firstName, 
                "lastName": lastName, 
                "gender": gender, 
                "isLatinx": isLatinx, 
                "originCountry":originCountry, 
                "currentLocation": currentLocation, 
                "affiliation": affiliation, 
                "position": position, 
                "seniority": seniority,
                "website": website, 
                "languages": set(languages), 
                "timezone": timezone, 
                "commsPreference": commsPreference, 
                "mentoringVertical": set(mentoringVertical),
                "menteeLimit": menteeLimit, 
                "menteeCharacteristics": preferredMenteeChars,
                "familiarTools": toolsAvailable,
                "mentorPreferrences": preferredMenteePrefs,
                "mentoringSkills": set(mentorSkills),
                "researchAreas": set(mentoringResearchAreas), 
                "careerAreas": set(mentoringCareerAdvice), 
                "leading Projects": leadingProject, 
                "leadershipSkills": set(leadershipSkills)
                }
    return cleanRow



def mentorMatch(mentee, mentorList):
    potentialMatches = {}
    for mentor in mentorList:
        matchPercents = {}

        #Check Language Matches 
        languages = mentee.languages
        #english is the default if none selected
        langIntersect = languages.intersection(mentor.languages)
        if len(langIntersect) == 0:
           continue
        else:
            langMatch = len(langIntersect)/(len(languages) + len(mentor.languages)/2) * 100
            matchPercents.update(langMatch = langMatch)

        #Check Mentoring Areas mentee wants to strengthen
        mentoringVerticals = mentee.mentoringVertical
        mentoringVerticalIntersect = mentoringVerticals.intersection(mentor.mentoringVertical)
        if len(mentoringVerticalIntersect) == 0:
            continue
        else:
            mentoringVerticalMatch = len(mentoringVerticalIntersect)/(len(mentoringVerticals) + len(mentor.mentoringVertical)/2) * 100
            matchPercents.update(mentoringVerticalMatch = mentoringVerticalMatch)

        
        #Check intersects of Skills
        if 'Strengthening skills' in mentoringVerticalIntersect:
            mentoringSkills = mentee.mentoringSkills
            mentoringSkillsIntersect = mentoringSkills.intersection(mentor.mentoringSkills)
            if len(mentoringSkillsIntersect) == 0:
                pass
            else:
                mentoringSkillsMatch = len(mentoringSkillsIntersect)/(len(mentoringSkills) + len(mentor.mentoringSkills)/2) * 100
                matchPercents.update(mentoringSkillsMatch = mentoringSkillsMatch)


        #Check intersects of Research
        if 'Research Guidance (AI Verticals)' in mentoringVerticalIntersect:
            researchAreas = mentee.researchAreas
            researchAreasIntersect = researchAreas.intersection(mentor.researchAreas)
            if len(researchAreasIntersect) == 0:
                pass
            else:
                researchAreasMatch = len(researchAreasIntersect)/(len(researchAreas) + len(mentor.researchAreas)/2) * 100
                matchPercents.update(researchAreasMatch = researchAreasMatch)


        #Check intersects of Career
        if 'Career Guidance' in mentoringVerticalIntersect:
            careerAreas = mentee.careerAreas
            careerAreasIntersect = careerAreas.intersection(mentor.careerAreas)
            if len(careerAreasIntersect) == 0:
                pass
            else:
                careerAreasMatch = len(careerAreasIntersect)/(len(careerAreas) + len(mentor.careerAreas)/2) * 100
                matchPercents.update(careerAreasMatch = careerAreasMatch)

        #Check intersects of Leadership
        if 'Management / Leadership' in mentoringVerticalIntersect:
            leadershipSkills = mentee.leadershipSkills
            leadershipSkillsIntersect = leadershipSkills.intersection(mentor.leadershipSkills)
            if len(leadershipSkillsIntersect) == 0:
                pass
            else:
                leadershipSkillsMatch = len(leadershipSkillsIntersect)/(len(leadershipSkills) + len(mentor.leadershipSkills)/2) * 100
                matchPercents.update(leadershipSkillsMatch = leadershipSkillsMatch)

        #Average Match Scores
        matchRate = float(0)

        for value in matchPercents.values():
            matchRate += value

        matchRate /= len(matchPercents.values())
        matchPercents.update(matchRate = matchRate)

        potentialMatches.update({mentor.mentorId: matchPercents})
    
    return potentialMatches




        


        
        
