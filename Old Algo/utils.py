from potentialMatch import *

def processMentee(sheet, row):

    #Mentee Id by row num
    menteeId = row
    print("Working on mentee: {}".format(row))

    #Name COL C & D
    #name = sheet.cell(row=row, column=3).value.split(' ', 1)
    firstName = sheet.cell(row=row, column=3).value
    lastName = sheet.cell(row=row, column=4).value

    #Email Col B
    if sheet.cell(row=row, column=2).value == None:
        email = "" 
    else:
        email = sheet.cell(row=row, column=2).value.strip()

    #Gender Col E
    if sheet.cell(row=row, column=5).value == None:
        gender = ""
    else:
        gender = sheet.cell(row=row, column=5).value.strip()

    #LatinX Identity Col F
    menteeSelfIdentification = sheet.cell(row=row, column=6).value
    isLatinx = (True, False)[menteeSelfIdentification == "No" or menteeSelfIdentification == "Ally"]

    #Country of Origin Col G
    originCountry = sheet.cell(row=row, column=7).value
    if originCountry is not None:
        originCountry = originCountry.strip()

    #Current Location Col H & I
    currentLocationCity = sheet.cell(row=row, column=8).value
    currentLocationCountry = sheet.cell(row=row, column=9).value
    currentLocation = currentLocationCity + ", " + currentLocationCountry
    

    #Affiliation Col K
    affiliation = sheet.cell(row=row, column=11).value
    if affiliation is not None:
        affiliation = affiliation.strip()

    #Current Postition Col K
    position = sheet.cell(row=row, column=10).value
    if position is not None:
        position = position.strip()

    #Website/Google Scholar COL L
    website = sheet.cell(row=row, column=12).value
    if website is not None:
        website = website.strip()

    #Languages COL M
    menteeLanguages = sheet.cell(row=row, column=13).value
    if menteeLanguages is not None:
        menteeLanguages = menteeLanguages.strip()
        menteeLanguages.replace('\n', '')
        if "," in menteeLanguages:
            languages = menteeLanguages.split(",")
        else:
            languages = []
            languages.append(menteeLanguages)
    else:
        languages = ['English']


    #Timezone COL 
    if sheet.cell(row=row, column=14).value == None:
        timezone = ""
    else:
        timezone = sheet.cell(row=row, column=14).value.strip()
        timezone = timezone.replace('\n', '')

    # Perferred way to connect COL O
    if sheet.cell(row=row, column=15).value == None:
        connectionType = ""
    else:
        connectionType = sheet.cell(row=row, column=14).value
        

    #Mentoring Area COL P
    menteeMentoringVerticals = sheet.cell(row=row, column=16).value
    if menteeMentoringVerticals is not None:
        menteeMentoringVerticals = menteeMentoringVerticals.strip()
        mentoringVertical = [item.strip() for item in menteeMentoringVerticals.split(',')]
            

    #Motivation Statement COL Q
    motivationStatement = sheet.cell(row=row, column=17).value
    if motivationStatement is not None:
        motivationStatement = motivationStatement.replace('\n', '').strip()

    # #Preffered Outcomes COL AB
    prefOutcomes = sheet.cell(row=row, column=28).value
    if prefOutcomes is not None:
        prefOutcomes = prefOutcomes.replace('\n', '').strip()
        if ',' in prefOutcomes:
            preferredOutcomes = prefOutcomes.split(',')
        else:
            preferredOutcomes = prefOutcomes
    else:
        preferredOutcomes = None

    # #Experience Statement (Not in current version of sign up)
    # expStatement = sheet.cell(row=row, column=16).value.strip('\n')
    # if expStatement is None:
    #     expStatement = 'No'
    # experienceStatement = (True, False)[expStatement == "No"]
    # #(if_test_is_false, if_test_is_true)[test]

    #Career Goals COL W
    careerGoals = sheet.cell(row=row, column=23).value
    if careerGoals is not None:
        careerGoals = careerGoals.replace('\n', '').strip()

    #Skills Needing Improvement COL Z
    menteeMentoringSkills = sheet.cell(row=row, column=26).value
    mentoringSkills = [item.strip() for item in menteeMentoringSkills.split(',')]
  

    
    #Research Areas Needing Improvement COL AA
    #This may need (extra / details) stripped out
    menteeResearch = sheet.cell(row=row, column=27).value
    menteeResearchAreas = [item.strip() for item in menteeResearch.split(',')]
    



    # #Career Areas Needing Improvement (This is not in current signup flow)
    # menteeCareerAreas = sheet.cell(row=row, column=19).value
    # if menteeCareerAreas == None:
    #     menteeCareerAreas = ""
    # else:
    #     menteeCareerAreas = menteeCareerAreas.replace('\n', '').strip()
    #     if "," in menteeCareerAreas:
    #         careerAreas = menteeCareerAreas.strip().split(",")
    #     else:
    #         careerAreas = []
    #         careerAreas.append(menteeCareerAreas)


    #Conferences mentee would like to present at COL Y and Z
    # confPref = sheet.cell(row=row, column=25).value
    # otherConfPref = sheet.cell(row=row, column=26).value
    # if confPref is None:
    #     menteeConfPref = ""
    # else:
    #     confPref = confPref.replace('\n', '').strip()
    #     if ',' in confPref:
    #         menteeConfPref = confPref.strip().split(', ')
    #     else:
    #         menteeConfPref = []
    #         menteeConfPref.append(confPref)
    # if otherConfPref is not None:
    #     otherConfPref = otherConfPref.replace('\n', '').strip()
    #     if ',' in otherConfPref:
    #         otherConfPref = otherConfPref.strip().split(', ')
    #         menteeConfPref = menteeConfPref + otherConfPref
    #     else:
    #         menteeConfPref.append(otherConfPref)

    #Papers witten COL S
    paperWritten = sheet.cell(row=row, column=19).value[0]
    if paperWritten == 'No' or paperWritten is None:
        menteeWriter = 0
    else:
        menteeWriter = int(paperWritten)


    # Paper submitted for peer review COL T
    peerReview = sheet.cell(row=row, column=20).value
    if peerReview == 'never' or peerReview is None:
        menteePeerReview = False
    else:
        menteePeerReview = True
    

    
    #Reviewer's ranking on their personal statement COL AD
    #menteeStatementRank = sheet.cell(row=row, column=30).value
    # This needs to be added by mentorship chairs and column needs to be re-assessed

    #Mentee ranking factors for preferential placement
    
    assignmentPriority = 0

    if 'Career Professional' in position:
        assignmentPriority += 10
    elif 'Senior Ph.D.' in position:
        assignmentPriority += 10
    elif 'Junior Ph.D.' in position:
        assignmentPriority += 6
    elif 'Graduate Student ' in position:
        assignmentPriority += 4
    elif 'Undergraduate Student' or 'Early Career' in position:
        assignmentPriority += 2
    if paperWritten is not None:
        assignmentPriority += menteeWriter
    if menteePeerReview:
        assignmentPriority += 1


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
                # "experienceStatement": experienceStatement, 
                "careerGoals": careerGoals,  
                "mentoringSkills": set(mentoringSkills),
                "researchAreas": set(menteeResearchAreas), 
                # "careerAreas": set(careerAreas), 
                # "menteeConfPref": set(menteeConfPref),
                #"menteePublishedHighImpact": menteePublishedHighImpact,
                #"menteePubTopTier": menteePubTopTier,
                "menteePeerReview": menteePeerReview,
                #"menteePeerReviewer": menteePeerReviewer,
                #"menteeReviewHI": menteeReviewHI,
                #"menteeReviewTopTier": menteeRevTopTier,
                # "menteeStatementRank": menteeStatementRank,
                "assignmentPriority": assignmentPriority,
                "connectionType" : connectionType
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

    #metor email address COL B
    mentorEmailAddress = sheet.cell(row=row, column=2).value
    if mentorEmailAddress is not None:
        email = mentorEmailAddress.strip()
    else:
        email = ""

    #mentor name COL C & D
    if sheet.cell(row=row, column=3).value is not None:
        firstName = sheet.cell(row=row, column=3).value
        lastName = sheet.cell(row=row, column=4).value

    #mentor gender COL E
    if sheet.cell(row=row, column=5).value is not None:
        gender = sheet.cell(row=row, column=4).value
    else:
        gender = ""

    #mentor self-identified as LatinX COL F
    isLatin = sheet.cell(row=row, column=6).value
    if isLatin == "Yes" or isLatin == "Maybe":
        isLatinx = True
    else:
        isLatinx = False

    #mentor country of origin COL G
    if sheet.cell(row=row, column=7).value is not None:
        originCountry = sheet.cell(row=row, column=7).value
    else:
        originCountry = ""

    #mentor current location (city, state, country) COL H & I
    if sheet.cell(row=row, column=8).value is not None:
        currentLocationCity = sheet.cell(row=row, column=8).value
        currentLocationCountry = sheet.cell(row=row, column=9).value
        currentLocation = currentLocationCity + ', ' + currentLocationCountry
    else:
       currentLocation = ""

    #mentor current position level COL J
    if sheet.cell(row=row, column=10).value is not None:
        position = sheet.cell(row=row, column=10).value
    else:
        position = ""
    
    #mentor current organization (career) COL K
    if sheet.cell(row=row, column=11).value is not None:
        affiliation = sheet.cell(row=row, column=11).value
    else:
        affiliation = ""
    
    #mentor seniority level COL L
    if sheet.cell(row=row, column=12).value is not None:
        seniority = sheet.cell(row=row, column=12).value
    else:
        seniority = ""
 
    #mentor googles scholar or linkenin or personal site COL M
    if sheet.cell(row=row, column=13).value is not None:
        website = sheet.cell(row=row, column=13).value.strip()
    else:
        website = ""

    #mentor preferred languages COL N
    if sheet.cell(row=row, column=14).value is not None:
        if ',' in sheet.cell(row=row, column=14).value:
            languages = sheet.cell(row=row, column=14).value.split(',')
        else:
            languages = []
            languages.append(sheet.cell(row=row, column=14).value)
    else:
        languages = ['English']
 
    #mentor preferred timezone COL O
    if sheet.cell(row=row, column=15).value is not None:
        timezone = sheet.cell(row=row, column=15).value
    else:
        timezone = ""

    #mentor connection preferrence COL P
    if sheet.cell(row=row, column=16).value is not None:
        connectionPreferrence = sheet.cell(row=row, column=16).value
    else:
        connectionPreferrence = ""    

    #mentor area of mentorship COL Q
    mentorAreas = sheet.cell(row=row, column=17).value
    mentoringVertical = []
    if mentorAreas is not None:
        mentorAreas = mentorAreas.strip()
        mentoringVertical = [item.strip() for item in mentorAreas.split(',')]


    
    #mentor weekly time commitment COL R
    commitment = sheet.cell(row=row, column=18).value[0]
    # Normal Limit Instantiation
    # menteeLimit = int(list(filter(str.isdigit, commitment))[0])
    # Only allowing one mentee per mentor intstantiation
    menteeLimit = int(commitment)

    #instantiate mentor match list
    if menteeLimit < 1:
        mentorMatches = None
    elif menteeLimit == 1:
        mentorMatches = [None]
    else:
        mentorMatches = [None, None]
        # This places a limit of 2 mentees max but we could do [None] * menteeLimit for max they can handle

    
    #mentor preferrence for characteristics in a mentee COL V
    preferredMenteeChars = sheet.cell(row=row, column=22).value

    #mentor preferrence for outcomes of mentoring COL AA
    outcomes = sheet.cell(row=row, column=27).value
    if outcomes is not None:
        if ',' in outcomes:
            mentorPrefOutcomes = outcomes.split(',')
        else:
            mentorPrefOutcomes = []
            mentorPrefOutcomes.append(outcomes)
    else:
        mentorPrefOutcomes = []

    # #Mentor discussing impact post program COL T
    # discuss = sheet.cell(row=row, column=20).value
    # if discuss == "Yes" or discuss == "Maybe":
    #     mentorDiscuss = True
    # else:
    #     mentorDiscuss = False
    # Removed from latest sign up 03/2025

    
    #mentor choices for skills they would like to help a mentee improve COL Y
    skillz = sheet.cell(row=row, column=25).value
    mentorSkills = []
    if skillz is not None:
        skillz = skillz.strip()
        mentorSkills = [item.strip() for item in skillz.split(',')]


    #mentor research areas that they could help mentee improve COL Z
    ra = sheet.cell(row=row, column=26).value
    mentoringResearchAreas = []
    if ra is not None:
        ra = ra.strip()
        mentoringResearchAreas = [item.strip() for item in ra.split(',')]

    # #mentor forms of career advice (NOT in current application)
    # ca = sheet.cell(row=row, column=23).value
    # mentoringCareerAdvice = []
    # if ca is not None:
    #     if ',' in ca:
    #         mentoringCareerAdvice = ca.split(',')
    #     else:
    #         mentoringCareerAdvice.append(ca)

    #previously reviewed research T
    pre = sheet.cell(row=row, column=20).value
    if pre is None:
        previousReviewer = False
    else:
        pre = pre.lower()
        if pre == 'no' or pre == 'never':
            previousReviewer = False
        else:
            previousReviewer = True

    #does mentor have published papers COL S
    published = sheet.cell(row=row, column=19).value
    if published is None:
        published = 'None'
    elif 'extensive' in published:
        mentorPublished = 'Extensive'
    elif 'moderate' in published:
        mentorPublished = 'Moderate'
    else:
        mentorPublished = 'Some'
    #previously reviewer at top research conferences 
    pre = sheet.cell(row=row, column=21).value
    if pre is None:
        topReviewer = False
    else:
        pre = pre.lower()
        if pre == 'no' or pre == 'never':
            topReviewer = False
        else:
            topReviewer = True

    # #does mentor have published papers in Top Tier conferences
    # ttPublished = sheet.cell(row=row, column=26).value
    # if ttPublished is None:
    #     ttPublished = 'No'
    # mentorTTPublished = (True, False)[published == "No"]
    # #(if_test_is_false, if_test_is_true)[test]

    # #previously reviewer for journals of High impact 
    # revHI = sheet.cell(row=row, column=27).value
    # if revHI is None:
    #     revHighImpact = False
    # else:
    #     revHI = revHI.lower()
    #     if revHI == 'no' or revHI == 'never':
    #         revHighImpact = False
    #     else:
    #         revHighImpact = True

    # #does mentor have published papers in Journals of High Impact
    # pubHI = sheet.cell(row=row, column=28).value
    # if pubHI is None:
    #     pubHI = 'No'
    # mentorPubHI = (True, False)[pubHI == "No"]
    # #(if_test_is_false, if_test_is_true)[test]

    # conferences mentor would like to line mentorship up with (Not in doc for neurips 2024)
    # conferencePref = sheet.cell(row=row, column=29).value
    # conferenceExtra = sheet.cell(row=row, column=30).value
    # if conferencePref is None:
    #     mentorConfPref = []
    # else:
    #     mentorConfPref = conferencePref.split(', ')
    # if conferenceExtra is not None:
    #     if ',' in conferenceExtra:
    #         conferenceExtra = conferenceExtra.strip().split(', ')
    #         mentorConfPref = mentorConfPref + conferenceExtra
    #     else:
    #         mentorConfPref.append(conferenceExtra)

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
                "connectionPreferrence": connectionPreferrence,
                "mentoringVertical": set(mentoringVertical),
                "menteeLimit": menteeLimit,
                "mentorMatches": mentorMatches, 
                "menteeCharacteristics": preferredMenteeChars,
                "mentorPrefOutcomes": mentorPrefOutcomes,
                #"mentorDiscuss": mentorDiscuss,
                "mentoringSkills": set(mentorSkills),
                "researchAreas": set(mentoringResearchAreas), 
                # "careerAreas": set(mentoringCareerAdvice),
                "previousReviewer": previousReviewer,
                "mentorPublished": mentorPublished,
                "topReviewer": topReviewer,
                #"mentorTopTierPublished": mentorTTPublished,
                #"reviewedHighImpact": revHighImpact,
                #"mentorPublishedHI": mentorPubHI,
                # "mentorConfPref": set(mentorConfPref)
                }
    return cleanRow



