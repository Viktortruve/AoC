import more_itertools
from collections import defaultdict
def mix(number, secret):
    return number ^ secret

def prune(number):
    return number % 16777216

def procedure(secret):
    number = secret*64
    secret = mix(number, secret)
    secret = prune(secret)
    
    number = int(secret/32)
    secret = mix(number, secret)
    secret = prune(secret)

    number = secret*2048    
    secret = mix(number, secret)
    secret = prune(secret)

    return secret

secrets = [int(item.strip()) for item in open("day22.txt").readlines()]

s = defaultdict(list)
for secret in secrets:
    seen = defaultdict(int)
    dgts = [int(str(secret)[-1])]
    dlts = [0]
    for _ in range(2000):
        secret = procedure(secret)
        digit = int(str(secret)[-1])
        delta = digit - dgts[-1]
        dgts.append(digit)
        dlts.append(delta)
    sliding_window = list(more_itertools.windowed(dlts[1:], 4))
    for j in range(4, len(dgts)):
        if sliding_window[j-4] in seen:
            continue
        else:
            s[sliding_window[j-4]].append(dgts[j])
            seen[sliding_window[j-4]] += 1

s = sorted(s.values(), key = lambda x: sum(x))
print(sum(s[-1]))