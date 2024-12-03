"""
Author : Veikoon
Day 03 of advent of code : https://adventofcode.com/2024/day/3
"""
import re

def load_input(path: str) -> list[str]:
    """Load input file from aoc line by line"""
    with open(path, "r", encoding="UTF-8") as f:
        return f.read()

def part_1(text: str) -> int:
    """Find all mul instructions and calculate them"""

    regex = r"mul\((\d+),(\d+)\)" # Regex : mul([any int],[any int])
    result = re.findall(regex, text)
    total_mul = sum(int(num1) * int(num2) for num1, num2 in result)
    print("The total of all mul instruction is : ", total_mul)

def part_2(text: str) -> int:
    """Find all mul instructions and calculate them"""

    # List of regex needed
    regex_mul = r"mul\((\d+),(\d+)\)" # Regex : mul([any int],[any int])
    regex_do = r"do\(\)" # Regex : do()
    regex_dont = r"don't\(\)" # Regex : don't()

    # Instructions are stored in tuple (index, instruction)
    tuples = []

    # Find all mul instruction followed with their index
    result = re.findall(regex_mul, text)
    result_index = [x.start() for x in re.finditer(regex_mul, text)]
    for i, numbers in zip(result_index, result):
        tuples.append((i, int(numbers[0]) * int(numbers[1])))

    # Find all do instruction followed by their index
    do_index = [x.start() for x in re.finditer(regex_do, text)]
    for do in do_index:
        tuples.append((do, "do"))

    # Find all dont instruction followed by their index
    dont_index = [x.start() for x in re.finditer(regex_dont, text)]
    for do in dont_index:
        tuples.append((do, "dont"))

    # Sort the list (by default sorted on the first index of the tuple)
    tuples.sort()

    # If instruction "do"/"dont" change the value of process
    # Else if process is True add the value of the mul instruction
    total_mul = 0
    process = True
    for instruction in tuples:
        if instruction[1] in ["do","dont"]:
            process = instruction[1] == "do"
        elif process:
            total_mul += instruction[1]
    print("The total of all processed mul instruction is : ", total_mul)


def main():
    """Main function"""

    # Load input file
    input_text = load_input("input.txt")
    part_1(input_text)
    part_2(input_text)

if __name__ == "__main__":
    main()
