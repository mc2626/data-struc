"""
-------------------------------------------------------
def read_family testing
-------------------------------------------------------
Author:  Your Name
ID:      Your ID
Email:   your email@mylaurier.ca
__updated__ = "2022-05-03"
-------------------------------------------------------
"""
# Imports

from Family_utilities import read_family

line = "Mila|18|female|human|0,1,5,6,7"
family = read_family(line)
print(family)
