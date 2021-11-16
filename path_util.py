import os
import re
import pathlib

def get_project_directory():
    SCRIPTPATH = os.path.realpath(__file__)
    # print("Script path: ", SCRIPTPATH)

    path = [""]
    i = 0
    backslash_count = SCRIPTPATH.count("\\")
    print(backslash_count)

    for char in SCRIPTPATH:
        if "\\" == char:
            i += 1
        # print(path)
        if i != backslash_count:
            path[0] += char

    # print(path)

    before = pathlib.PureWindowsPath(rf'{path}')
    after_path = before.as_posix().replace('[','').replace(']', '').replace("'",'')
    # .pop(']').pop('[')

    print(after_path)
    return after_path
