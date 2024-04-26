# Write your code here
def rotate(xs, n):
    new_list = xs[:n]
    del xs[:n]

    return xs + new_list


xs = [1,2,3,4,5]


print(rotate(xs, 2))