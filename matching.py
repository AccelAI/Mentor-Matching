'''
The matching algo

Dead stop if no matches:
** Languages

Matched on simple intersect from multichoice answers
** Language
** Timezone
** preferred connection
** Skills
** Research
** Specific Domain
** Hope to achieve (mentee) to What kinds of support are you able to offer? (mentor)

Matched on string inferance or other method from freeform answers (v 1.1)
*** Mentee:  Motivation statement, Profile statement, Career Goals
*** Mentor:  Mentee Characteristics, Specific Preferences, Hope to contribute


Mentors limited to 2 mentees total
'''
def calculate_mentorship_compatibility(mentor, mentee):
    """Calculate compatibility score between mentor and mentee"""
    
    # Parse languages helper function
    def parse_comma_separated(value):
        if isinstance(value, str):
            return {item.strip() for item in value.split(',')}
        return set()
    
    # MANDATORY: Check language compatibility first
    if 'languages' in mentor and 'languages' in mentee:
        mentor_languages = parse_comma_separated(mentor['languages'])
        mentee_languages = parse_comma_separated(mentee['languages'])
        
        # If no common languages, automatic zero compatibility
        if not (mentor_languages & mentee_languages):
            return {'incompatible_languages': True, 'shared_languages': 0}
    
    scores = {}
    
    # 1. Exact matches (binary scoring)
    exact_match_fields = ['is_latinx', 'origin', 'location', 'preferred_timezone', 'specific_domain']
    for field in exact_match_fields:
        if field in mentor and field in mentee:
            scores[field] = 1.0 if mentor[field] == mentee[field] else 0.0
    
    # 2. Set intersections (for comma-separated values)
    intersection_fields = ['languages', 'preferred_connection', 'research', 'skills']
    for field in intersection_fields:
        if field in mentor and field in mentee:
            mentor_set = parse_comma_separated(mentor[field])
            mentee_set = parse_comma_separated(mentee[field])
            
            if mentor_set and mentee_set:
                intersection = len(mentor_set & mentee_set)
                union = len(mentor_set | mentee_set)
                scores[field] = intersection / union  # Jaccard similarity
            else:
                scores[field] = 0.0
    
    # 3. Special matching: mentee desired_outcomes vs mentor support_offered
    if 'desired_outcomes' in mentee and 'support_offered' in mentor:
        mentee_needs = set(mentee['desired_outcomes'])
        mentor_offers = set(mentor['support_offered'])
        
        if mentee_needs and mentor_offers:
            overlap = len(mentee_needs & mentor_offers)
            scores['outcome_support_match'] = overlap / len(mentee_needs)
        else:
            scores['outcome_support_match'] = 0.0
    
    return scores

def get_weighted_compatibility_score(mentor, mentee, weights=None):
    """Get overall weighted compatibility score"""
    
    scores = calculate_mentorship_compatibility(mentor, mentee)
    
    # Check if automatically incompatible due to language barrier
    if 'incompatible_languages' in scores:
        return 0.0, scores
    
    # Default weights - adjust based on importance
    default_weights = {
        'outcome_support_match': 3.0,  # Most important
        'research': 2.5,               # Very important
        'skills': 2.0,                 # Important
        'preferred_timezone': 2.0,     # Important for scheduling
        'languages': 1.5,              # Helpful (they already have common language)
        'preferred_connection': 1.5,   # Helpful
        'origin': 1.0,                 # Nice to have
        'location': 1.0,               # Nice to have
        'is_latinx': 1.0,              # Community connection
        'specific_domain': 1.0,        # Domain alignment
    }
    
    if weights:
        default_weights.update(weights)
    
    total_score = 0
    max_possible = 0
    
    for field, score in scores.items():
        weight = default_weights.get(field, 1.0)
        total_score += score * weight
        max_possible += weight
    
    return total_score / max_possible if max_possible > 0 else 0, scores

# Usage with early exit for language incompatibility:
def find_compatible_mentors(mentee, mentor_list):
    """Find all compatible mentors, storing only essential mentor data"""
    compatible = []
    
    for mentor in mentor_list:
        score, details = get_weighted_compatibility_score(mentor, mentee)
        
        if score > 0:  # Only include if compatible (score > 0)
            # Extract only essential mentor information
            mentor_summary = {
                'mentor_id': mentor.get('id'),
                'mentor_firstname': mentor.get('first_name'),
                'mentor_lastname': mentor.get('last_name'), 
                'mentor_email': mentor.get('email')
            }
            
            compatible.append({
                'mentor': mentor_summary,
                'compatibility_score': score,
                'match_details': details
            })
    
    # Sort by compatibility score (highest first)
    return sorted(compatible, key=lambda x: x['compatibility_score'], reverse=True)