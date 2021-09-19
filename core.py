import os


def get_percents(to_get):
    to_return = {}
    total_sum = 0
    for key in to_get:
        total_sum += to_get[key]
    for key in to_get:
        to_return[key] = float(str(((to_get[key] / total_sum) * 100))[0:4])
    return to_return


def get_all():
    all_files = os.popen("cd ..&&tree /A /F")
    f = open("all.txt", "w")
    f.write(all_files.read())
    f.close()


def find_langs():
    langs = {"python": 0, "html": 0, "css": 0, "js": 0}
    f = (open("all.txt", "r").read()).split("\n")
    venv_ignore = False
    node_ignore = False
    for item in f:
        if not venv_ignore:
            try:
                x = item.split(".")[1]
            except IndexError:
                x = item
            if (x in langs.keys()) or (x == "py"):
                if x == "py":
                    langs["python"] += 1
                else:
                    langs[x] += 1
        if "venv" in item:
            venv_ignore = True
        if venv_ignore and ("|" in item):
            venv_ignore = False
        if "node_modules" in item:
            node_ignore = True
        if node_ignore and ("+---font" == item):
            node_ignore = False
    return langs
