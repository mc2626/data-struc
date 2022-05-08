"""
-------------------------------------------------------
Family Utilities
-------------------------------------------------------
Author:  Your Name
ID:      Your ID
Email:   your email@mylaurier.ca
__updated__ = "2022-05-03"
-------------------------------------------------------
"""
# Imports
from Family import Family


def get_family():
    """
    -------------------------------------------------------
    Creates a Family object by requesting data from a user.
    Use: family = get_family()
    -------------------------------------------------------
    Returns:
        family - a family object based upon the user input (Family).
    ------------------------------------------------------
    """
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")
    being = input("Enter being: ")

    print(Family.sports_menu())
    sports = []
    sport = input("Enter sports codes: ")
    while sport != "":
        sports.append(sport)
        sport = input("Enter sports codes: ")

    family = Family(name, age, gender, being, sports)
    return family


def read_family(line):
    """
    -------------------------------------------------------
    Creates and returns a Family object from a line of formatted string data.
    Use: family = read_family(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of movie data in the format
          name|age|gender|being|sport codes (str)
    Returns:
        family - a Family object based upon the data from line (Family)
    ------------------------------------------------------
    """
    lst = line.split("|")
    # *populate sports_list because list is required as argument in family
    # object
    sports_list = []
    temp_sports_list = lst[4].split(",")
    for ele in temp_sports_list:
        sports_list.append(ele)
    family = Family(lst[0], int(lst[1]), lst[2], lst[3], sports_list)

    return family


def read_families(fv):
    """
    -------------------------------------------------------
    Reads a file of string data into a list of Family objects.
    Use: movies = read_families(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of family data (file)
    Returns:
        families - a list of family objects (list of Family)
    ------------------------------------------------------
    """
    families = []
    for line in fv:
        family = read_family(line)
        families.append(family)
    return families


def sports_count(families):
    """
    -------------------------------------------------------
    Counts the number of family members that play each sport
    given in Family.SPORTS.
    The original list of family must be unchanged.
    Use: counts = sports_count(families)
    -------------------------------------------------------
    Parameters:
        families - a list of Family objects (list of Family)
    Returns:
        counts - the number of family members for each sport in
        Family.SPORTS.
        The index of each number in counts is the index of
        the matching sport in Family.SPORTS. (list of int)
    ------------------------------------------------------
    """
    print(Family.sports_menu())

    # create placeholders with number 0
    counts = []
    for i in range(len(Family.SPORTS)):
        counts.append(0)
        i += 1

    # populate placeholders
    for family in families:
        if family.sports is not None:
            for sport in family.sports[:(len(Family.SPORTS))]:
                counts[int(sport)] += 1
    return counts
