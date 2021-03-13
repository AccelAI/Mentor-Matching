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

    # for mentee in allMentees:
    #     mentee.printAll()

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
    menteeTopMentors = {}
    for mentee in allMentees:
        menteeId = mentee.menteeId
        menteePotentialMatches = mentorMatch(mentee, allMentors)        
        menteeMatches[menteeId] = menteePotentialMatches

        #menteeTopMentors[menteeId] = maxMatches(menteePotentialMatches)

    #print(menteeTopMentors)
    # for k, v in menteeTopMentors.items():
    #     print("Mentee: {}\tTop Mentors: {}".format(k, v))s
        # maxMatches(menteePotentialMatches)

    #print(menteeMatches)
    for k, v in menteeMatches.items():
        print("{} : {}".format(k, v))
    #for mentor in allMentors:
    #    print("Mentor {} highest matches: {}".format(mentor.firstName, mentor.mentorMatches))


    # Assign Mentees to Mentors based on mentee match % and mentors mentee limit
    #assignToMentor(menteeTopMentors, allMentors, allMentees)    

    

    #wb.save("LXAI_MP_Matched.xlsx")

