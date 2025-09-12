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

