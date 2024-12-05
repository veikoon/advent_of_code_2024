"""
Author : Veikoon
Day 04 of advent of code : https://adventofcode.com/2024/day/4
"""
import re

def load_input(path: str) -> list[str]:
    """Load input file from aoc line by line"""
    with open(path, "r", encoding="UTF-8") as f:
        return f.read().splitlines()

def part_1(text: str) -> int:
    """Find all XMAS word"""

    word = r"XMAS"
    word_count = 0

    # Creating translated matrix of text input (read as collumn instead of lines)
    translated_text = [''.join(line) for line in zip(*text)]

    # Creating diagonal
    max_col = len(text[0])
    max_row = len(text)
    fdiag = [""] * (max_row + max_col - 1)
    bdiag = [""] * len(fdiag)
    min_bdiag = -max_row + 1

    for x in range(max_col):
        for y in range(max_row):
            fdiag[x+y] += text[y][x]
            bdiag[x-y-min_bdiag] += text[y][x]

    # Horizontal
    for line in text:
        word_count += len(re.findall(word, line)) + len(re.findall(word[::-1], line))

    # Vertical
    for line in translated_text:
        word_count += len(re.findall(word, line)) + len(re.findall(word[::-1], line))

    # First diagonal
    for line in fdiag:
        word_count += len(re.findall(word, line)) + len(re.findall(word[::-1], line))

    # Second diagonal
    for line in bdiag:
        word_count += len(re.findall(word, line)) + len(re.findall(word[::-1], line))

    print("Total of XMAS word : ", word_count)

def part_2(text: str) -> int:
    """Find all X format of MAS word"""

    word_count = 0
    for x in range(len(text) - 2):
        for y in range(len(text[0]) - 2) :

            corners = [text[x][y], text[x][y+2], text[x+2][y], text[x+2][y+2]]
            middle = text[x+1][y+1]

            if middle != "A" or\
                corners[0] == corners[3] or\
                corners[1] == corners[2] or\
                any(corner not in ["M","S"] for corner in corners) :
                continue
            word_count += 1
    print("Total of MAS in X : ", word_count)

def main():
    """Main function"""

    # Load input file
    input_text = load_input("input.txt")
    part_1(input_text)
    part_2(input_text)

if __name__ == "__main__":
    main()
