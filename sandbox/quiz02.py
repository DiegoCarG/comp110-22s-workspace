"""Practicing functions on study guide."""

__author__ = 730427471


def odd_and_even(original: list[int]) -> list[int]:
    i: int = 0
    new: list[int] = []
    while i < len(original):
        if i % 2 == 0 and original[i] % 2 != 0:
            new.append(original[i])
        i += 1
    return new


def average_grades(student_grades: dict[str, list[int]]) -> dict[str, float]:
    averages: dict[str, float] = {}
    for key in student_grades:
        total: int = 0
        for value in student_grades[key]:
            total += value
            averages[key] = total / len(student_grades[key])
    return averages


print(average_grades({'Bill': [75, 94, 97], 'Annie': [88, 93, 99]}))

        