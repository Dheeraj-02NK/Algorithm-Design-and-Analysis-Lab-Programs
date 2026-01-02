class Node234:
    def __init__(self):
        self.k = []          # keys
        self.c = []          # children

    def leaf(self): return len(self.c) == 0
    def full(self): return len(self.k) == 3


class Tree234:
    def __init__(self): 
        self.root = Node234()

    def split(self, p, i):
        n = p.c[i]
        mid = n.k[1]

        left = Node234();  left.k = [n.k[0]]
        right = Node234(); right.k = [n.k[2]]

        if not n.leaf():
            left.c = n.c[:2]
            right.c = n.c[2:]

        p.k.insert(i, mid)
        p.c[i] = left
        p.c.insert(i + 1, right)

    def insert(self, x):
        r = self.root
        if r.full():
            nr = Node234()
            nr.c.append(r)
            self.split(nr, 0)
            self.root = nr
        self._ins(self.root, x)

    def _ins(self, n, x):
        if n.leaf():
            n.k.append(x)
            n.k.sort()
            return
        i = 0
        while i < len(n.k) and x > n.k[i]:
            i += 1

        if n.c[i].full():
            self.split(n, i)
            if x > n.k[i]:
                i += 1

        self._ins(n.c[i], x)

    def search(self, x, n=None):
        if n is None:
            n = self.root

        i = 0
        while i < len(n.k) and x > n.k[i]:
            i += 1

        if i < len(n.k) and x == n.k[i]:
            return True
        if n.leaf():
            return False

        return self.search(x, n.c[i])

    # NEW: DISPLAY TREE (LEVEL ORDER)
    def display(self):
        queue = [self.root]
        level = 0

        print("\n--- 2-3-4 Tree Structure (Level Order) ---")
        while queue:
            next_level = []
            print(f"Level {level}:", end=" ")

            for node in queue:
                print(node.k, end="  ")
                for child in node.c:
                    next_level.append(child)

            print()
            queue = next_level
            level += 1


# ---------------------------
# MAIN PROGRAM
# ---------------------------
if __name__ == "__main__":
    # 1. USER INPUT ORDER
    nums = list(map(int, input("Enter numbers to insert: ").split()))

    t = Tree234()
    for v in nums:
        t.insert(v)

    print("\nInput Order:", nums)

    # 2. DISPLAY TREE
    t.display()

    # 3. SEARCH OPERATION
    key = int(input("\nEnter value to search: "))
    found = t.search(key)

    print("\nSearch Result:")
    print(f"{key} FOUND in tree" if found else f"{key} NOT FOUND in tree")