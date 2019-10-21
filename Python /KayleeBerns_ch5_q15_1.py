
def calc_average (test_1, test_2, test_3, test_4, test_5):
    return (test_1 + test_2 + test_3 + test_4 + test_5 ) /5

if __name__ == "__main__":
    input_test_1 = input("Enter value for test 1 score")
    input_test_2 = input("Enter value for test 2 score")
    input_test_3 = input("Enter value for test 3 score")
    input_test_4 = input("Enter value for test 4 score")
    input_test_5 = input("Enter value for test 5 score")
    print(calc_average(int(input_test_1), int(input_test_2), int(input_test_3), int(input_test_4), int(input_test_5)))
