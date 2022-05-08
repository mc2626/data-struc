"""
-------------------------------------------------------
Family Class
-------------------------------------------------------
Author:  your name
Email:   your email
__updated__ = "2022-05-08"
-------------------------------------------------------
"""


class Family:

    SPORTS = (
        "volleyball", "skiing", "running", "biking", "swimming", "rollerblading", "skating", "hiking")

    @staticmethod
    def sports_menu():
        """
        -------------------------------------
        Creates a string of Family sports in the format:
        Sports:
            0 - volleyball
            1 - skiing
            2 - running
            ...
            7 - hiking
        Use: s = Family.sports_menu()
        Use: print(Family.sports_menu())
        -------------------------------------
        Returns:
        string - A numbered string of Family sports.
        -------------------------------------
        """
        string = "Sports: \n"
        for i in range(len(Family.SPORTS)):
            if i <= 9:
                string += " " + str(i) + " - " + Family.SPORTS[i] + "\n"
            else:
                string += str(i) + " - " + Family.SPORTS[i] + "\n"
        return string

    def __init__(self, name, age, gender, being, sports):
        """
        --------------------------------------
        Initializes a Family object.
        Use: family = Movie(name, age, gender, being, sport)
        --------------------------------------
        Parameters:
            name - family member name (str)
            age - family member age (int)
            gender - family memeber gender (str)
            being - type of family member (str)
            sports - numbers representing family member sport_list (list of int)
        Returns:
            A new Family object (Family)
        -------------------------------------------------------
        """
        self.name = name
        self.age = age
        self.gender = gender
        self.being = being
        self.sports = sports

    def __str__(self):
        """
        -------------------------------------------------------
        Creates a formatted string of family data.
        Use: print(family)
        Use: print( "{}".format(family))
        Use: string = str(family)
        -------------------------------------------------------
        Returns:
            string - the formatted contents of family (str)
        -------------------------------------------------------
        """
        # Generate the list of sports as a string.
        sports_list = self.sports_string()

        string = """Name:   {}
Age:    {}
Gender: {}
Being:  {}
Sports: {}""".format(self.name, self.age, self.gender, self.being,
                     sports_list)

        return string

    def __eq__(self, other):
        """
        -------------------------------------------------------
        Compares this family member against another family member for equality.
        Use: family == other
        -------------------------------------------------------
        Parameters:
            other - other family member to compare to (Family)
        Returns:
            result - True age matchs, False otherwise (boolean)
        -------------------------------------------------------
        """
        result = (self.age) == \
            (other.age)
        return result

    def __lt__(self, other):
        """
        -------------------------------------------------------
        Determines if this family member comes before another family member.
        Use: family < other
        -------------------------------------------------------
        Parameters:
            other - family member to compare to (Family)
        Returns:
            result - True if family member precedes other, False otherwise (boolean)
        -------------------------------------------------------
        """
        result = (self.age) < \
            (other.age)
        return result

    def __le__(self, other):
        """
        -------------------------------------------------------
        Determines if this family member precedes or is or equal to another family member.
        Use: family <= other
        -------------------------------------------------------
        Parameters:
            other - family member to compare to (Family)
        Returns:
            result - True if this family member precedes or is equal to other,
              False otherwise (boolean)
        -------------------------------------------------------
        """
        result = self < other or self == other
        return result

    def sports_string(self):
        """
        -------------------------------------------------------
        Returns comma delimited string of sports based upon the
        current family object's integer sports list.
        e.g.: [0, 2] returns "volleyball, running"
        Use: string = family.sports_string()
        -------------------------------------------------------
        Returns:
            string - string of sports (str)
        -------------------------------------------------------
        """
        string = ""
        if self.sports is not None:
            for i in self.sports[:-1]:
                string += Family.SPORTS[int(i)] + ", "
            string += Family.SPORTS[int(self.sports[-1])]
        return string
