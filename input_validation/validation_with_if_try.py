"""
Program: Basic Input and Format Output Program - Module 3
Author: Ryan Blankenship
Last date modified: 09/15/2019
The purpose of this program is to take tests scores,
in this 3 entered by the user. It will then return
the average of the 3 test scores.

Update: Function now taking parameters.
"""


def average(score1, score2, score3):
    if score1 <= 0:
        raise ValueError
    else:
        average_score = (float(score1) + float(score2) + float(score3)) / 3
        return average_score


if __name__ == '__main__':
    last_name = input("Please enter your last name:")
    first_name = input("Please enter your first name:")
    age = input("Please enter your age:")
    score_one = int(input("Please enter your first test score:"))
    score_two = int(input("Please enter your second test score:"))
    score_three = int(input("Please enter your third test score:"))
    average_scores = average(score_one, score_two, score_three)
    print(last_name + ',' + first_name + ' ' + 'age:' + age + ' ' +
          'average score: ' + '%5.2f' % average_scores)
    # the expected output is user input of 3 test scores then displaying the average.
