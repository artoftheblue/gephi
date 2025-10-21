from itertools import chain, combinations

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

for i in [[1, 1, 1, 4, 2], # CURNY
          [1, 1, 1, 2, 2], # STAIG
          [1, 1, 1, 1, 2, 2]]: # DROIL
    bundle = 0
    pivotal = 0
    for p in powerset(i):
        if sum(p) > sum(i) * 0.3:
            bundle += 1
            pivotal += len(p)
    print(i, bundle, pivotal)