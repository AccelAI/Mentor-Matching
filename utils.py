from potentialMatch import *

def processMentee(sheet, row):

    #Mentee Id
    menteeId = row

    #Name
    name = sheet.cell(row=row, column=2).value.split(' ', 1)
    firstName = name[0]
    lastName = name[1]

    #Email
    if sheet.cell(row=row, column=3).value == None:
        email = "" 
    else:
        email = sheet.cell(row=row, column=3).value.strip()

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
    originCountry = sheet.cell(row=row, column=7).value

    #Current Location
    currentLocation = sheet.cell(row=row, column=8).value

    #Affiliation
    affiliation = sheet.cell(row=row, column=9).value

    #Current Postition
    position = sheet.cell(row=row, column=10).value

    #Website
    website = sheet.cell(row=row, column=12).value

    #Languages
    menteeLanguages = sheet.cell(row=row, column=13).value
    if menteeLanguages is not None:
        if "," in menteeLanguages:
            languages = menteeLanguages.strip().split(",")
        else:
            languages = []
            languages.append(menteeLanguages.strip())
    else:
        languages = ['English']


    #Timezone
    if sheet.cell(row=row, column=15).value == None:
        timezone = ""
    else:
        timezone = sheet.cell(row=row, column=15).value


    #Mentoring Area
    menteeMentoringVerticals = sheet.cell(row=row, column=17).value
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
    motivationStatement = sheet.cell(row=row, column=18).value

    #Preffered Outcomes
    prefOutcomes = sheet.cell(row=row, column=19).value
    if ',' in prefOutcomes:
        preferredOutcomes = prefOutcomes.split(',')
    else:
        preferredOutcomes = prefOutcomes

    #Experience Statement
    expStatement = sheet.cell(row=row, column=21).value
    if expStatement is None:
        expStatement = 'No'
    experienceStatement = (True, False)[expStatement == "No"]
    #(if_test_is_false, if_test_is_true)[test]

    #Career Goals
    careerGoals = sheet.cell(row=row, column=22).value

    #Skills Needing Improvement
    menteeMentoringSkills = sheet.cell(row=row, column=24).value
    if menteeMentoringSkills == None:
        menteeMentoringSkills = []
    elif "," in menteeMentoringSkills:
        mentoringSkills = menteeMentoringSkills.split(",")
    else:
        mentoringSkills = []
        mentoringSkills.append(menteeMentoringSkills)

    
    #Research Areas Needing Improvement
    #This may need (extra / details) stripped out
    menteeResearchAreas = sheet.cell(row=row, column=26).value
    if menteeResearchAreas == None:
        menteeResearchAreas = ""
    if "," in menteeResearchAreas:
        researchAreas = menteeResearchAreas.strip().split(",")
    else:
        researchAreas = []
        researchAreas.append(menteeResearchAreas)

    #Career Areas Needing Improvement
    menteeCareerAreas = sheet.cell(row=row, column=28).value
    if menteeCareerAreas == None:
        menteeCareerAreas = ""
    if "," in menteeCareerAreas:
        careerAreas = menteeCareerAreas.strip().split(",")
    else:
        careerAreas = []
        careerAreas.append(menteeCareerAreas)


    #Conferences mentee would like to present at
    confPref = sheet.cell(row=row, column=33).value
    otherConfPref = sheet.cell(row=row, column=34).value
    if confPref is None:
        menteeConfPref = ""
    if ',' in confPref:
        menteeConfPref = confPref.strip().split(',')
    else:
        menteeConfPref = []
        menteeConfPref.append(confPref)
    if otherConfPref is not None:
        if ',' in otherConfPref:
            otherConfPref = otherConfPref.strip().split(',')
        menteeConfPref.append(otherConfPref)

    #publication in AI Journals of high impact
    pubHI = sheet.cell(row=row, column=35).value
    if pubHI == 'No' or pubHI is None:
        menteePublishedHighImpact = False
    else:
        menteePublishedHighImpact = True

    #publication in top tier ai conferences
    pubTT = sheet.cell(row=row, column=36).value
    if pubTT is None or pubTT == "No":
        menteePubTopTier = False
    else:
        menteePubTopTier = True

    #peer reviewd publications in workshops
    workshops = sheet.cell(row=row, column=37).value
    if workshops == 'never' or workshops is None:
        menteePubWorkshop = False
    else:
        menteePubWorkshop = True
    
    #served as a peer reviewer before
    reviewer = sheet.cell(row=row, column=38).value
    if reviewer is None or reviewer == 'never':
        menteePeerReviewer = False
    else:
        menteePeerReviewer = True

    #Servered as a reviewer for a journal of high impact
    reviewerHI = sheet.cell(row=row, column=39).value
    if reviewerHI is None or reviewerHI == 'never':
        menteeReviewHI = False
    else:
        menteeReviewHI = True

    #Serverd as a reviewer in top tier ai conference
    reviewerTT = sheet.cell(row=row, column=40).value
    if reviewerTT is None or reviewerTT == 'never':
        menteeRevTopTier = False
    else:
        menteeRevTopTier = True
    
    #Reviewer's ranking on their personal statement
    menteeStatementRank = sheet.cell(row=row, column=42).value

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
                "menteeConfPref": menteeConfPref,
                "menteePublishedHighImpact": menteePublishedHighImpact,
                "menteePubTopTier": menteePubTopTier,
                "menteePubWorkshop": menteePubWorkshop,
                "menteePeerReviewer": menteePeerReviewer,
                "menteeReviewHI": menteeReviewHI,
                "menteeReviewTopTier": menteeRevTopTier,
                "menteeStatementRank": menteeStatementRank
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
    mentorMatches = [None] * menteeLimit

    
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
        conPref = []
    else:
        conPref = conferencePref.split(',')
    if conferenceExtra is not None:
        conferenceExtra = conferenceExtra.split(',')
        conPref.append(conferenceExtra)

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
                "mentorConferencePref": conPref
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
                pass
            else:
                mentoringSkillsMatch = (len(mentoringSkillsIntersect)/(len(mentoringSkills) + len(mentor.mentoringSkills)/2) * 100)
                matchPercents.update(mentoringSkillsMatch = round(mentoringSkillsMatch, 2))


        #Check intersects of Research
        if 'Research Guidance (AI Verticals)' in mentoringVerticalIntersect:
            researchAreas = mentee.researchAreas
            researchAreasIntersect = researchAreas.intersection(mentor.researchAreas)
            if len(researchAreasIntersect) == 0:
                pass
            else:
                researchAreasMatch = (len(researchAreasIntersect)/(len(researchAreas) + len(mentor.researchAreas)/2) * 100)
                matchPercents.update(researchAreasMatch = round(researchAreasMatch, 2))


        #Check intersects of Career
        if 'Career Guidance' in mentoringVerticalIntersect:
            careerAreas = mentee.careerAreas
            careerAreasIntersect = careerAreas.intersection(mentor.careerAreas)
            if len(careerAreasIntersect) == 0:
                pass
            else:
                careerAreasMatch = (len(careerAreasIntersect)/(len(careerAreas) + len(mentor.careerAreas)/2) * 100)
                matchPercents.update(careerAreasMatch = round(careerAreasMatch, 2))

        #Check intersects of Review Research
        if 'Review Research' in mentoringVerticalIntersect:
            reviewerMatch = 100
        else:
            reviewerMatch = 0
        matchPercents.update(reviewerMatch = reviewerMatch)

        print(mentoringVerticalIntersect)

        #Average Match Scores
        matchRate = float(0)
        # potentialMatches = []
        for value in matchPercents.values():
            matchRate += value

        matchRate /= (len(matchPercents.values()))
        matchPercents.update(matchRate = round(matchRate, 2))

        menteePotentialMatches.update({mentor.mentorId: matchPercents})

        #Build list of potential match objects
        # temp = PotentialMatch(mentee, mentor, matchRate, matchPercents)
        # potentialMatches.append(temp)
        # print(potentialMatches)

        
        #Assigning mentees based on highest matchrate with mentor
        # def maxMatch(rate) :
        #     #basecase
        #     if rate == 0:
        #         return
        #     else :
        #         checkList = mentor.mentorMatches
        #         # checkList = []
        #         temp = PotentialMatch(mentee, mentor, rate, matchPercents)
        #         # print("Potential Match has a {}".format(temp.mentee.firstName))
        #         for n, match in enumerate(checkList):
        #             # print(mentee.firstName)
        #             if checkList[n] is None :
        #                 checkList[n] = temp
        #                 break

        #             if checkList[n].matchRate < temp.matchRate:
        #                 temp2 = checkList[n]
        #                 checkList[n] =  temp
        #                 temp = temp2
        #                 # print("Match {}: {}".format(n, match))
        #                 #max value assigned to each position in list of dictionaries
                
        #         mentor.mentorMatches = checkList

        #         # print("Mentor {} highest matches: {}".format(mentor.firstName, mentor.mentorMatches))
                    

        #         # while n < len(checkList) :
        #         #     # replace with mentee object if checkList[n] is None
        #         #     if checkList[n] is None :
        #         #         checkList[n] = mentee
        #         #         n += 1
        #         #     else :
        #         #         # print(checkList[n])
        #         #         return
            
         
        
        # # maxMatch(matchRate)
                    
                    

        
    
    return menteePotentialMatches


