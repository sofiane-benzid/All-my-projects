import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py <CSV file containing the STR counts for a list of individuals> <text file containing the DNA sequence>")
    # TODO: Read database file into a variable
    data = open(sys.argv[1], "r")
    reader1 = csv.reader(data)
    # TODO: Read DNA sequence file into a variable
    sequence = open(sys.argv[2], "r")
    reader2 = sequence.read()
    # TODO: Find longest match of each STR in DNA sequence\
    strs = next(reader1)[1:]
    strlist = []
    for i in range(len(strs)):
        strlist.append(longest_match(reader2, strs[i]))
    # TODO: Check database for matching profiles
    exists = False
    for row in reader1:
        str2 = row[1:]
        if [int(x) for x in str2] == strlist:
            print(row[0])
            exists = True
    if exists == False:
        print("No match")

    database.close()
    sequence.close()
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
