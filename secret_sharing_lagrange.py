import numpy as np
import random
from fractions import Fraction
from decimal import *
import time
from threading import Thread, Lock, Condition, Semaphore
from multiprocessing import Process
from concurrent.futures.thread import ThreadPoolExecutor


# Generate a large prime number greater than 255
# Generate a large prime number greater than 255
p = 2 ** 127 - 1
_PRIME = 2 ** 127 - 1
# Use the generated prime number as modulo
modulo = p

MAX_THREAD=16
thread_count = 0
thread_lock = Lock()
thread_cond = Condition(thread_lock)
thread_semaphore = Semaphore(value=MAX_THREAD)

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
    start_time = time.process_time()
    
    poly = [secret] + [_RINT(_PRIME - 1) for i in range(shares - 1)]
    points = [(i, _eval_at(poly, i, _PRIME))
              for i in range(1, shares + 1)]
    end_time = time.process_time()
    elapsed_time_ms = (end_time - start_time) * 1000
    return points, elapsed_time_ms, poly    

def _lagrange_interpolate_sequence(shared_points, focus_y):
    answer = 1
    sub_ans_list = []
    fl = False
    for i in range(len(shared_points)):
        if i == focus_y:
            continue
        numerator = (shared_points[i][0] % modulo)
        denum = (shared_points[i][0] - shared_points[focus_y][0]) % modulo
        sub_ans = (numerator * modInv(denum, modulo)) % modulo
        sub_ans_list.append(sub_ans)
        if fl == False:
            answer = (sub_ans % modulo)
            fl = True
        else:
            answer = ((answer % modulo) * (sub_ans % modulo)) %modulo
    
    answer = ((answer % modulo) * (shared_points[focus_y][1] % modulo))%modulo
    return answer
def _extended_gcd(a, b):
    """
    Division in integers modulus p means finding the inverse of the
    denominator modulo p and then multiplying the numerator by this
    inverse (Note: inverse of A is B such that A*B % p == 1). This can
    be computed via the extended Euclidean algorithm
    http://en.wikipedia.org/wiki/Modular_multiplicative_inverse#Computation
    """
    x = 0
    last_x = 1
    y = 1
    last_y = 0
    while b != 0:
        quot = a // b
        a, b = b, a % b
        x, last_x = last_x - quot * x, x
        y, last_y = last_y - quot * y, y
    return last_x, last_y

def _divmod(num, den, p):
    inv, _ = _extended_gcd(den, p)
    return num * inv
def _lagrange_interpolate_sequence(args):
    shared_points, focus_y, sum_list = args
    answer = 1
    sub_ans_list = []
    fl = False
    for i in range(len(shared_points)):
        if i == focus_y:
            continue
        numerator = (shared_points[i][0] % modulo)
        denum = (shared_points[i][0] - shared_points[focus_y][0]) % modulo
        sub_ans = (numerator * modInv(denum, modulo)) % modulo
        sub_ans_list.append(sub_ans)
        if fl == False:
            answer = (sub_ans % modulo)
            fl = True
        else:
            answer = ((answer % modulo) * (sub_ans % modulo)) %modulo
    
    answer = ((answer % modulo) * (shared_points[focus_y][1] % modulo))%modulo
    thread_lock.acquire()
    sum_list.append(answer)
    thread_lock.release()

    
def _lagrange_interpolate(shared_points, use_thread=False):
    global thread_count
    sum_list = []
    threads = [None] * len(shared_points)
    arg_list = []

    if use_thread:
        print("thread")
        for i in range(len(shared_points)):
            arg_list.append((shared_points, i, sum_list))
        with ThreadPoolExecutor() as executor:
            executor.map(_lagrange_interpolate_sequence, arg_list)
        
    else:
        for i in range(len(shared_points)):
            _lagrange_interpolate_sequence((shared_points, i, sum_list))

    return sum(sum_list)





def reveal_secret(keys, use_thread=False):
    start_time = time.time()
    ordered_keys = sorted(keys, key=lambda pair: pair[0])
    secret = _lagrange_interpolate(ordered_keys, use_thread=use_thread) % modulo
    end_time = time.time()
    elapsed_time_ms = (end_time - start_time) * 1000

    return secret,elapsed_time_ms