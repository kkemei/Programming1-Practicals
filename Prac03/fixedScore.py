"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def convert_score_to_value(score):
    if score > 100 or score < 0:
        return score
    elif score > 90:
        return score
    elif score >= 50:
        return score
    else:
        return score

def main():
    score = float(input("Enter score: "))
    if score > 100 or score < 0:
        print("Invalid score")
    elif score > 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")
main()

