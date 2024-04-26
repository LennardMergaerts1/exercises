# Write your code here
def median(ns):
    sorted_list = sorted(ns)
    middle = len(sorted_list) // 2

    if len(sorted_list) // 2 == 0:
        