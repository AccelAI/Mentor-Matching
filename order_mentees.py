'''
The goal of this function is to create an order list of the mentees in descending
order based on their ranking score.

Ranking score is determined by their seniority level in academia or career, and
how many professional papers they have publised.

One ordered in this list, this is the order they will be matched in so that higher
ranked mentees have a better chance of getting their preferred mentors by being
earlier in the matching process.

'''

def match_order(mentees):
    ranked_mentees=[]
    for mentee in mentees:
        if len(ranked_mentees) == 0:
            ranked_mentees.append(mentee)
        else:
            position = len(ranked_mentees) - 1
            not_inserted = True
            while(not_inserted):
                if ranked_mentees[position]['ranking_score']  >= mentee['ranking_score']:
                    ranked_mentees.insert(position + 1, mentee)
                    not_inserted = False
                elif position == 0:
                    ranked_mentees.insert(position, mentee)
                    not_inserted = False
                else:
                    position -= 1
    count = 1
    for mentee in ranked_mentees:
        mentee['id'] = count
        count += 1
    return ranked_mentees
    