def mentorMatches():


     #Find Max matches for mentor
        matches = [x.matchRate for x in potentialMatches]
        print("Mentee {} matches: {}".format(mentee.firstName, matches))
        maxMatch = max(matches)
        print("Mentee {} maxmatch: {}".format(mentee.firstName, maxMatch))


def maxMatches(potentialMatches):
    """
    This function finds up to the top three best matches
    by percent for each mentee. The function will return a
    dictionary of matches, if not none, with up to three
    top matches.
    """
    matchPercents = []
    #A list of all the mentor Id's that the mentee matched to
    ptMtchKeys = list(potentialMatches.keys())

    #Create a list of all averaged match percents for each mentor
    for matchObject in potentialMatches.values():
        matchPercents.append(matchObject['matchRate'])

    #isolating the mentees top three mentor options
    if len(matchPercents) > 3:
        starter = matchPercents[:3]
        percentFirst = max(starter)
        percentThird = min(starter)
        topThree = {}
        for num in starter:
            if num != percentFirst and num != percentThird:
                percentSecond = num
        i = 3
        while i < len(matchPercents):
            newNum = matchPercents[i]
            if newNum > percentThird:
                percentThird = newNum
            if percentThird > percentSecond:
                temp = percentThird
                percentThird = percentSecond
                percentSecond = temp
            if percentSecond > percentFirst:
                temp = percentSecond
                percentSecond = percentFirst
                percentFirst = temp
            i += 1

        position = matchPercents.index(percentFirst)
        topThree[ptMtchKeys[position]] = percentFirst
        position = matchPercents.index(percentSecond)
        topThree[ptMtchKeys[position]] = percentSecond
        position = matchPercents.index(percentThird)
        topThree[ptMtchKeys[position]] = percentThird
        return topThree
    elif len(matchPercents) > 0:
        topMatches = {}
        for percent in matchPercents:
            position = matchPercents.index(percent)
            topMatches[ptMtchKeys[position]] = percent
        return topMatches
    else:
        return None

