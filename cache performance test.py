
# provide detailed information about how much time your program spends in each function
import cProfile
import random
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore")
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

# tree = vEB(16)
# for i in [2, 3, 4, 5, 7, 14, 15]:
#     tree.insert(i)
# assert tree.member(7)  # should be True
# assert not tree.member(6)  # should be False
# assert tree.successor(6) == 7  # should be True







# implement the binary search tree (BST)
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = BSTNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = BSTNode(key)
            else:
                self._insert(node.left, key)
        else:  # key >= node.key
            if node.right is None:
                node.right = BSTNode(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key) is not None

    def _search(self, node, key):
        if node is None:
            return None
        elif key == node.key:
            return node
        elif key < node.key:
            return self._search(node.left, key)
        else:  # key > node.key
            return self._search(node.right, key)

    def inorder_traversal(self):
        self._inorder_traversal(self.root)
        print()  # print a newline

    def _inorder_traversal(self, node):
        if node is not None:
            self._inorder_traversal(node.left)
            print(node.key, end=' ')
            self._inorder_traversal(node.right)







# start the test


def test_vEB_large():
    tree = vEB(2**16)  # Increase universe size
    for i in random.sample(range(2**16), 10000):  # Insert 10,000 random numbers
        tree.insert(i)
    print(tree.successor(60000))  # Find successor of a larger number

def test_BST_large():
    bst = BST()
    for i in random.sample(range(2**16), 10000):  # Insert 10,000 random numbers
        bst.insert(i)
    bst.inorder_traversal()  # This could print a lot of numbers!
    print("Found" if bst.search(60000) else "Not Found")  # Search for a larger number

cProfile.run('test_vEB_large()')
cProfile.run('test_BST_large()')




# Results:


#          114 function calls (77 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#       6/2    0.000    0.000    0.000    0.000 main.py:15(<listcomp>)
#         1    0.000    0.000    0.000    0.000 main.py:152(test_vEB)
#        44    0.000    0.000    0.000    0.000 main.py:17(high)
#        15    0.000    0.000    0.000    0.000 main.py:20(low)
#         2    0.000    0.000    0.000    0.000 main.py:23(index)
#      18/7    0.000    0.000    0.000    0.000 main.py:34(insert)
#       3/1    0.000    0.000    0.000    0.000 main.py:49(successor)
#      21/1    0.000    0.000    0.000    0.000 main.py:9(__init__)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# 20 30 40 50 60 70 80
# Found
#          70 function calls (38 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         7    0.000    0.000    0.000    0.000 main.py:102(insert)
#      21/6    0.000    0.000    0.000    0.000 main.py:108(_insert)
#         1    0.000    0.000    0.000    0.000 main.py:120(search)
#       4/1    0.000    0.000    0.000    0.000 main.py:123(_search)
#         1    0.000    0.000    0.000    0.000 main.py:133(inorder_traversal)
#      15/1    0.000    0.000    0.000    0.000 main.py:137(_inorder_traversal)
#         1    0.000    0.000    0.000    0.000 main.py:158(test_BST)
#         7    0.000    0.000    0.000    0.000 main.py:93(__init__)
#         1    0.000    0.000    0.000    0.000 main.py:99(__init__)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         9    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#
# Process finished with exit code 0






# Data for Van Emde Boas tree
veb_functions = ['<module>', '<listcomp>', 'test_vEB', 'high', 'low', 'index', 'insert', 'successor', '__init__']
veb_times = [0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000]

# Data for Binary Search Tree
bst_functions = ['<module>', 'insert', '_insert', 'search', '_search', 'inorder_traversal', '_inorder_traversal', 'test_BST', '__init__']
bst_times = [0.000, 0.000, 0.000, 0.000, 0.000, 0.002, 0.002, 0.002, 0.000]


# Convert times to microseconds
veb_times_microseconds = [time * 10**6 for time in veb_times]
bst_times_microseconds = [time * 10**6 for time in bst_times]



# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(veb_functions, veb_times_microseconds, label='Van Emde Boas Tree')
plt.bar(bst_functions, bst_times_microseconds, label='Binary Search Tree')
plt.xlabel('Function')
plt.ylabel('Total Time (microseconds)')
plt.title('Total Time Spent in Each Function')
plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()
plt.show()

