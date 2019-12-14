from math import ceil

print("A:")

reactions = {}
stored = {}
consumed = {} # testing
to_visit = []
#for row in open("input/day14.txt"):
for row in open("test14.txt"):
    use, get = row.split(" => ")
    use = use.split(", ")
    getNum, getChem = get.split()
    reqs = {}
    for req in use:
        reqNum, reqChem = req.split()
        reqs[reqChem] = int(reqNum)
        stored[reqChem] = 0
        consumed[reqChem] = 0 # testing
    reactions[getChem] = (int(getNum), reqs)

ingredients = lambda root: reactions[root][1]
gives = lambda root: reactions[root][0]
uses = lambda root, ingr: ingredients(root)[ingr]


def dfs(root, needed):
    """ Root: chem, needed: how many of this chem do we need? """
    if "ORE" in ingredients(root):
        consumed["ORE"] += needed * uses(root, "ORE")
        return needed * uses(root, "ORE")
    cost = 0
    for ingr in ingredients(root):
        need_ingr = needed * uses(root, ingr)
        #print(needed, root, "needs", need_ingr, "of", ingr)
        produce = ceil(need_ingr / gives(ingr))
        gets = produce * gives(ingr)
        if gets > need_ingr and need_ingr + stored[ingr] >= gets:
            use_stored = need_ingr % gives(ingr) 
            stored[ingr] -= use_stored
            need_ingr -= use_stored
            produce = ceil(need_ingr / gives(ingr))
            gets = produce * gives(ingr)
            #print("gets", gets, "stored", stored[ingr], "use", use_stored)
        extra = gets - need_ingr
        stored[ingr] += extra
        consumed[ingr] += gets 
        #if extra:
        #    print("Spill:", extra)
        cost += dfs(ingr, produce)
    return cost

print(dfs("FUEL", 1))
