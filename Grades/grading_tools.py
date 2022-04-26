"""Calculate my grades."""

__author__ = "Diego Cardenas"


import numpy as np


class course:
    """Create a course object which contains all relevant info."""
    
    def __init__(self, course_name: str, credit_hours: int, grading_criteria: list[float], current_grades: list[float]):
        """Initalize class."""
        self.course_name = course_name
        self.credit_hours = credit_hours
        self.grading_criteria = grading_criteria
        self.current_grades = current_grades
    
    def __repr__(self) -> dict[str, list[str]]:
        """Represents the values inputed into a couse object as a dictionary."""
        return_dict: dict[str, list[str]] = {}
        return_dict["Course Code"] = list(f"{self.course_name}")
        return_dict["Credit Hours"] = list(f"{self.credit_hours}")
        return_dict["GPA"] = list(f"{self.GPA()}")

        return return_dict

    def GPA(self) -> float:
        """Create a method to calculate the GPA for any given course object."""
        np_criteria = np.array(self.grading_criteria)
        np_grades = np.array(self.current_grades)
        # multiply all grades by criteria %s to get a weighted array
        np_weighted = np_criteria * np_grades
        # add up the weighted values to get a grade/100
        total = sum(np_weighted)

        # Now convert score/100 to the corresponding GPA
        # Try scrapping this and looping thru 2 corresponding lists

        GPA_scale: list[float] = [4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0]
        corresponding_mins: list[float] = [92.5, 89.5, 86.5, 82.5, 79.5, 76.5, 72.5, 69.5, 66.5, 62.5, 60, 0]
        return_list: list[float] = []
        for i in range(len(corresponding_mins)):
            if corresponding_mins[i] <= total:
                return_list.append(GPA_scale[i])

        return max(return_list)


    
        



