"""
File: population.py
Author: Rustambek Sobithanov
Purpose: The following function reads a file the contents of which are state names with their population size,
         prints them in the order of, "state - population", and in the end, prints the total number of states
         given and the total population size of those states.
"""


def main():
    file_name = input('file: ').strip()
    a_file = open(file_name, 'r')
    data = a_file.readlines()
    population = {}
    for info in data:
        if len(info) <= 1 or info.strip().split()[0] == '#':  # ignoring the blank lines and comments
            continue
        else:
            pop_list = []
            name = []
            detail = info.strip('\n').split()
            pop_list.append(int(detail[-1]))
            for i in range(len(detail) - 1):
                name.append(detail[i])
            state_name = ' '.join(name)
            population[state_name] = pop_list[0]
    total_population = 0
    for key, value in population.items():
        print(f'State/Territory: {key}')
        print(f'Population:      {value}')
        print()
        total_population += value
    print(f'# of States/Territories: {len(population)}')
    print(f'Total Population:        {total_population}')


main()
