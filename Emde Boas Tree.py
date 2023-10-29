# implement the Van Emde Boas Tree data structure

class vEB:
    def __init__(self, u):
        self.u = u  # universe size
        self.min = None
        self.max = None
        if u != 2:
            self.summary = vEB(int(u**0.5))
            self.cluster = [vEB(int(u**0.5)) for _ in range(int(u**0.5))]

    def high(self, x):
        return int(x / (self.u**0.5))

    def low(self, x):
        return int(x % (self.u**0.5))

    def index(self, x, y):
        return int(x * (self.u**0.5) + y)

    def member(self, x):
        if x == self.min or x == self.max:
            return True
        elif self.u == 2:
            return False
        else:
            return self.cluster[self.high(x)].member(self.low(x))

    def insert(self, x):
        if self.min is None:
            self.min = self.max = x
        else:
            if x < self.min:
                x, self.min = self.min, x
            if self.u > 2:
                if self.cluster[self.high(x)].min is None:
                    self.summary.insert(self.high(x))
                    self.cluster[self.high(x)].min = self.cluster[self.high(x)].max = self.low(x)
                else:
                    self.cluster[self.high(x)].insert(self.low(x))
            if x > self.max:
                self.max = x

    def successor(self, x):
        if self.u == 2:
            if x == 0 and self.max == 1:
                return 1
            else:
                return None
        elif self.min is not None and x < self.min:
            return self.min
        else:
            max_low = self.cluster[self.high(x)].max
            if max_low is not None and self.low(x) < max_low:
                offset = self.cluster[self.high(x)].successor(self.low(x))
                return self.index(self.high(x), offset)
            else:
                succ_cluster = self.summary.successor(self.high(x))
                if succ_cluster is None:
                    return None
                else:
                    offset = self.cluster[succ_cluster].min
                    return self.index(succ_cluster, offset)




# tree = vEB(16)
# for i in [2, 3, 4, 5, 7, 14, 15]:
#     tree.insert(i)
# print(tree.successor(6))  # prints 7

tree = vEB(16)
for i in [2, 3, 4, 5, 7, 14, 15]:
    tree.insert(i)
assert tree.member(7)  # should be True
assert not tree.member(6)  # should be False
assert tree.successor(6) == 7  # should be True
