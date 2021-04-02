from potentialMatch import *

def processMentee(sheet, row):

    #Mentee Id
    menteeId = row

    #Name
    name = sheet.cell(row=row, column=3).value.split(' ', 1)
    firstName = name[0]
    lastName = name[1]

    #Email
    if sheet.cell(row=row, column=2).value == None:
        email = "" 
    else:
        email = sheet.cell(row=row, column=2).value.strip()

    #Gender
    if sheet.cell(row=row, column=4).value == None:
        gender = ""
    else:
        gender = sheet.cell(row=row, column=4).value.strip()

    #LatinX Identity
    menteeSelfIdentification = sheet.cell(row=row, column=5).value
    isLatinx = (True, False)[menteeSelfIdentification == "No" or menteeSelfIdentification == "Ally"]
                #(if_test_is_false, if_test_is_true)[test]

    #Country of Origin
    originCountry = sheet.cell(row=row, column=6).value

    #Current Location
    currentLocation = sheet.cell(row=row, column=7).value

    #Affiliation
    affiliation = sheet.cell(row=row, column=8).value

    #Current Postition
    position = sheet.cell(row=row, column=9).value

    #Website
    website = sheet.cell(row=row, column=10).value

    #Languages
    menteeLanguages = sheet.cell(row=row, column=11).value
    if menteeLanguages is not None:
        if "," in menteeLanguages:
            languages = menteeLanguages.strip().split(",")
        else:
            languages = []
            languages.append(menteeLanguages.strip())
    else:
        languages = ['English']


    #Timezone
    if sheet.cell(row=row, column=12).value == None:
        timezone = ""
    else:
        timezone = sheet.cell(row=row, column=12).value


    #Mentoring Area
    menteeMentoringVerticals = sheet.cell(row=row, column=13).value
    if ' e.g., writing, communication,' in menteeMentoringVerticals:
        menteeMentoringVerticals = menteeMentoringVerticals.replace(' e.g., writing, communication,', '')
    if ' (Writing or Communication or Engineering)' in menteeMentoringVerticals:
        menteeMentoringVerticals = menteeMentoringVerticals.replace(' (Writing or Communication or Engineering)', '')
    if ' (New Degree or Job or Promotion)' in menteeMentoringVerticals:
        menteeMentoringVerticals = menteeMentoringVerticals.replace(' (New Degree or Job or Promotion)', '')
    if 'Improve as a Reviewer of Research Papers' in menteeMentoringVerticals:
        menteeMentoringVerticals = menteeMentoringVerticals.replace('Improve as a Reviewer of Research Papers', 'Review Research')
    if "," in menteeMentoringVerticals:
        mentoringVertical = menteeMentoringVerticals.strip().split(", ")
        for item in menteeMentoringVerticals:
            item = item.lstrip()
    else:
        mentoringVertical = []
        mentoringVertical.append(menteeMentoringVerticals.lstrip())

    #Motivation Statement
    motivationStatement = sheet.cell(row=row, column=14).value

    #Preffered Outcomes
    prefOutcomes = sheet.cell(row=row, column=15).value
    if ',' in prefOutcomes:
        preferredOutcomes = prefOutcomes.split(',')
    else:
        preferredOutcomes = prefOutcomes

    #Experience Statement
    expStatement = sheet.cell(row=row, column=16).value
    if expStatement is None:
        expStatement = 'No'
    experienceStatement = (True, False)[expStatement == "No"]
    #(if_test_is_false, if_test_is_true)[test]

    #Career Goals
    careerGoals = sheet.cell(row=row, column=17).value

    #Skills Needing Improvement
    menteeMentoringSkills = sheet.cell(row=row, column=18).value
    if menteeMentoringSkills is None:
        mentoringSkills = []
    elif "," in menteeMentoringSkills:
        mentoringSkills = menteeMentoringSkills.split(",")
    else:
        mentoringSkills = []
        mentoringSkills.append(menteeMentoringSkills)

    
    #Research Areas Needing Improvement
    #This may need (extra / details) stripped out
    menteeResearchAreas = sheet.cell(row=row, column=19).value
    if menteeResearchAreas == None:
        menteeResearchAreas = ""
    if "," in menteeResearchAreas:
        researchAreas = menteeResearchAreas.strip().split(",")
    else:
        researchAreas = []
        researchAreas.append(menteeResearchAreas)

    #Career Areas Needing Improvement
    menteeCareerAreas = sheet.cell(row=row, column=20).value
    if menteeCareerAreas == None:
        menteeCareerAreas = ""
    if "," in menteeCareerAreas:
        careerAreas = menteeCareerAreas.strip().split(",")
    else:
        careerAreas = []
        careerAreas.append(menteeCareerAreas)


    #Conferences mentee would like to present at
    confPref = sheet.cell(row=row, column=27).value
    otherConfPref = sheet.cell(row=row, column=28).value
    if confPref is None:
        menteeConfPref = ""
    if ',' in confPref:
        menteeConfPref = confPref.strip().split(', ')
    else:
        menteeConfPref = []
        menteeConfPref.append(confPref)
    if otherConfPref is not None:
        if ',' in otherConfPref:
            otherConfPref = otherConfPref.strip().split(', ')
            menteeConfPref = menteeConfPref + otherConfPref
        else:
            menteeConfPref.append(otherConfPref)

    #publication in AI Journals of high impact
    pubHI = sheet.cell(row=row, column=26).value
    if pubHI == 'No' or pubHI is None:
        menteePublishedHighImpact = False
    else:
        menteePublishedHighImpact = True

    #publication in top tier ai conferences
    pubTT = sheet.cell(row=row, column=24).value
    if pubTT is None or pubTT == "No":
        menteePubTopTier = False
    else:
        menteePubTopTier = True

    #peer reviewd publications in workshops
    workshops = sheet.cell(row=row, column=22).value
    if workshops == 'never' or workshops is None:
        menteePubWorkshop = False
    else:
        menteePubWorkshop = True
    
    #served as a peer reviewer before
    reviewer = sheet.cell(row=row, column=21).value
    if reviewer is None or reviewer == 'never':
        menteePeerReviewer = False
    else:
        menteePeerReviewer = True

    #Servered as a reviewer for a journal of high impact
    reviewerHI = sheet.cell(row=row, column=25).value
    if reviewerHI is None or reviewerHI == 'never':
        menteeReviewHI = False
    else:
        menteeReviewHI = True

    #Serverd as a reviewer in top tier ai conference
    reviewerTT = sheet.cell(row=row, column=23).value
    if reviewerTT is None or reviewerTT == 'never':
        menteeRevTopTier = False
    else:
        menteeRevTopTier = True

    
    #Reviewer's ranking on their personal statement
    menteeStatementRank = sheet.cell(row=row, column=30).value

    #Mentee ranking factors for preferential placement
    if menteeStatementRank is not None:
        assignmentPriority = int(menteeStatementRank)
    else:
        assignmentPriority = 0

    if 'Career Professional' in position:
        assignmentPriority += 10
    elif 'Senior Ph.D.' in position:
        assignmentPriority += 10
    elif 'Junior Ph.D.' in position:
        assignmentPriority += 6
    elif 'Graduate Student ' in position:
        assignmentPriority += 4
    elif 'Undergraduate Student' in position:
        assignmentPriority += 2
    if menteePublishedHighImpact:
        assignmentPriority += 2
    if menteePubTopTier:
        assignmentPriority += 2
    if menteePubWorkshop:
        assignmentPriority += 1
    if menteePeerReviewer:
        assignmentPriority += 1
    if menteeReviewHI:
        assignmentPriority += 2
    if menteeRevTopTier:
        assignmentPriority += 2

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
                "mentoringVertical": set(mentoringVertical),
                "motivationStatement": motivationStatement, 
                "preferredOutcomes": preferredOutcomes, 
                "experienceStatement": experienceStatement, 
                "careerGoals": careerGoals,  
                "mentoringSkills": set(mentoringSkills),
                "researchAreas": set(researchAreas), 
                "careerAreas": set(careerAreas), 
                "menteeConfPref": set(menteeConfPref),
                "menteePublishedHighImpact": menteePublishedHighImpact,
                "menteePubTopTier": menteePubTopTier,
                "menteePubWorkshop": menteePubWorkshop,
                "menteePeerReviewer": menteePeerReviewer,
                "menteeReviewHI": menteeReviewHI,
                "menteeReviewTopTier": menteeRevTopTier,
                "menteeStatementRank": menteeStatementRank,
                "assignmentPriority": assignmentPriority
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

    #mentor name
    if sheet.cell(row=row, column=3).value is not None:
        Name = sheet.cell(row=row, column=3).value.split(' ', 1)
        firstName = Name[0]
        lastName = Name[1]
    else:
        Name = ""

    #mentor gender
    if sheet.cell(row=row, column=4).value is not None:
        gender = sheet.cell(row=row, column=4).value
    else:
        gender = ""

    #mentor self-identified as LatinX
    isLatin = sheet.cell(row=row, column=5).value
    if isLatin == "Yes" or isLatin == "Maybe":
        isLatinx = True
    else:
        isLatinx = False

    #mentor country of origin
    if sheet.cell(row=row, column=6).value is not None:
        originCountry = sheet.cell(row=row, column=6).value
    else:
        originCountry = ""

    #mentor current location (city, state, country)
    if sheet.cell(row=row, column=7).value is not None:
        currentLocation = sheet.cell(row=row, column=7).value
    else:
       currentLocation = ""
    
    #mentor current organization (career)
    if sheet.cell(row=row, column=8).value is not None:
        affiliation = sheet.cell(row=row, column=8).value
    else:
        affiliation = ""
    
    #mentor seniority level
    if sheet.cell(row=row, column=9).value is not None:
        seniority = sheet.cell(row=row, column=9).value
    else:
        seniority = ""
 
    #mentor googles scholar or linkenin or personal site
    if sheet.cell(row=row, column=10).value is not None:
        website = sheet.cell(row=row, column=10).value.strip()
    else:
        website = ""

    #mentor preferred languages
    if sheet.cell(row=row, column=11).value is not None:
        if ',' in sheet.cell(row=row, column=11).value:
            languages = sheet.cell(row=row, column=11).value.split(',')
        else:
            languages = []
            languages.append(sheet.cell(row=row, column=11).value)
    else:
        languages = ['English']
 
    #mentor preferred timezone
    if sheet.cell(row=row, column=12).value is not None:
        timezone = sheet.cell(row=row, column=12).value
    else:
        timezone = ""

    #mentor area of mentorship
    mentorAreas = sheet.cell(row=row, column=14).value
    if ' e.g., writing, communication,' in mentorAreas:
        mentorAreas = mentorAreas.replace(' e.g., writing, communication,', '')
    if ' (Writing or Communication or Engineering)' in mentorAreas:
        mentorAreas = mentorAreas.replace(' (Writing or Communication or Engineering)', '')
    if ' (New Degree or Job or Promotion)' in mentorAreas:
        mentorAreas = mentorAreas.replace(' (New Degree or Job or Promotion)', '')
    if 'Reviewing Research Papers' in mentorAreas:
        mentorAreas = mentorAreas.replace('Reviewing Research Papers', 'Review Research')
    if ',' in mentorAreas:
        mentoringVertical = mentorAreas.strip().split(', ')
        for item in mentoringVertical:
            item = item.lstrip()
    else:
        mentoringVertical = []
        mentoringVertical.append(mentorAreas.lstrip())
    
    #mentor weekly time commitment
    commitment = sheet.cell(row=row, column=15).value
    menteeLimit = int(list(filter(str.isdigit, commitment))[0])

    #instantiate mentor match list
    if menteeLimit < 1:
        mentorMatches = None
    elif menteeLimit < 2:
        mentorMatches = [None]
    else:
        mentorMatches = [None, None]

    
    #mentor preferrence for characteristics in a mentee
    preferredMenteeChars = sheet.cell(row=row, column=16).value

    #mentor preferrence for outcomes of mentoring
    outcomes = sheet.cell(row=row, column=18).value
    extra = sheet.cell(row=row, column=19).value
    if outcomes is not None:
        if ',' in outcomes:
            mentorPrefOutcomes = outcomes.split(',')
        else:
            mentorPrefOutcomes = []
            mentorPrefOutcomes.append(outcomes)
    else:
        mentorPrefOutcomes = []
    if extra is not None:
        mentorPrefOutcomes.append(extra)

    #Mentor discussing impact post program
    discuss = sheet.cell(row=row, column=20).value
    if discuss == "Yes" or discuss == "Maybe":
        mentorDiscuss = True
    else:
        mentorDiscuss = False

    
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

    #previously reviewed research 
    pre = sheet.cell(row=row, column=24).value
    if pre is None:
        previousReviewer = False
    else:
        pre = pre.lower()
        if pre == 'no' or pre == 'never':
            previousReviewer = False
        else:
            previousReviewer = True

    #does mentor have published papers
    published = sheet.cell(row=row, column=25).value
    if published is None:
        published = 'No'
    mentorPublished = (True, False)[published == "No"]
    #(if_test_is_false, if_test_is_true)[test]

    #previously reviewer at top research conferences 
    pre = sheet.cell(row=row, column=26).value
    if pre is None:
        topReviewer = False
    else:
        pre = pre.lower()
        if pre == 'no' or pre == 'never':
            topReviewer = False
        else:
            topReviewer = True

    #does mentor have published papers in Top Tier conferences
    ttPublished = sheet.cell(row=row, column=27).value
    if ttPublished is None:
        ttPublished = 'No'
    mentorTTPublished = (True, False)[published == "No"]
    #(if_test_is_false, if_test_is_true)[test]

    #previously reviewer for journals of High impact 
    revHI = sheet.cell(row=row, column=28).value
    if revHI is None:
        revHighImpact = False
    else:
        revHI = revHI.lower()
        if revHI == 'no' or revHI == 'never':
            revHighImpact = False
        else:
            revHighImpact = True

    #does mentor have published papers in Journals of High Impact
    pubHI = sheet.cell(row=row, column=29).value
    if pubHI is None:
        pubHI = 'No'
    mentorPubHI = (True, False)[pubHI == "No"]
    #(if_test_is_false, if_test_is_true)[test]

    # conferences mentor would like to line mentorship up with
    conferencePref = sheet.cell(row=row, column=30).value
    conferenceExtra = sheet.cell(row=row, column=31).value
    if conferencePref is None:
        mentorConfPref = []
    else:
        mentorConfPref = conferencePref.split(', ')
    if conferenceExtra is not None:
        if ',' in conferenceExtra:
            conferenceExtra = conferenceExtra.strip().split(', ')
            mentorConfPref = mentorConfPref + conferenceExtra
        else:
            mentorConfPref.append(conferenceExtra)

    cleanRow = {"mentorId": mentorId, 
                "email": email, 
                "firstName": firstName, 
                "lastName": lastName, 
                "gender": gender, 
                "isLatinx": isLatinx, 
                "originCountry":originCountry, 
                "currentLocation": currentLocation, 
                "affiliation": affiliation,
                "seniority": seniority,
                "website": website, 
                "languages": set(languages), 
                "timezone": timezone, 
                "mentoringVertical": set(mentoringVertical),
                "menteeLimit": menteeLimit,
                "mentorMatches": mentorMatches, 
                "menteeCharacteristics": preferredMenteeChars,
                "mentorPrefOutcomes": mentorPrefOutcomes,
                "mentorDiscuss": mentorDiscuss,
                "mentoringSkills": set(mentorSkills),
                "researchAreas": set(mentoringResearchAreas), 
                "careerAreas": set(mentoringCareerAdvice),
                "previousReviewer": previousReviewer,
                "mentorPublished": mentorPublished,
                "topReviewer": topReviewer,
                "mentorTopTierPublished": mentorTTPublished,
                "reviewedHighImpact": revHighImpact,
                "mentorPublishedHI": mentorPubHI,
                "mentorConfPref": set(mentorConfPref)
                }
    return cleanRow



