"""
Author : Veikoon
Day 01 of advent of code : https://adventofcode.com/2024/day/1
"""

def load_input(path: str) -> list[str]:
    """Load input file from aoc line by line"""
    with open(path, "r", encoding="UTF-8") as f:
        return f.read().splitlines()

def part_1(col_1: list[int], col_2: list[int]):
    """Part 1 : Find the total distance between all pair of sorted number"""
    total_distance = 0
    for num_1, num_2 in zip(col_1, col_2):
        total_distance += abs(num_1 - num_2)
    return total_distance

def part_2(col_1: list[int], col_2: list[int]):
    """Part 2 : Find the similarity score"""
    total_similarity = 0
    for num in col_1:
        total_similarity += col_2.count(num) * num
    return total_similarity

def main():
    """Main function"""

    # Load input file
    input_list = load_input("input.txt")

    # Load each collumns as a sorted list
    col_1 = sorted([int(line.split("   ")[0]) for line in input_list])
    col_2 = sorted([int(line.split("   ")[1]) for line in input_list])

    total_distance = part_1(col_1, col_2)
    print("The total distance is : ", total_distance)
    total_distance = part_2(col_1, col_2)
    print("The total similarity is : ", total_distance)

if __name__ == "__main__":
    main()
