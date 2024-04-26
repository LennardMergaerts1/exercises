# Write your code here
def is_prime(n):
    for y in range(2, n):
        if n % y == 0:
            return False
    return n > 1