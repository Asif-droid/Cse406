import random
import time

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



# seed_value = 85
# random.seed(seed_value)
# random_number = random.getrandbits(128)

rands=list()
def get_prime():
    for i in range(0,100000):
    #   random.seed(i)
        random_number = random.getrandbits(256)
        if(is_prime(random_number)):
            rand2=(random_number-1)//2
            if(is_prime(rand2)):
            # print(i)
            # print(random_number)
            # rands.append(random_number)
                return random_number



# print(f'p =',end_time-start_time)
# print((random_number==252336560693540533935881068298825202077))
# print(is_prime(random_number))
# print(random_number)
# 12345678901234567890123456789012
# 246393973435219186612868762789119448499
# prime = 279072529952872317389370565228922158811
# 85
# 279072529952872317389370565228922158811
# 205
# 33529439325394706373427604837362954427
# 261
# 10304771739174187495473608432800635137
# 135218273965013541594514498836955660439


# 51114
# 135218273965013541594514498836955660439
# 55104
# 12139064909485241074212624282092151743
# 66439
# 226212990148262696675945831954250633899
# 69931
# 209517841256976602933834934439707632063

# the last 226212990148262696675945831954250633899 seed 66439




def calculate_primitive_root(p):
    factors = [2,(p-1)//2]
    # for i in range(2, p):
    #     if (p - 1) % i == 0:
    #         factors.append(i)

    for g in range(2, p):
        found = True
        for factor in factors:
            temp = power(g, (p - 1) // factor, p)
            if temp == 1:
                found = False
                break
        if found:
            return g

    return None

# Example usage
# prime_number = rands[0]
# start_time = time.time()
# primitive_root = calculate_primitive_root(prime_number)
# end_time = time.time()
# print(f'g =',end_time-start_time)
# if primitive_root:
#     print(f"The primitive root of {prime_number} is: {primitive_root}")
# else:
#     print(f"No primitive root found for {prime_number}.")

# g=2

# start_time = time.time()
# a=0
# b=0
# for i in range (300):
#   random.seed(i)
#   rnd_num = random.getrandbits(64)
#   if(is_prime(rnd_num)):
#     if(a==0):
#       a=rnd_num
#     else:
#       b=rnd_num
#       break

# end_time = time.time()
def sm_a():
    for i in range (300):
      
      rnd_num = random.getrandbits(128)
      if(is_prime(rnd_num)):
          return rnd_num



def create_public_key(private_x,primitive_root,prime_number):
    public_x=power(primitive_root,private_x,prime_number)
    return public_x


def construct_shared_key(public_x,private_x,prime_number):
    shared_key=power(public_x,private_x,prime_number)
    return shared_key


p_t=0
g_t=0
a_t=0
A_t=0
s_t=0
for i in range(3):
    p_s_t = time.time()
    p=get_prime()
    p_e_t = time.time()
    p_t+=p_e_t-p_s_t
    g_s_t = time.time()
    g=calculate_primitive_root(p)
    g_e_t = time.time()
    g_t+=g_e_t-g_s_t
    a_s_t = time.time()
    a=sm_a()
    a_e_t = time.time()
    a_t+=a_e_t-a_s_t
    b=sm_a()
    A_s_t = time.time()
    A=create_public_key(a,g,p)
    A_e_t = time.time()
    A_t+=A_e_t-A_s_t
    B=create_public_key(b,g,p)
    s_s_t = time.time()
    s=construct_shared_key(A,b,p)
    s_e_t = time.time() 
    s_t+=s_e_t-s_s_t
    s1=construct_shared_key(B,a,p)
    print(f'prime =',p)
    print(f'primitive_root =',g)
    print(f'private_key =',a)
    print(f'private_key =',b)
    print(f'public_key =',A)
    print(f'public_key =',B)
    print(f'shared_key1 =',s)
    print(f'shared_key2 =',s1)

print(f'p =',p_t/3)
print(f'g =',g_t/3)
print(f'a =',a_t/3)
print(f'A =',A_t/3)
print(f's =',s_t/3)
print("///////////////////////////////////end//////////////////////////////////////")
