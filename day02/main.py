"""
Author : Veikoon
Day 02 of advent of code : https://adventofcode.com/2024/day/2
"""

def load_input(path: str) -> list[str]:
    """Load input file from aoc line by line"""
    with open(path, "r", encoding="UTF-8") as f:
        return f.read().splitlines()

def is_increasing_or_decreasing(numbers: list[int]) -> bool:
    """Return True if either the list is sorted or sorted reversly"""
    return numbers == sorted(numbers) or numbers == sorted(numbers, reverse=True)

def is_adjacent_difference_safe(numbers: list[int]) -> bool:
    """Return True if adjacent difference is beetween 1 and 3"""

    for i,e in enumerate(numbers):
        if i == 0:
            continue
        difference = abs(numbers[i-1]-e)
        if not 1 <= difference <= 3:
            return False
    return True

def is_safe(numbers: list[int]) -> bool:
    """Return True if the list is safe"""
    return is_increasing_or_decreasing(numbers) and is_adjacent_difference_safe(numbers)

def part_1(input_list: list[int]):
    """Count the number of safe line"""
    total_safe = 0
    for line in input_list:
        if is_safe(line):
            total_safe += 1
    return total_safe

def part_2(input_list: list[int]):
    """Count the number of safe line with a one element tolerance"""
    total_safe = 0
    for line in input_list:
        for index in range(len(line)):
            line_copy = list(line)
            line_copy.pop(index)
            if is_safe(line_copy):
                total_safe += 1
                break
    return total_safe

def main():
    """Main function"""

    # Load input file
    input_list = load_input("input.txt")
    input_list = [[int(num) for num in line.split(" ")] for line in input_list]

    total_safe = part_1(input_list)
    print("The total of safe lines is: ", total_safe)
    total_safe_with_tolerance = part_2(input_list)
    print("The total of safe lines with one element tolerance is: ", total_safe_with_tolerance)


if __name__ == "__main__":
    main()
