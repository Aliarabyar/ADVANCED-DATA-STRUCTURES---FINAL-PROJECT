# ADVANCED-DATA-STRUCTURES-FINAL-PROJECT
ADVANCED DATA STRUCTURES - FINAL PROJECT


This work investigates the essential properties, operations, and applications
of binary search trees (BSTs). This fundamental data structure provides efficient access
to elements, offering operations like insertion, deletion, and search in logarithmic time
complexity. The content is primarily based on the study of Chapter 12 of the fourth
edition of the book ”Introduction to Algorithms”. A series of exercises from the book
are solved and discussed in detail, providing a practical understanding of BSTs. The
problems cover various aspects such as insertion, deletion, and Querying binary search
trees. The project aims to enhance my understanding of the concept, providing a robust
foundation for further exploration of more complex tree structures.
Keywords: Binary Search Trees, Data Structures, Algorithms, Insertion, Deletion, Search,
Querying a binary search tree


1 INTRODUCTION

The Binary Search Tree (BST) is a pivotal data structure that provides support for a range of dynamic set operations including SEARCH, MINIMUM, MAXIMUM, PREDECESSOR, SUCCESSOR, INSERT, and DELETE. This functionality allows a BST to be utilized effectively as both a dictionary and a priority queue.

Fundamental operations on a BST are dependent on its height. In an ideal scenario, when the BST is a complete binary tree with $n$ nodes, the operations run in $O(\log n)$ worst-case time. However, if the tree degenerates into a linear chain, the same operations escalate to $O(n)$ worst-case time.

The structure of a BST, as the name indicates, is a binary tree. Each node in this structure holds a key, optional satellite data ${ }^1$, and pointers to its left and right child nodes. Some implementations also include a pointer to the parent node. If a node is missing a child or a parent, the corresponding attribute points to a NIL value.