def mentorMatch(mentee, mentorList):
    menteePotentialMatches = {}

    print("In mentorMatch function, working on Mentee: {} - {} {}".format(mentee.menteeId, mentee.firstName, mentee.lastName))
  
    for mentor in mentorList:
        matchPercents = {}
        #Check Language Matches 
        languages = mentee.languages
        #english is the default if none selected
        langIntersect = languages.intersection(mentor.languages)
        if len(langIntersect) == 0:
           print("Mentee {} : Mentor {} - No Lanuguage intersect".format(mentee.menteeId, mentor.mentorId))
           continue
        else:
            langMatch = (len(langIntersect)/(len(languages) + len(mentor.languages)/2) * 100)
            matchPercents.update(langMatch = round(langMatch, 2))

        #Check Mentoring Areas mentee wants to strengthen
        mentoringVerticals = mentee.mentoringVertical
        mentoringVerticalIntersect = mentoringVerticals.intersection(mentor.mentoringVertical)
        if len(mentoringVerticalIntersect) == 0:
            print("Mentee {} : Mentor {} - No mentoring intersect".format(mentee.menteeId, mentor.mentorId))
            continue
        else:
            mentoringVerticalMatch = (len(mentoringVerticalIntersect)/(len(mentoringVerticals) + len(mentor.mentoringVertical)/2) * 100)
            matchPercents.update(mentoringVerticalMatch = round(mentoringVerticalMatch, 2))

        
        #Check intersects of Skills
        if 'Strengthening skills' in mentoringVerticalIntersect:
            mentoringSkills = mentee.mentoringSkills
            mentoringSkillsIntersect = mentoringSkills.intersection(mentor.mentoringSkills)
            if len(mentoringSkillsIntersect) == 0:
                print("Mentee {} : Mentor {} - No skill intersect".format(mentee.menteeId, mentor.mentorId))
                matchPercents.update(mentoringSkillsMatch = 0)
            else:
                mentoringSkillsMatch = (len(mentoringSkillsIntersect)/(len(mentoringSkills) + len(mentor.mentoringSkills)/2) * 100)
                matchPercents.update(mentoringSkillsMatch = round(mentoringSkillsMatch, 2))


        #Check intersects of Research
        if 'Research Guidance (AI Verticals)' in mentoringVerticalIntersect:
            researchAreas = mentee.researchAreas
            researchAreasIntersect = researchAreas.intersection(mentor.researchAreas)
            if len(researchAreasIntersect) == 0:
                print("Mentee {} : Mentor {} - No research intersect".format(mentee.menteeId, mentor.mentorId))
                matchPercents.update(researchAreasMatch = 0)
            else:
                researchAreasMatch = (len(researchAreasIntersect)/(len(researchAreas) + len(mentor.researchAreas)/2) * 100)
                matchPercents.update(researchAreasMatch = round(researchAreasMatch, 2))


        #Check intersects of Career (NOT in current application flow)
        # if 'Career Guidance' in mentoringVerticalIntersect:
        #     careerAreas = mentee.careerAreas
        #     careerAreasIntersect = careerAreas.intersection(mentor.careerAreas)
        #     if len(careerAreasIntersect) == 0:
        #         matchPercents.update(careerAreasMatch = 0)
        #     else:
        #         careerAreasMatch = (len(careerAreasIntersect)/(len(careerAreas) + len(mentor.careerAreas)/2) * 100)
        #         matchPercents.update(careerAreasMatch = round(careerAreasMatch, 2))

        #Check intersects of Review Research
        if 'Review Research' in mentoringVerticalIntersect:
            reviewerMatch = 100
        else:
            reviewerMatch = 0
        matchPercents.update(reviewerMatch = reviewerMatch)

        
        #Check intersects of Conference Preferences
        # confPref = mentee.menteeConfPref
        # confPrefIntersect = confPref.intersection(mentor.mentorConfPref)
        # if len(confPrefIntersect) == 0:
        #     print("Mentee {} : Mentor {} - No conferece intersect".format(mentee.menteeId, mentor.mentorId))
        #     continue
        # else:
        #     confPrefMatch = (len(confPrefIntersect)/(len(confPref) + len(mentor.mentorConfPref)/2)*100)
        #     matchPercents.update(confPrefMatch = round(confPrefMatch, 2))



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
    must be within 50% of the best match
    """

    matches = {}
    matchPercents = []

    # Create a list of all matched mentors and the master match rate
    for mentor, matchObject in potentialMatches.items():
        matches[matchObject['matchRate']] = mentor
        matchPercents.append(float(matchObject['matchRate']))
    try:
        matchMax = max(matchPercents)
        killKeys = []
        for key in matches.keys():
            if key < (matchMax * 0.01):
                killKeys.append(key)
        for key in killKeys:
            del matches[key]
    except:
        print("Something wrong with max")
    if matches == {}:
        return None
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
    import copy
    
    menteesToAssign = copy.deepcopy(menteeAcceptableMentors)
    assignPriority = copy.deepcopy(priority)
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
        assignPriority.remove(mtId)

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
            unmatched[mtId] = {'firstName': mentees[mtId].firstName,
                                'lastName': mentees[mtId].lastName,
                                'email': mentees[mtId].email}
            print("Unmatched[{}] = {} {}".format(mtId, mentees[mtId].firstName, mentees[mtId].lastName))
            del menteesToAssign[mtId]
            assignPriority.remove(mtId)
    return unmatched