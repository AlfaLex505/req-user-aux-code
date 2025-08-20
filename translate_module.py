"""
Module for translating the module numbers.
"""

import re

x_regex = r'^(?:\d+|X)(?:\.(?:\d+|X)){0,4}'
text_regex = r' ([A-Z].*)'


def translate_x(file_name):
    """
    Function for translating the X's into real numbers in the text.
    """
    with open(file_name, mode = 'r', errors = 'ignore',
        encoding = 'utf-8') as file_ptr:
        lines = file_ptr.readlines()

    all_versions = []
    max_lenght = 0
    for line in lines:
        match = re.search(x_regex, line)
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
                version[index] = str(int(all_versions[i-1][index]) + 1)
            else:
                version[index] = all_versions[i-1][index]
        i += 1

    return all_versions


def read_text(file_name):
    """
    Function for extracting the text part of the file.
    """
    with open(file_name, mode = 'r', errors = 'ignore',
        encoding = 'utf-8') as file_ptr:
        lines = file_ptr.readlines()

    text_list = []
    for line in lines:
        match = re.search(text_regex, line)
        if match:
            text_list.append(match.group())
    
    return text_list


def merge_lists(all_versions, text_list):
    """
    Function for merging both lists together.
    """
    if len(all_versions) != len(text_list):
        return print(f"List doesn't match their lenghts!\n" +
                     f"Version list lenght: {len(all_versions)}\n" +
                     f"Text list lenght: {len(text_list)}")
    
    for i in range(len(all_versions)):
        while '0' in all_versions[i]:
            all_versions[i].remove('0')
        str_version = '.'.join(all_versions[i])
        all_versions[i] = str_version
    
    for i in range(len(all_versions)):
        complete_str = all_versions[i] + text_list[i] + '\n'
        
        with open('req-funcionales-output.txt', mode = 'a+', errors = 'ignore',
        encoding = 'utf-8') as file_ptr:
            file_ptr.write(complete_str)


def main():
    """
    Main function.
    """
    file_name = 'req-funcionales.txt'
    all_versions = translate_x(file_name)
    text_list = read_text(file_name)
    merge_lists(all_versions, text_list)


if __name__ == '__main__':
    main()
