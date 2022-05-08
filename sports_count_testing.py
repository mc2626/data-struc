"""
-------------------------------------------------------
def sports_counts testing
-------------------------------------------------------
Author:  Your Name
ID:      Your ID
Email:   your email@mylaurier.ca
__updated__ = "2022-05-05"
-------------------------------------------------------
"""
# Imports
from Family import Family
from Family_utilities import sports_count, read_families

fv = open('family.txt', 'r')
families = read_families(fv)
fv.close()

counts = sports_count(families)
print(f"Sports List:       {[i for i in Family.SPORTS if True]}")
print(f"Sports Count List: {counts}")
