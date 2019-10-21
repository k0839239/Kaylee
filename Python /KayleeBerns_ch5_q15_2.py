def determine_grade(test_score):
    if test_score >= 90 and test_score <= 100:
        return 'A'
    elif test_score >= 80 and test_score <= 89:
        return 'B'
    elif test_score >= 70 and test_score <= 79:
        return 'C'
    elif test_score >= 60 and test_score <= 69:
        return 'D'
    elif test_score <= 60 and test_score >= 0:
        return 'F'
    else:
        return "invalid score"


if __name__ == "__main__":
    input_test_score = input("Enter value fot test score")
    print(determine_grade(int(input_test_score)))
