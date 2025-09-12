from data_cleanup import mentee_cleanup, mentor_cleanup
from file_io import read_csv_to_dict, print_data_info
from order_mentees import match_order
'''
Goal

Create a more flexible mentor matching system that can be used by LXAI
in the future without me needing to rewrite this every time

Provide good matches between mentor and mentee
Provide back up matches if first pick doesnt work
Provide insight on why the matches happened or if none, why

componenet

** Read in from 2 different csv files
** Load Mentees and Mentors in to respective dicts with all details
** Clean the data as the new headers are super long and not all fields necessary for matching
** Create an order for mentee matching based on new criteria for first dibs
** Run matching in go order so best mentees get first dibs on top match
** Ouput the matches in usable format
'''

mentees_csv = '2025_neurips_mentees.csv'
mentors_csv = '2025_neurips_mentors.csv'

def lxai_mentor_matching():
    
    # Pull in the raw data from the csv files
    mentees_raw = read_csv_to_dict(mentees_csv)
    mentors_raw = read_csv_to_dict(mentors_csv)

    # clean up the dictionary opjects with shorter keys and strip unnecessary data k/v
    mentees = mentee_cleanup(mentees_raw)
    mentors = mentor_cleanup(mentors_raw)

    # put mentees in an list ordered by ranking score
    mentees = match_order(mentees)


if __name__ == '__main__':
    lxai_mentor_matching()
    print("All Done!")