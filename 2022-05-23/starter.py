#!/usr/bin/python3

def parse_input(filename: str) -> list:
    """
    Reads input from file for KickStart 2020 round B
    T: num of test cases to follow
    N lines:
        W, H, L, U, R, D: data tokens
    
    TASK: Find probability rover does not fall in the hole
    filename str: Name of input file
    returns: list[int]
    """
    with open(filename) as f:
        num_test_cases = int(f.readline())
        test_cases = []
        for _ in range(num_test_cases):
            test_cases.append([int(token) for token in f.readline().strip().split(" ")])
    return test_cases


def write_output(filename: str, values: list) -> None:
    """
    Writes the data to file in a generic format for Google Kickstarter
    filename str: Name of file to write output to
    values list[tuple(int, int)]: Final rover positions
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
        truth_line = truth.readline()
        test_line = test.readline()
        if (not truth_line) or (not test_line):
            break
        if truth_line != test_line:
            print(f"Line {i}: {truth_line.strip()} != {test_line.strip()}")
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
