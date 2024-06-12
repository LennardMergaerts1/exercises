# Write your code here
import re

def only_DNA(string):
    return re.fullmatch('[ACGT]*', string)