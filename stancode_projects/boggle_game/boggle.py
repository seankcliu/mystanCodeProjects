"""
File: boggle.py
Name: Sean Liu
----------------------------------------
This program will simulate the word game Boggle
which will find the word combination on the 4x4 grid.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
    """
    This function will find all the words in sequences of adjacent letters from the 4x4 input.
    """
    start = time.time()
    ####################
    while True:
        letter1 = input('1 row of letters: ')
        if len(letter1) is not 7:
            print('Illegal input')
            break
        elif letter1[1] is not ' ' or letter1[3] is not ' ' or letter1[5] is not ' ':
            print('Illegal input')
            break
        else:
            letter2 = input('2 row of letters: ')
            if len(letter2) is not 7:
                print('Illegal input')
                break
            elif letter2[1] is not ' ' or letter2[3] is not ' ' or letter2[5] is not ' ':
                print('Illegal input')
                break
            else:
                letter3 = input('3 row of letters: ')
                if len(letter3) is not 7:
                    print('Illegal input')
                    break
                elif letter3[1] is not ' ' or letter3[3] is not ' ' or letter3[5] is not ' ':
                    print('Illegal input')
                    break
                else:
                    letter4 = input('4 row of letters: ')
                    if len(letter4) is not 7:
                        print('Illegal input')
                        break
                    elif letter4[1] is not ' ' or letter4[3] is not ' ' or letter4[5] is not ' ':
                        print('Illegal input')
                        break
        all_words = read_dictionary()
        find_word(letter1, letter2, letter3, letter4, all_words)
        break

    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_word(letter1: str, letter2: str, letter3: str, letter4: str, all_words: list) -> None:
    """
    This function leads to a helper function that can find all the words.
    """
    # All the letters are put into a string. The index is helpful for looking for adjacent letters.
    letter_input = letter1[0] + letter1[2] + letter1[4] + letter1[6] + letter2[0] + letter2[2] + letter2[4] + \
                   letter2[6] + letter3[0] + letter3[2] + letter3[4] + letter3[6] + letter4[0] + letter4[2] + \
                   letter4[4] + letter4[6]
    ans_lst = []
    find_word_helper(letter_input, all_words, '', ans_lst, [], [])
    print(f'There are {len(ans_lst)} words in total.')


def find_word_helper(letter_input: str, all_words: list, current_str: str, ans_lst: list, index: list, used: list) -> \
        None:
    # Base case
    if current_str in all_words and current_str not in ans_lst:
        ans_lst.append(current_str)
        print(f'Found "{current_str}"')

    # The indices are used to find neighboring letters in a 4x4 setting.
    if len(used) == 0:
        # For the first round, each letter can be beginning of a word.
        index.extend(range(0, 16))
    elif used[-1] == 0:
        index.extend([1, 4, 5])
    elif used[-1] == 3:
        index.extend([2, 6, 7])
    elif used[-1] == 12:
        index.extend([8, 9, 13])
    elif used[-1] == 15:
        index.extend([10, 11, 14])
    elif used[-1] == 1 or used[-1] == 2:
        index.extend([(used[-1] - 1), (used[-1] + 1), (used[-1] + 3), (used[-1] + 4), (used[-1] + 5)])
    elif used[-1] == 4 or used[-1] == 8:
        index.extend([(used[-1] - 4), (used[-1] - 3), (used[-1] + 1), (used[-1] + 4), (used[-1] + 5)])
    elif used[-1] == 7 or used[-1] == 11:
        index.extend([(used[-1] - 5), (used[-1] - 4), (used[-1] - 1), (used[-1] + 3), (used[-1] + 4)])
    elif used[-1] == 13 or used[-1] == 14:
        index.extend([(used[-1] - 5), (used[-1] - 4), (used[-1] - 3), (used[-1] - 1), (used[-1] + 1)])
    elif used[-1] == 5 or used[-1] == 6 or used[-1] == 9 or used[-1] == 10:
        index.extend([(used[-1] - 5), (used[-1] - 4), (used[-1] - 3), (used[-1] - 1), (used[-1] + 1), (used[-1] + 3),
                      (used[-1] + 4),
                      (used[-1] + 5)])

    # Recursive case
    for i in range(len(letter_input)):
        if i in index and i not in used:
            # Choose
            current_str += letter_input[i]
            used.append(i)

            # Explore
            if has_prefix(current_str, all_words):
                find_word_helper(letter_input, all_words, current_str, ans_lst, [], used)

            # Un-choose
            current_str = current_str[:-1]
            used.pop()


def read_dictionary() -> list:
    """
    This function stores all the words with length larger than 3 into a list.
    """
    all_words = []
    with open(FILE, 'r') as f:
        for line in f:
            line = line.strip()
            if len(line) > 3:
                all_words.append(line)
    return all_words


def has_prefix(sub_s: str, all_words: list) -> bool:
    """
    This function detect if any words in the dictionary has a prefix of the input string.
    """
    for word in all_words:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
