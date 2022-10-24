#!/usr/bin/python3

def parse_input(filename: str) -> \
        'list[tuple[list[int], list[tuple[str, int, int]]]]':
    """
    Reads input from file
    T: num of test cases to follow
    N, Q: length of array and number of operations
    A: Starting values for array
    I: The operations to perform

    TASK:

    Given an array A and a set of instructions I, calculate the sum of
    all queries ("q" instructions).
    Instructions can be:
     - ["u", i, x]  # Update the ith element of A (1-indexed) with x
     - ["q", i, j]  # Calculate the score for the subarray from the ith to
                    # the jth element (inclusive)

    The score of a sub array S is calculated by:
    1*S[0] - 2*S[1] + 3*S[2] -4*...

    returns: list[tuple[list[int], list[tuple[str, int, int]]]]
    """
    with open(filename) as f:
        num_test_cases = int(f.readline())
        test_cases: 'list[tuple[list[int], list[tuple[str, int, int]]]]' = []
        for _ in range(num_test_cases):
            N, Q = f.readline().split()
            A = [int(a) for a in f.readline().split()]
            I: 'list[tuple[str, int, int]]' = []
            for _ in range(int(Q)):
                q, i, j = f.readline().split()
                I.append((q, int(i), int(j)))
            test_cases.append((A, I))
    return test_cases


def write_output(filename: str, values: list) -> None:
    """
    Writes the data to file in a generic format for Google Kickstarter
    filename str: Name of file to write output
    values list: Solution from calculate_result()
    """
    out_txt = [f"Case #{i+1}: {y}" for i, y in enumerate(values)]
    print("Output writing to file:")
    print("\n".join(out_txt))
    with open(filename, "w") as f:
        f.write("\n".join(out_txt))


def compare_result(truth_outfile: str, test_outfile: str) -> None:
    """
    Compares the correct output file with a user generated one.
    Use for testing new algorithms
    truth_outfile str: The known correct answers
    test_outfile str: The user generated answer file
    returns: None
        Prints mis-matches lines to stdout
    """
    truth = open(truth_outfile, "r")
    test = open(test_outfile, "r")
    i = 0
    while True:
        truth_line = truth.readline().strip()
        test_line = test.readline().strip()
        if (not truth_line) or (not test_line):
            break
        if truth_line != test_line:
            print(f"Line {i}: {truth_line} != {test_line}")
        i += 1
    truth.close()
    test.close()


def main() -> None:
    """
    To use, replace the file names and insert code into `calculate_result()`
    """
    #########
    in_filename = "data/sample_test_set_1/sample_ts1_input.txt"
    truth_result_filename = "data/sample_test_set_1/sample_ts1_output.txt"
    out_filename = "sample_test_set_1.out"
    #########
    data = parse_input(in_filename)
    result = calculate_result(data)
    write_output(out_filename, result)
    compare_result(truth_result_filename, out_filename)


def example_calculate_result(data: list) -> list:
    """Simple function for testing"""
    return [1 for _ in data]


def calculate_result(data: list) -> list:
    """Add custom algorithm here"""
    result = example_calculate_result(data)
    return result


if __name__ == "__main__":
    main()
