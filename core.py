import os


def get_percents(to_get):
    to_return = {}
    total_sum = 0
    for key in to_get:
        total_sum += to_get[key]
    for key in to_get:
        to_return[key] = float(str(((to_get[key] / total_sum) * 100))[0:4])
    return to_return


def get_all(ignore=None):
    if ignore is None:
        ignore = []
    all_directories = os.walk("..")
    all_files_list = []
    for directory in all_directories:
        ignore_item = False
        path_list = directory[0].split("\\")
        print(path_list)
        for item in ignore:
            if item in path_list:
                ignore_item = True
        if not ignore_item:
            for file in directory[2]:
                all_files_list.append(file)
    return all_files_list


def find_langs():
    langs = {}
    all_files = get_all(["venv", "node_modules", ".git"])
    for file in all_files:
        ending = file.split(".")
        ending = ending[len(ending) - 1]
        if ending in langs:
            langs[ending] += 1
        else:
            langs[ending] = 1
    return langs