def mentorMatch(mentee, mentorList):
    menteePotentialMatches = {}
  
    for mentor in mentorList:
        matchPercents = {}
        #Check Language Matches 
        languages = mentee.languages
        #english is the default if none selected
        langIntersect = languages.intersection(mentor.languages)
        if len(langIntersect) == 0:
           continue
        else:
            langMatch = (len(langIntersect)/(len(languages) + len(mentor.languages)/2) * 100)
            matchPercents.update(langMatch = round(langMatch, 2))

        #Check Mentoring Areas mentee wants to strengthen
        mentoringVerticals = mentee.mentoringVertical
        mentoringVerticalIntersect = mentoringVerticals.intersection(mentor.mentoringVertical)
        if len(mentoringVerticalIntersect) == 0:
            continue
        else:
            mentoringVerticalMatch = (len(mentoringVerticalIntersect)/(len(mentoringVerticals) + len(mentor.mentoringVertical)/2) * 100)
            matchPercents.update(mentoringVerticalMatch = round(mentoringVerticalMatch, 2))

        
        #Check intersects of Skills
        if 'Strengthening skills' in mentoringVerticalIntersect:
            mentoringSkills = mentee.mentoringSkills
            mentoringSkillsIntersect = mentoringSkills.intersection(mentor.mentoringSkills)
            if len(mentoringSkillsIntersect) == 0:
                matchPercents.update(mentoringSkillsMatch = 0)
            else:
                mentoringSkillsMatch = (len(mentoringSkillsIntersect)/(len(mentoringSkills) + len(mentor.mentoringSkills)/2) * 100)
                matchPercents.update(mentoringSkillsMatch = round(mentoringSkillsMatch, 2))


        #Check intersects of Research
        if 'Research Guidance (AI Verticals)' in mentoringVerticalIntersect:
            researchAreas = mentee.researchAreas
            researchAreasIntersect = researchAreas.intersection(mentor.researchAreas)
            if len(researchAreasIntersect) == 0:
                matchPercents.update(researchAreasMatch = 0)
            else:
                researchAreasMatch = (len(researchAreasIntersect)/(len(researchAreas) + len(mentor.researchAreas)/2) * 100)
                matchPercents.update(researchAreasMatch = round(researchAreasMatch, 2))


        #Check intersects of Career
        if 'Career Guidance' in mentoringVerticalIntersect:
            careerAreas = mentee.careerAreas
            careerAreasIntersect = careerAreas.intersection(mentor.careerAreas)
            if len(careerAreasIntersect) == 0:
                matchPercents.update(careerAreasMatch = 0)
            else:
                careerAreasMatch = (len(careerAreasIntersect)/(len(careerAreas) + len(mentor.careerAreas)/2) * 100)
                matchPercents.update(careerAreasMatch = round(careerAreasMatch, 2))

        #Check intersects of Review Research
        if 'Review Research' in mentoringVerticalIntersect:
            reviewerMatch = 100
        else:
            reviewerMatch = 0
        matchPercents.update(reviewerMatch = reviewerMatch)

        
        #Check intersects of Conference Preferences
        confPref = mentee.menteeConfPref
        confPrefIntersect = confPref.intersection(mentor.mentorConfPref)
        if len(confPrefIntersect) == 0:
            continue
        else:
            confPrefMatch = (len(confPrefIntersect)/(len(confPref) + len(mentor.mentorConfPref)/2)*100)
            matchPercents.update(confPrefMatch = round(confPrefMatch, 2))



        #Average Match Scores
        matchRate = float(0)
        # potentialMatches = []
        for value in matchPercents.values():
            matchRate += value

        matchRate /= (len(matchPercents.values()))
        matchPercents.update(matchRate = round(matchRate, 2))

        menteePotentialMatches.update({mentor.mentorId: matchPercents})

    
    return menteePotentialMatches

