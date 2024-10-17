"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    grade = parameter(score)
    print(grade)
    score = random.randint(1,100)
    grade = parameter(score)
    print(grade)


def parameter(score):
    if score <= 0:
        grade = "Invalid score"
    elif score > 100:
        grade = "Invalid score"
    elif score >= 90:
        grade = "Excellent"
    elif score >= 50:
        grade = "Passable"
    elif score < 50:
        grade = "Bad"
    return grade


main()