def assignToMentor(menteeTopMentors, allMentors, allMentees):
    """
    The final step in getting mentees assigned to mentors this functions
    will screen out the no match mentees first, then try to assign the
    single match mentees, then assign the multi match mentees, and finally
    any mentees that are left unmatched once all mentors with matches are
    slotted, will be added to the unmatched list
    """
    menteesToAssign = menteeTopMentors.copy()
    noMatches = []
    unmatched = {}
    singleMatch = []
    assigned = []
    #If the mentee has None matches, add them to the unmatched dictionary
    for k, v in menteesToAssign.items():
        if v is None:
            noMatches.append(k)
            unmatched[k] = {'firstName': allMentees[k].firstName,
                            'lastName': allMentees[k].lastName,
                            'email': allMentees[k].email}
    #Remove any Nones from the mentees to assign
    for mtId in noMatches:
        del menteesToAssign[mtId]
    
    #Next assign any mentees that can be assigned to their mentor
    for k, v in menteesToAssign.items():
        if len(v) == 1: #If the metee only has a single match to a mentor
            singleMatch.append(k) #Add the mentee to the single match list for tracking
            mentorKey = int(list(v.keys())[0]) - 2 #This is the position of the mentor in allMentors
            singleMatchRate = int(list(v.values())[0]) #This is the matchRate of the mentee to the mentor
            if singleMatchRate > 50: #If the match is grater than a 50%
                checklist = allMentors[mentorKey].mentorMatches #This is the list from the mentor of currently assigned mentees, starts as nones
                for n, spot in enumerate(checklist):
                    if checklist[n] is None:
                        checklist[n] = allMentees[k - 2] # k - 2 because mentee ID is off from index postion by 2
                        assigned.append(k) #if it is assigned, add to assigned list so we can take off to be assigned
                        break
                    else:
                        incomingMenteePercent = list(menteesToAssign[k].values())[0] #The challenger mentee match to mentro %
                        curAssignedMeteeId = checklist[n].menteeId #The mentee id that is currently assigned to the mentor in this slot
                        curAssignedMeteePercent = list(menteeTopMentors[curAssignedMeteeId].values())[0] #The currently assigned mentee's match rate to the mentor
                        print("Current Assigned % = {} and Challenger % = {}".format(curAssignedMeteePercent, incomingMenteePercent))

                        if curAssignedMeteePercent < incomingMenteePercent: #if the challenger has a better % to the mentor than the current
                            assigned.remove(checklist[n].menteeId) #Remove current from the assigned list as they are no longer assigned
                            checklist[n] = allMentees[k - 2] #Put the new assignee into the match slot on the list that will attach to mentor
                            assigned.append(k) #put the new assignee on the assigned list
                allMentors[mentorKey].mentorMatches = checklist #Assign the checklist of matched mentees to the mentor object
                print("All Mentors.mentoMatches: {}".format(allMentors[mentorKey].mentorMatches)) #print to confirm
            else:
                #if the mentee has a single match and the % is less than 50% pass for now
                pass

    print("Assigned: {}".format(assigned)) #Print the assigned list to confirm those that were assigned
    #Remove any mentees that did get assigned from mentees to assign
    for mentee in assigned:
        menteesToAssign.pop(mentee)

    #For mentees in single match and not in assigned, add them to the unmatched dictionary to be contacted
    for mentee in singleMatch:
        if mentee not in assigned:
            unmatched[mentee] = {'firstName': allMentees[mentee].firstName,
                                'lastName': allMentees[mentee].lastName,
                                'email': allMentees[mentee].email}
