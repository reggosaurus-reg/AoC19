from math import ceil

print("A:")

reactions = {}
stored = {}
to_visit = []
for row in open("input/day14.txt"):
    use, get = row.split(" => ")
    use = use.split(", ")
    getNum, getChem = get.split()
    reqs = {}
    for req in use:
        reqNum, reqChem = req.split()
        reqs[reqChem] = int(reqNum)
        stored[reqChem] = 0
    reactions[getChem] = (int(getNum), reqs)

reactions["ORE"] = (1, {})
stored["FUEL"] = 0
ingredients = lambda root: reactions[root][1]
gives = lambda root: reactions[root][0]
uses = lambda root, ingr: ingredients(root)[ingr]

def run_dfs(root, needed):
    return dfs(root, needed, stored.copy())

def dfs(root, needed, stored):
    if root == "ORE":
        return needed

    # Reuse chemicals
    stored_to_use = min(needed, stored[root])
    needed = needed - stored_to_use
    stored[root] -= stored_to_use 

    if not needed:
        return 0

    # How many do we have to produce?
    unit_size = gives(root)
    produce = ceil(needed / unit_size)

    # Store overflowing chemicals
    overflow = (unit_size - (needed % unit_size)) % unit_size
    stored[root] += overflow

    cost = 0
    for ingr in ingredients(root):
        cost += dfs(ingr, produce * uses(root, ingr), stored) 

    return cost


print(run_dfs("FUEL", 1))

print("B:")

low = 1250000
high = 2500000
while high - low > 1:
    guess = (high + low) // 2
    res = run_dfs("FUEL", guess)
    if res < 1000000000000:
        low = guess
    else: 
        high = guess

print(guess)