def mentorMatches():

     #Find Max matches for mentor
        matches = [x.matchRate for x in potentialMatches]
        print("Mentee {} matches: {}".format(mentee.firstName, matches))
        maxMatch = max(matches)
        print("Mentee {} maxmatch: {}".format(mentee.firstName, maxMatch))


def acceptableMatches(potentialMatches):
    """
    This function finds matches for mentee to mentor
    with the limiting factor being that the match %
    must be within 20% of the best match
    """

    matches = {}
    matchPercents = []

    # Create a list of all matched mentors and the masted match rate
    for mentor, matchObject in potentialMatches.items():
        matches[matchObject['matchRate']] = mentor
        matchPercents.append(float(matchObject['matchRate']))
    matchMax = max(matchPercents)
    killKeys = []
    for key in matches.keys():
        if key < (matchMax * 0.8):
            killKeys.append(key)
    for key in killKeys:
        del matches[key]
    for match in matches:
        print(match)
    return matches


def menteePriority(allMentees):
    """
    This function will prioritize the mentees order
    or assignment to mentors based on the assignmentPriority
    """
    priorityList = []
    for mentee in allMentees:
        if len(priorityList) == 0: # If list is empty add first mentee
            priorityList.append({mentee.menteeId: mentee.assignmentPriority}) # Put the mentee id and their priority points in list
        else:
            i = 0
            while i < len(priorityList):
                currentAP = list(priorityList[i].values()) # the assignment priority of current position in priorityList
                if currentAP[0] < mentee.assignmentPriority: #comparing current list position assigment priority to current mentee from allMentees AP
                    priorityList.insert(i, {mentee.menteeId: mentee.assignmentPriority})
                    break
                i = i + 1
            if {mentee.menteeId: mentee.assignmentPriority} not in priorityList: # if we hit the end of priorityList we check if current mentee was inserted
                priorityList.append({mentee.menteeId: mentee.assignmentPriority}) # If not we insert at the end
    
    return priorityList # we return our list of {id: rankPoints}'s so we can assign mentees to mentors based on priority points

