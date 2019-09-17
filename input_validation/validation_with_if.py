"""
Program: Basic Input and Format Output Program - Module 3
Author: Ryan Blankenship
Last date modified: 09/09/2019
The purpose of this program is to take tests scores,
in this 3 entered by the user. It will then return
the average of the 3 test scores.
"""


def average(score1, score2, score3):

    if score1 <= 0 or score2 <= 0 or score3 <= 0:
        print("No negative scores please.")
        return -1
    else:
        average_score = (int(score1) + int(score2) + int(score3)) / 3
        return average_score


if __name__ == '__main__':
    last_name = input("Please enter your last name:")
    first_name = input("Please enter your first name:")
    age = input("Please enter your age:")
    score1 = int(input("Please enter your first test score:"))
    score2 = int(input("Please enter your second test score:"))
    score3 = int(input("Please enter your third test score:"))
    average_score = average()
    print(last_name + ',' + first_name + ' ' + 'age:' + age + ' ' +
          'average score: ' + '%5.2f' % average_score)
    # the expected output is user input of 3 test scores then displaying the average.
