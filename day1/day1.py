#!/usr/bin/env python3

def compute_frequency(numbers):
    """Return total frequency."""
    return sum(numbers)


def find_repeated(numbers):
    """Find the repeated one."""
    current = 0
    visited = {current}
    while True:
        for number in numbers:
            current += number
            if current in visited:
                return current
            visited.add(current)


def read_numbers():
    with open('day1.data', mode='rt') as data_file:
        numbers = [int(n) for n in data_file]
    return numbers


def main():
    numbers = read_numbers()
    print(compute_frequency(numbers))
    print(find_repeated(numbers))

if __name__ == '__main__':
    main()
