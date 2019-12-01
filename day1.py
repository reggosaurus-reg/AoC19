data = open("input/day1.txt")

print("A: ")

fuel = lambda module: module // 3 - 2
print(sum(fuel(int(row)) for row in data))

print("B: ")

def fuel_rec(module):
    total = fuel(module)
    return total + fuel_rec(total) if total > 0 else 0

data.seek(0)
print(sum(fuel_rec(int(row)) for row in data))
