import json

def mentee_cleanup(mentees):
    cleaned_mentees = []
    for mentee in mentees:
        new_mentee = {}
        new_mentee['ranking_score'] = 0
        for k,v in mentee.items():
            if k == 'Email Address':
                new_mentee['email'] = v
            elif 'First name' in k:
                new_mentee['first_name'] = v
            elif 'Last name' in k:
                new_mentee['last_name'] = v
            elif 'Do you identify' in k:
                new_mentee['is_latinx'] = v
            elif 'Origin' in k:
                new_mentee['origin'] = v
            elif 'Current Location' in k:
                new_mentee['location'] = v
            elif 'Institution, Company or Organization' in k:
                new_mentee['affiliation'] = v
            elif 'Current Position' in k:
                    if 'Career Professional' in v:
                        new_mentee['ranking_score'] += 10
                    elif 'Senior Ph.D.' in v:
                        new_mentee['ranking_score'] += 10
                    elif 'Junior Ph.D' in v:
                        new_mentee['ranking_score'] += 6
                    elif 'Graduate Student' or 'M. Sc.' in v:
                        new_mentee['ranking_score'] += 4
                    elif 'Undergraduate Student' or 'Early Career' or 'Undergrad' in v:
                        new_mentee['ranking_score'] += 2
            elif 'do you speak' in k:
                new_mentee['languages'] = v
            elif 'preferred timezone' in k:
                new_mentee['preferred_timezone'] = v
            elif 'prefer to connect ' in k:
                new_mentee['preferred_connection'] = v
            elif 'hope to achieve' in k:
                desired_outcome = []
                if "detailed feedback" in v:
                    desired_outcome.append("Feedback")
                if "Prepare a submission" in v:
                    desired_outcome.append("Conference")
                if "career options" in v:
                    desired_outcome.append("Career advice")
                if "best practices and tools" in v:
                    desired_outcome.append("Best practices")
                if "lasting connection" in v:
                    desired_outcome.append("lasting connection")
                new_mentee['desired_outcomes'] = desired_outcome
            elif 'skills you are interested in being mentored' in k:
                new_mentee['skills'] = v
            elif 'research areas you are interested in being mentored' in k:
                new_mentee['research'] = v
            elif 'specific research field or application domain' in k:
                new_mentee['specific_domain'] = v
            elif 'How many research papers' in k:
                new_mentee['ranking_score'] += int(v[0])
            elif 'Have you submitted a paper' in k:
                if v == 'Yes':
                    new_mentee['ranking_score'] += 3
            else:
                pass
        
        cleaned_mentees.append(new_mentee)
    return(cleaned_mentees)

def mentor_cleanup(mentors):
    cleaned_mentors = []
    count = 1
    for mentor in mentors:
        new_mentor = {}
        new_mentor['id'] = count
        for k,v in mentor.items():
            if k == 'Email Address':
                new_mentor['email'] = v
            elif 'First name' in k:
                new_mentor['first_name'] = v
            elif 'Last name' in k :
                new_mentor['last_name'] = v
            elif 'Gender' in k:
                new_mentor['gender'] = v
            elif 'Do you identify' in k:
                new_mentor['is_latinx'] = v
            elif 'Origin' in k:
                new_mentor['origin'] = v
            elif 'Current Location' in k:
                new_mentor['location'] = v
            elif 'Current Position' in k:
                new_mentor['position'] = v   
            elif 'Institution, Company or Organization' in k:
                new_mentor['affiliation'] = v
            elif 'Seniority' in k:
                new_mentor['seniority'] = v
            elif 'do you speak' in k:
                new_mentor['languages'] = v
            elif 'preferred timezone' in k:
                new_mentor['preferred_timezone'] = v
            elif 'prefer to connect' in k:
                new_mentor['preferred_connection'] = v
            elif 'kinds of support' in k:
                support_offered = []
                if "detailed feedback" in v:
                    support_offered.append("Feedback")
                if "conference submission" in v:
                    support_offered.append("Conference")
                if "career advice" in v:
                    support_offered.append("Career advice")
                if "tools or best practices" in v:
                    support_offered.append("Best practices")
                if "lasting connection" in v:
                    support_offered.append("lasting connection")
                new_mentor['support_offered'] = support_offered
            elif 'How much time do you have available' in k:
                if v[0] == '1':
                    new_mentor['mentee_slots'] = [None]
                else:
                    new_mentor['mentee_slots'] = [None, None]
            elif 'characteristics/profile of a mentee' in k:
                new_mentor['desired_mentee'] = v
            elif 'Do have any specific preferences for accepting a mentee?' in k:
                new_mentor['specific_preference'] = v
            elif 'What skills do you want to help mentees to improve?' in k:
                new_mentor['skills'] = v
            elif 'What are the research areas you are interested in mentoring' in k:
                new_mentor['research'] = v
            elif 'Do you work in a specific research field or application domain?' in k:
                new_mentor['specific_domain'] = v
            else:
                pass
            count += 1
        cleaned_mentors.append(new_mentor)
    return(cleaned_mentors)