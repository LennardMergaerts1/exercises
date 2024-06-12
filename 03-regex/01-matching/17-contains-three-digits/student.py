
# Write your code here
import re

def only_three_digits(string):
    return re.fullmatch('.*[0-9].*[0-9].*[0-9].*', string)