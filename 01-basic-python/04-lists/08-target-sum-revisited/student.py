# Write your code here
def target_sum(ns, target):
    for y in range(len(ns)):
        for z in range(y+1, len(ns)):
            if ns[y] + ns[z] == target:
                return True
    return False    