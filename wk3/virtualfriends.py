nameToNum = dict()



class UFDS:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n
        self.sizes = [1] * n
        self.numdisjoint = n

    def find(self, x):
        xp = x
        children = []
        while xp != self.parents[xp]:
            children.append(xp)
            xp = self.parents[xp]
        for c in children:
            self.parents[c] = xp
        return xp

    def union(self, a, b):
        ap = self.find(a)
        bp = self.find(b)
        if ap == bp:
            return

        if self.ranks[ap] < self.ranks[bp]:
            self.parents[ap] = bp
            self.sizes[bp] += self.sizes[ap]
        elif self.ranks[bp] < self.ranks[ap]:
            self.parents[bp] = ap
            self.sizes[ap] += self.sizes[bp]
        else:
            self.parents[bp] = ap
            self.ranks[ap] += 1
            self.sizes[ap] += self.sizes[bp]

        self.numdisjoint -= 1

    def size(self, x):
        return self.sizes[self.find(x)]



numOfTestCases = int(input())

count = 0

for i in range(numOfTestCases):
    F = int(input())
    u = UFDS(F*2)

    for j in range(F):
        a, b = input().split(' ')
        if a not in nameToNum:
            nameToNum[a] = count
            count += 1
        if b not in nameToNum:
            nameToNum[b] = count
            count += 1
        a = nameToNum[a]
        b = nameToNum[b]
        u.union(a, b)
        print(u.size(a))