def assign_mentees_to_mentors(mentee_list, mentor_list):
    """
    Assign mentees to mentors based on their existing compatibility lists and available slots.
    
    Returns:
        - Updated mentor_list with assigned mentees
        - List of unassigned mentees
    """
    
    # Create a lookup dictionary for mentors by ID for efficient access
    mentor_lookup = {mentor['id']: mentor for mentor in mentor_list}
    
    unassigned_mentees = []
    
    for mentee in mentee_list:
        assigned = False
        
        # Check if mentee has compatibility list
        if 'compatible_list' not in mentee or not mentee['compatible_list']:
            unassigned_mentees.append({
                'mentee': {
                    'first_name': mentee.get('first_name'),
                    'last_name': mentee.get('last_name'),
                    'email': mentee.get('email')
                },
                'reason': 'No compatible mentors found'
            })
            continue
        
        # Try to assign to most compatible mentor with available slots
        for match in mentee['compatible_list']:
            mentor_id = match['mentor']['mentor_id']
            
            # Find the mentor in our mentor list
            if mentor_id in mentor_lookup:
                mentor = mentor_lookup[mentor_id]
                
                # Check if mentor has available slots
                if mentor['mentee_slots'] and None in mentor['mentee_slots']:
                    # Find first available slot
                    for i, slot in enumerate(mentor['mentee_slots']):
                        if slot is None:
                            # Assign mentee to this slot
                            mentor['mentee_slots'][i] = {
                                'first_name': mentee.get('first_name'),
                                'last_name': mentee.get('last_name'),
                                'email': mentee.get('email'),
                                'compatibility_score': match['compatibility_score'],
                                'match_details': match['match_details']
                            }
                            assigned = True
                            print(f"✅ Assigned {mentee.get('first_name')} {mentee.get('last_name')} to mentor {mentor.get('first_name', 'Unknown')} {mentor.get('last_name', 'Unknown')} (Score: {match['compatibility_score']:.3f})")
                            break
                    
                    if assigned:
                        break
        
        # If mentee couldn't be assigned to any mentor
        if not assigned:
            unassigned_mentees.append({
                'mentee': {
                    'first_name': mentee.get('first_name'),
                    'last_name': mentee.get('last_name'),
                    'email': mentee.get('email')
                },
                'reason': 'All compatible mentors are full'
            })
    
    # Print summary
    print(f"\n📊 Assignment Summary:")
    print(f"Total mentees processed: {len(mentee_list)}")
    print(f"Successfully assigned: {len(mentee_list) - len(unassigned_mentees)}")
    print(f"Unassigned: {len(unassigned_mentees)}")
    
    if unassigned_mentees:
        print(f"\n❌ Unassigned mentees:")
        for unassigned in unassigned_mentees:
            mentee_info = unassigned['mentee']
            print(f"  - {mentee_info['first_name']} {mentee_info['last_name']} ({mentee_info['email']}) - {unassigned['reason']}")
    
    return mentor_list, unassigned_mentees