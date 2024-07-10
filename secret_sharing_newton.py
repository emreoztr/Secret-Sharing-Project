import numpy as np
import random
from fractions import Fraction
from decimal import *
import time


# Generate a large prime number greater than 255
p = 257
_PRIME = 257
# Use the generated prime number as modulo
modulo = p


def extended_gcd(a, b):
    """
    Return (gcd, x, y) where gcd is the greatest common divisor of a and b,
    and x, y are integers satisfying ax + by = gcd.
    """
    if b == 0:
        return (a, 1, 0)
    else:
        gcd, x, y = extended_gcd(b, a % b)
        return (gcd, y, x - (a // b) * y)

def modInv(a, m):
    """
    Return the modular inverse of a modulo m, or None if it does not exist.
    """
    if a == -1:
        # special case for a = -1
        if m % 2 == 0:
            return None  # modular inverse does not exist
        else:
            return -1 % m
    else:
        gcd, x, y = extended_gcd(a, m)
        if gcd != 1:
            return None  # modular inverse does not exist
        else:
            return x % m

def modinv(A, M):
 
    for X in range(1, M):
        if (((A % M) * (X % M)) % M == 1):
            return X
    return -1
 

def _construct_secret_polynomial(secret, share_count):
    coefficients = [secret]
    for i in range(share_count - 1):
        coefficients.append(random.randint(1, modulo))
    return np.polynomial.Polynomial(coefficients)
def _eval_at(poly, x, prime):
    """Evaluates polynomial (coefficient tuple) at x, used to generate a
    shamir pool in make_random_shares below.
    """
    accum = 0
    for coeff in reversed(poly):
        accum *= x
        accum += coeff
        accum %= prime
    return accum
import functools
_RINT = functools.partial(random.SystemRandom().randint, 0)
def share_secret(secret, shares=2, prime=_PRIME):
    poly = [secret] + [_RINT(_PRIME - 1) for i in range(shares - 1)]
    points = [(i, _eval_at(poly, i, _PRIME))
              for i in range(1, shares + 1)]
    return points    

def _newton_interpolate_sequence(shared_points, focus_y):
    n = len(shared_points)
    divided_diffs = [shared_points[i][1] for i in range(n)]
    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            divided_diffs[j] = ((divided_diffs[j] - divided_diffs[j - 1]) * modInv(shared_points[j][0] - shared_points[j - i][0], modulo) % modulo)
    interpolation = divided_diffs[n - 1]
    for i in range(n - 2, -1, -1):
        interpolation = ((interpolation * (focus_y - shared_points[i][0])) % modulo + divided_diffs[i]) % modulo
    return interpolation


def _newton_interpolate(shared_points):
    sum_list = []
    
    for i in range(len(shared_points)):
        sum_list.append((_newton_interpolate_sequence(shared_points, shared_points[i][0]))%modulo)

    print(sum_list)
    return sum(sum_list)

def newton_interpolation(shared_points, z=0):
    n = len(shared_points)
    # create a nested list to store the divided differences
    div_diff = [[0 for i in range(n)] for j in range(n)]
    # initialize the first column with the y values
    for i in range(n):
        div_diff[i][0] = shared_points[i][1]
    # compute the divided differences
    for j in range(1, n):
        for i in range(n-j):
            div_diff[i][j] = (((div_diff[i+1][j-1] - div_diff[i][j-1])) * modinv(shared_points[i+j][0] - shared_points[i][0], modulo))%modulo
    # initialize the result with the last divided difference
    result = div_diff[0][n-1]
    # compute the polynomial at z using the nested multiplication formula
    for i in range(n-2, -1, -1):
        result = result * (z - shared_points[i][0]) + div_diff[0][i]
    return result


def reveal_secret(keys, use_thread):
    start_time = time.process_time()
    ordered_keys = sorted(keys, key=lambda pair: pair[0])
    secret = newton_interpolation(ordered_keys) % modulo
    end_time = time.process_time()
    elapsed_time_ms = (end_time - start_time) * 1000

    return secret,elapsed_time_ms