#!/usr/bin/env python3
"""Simple program to read CSV file into a list of dictionaries."""

import csv
from typing import List, Dict, Any

def read_csv_to_dict(filepath: str) -> List[Dict[str, Any]]:
    """
    Read a CSV file and return a list of dictionaries.
    Each row becomes a dictionary with column headers as keys.
    """
    data = []
    
    try:
        with open(filepath, 'r', newline='', encoding='utf-8') as csvfile:
            # DictReader automatically uses first row as headers
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                data.append(dict(row))  # Convert OrderedDict to regular dict
                
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []
    
    return data

def print_data_info(data: List[Dict[str, Any]]) -> None:
    """Print basic information about the loaded data."""
    if not data:
        print("No data loaded.")
        return
    
    print(f"Loaded {len(data)} rows")
    print(f"Columns: {list(data[0].keys())}")
    print("\nFirst few rows:")
    
    for i, row in enumerate(data[:3]):  # Show first 3 rows
        print(f"Row {i + 1}: {row}")

import csv
from datetime import datetime

def export_mentor_assignments_to_csv(mentor_list, mentee_list, filename=None):
    """
    Export mentor assignments to a CSV file optimized for email coordination.
    Focuses on contact info, timing, and communication preferences.
    """
    
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"mentor_assignments_{timestamp}.csv"
    
    # Create mentee lookup for additional details if provided
    mentee_lookup = {}
    if mentee_list:
        mentee_lookup = {mentee.get('email'): mentee for mentee in mentee_list}
    
    # Define CSV headers
    headers = [
        # Mentor Information
        'mentor_id',
        'mentor_first_name', 
        'mentor_last_name',
        'mentor_email',
        'mentor_affiliation',
        'mentor_timezone',
        'mentor_communication_preference',
        
        # Mentee Information  
        'mentee_first_name',
        'mentee_last_name', 
        'mentee_email',
        'mentee_affiliation',
        'mentee_timezone',
        'mentee_communication_preference',
        
        # Match Information
        'compatibility_score',
        'key_matches',
        
        # Coordination Notes
        'assignment_status',
        'notes_for_coordinator'
    ]
    
    rows = []
    total_assignments = 0
    mentors_with_assignments = 0
    
    for mentor in mentor_list:
        has_mentees = False
        
        # Check if mentor has any assigned mentees
        if 'mentee_slots' in mentor and mentor['mentee_slots']:
            for slot in mentor['mentee_slots']:
                if slot is not None:  # Assigned mentee
                    has_mentees = True
                    total_assignments += 1
                    
                    # Get additional mentee details if available
                    mentee_email = slot.get('email', '')
                    mentee_details = mentee_lookup.get(mentee_email, {})
                    
                    # Extract key matching areas for easy reference
                    key_matches = []
                    if 'match_details' in slot:
                        high_matches = [k for k, v in slot['match_details'].items() 
                                      if isinstance(v, (int, float)) and v >= 0.8]
                        key_matches = high_matches[:3]  # Top 3 strong matches
                    
                    row = {
                        # Mentor info
                        'mentor_id': mentor.get('id', ''),
                        'mentor_first_name': mentor.get('first_name', ''),
                        'mentor_last_name': mentor.get('last_name', ''),
                        'mentor_email': mentor.get('email', ''),
                        'mentor_affiliation': mentor.get('affiliation', ''),
                        'mentor_timezone': mentor.get('preferred_timezone', ''),
                        'mentor_communication_preference': mentor.get('preferred_connection', ''),
                        
                        # Mentee info
                        'mentee_first_name': slot.get('first_name', ''),
                        'mentee_last_name': slot.get('last_name', ''),
                        'mentee_email': mentee_email,
                        'mentee_affiliation': mentee_details.get('affiliation', ''),
                        'mentee_timezone': mentee_details.get('preferred_timezone', ''),
                        'mentee_communication_preference': mentee_details.get('preferred_connection', ''),
                        
                        # Match info
                        'compatibility_score': f"{slot.get('compatibility_score', 0):.3f}",
                        'key_matches': ', '.join(key_matches),
                        
                        # Coordination
                        'assignment_status': 'ASSIGNED - Ready for introduction email',
                        'notes_for_coordinator': f"Match score: {slot.get('compatibility_score', 0):.1%}"
                    }
                    rows.append(row)
        
        if has_mentees:
            mentors_with_assignments += 1
        else:
            # Include mentors with no assignments so coordinator knows they're available
            row = {
                # Mentor info
                'mentor_id': mentor.get('id', ''),
                'mentor_first_name': mentor.get('first_name', ''),
                'mentor_last_name': mentor.get('last_name', ''),
                'mentor_email': mentor.get('email', ''),
                'mentor_affiliation': mentor.get('affiliation', ''),
                'mentor_timezone': mentor.get('preferred_timezone', ''),
                'mentor_communication_preference': mentor.get('preferred_connection', ''),
                
                # Empty mentee info
                'mentee_first_name': '',
                'mentee_last_name': '',
                'mentee_email': '',
                'mentee_affiliation': '',
                'mentee_timezone': '',
                'mentee_communication_preference': '',
                
                # No match info
                'compatibility_score': '',
                'key_matches': '',
                
                # Coordination
                'assignment_status': 'AVAILABLE - No mentees assigned',
                'notes_for_coordinator': 'Available for additional assignments'
            }
            rows.append(row)
    
    # Sort rows: assigned mentorships first (by mentor name), then available mentors
    rows.sort(key=lambda x: (
        x['assignment_status'] != 'ASSIGNED - Ready for introduction email',
        x['mentor_last_name'],
        x['mentor_first_name']
    ))
    
    # Write CSV file
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
    
    # Print summary
    print(f"📄 CSV Export Complete!")
    print(f"File saved as: {filename}")
    print(f"Total mentor-mentee pairs: {total_assignments}")
    print(f"Mentors with assignments: {mentors_with_assignments}")
    print(f"Available mentors: {len(mentor_list) - mentors_with_assignments}")
    print(f"Total rows in CSV: {len(rows)}")
    print(f"\n💡 Coordinator Tips:")
    print(f"   - Filter by 'assignment_status' = 'ASSIGNED' to see pairs needing introduction emails")
    print(f"   - Check timezone compatibility for scheduling first meetings")
    print(f"   - Use communication preferences to suggest best contact methods")
    print(f"   - Use 'key_matches' column to personalize introduction emails")
    
    return filename

# Usage:
# csv_filename = export_mentor_assignments_to_csv(mentors, mentee_list)