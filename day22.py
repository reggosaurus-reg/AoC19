print("A:")

# Techniques

def deal_into_new_stack(deck):
    return deck[::-1]

def deal_with_increment(deck, incr):
    stack = [0 for _ in range(DECK_SIZE)]
    for i in range(DECK_SIZE):
        stack[(incr * i) % DECK_SIZE] = deck[i]
    return stack

def cut(deck, index):
    return deck[index:] + deck[:index] # Verify

# Perform techniques

DECK_SIZE = 10007
deck = [i for i in range(DECK_SIZE)]
for row in open("input/day22.txt"):
    print(0)
    if row[:3] == "cut":
        deck = cut(deck, int(row[4:]))
    if row[:9] == "deal with":
        deck = deal_with_increment(deck, int(row[20:]))
    if row[:9] == "deal into":
        deck = deal_into_new_stack(deck)


print(deck.index(2019))

print("A:")
