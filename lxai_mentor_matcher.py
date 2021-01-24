from openpyxl import *
from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font
from mentee import *
from mentor import *
from utils import *



def main():

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

    #for mentee in allMentees:
    #    mentee.printAll()

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
    
    for mentee in allMentees:
        menteeId = mentee.menteeId
        menteePotentialMatches = mentorMatch(mentee, allMentors)        
        menteeMatches[menteeId] = menteePotentialMatches

        # maxMatches(menteePotentialMatches)

    # print(menteeMatches)
    for mentor in allMentors:
        print("Mentor {} highest matches: {}".format(mentor.firstName, mentor.mentorMatches))


    wb.save("LXAI_MP_Matched.xlsx")

if __name__ == '__main__':
    main()

