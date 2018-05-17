import re


def get_string(element):
    try:
        text = element.get_text()
    except AttributeError:
        return "N/A"
    else:
        if text == '':
            return extract_link_from_tag(element)
        else:
            return text


def extract_link_from_tag(element):
    try:
        find_link = re.search(r'''
            (https?:\/\/
            (www\.)?
            [-a-zA-Z0-9@:%._\+~#=]{2,256}
            \.[a-z]{2,6}
            \b([-a-zA-Z0-9@:%_\+.~#?&//=]*))''', str(element), re.VERBOSE)
        return find_link.group(1)
    except AttributeError:
        return "N/A"
