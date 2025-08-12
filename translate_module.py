"""
Module for translating the module numbers.
"""

import re

regex = r'^(?:\d+|X)(?:\.(?:\d+|X)){0,4}'

def translate_x():
    """
    Function for translating the X's into real numbers in the text.
    """
    with open('Aux-file.txt', mode = 'r', errors = 'ignore',
        encoding = 'utf-8') as file_ptr:
        lines = file_ptr.readlines()

    all_versions = []
    max_lenght = 0
    for line in lines:
        match = re.search(regex, line)
        if match:
            aux_list = match.group().split('.')
            max_lenght = max(max_lenght, len(aux_list))
            all_versions.append(aux_list)
    
    for version in all_versions:
        while len(version) < max_lenght:
            version.append('0')

    i = 0
    for version in all_versions:
        indexes = [i for i, val in enumerate(version) if val == 'X']

        for index in indexes:
            if index == indexes[-1]:
                # print(f'Will do an addition on index {index}')
                version[index] = str(int(all_versions[i-1][index]) + 1)
            else:
                # print(f'Won\'t do an addition on index {index}')
                version[index] = all_versions[i-1][index]

        print(f'{version} {indexes}')

        i += 1


def main():
    """
    Main function.
    """
    translate_x()


if __name__ == '__main__':
    main()
