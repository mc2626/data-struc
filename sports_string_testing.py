"""
-------------------------------------------------------
def sports_string
-------------------------------------------------------
Author:  Your Name
ID:      Your ID
Email:   your email@mylaurier.ca
__updated__ = "2022-05-03"
-------------------------------------------------------
"""
# Imports
from Family import Family

family = Family('Mila', 18, 'female', 'human', [0, 1, 5, 6, 7])
string = family.sports_string()
print(f"Sport(s): {string}")
