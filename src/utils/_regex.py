import re

def get_values_by_regex(contents, regex, is_all=False):
    # print(regex)
    matches = re.finditer(regex, contents, re.MULTILINE)
    groups = []
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
        group = match.group()
        groups.append(group)

        if not is_all:
            return groups

    groups = [group.replace('"', '') for group in groups] 
    
    return groups


def get_regex_by_type(key_name, regular_key):

    regex = None

    if isinstance(regular_key, str):
        regex = r"\"%s\":\"[\w\W][^,\{\}\]\[\(\)]*\"" %(key_name)

    elif isinstance(regular_key, int):
        regex = r"\"%s\":[\w\W][^,\{\}\]\[\(\)]*" %(key_name)
    elif isinstance(regular_key, dict):
        regex = r"\"%s\":\{.*?\}" %(key_name)
    elif isinstance(regular_key, list):
        regex = r"\"%s\":\[.*?\]" %(key_name)

    return regex

