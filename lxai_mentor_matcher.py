from openpyxl import *
from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font
from mentee import *
from mentor import *
from utils import *



def main():

    wb = Workbook()
    #create new xlsxwriter workbook object

    mentees = load_workbook('mentees.xlsx')
    # mentors = load_workbook('mentors.xlxs')

    matches = wb.active

    matches.title = "Mentor to Mentee"

    menteeSheet = mentees.active
    # mentorSheet = mentors.active

    row = 2
    allMentees = []
    # allMentors = []

    while menteeSheet.cell(row=row, column=1).value != None:
        menteeRow = processMentee(menteeSheet, row)
        mentee = Mentee()
        for k,v in menteeRow:
            setattr(mentee, k, v)
    
        allMentees.append(mentee)
        row = row + 1

    for mentee in allMentees:
        mentee.printAll()



    wb.save("LXAI_MP_Matched.xlsx")

if __name__ == '__main__':
    main()

