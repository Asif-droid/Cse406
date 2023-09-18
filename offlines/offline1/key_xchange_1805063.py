
import random
p=226212990148262696675945831954250633899
g=2




def power(x, y, p) :
    res = 1     # Initialize result
 
    # Update x if it is more
    # than or equal to p
    x = x % p
     
    if (x == 0) :
        return 0
 
    while (y > 0) :
         
        # If y is odd, multiply
        # x with result
        if ((y & 1) == 1) :
            res = (res * x) % p
 
        # y must be even now
        y = y >> 1      # y = y/2
        x = (x * x) % p
         
    return res


def is_prime(n, k=40):
    if n <= 1:
        return False

    # Handle small primes
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    if n in small_primes:
        return True

    # Check divisibility by small primes
    for prime in small_primes:
        if n % prime == 0:
            return False

    # Perform Miller-Rabin primality test
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = power(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = power(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True



def get_prime():
    for i in range(0,100000):
        random.seed(i)
        random_number = random.getrandbits(128)
        if(is_prime(random_number)):
            rand2=(random_number-1)//2
            if(is_prime(rand2)):
                # print(i)
                # print(random_number)
                return random_number
            

def calculate_primitive_root(p,min,max):
    factors = [2,(p-1)//2]
    # for i in range(2, p):
    #     if (p - 1) % i == 0:
    #         factors.append(i)

    for g in range(min, max):
        found = True
        for factor in factors:
            temp = power(g, (p - 1) // factor, p)
            if temp == 1:
                found = False
                break
        if found:
            return g

    return None

def create_public_key(private_x,base,prime):
    public_x=power(base,private_x,prime)
    return public_x
def construct_shared_key(public_x,private_x,prime):
    shared_key=power(public_x,private_x,prime)
    return shared_key
    # cap_a=power(g,a,p)
    # cap_b=power(g,b,p)
    # print(cap_a)
    # print(cap_b)
    # sh_a=power(cap_b,a,p)
    # sh_b=power(cap_a,b,p)
    # if(sh_a==sh_b):
    #     print("yahooooooooooooooo")
    # print(sh_a)
    # print(sh_b)