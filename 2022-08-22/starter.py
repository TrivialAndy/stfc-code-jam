#!/usr/bin/python3

import sys

def print_output(output: str):
    """
    Output wrapper that also flushes the buffer. Output is read by the judge script.
    """
    print(output)
    sys.stdout.flush()

def main() -> None:
    """
    To run:
        $ python interactive_runner.py python local_testing_tool.py test_number -- python starter.py
        test_number is either 0 (Test Set 1), 1 (Test Set 2) or 2 (Test Set 3).
        See interactive_runner.py for more details.
    To customise:
      - change how you decide on the value of P
      - add compensation for the quantum fluctuations
    """
    T, B = [int(i) for i in input().split()] # T = number of test cases; B = length of array in all cases
    max_queries = 150
    for case_number in range(T):
        # set up array
        array = [0] * B
        # query judge for array values
        for q in range(max_queries):
            P = 1 # array index to query (1-indexed)
            print_output(P) # send query
            value = input() # response
            if value == "N":
                raise Exception(f"Malformed input for query {q}: P = {P}")
            array[P-1] = int(value)
        # send array to judge for judgement
        print_output("".join([str(x) for x in array]))
        correct = input()
        if correct == "N":
            break # judge will print the case number and wrong answer
        else:
            continue

if __name__ == "__main__":
    main()

