#!/usr/bin/python3

def parse_input(filename: str) -> 'list[list[int]]':
    """
    Reads input from file
    T: num of test cases to follow
    K: number of notes in the song
    A_!, A_2, ..., A_K: The pitch of each note

    TASK:

    An alien wants to convert songs onto a 4 key piano.
    Rules are:
      - The first note can be any note
      - Subsequent notes should be higher on the piano if they are higher,
        lower if lower, and can be the same if the pitch is just right
      - Notes do not have to be the same key if they are not successive

    What is the minimum number of times a rule is broken in translating the
    songs

    returns: The notes for each test case (list[list[int]])
    """
    with open(filename) as f:
        num_test_cases = int(f.readline())
        test_cases: 'list[list[int]]' = []
        for _ in range(num_test_cases):
            K = int(f.readline())
            A = [int(a) for a in f.readline().split()]
            test_cases.append(A)
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
    return [1 for  _ in data]


def calculate_result(data: list) -> list:
    """Add custom algorithm here"""
    result = example_calculate_result(data)
    return result


if __name__ == "__main__":
    main()

