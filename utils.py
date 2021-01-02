
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
    if "," in menteeLanguages:
        languages = menteeLanguages.strip().split(",")
    else:
        languages = list(menteeLanguages.strip())


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
        commsPreference = list(menteeCommsPreference)

    #Mentoring Area
    menteeMentoringAreas = sheet.cell(row=row, column=15).value
    if "," in menteeMentoringAreas:
        mentoringArea = menteeMentoringAreas.strip().split(",")
    else:
        mentoringArea = list(menteeMentoringAreas)

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
    if "," in menteeMentoringSkills:
        mentoringSkills = menteeMentoringSkills.strip().split(",")
    else:
        mentoringSkills = list(menteeMentoringSkills)

    
    #Research Areas Needing Improvement
    menteeResearchAreas = sheet.cell(row=row, column=23).value
    if "," in menteeResearchAreas:
        researchAreas = menteeResearchAreas.strip().split(",")
    else:
        researchAreas = list(menteeResearchAreas)

    #Career Areas Needing Improvement
    menteeCareerAreas = sheet.cell(row=row, column=24).value
    if "," in menteeCareerAreas:
        careerAreas = menteeCareerAreas.strip().split(",")
    else:
        careerAreas = list(menteeCareerAreas)

    #Do they aspire to lead?
    menteeLeadAspiration = sheet.cell(row=row, column=25).value
    leadAspiration = (True, False)[menteeLeadAspiration == "No"]
                    #(if_test_is_false, if_test_is_true)[test]

    #Leadership Skills Needing Improvement
    menteeLeadershipSkills = sheet.cell(row=row, column=26).value
    if "," in menteeLeadershipSkills:
        leadershipSkills = menteeLeadershipSkills.strip().split(",")
    else:
        leadershipSkills = list(menteeLeadershipSkills)

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
                "languages":languages, 
                "timezone": timezone, 
                "commsPreference": commsPreference, 
                "mentoringArea": mentoringArea,
                "motivationStatement": motivationStatement, 
                "preferredOutcomes": preferredOutcomes, 
                "professionalCharacteristics": professionalCharacteristics,
                "experienceStatement": experienceStatement, 
                "careerGoals": careerGoals, 
                "impactDiscussion": impactDiscussion, 
                "mentoringSkills": mentoringSkills,
                "researchAreas": researchAreas, 
                "careerAreas": careerAreas, 
                "leadAspiration": leadAspiration, 
                "leadershipSkills": leadershipSkills
                }
    return cleanRow


        