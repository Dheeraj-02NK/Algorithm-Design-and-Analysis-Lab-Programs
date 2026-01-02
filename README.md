# Design and Analysis of Algorithms – Lab Programs

This repository contains Python implementations of important algorithms from the **Design and Analysis of Algorithms (DAA)** course.  
Each program is implemented with a clear approach, proper design, and time complexity analysis.

---

## List of Programs

### 1. 2-3-4 Tree – Insertion and Search
**Objective:**  
To design and implement insertion and search operations in a 2-3-4 Tree.

**Description:**  
A 2-3-4 Tree is a self-balancing multiway search tree where each node can have 2, 3, or 4 children.  
The tree maintains balance by splitting nodes during insertion.

**Operations Implemented:**
- Insert a key
- Search for a key

**Time Complexity:**
- Insertion: O(log n)
- Search: O(log n)

**Space Complexity:**
- O(n)

---

### 2. Dijkstra’s Algorithm Using Binary Heap
**Objective:**  
To find the shortest path from a source vertex to all other vertices in a weighted graph using a Binary Heap.

**Description:**  
Dijkstra’s algorithm is a greedy algorithm that uses a priority queue (binary heap) to efficiently extract the vertex with the minimum distance.

**Constraints:**
- All edge weights must be non-negative.

**Time Complexity:**
- O((V + E) log V)

**Space Complexity:**
- O(V + E)

---

### 3. String Matching – Naive and Rabin–Karp Algorithms
**Objective:**  
To solve the string matching problem using the Naive approach and the Rabin–Karp algorithm and compare their complexities.

**Description:**  
The Naive algorithm compares the pattern with the text at every possible position.  
Rabin–Karp improves efficiency using hashing and a rolling hash technique.

**Time Complexity Comparison:**

| Algorithm | Best Case | Average Case | Worst Case |
|---------|----------|--------------|------------|
| Naive | O(n) | O(nm) | O(nm) |
| Rabin–Karp | O(n) | O(n + m) | O(nm) |

---

### 4. Matrix Chain Multiplication
**Objective:**  
To determine the minimum number of scalar multiplications required to multiply a chain of matrices.

**Description:**  
This problem is solved using Dynamic Programming by exploiting optimal substructure and overlapping subproblems.

**Time Complexity:**
- O(n³)

**Space Complexity:**
- O(n²)

---

### 5. RSA Public Key Cryptography – Decryption
**Objective:**  
To implement the RSA public key cryptosystem and decrypt a given ciphertext.

**Description:**  
RSA is an asymmetric cryptographic algorithm that uses a public key for encryption and a private key for decryption.

**Steps Implemented:**
- Key generation
- Encryption
- Decryption

**Time Complexity:**
- Modular exponentiation: O(log n)

---

## Technologies Used
- Programming Language: Python 3
- Libraries:
  - heapq (Binary Heap implementation)
  - math (RSA calculations)

---

## How to Run the Programs
1. Clone the repository
