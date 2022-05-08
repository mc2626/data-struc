"""
-------------------------------------------------------
def read_families testing
-------------------------------------------------------
Author:  Your Name
ID:      Your ID
Email:   your email@mylaurier.ca
__updated__ = "2022-05-03"
-------------------------------------------------------
"""
# Imports
from Family_utilities import read_families

fv = open('family.txt', 'r')
families = read_families(fv)
fv.close()

for family in families:
    print(family)
    print()
