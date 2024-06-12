import re

def parse_time(string):
    match = re.fullmatch("[\d{2}]:[\d{2}]:[\d{2}]:[\.\d{3}]?")

    if match:
        h, m, s, ms = match.groups('.000')
        ms = ms[1:]  # drop dot
        (int(h), int(m), int(s), int(ms))
    else:
        return None