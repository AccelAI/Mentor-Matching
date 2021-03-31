#!/usr/bin/env python3

from openpyxl import *
from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font
from mentee import *
from mentor import *
from utils import *


if __name__ == '__main__':
    wb = Workbook()
    #create new xlsxwriter workbook object

    mentees = load_workbook('mentees.xlsx')
    mentors = load_workbook('mentors.xlsx')

    matches = wb.active

    matches.title = "Mentor to Mentee"

    menteeSheet = mentees.active
    mentorSheet = mentors.active

    row = 2
    allMentees = []
    allMentors = []

    while menteeSheet.cell(row=row, column=1).value != None:
        menteeRow = processMentee(menteeSheet, row)
        mentee = Mentee()
        for k,v in menteeRow.items():
            setattr(mentee, k, v)
    
        allMentees.append(mentee)
        row = row + 1

    # for k in allMentees.keys():
    #    print(k)

    row = 2
    while mentorSheet.cell(row=row, column=1).value != None:
        mentorRow = processMentor(mentorSheet, row)
        mentor = Mentor()
        for k,v in mentorRow.items():
            setattr(mentor, k, v)
    
        allMentors.append(mentor)
        row = row + 1

    # for mentor in allMentors:
    #     mentor.printAll()

    #Statistics
    #Average Match
    menteeMatches = {}
    menteeAcceptableMentors = {}
    for mentee in allMentees:
        menteeId = mentee.menteeId
        menteePotentialMatches = mentorMatch(mentee, allMentors)        
        menteeMatches[menteeId] = menteePotentialMatches

        menteeAcceptableMentors[menteeId] = acceptableMatches(menteePotentialMatches)

 
    #for k, v in menteeAcceptableMentors.items():
    #    print("Mentee: {}\tTop Mentors: {}".format(k, v))

    priorityWithRating = menteePriority(allMentees)
    priority = []
    for item in priorityWithRating:
        priority.append(list(item.keys())[0])

    # Assign Mentees to Mentors based on mentee match % and mentors mentee limit
    unmatched = assignToMentor(menteeAcceptableMentors, priority, allMentors, allMentees)    

    if unmatched != {}:
        print(list(unmatched.keys))
    else:
        print("All mentees matched")

    #wb.save("LXAI_MP_Matched.xlsx")

