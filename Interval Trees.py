
# define the node structure of our Interval Tree
class Node:
    def __init__(self, interval, max_value):
        self.interval = interval  # Interval is a tuple (low, high)
        self.max_value = max_value
        self.left = None
        self.right = None


# create the IntervalTree class.
# It will have the root of the tree and methods for inserting intervals and searching for overlapping intervals.
class IntervalTree:
    def __init__(self):
        self.root = None

    def insert(self, interval):
        self.root = self._insert(self.root, interval)

    def _insert(self, node, interval):
        if node is None:
            return Node(interval, interval[1])

        if interval[0] < node.interval[0]:
            node.left = self._insert(node.left, interval)
        else:
            node.right = self._insert(node.right, interval)

        if node.max_value < interval[1]:
            node.max_value = interval[1]

        return node

    def search(self, point):
        return self._search(self.root, point)

    def _search(self, node, point):
        if node is None:
            return []

        if node.interval[0] <= point <= node.interval[1]:
            return [node.interval] + self._search(node.left, point) + self._search(node.right, point)

        if node.left and node.left.max_value >= point:
            return self._search(node.left, point)
        else:
            return self._search(node.right, point)




tree = IntervalTree()


# # Test Case 1:
# intervals = [(15, 20), (10, 30), (17, 19), (5, 20), (12, 15), (30, 40)]
#
# for i in intervals:
#     tree.insert(i)
#
# print(tree.search(14))




# # Test Case 2:
# intervals = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
#
# for i in intervals:
#     tree.insert(i)
#
# print(tree.search(5))




# # Test Case 3:
# intervals = [(1, 10), (20, 30), (40, 50), (60, 70), (80, 90)]
#
# for i in intervals:
#     tree.insert(i)
#
# print(tree.search(35))




# Test Case 4:
intervals = [(10, 20), (12, 25), (15, 30), (18, 35), (20, 40)]

for i in intervals:
    tree.insert(i)

print(tree.search(22))