def assignToMentor(menteeAcceptableMentors, priority, allMentors, allMentees):
    """
    The final step in getting mentees assigned to mentors this functions
    will take in the list of acceptable mentors for each mentee, the priority
    to assign mentees to mentors, then all mentors and all mentees in their
    respective dicts.
    The goal is to assign mentees to the mentor objects, filling up thier
    assigedMentees slots until we have matched as many mentees as possible
    """
    menteesToAssign = menteeAcceptableMentors.copy()
    assignPriority = priority.copy()
    noMatches = []
    unmatched = {}
    assigned = []
    mentees = {}
    mentors = {}
    for item in allMentees:
        mentees[item.menteeId] = item
    for item in allMentors:
        mentors[item.mentorId] = item

    #If the mentee has None matches, add them to the unmatched dictionary
    for k, v in menteesToAssign.items():
        if v is None:
            noMatches.append(k)
            unmatched[k] = {'firstName': mentees[k].firstName,
                            'lastName': mentees[k].lastName,
                            'email': mentees[k].email}
    #Remove any Nones from the mentees to assign
    for mtId in noMatches:
        del menteesToAssign[mtId]
    for item in assignPriority:
        if item in noMatches:
            assignPriority.remove(item)
    
    place = 0
    #Next assign any mentees that can be assigned to their mentor
    while(len(assignPriority) > 0): #We'll go in order of the priority list
        mtId = assignPriority[place]
        matched = False
        availableMatches = menteesToAssign[mtId] # Pull the mentees list of matches to mentors
        topMentors = sorted(menteesToAssign[mtId].keys(), reverse=True) # a decending order of match rates with various mentors
        for mtchPct in topMentors: # Going from best match to worst
            mtrId = availableMatches[mtchPct] # Get the mentor id using their match % to the mentee
            positions = len(mentors[mtrId].mentorMatches) # Number of mentee slots on the mentor object
            i = 0
            while i < positions: # Each mentor object starts with list of nones for matches, we're looking for an open position
                if mentors[mtrId].mentorMatches[i] is None: # If a none spot is available
                    setattr(mentees[mtId], 'matchPercent', mtchPct) # Add this specific matches % to the mentee object
                    mentors[mtrId].mentorMatches[i] = mentees[mtId] # Assign this mentee to it
                    matched = True # Set matched to true so when we break from this inner loop we can move to next mentee
                    assigned.append(mtId)
                    break
                i += 1
            if matched is True:
                del menteesToAssign[mtId]
                assignPriority.remove(mtId)
                break
        if matched is False:
            print("Mentee {} is unmatched".format(mtId))
            unmatched[mtId] = {'firstName': mentees[mtId].firstName,
                                'lastName': mentees[mtId].lastName,
                                'email': mentees[mtId].email}
            del menteesToAssign[mtId]
            assignPriority.remove(mtId)
    return unmatched