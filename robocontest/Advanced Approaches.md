### **Kengaytirilgan Yondashuvlar (Advanced Approaches)**

Kengaytirilgan yondashuvlar ma'lumotlarni samarali ishlash va tezkor hisoblash uchun kuchli algoritmik vositalardir. Ular ko'pincha o'zgaruvchan yoki katta hajmdagi ma'lumotlar bilan ishlashda foydalidir. Quyida **Fenwick Tree (Binary Indexed Tree)**, **Segment Tree**, va **Union-Find** kabi kuchli ma'lumot tuzilmalarini ko'rib chiqamiz.

---

### **1. Fenwick Tree (Binary Indexed Tree) — Tezkor Prefix Summalarni Hisoblash**

**Fenwick Tree** (yoki **Binary Indexed Tree** yoki **BIT**) — bu qo'shish va prefix summalarini samarali hisoblash imkonini beruvchi ma'lumot tuzilmasidir. U asosan **prefix sum** masalalari uchun ishlatiladi, lekin boshqa masalalar uchun ham foydalanish mumkin.

#### **Fenwick Tree qanday ishlaydi?**

Fenwick Tree yordamida:

- **Prefix summalar**: Odatda prefix summalarni hisoblash O(n)O(n) vaqt oladi, lekin Fenwick Tree yordamida buni O(log⁡n)O(\log n) vaqt ichida amalga oshirish mumkin.
- **Yangilash (update)**: Biror elementni yangilashni O(log⁡n)O(\log n) da amalga oshirish mumkin.

**Fenwick Tree yaratish jarayoni**:

1. **Init (Boshlang'ich)**: Fenwick Tree boshlang'ichda barcha elementlarni 0 qilib tashkil etadi.
2. **Add**: Elementga qo'shish operatsiyasi amalga oshiriladi.
3. **Query**: Prefix sumni hisoblashni amalga oshiradi.

#### **Fenwick Tree kodi misoli**:

```python
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, index, delta):
        while index <= self.n:
            self.tree[index] += delta
            index += index & -index  # Fenwick Tree ni yangilash (low bitni qo'shish)

    def query(self, index):
        sum = 0
        while index > 0:
            sum += self.tree[index]
            index -= index & -index  # Prefix sumni hisoblash (low bitni kamaytirish)
        return sum

# Misol
n = 10
fenwick = FenwickTree(n)
fenwick.update(3, 5)
fenwick.update(5, 7)
print(fenwick.query(5))  # 5 + 7 = 12
print(fenwick.query(3))  # 5
```

**Vaqt murakkabligi**:

- **Update**: O(log⁡n)O(\log n)
- **Query**: O(log⁡n)O(\log n)

---

### **2. Segment Tree — Intervallarni Qo'shish yoki Eng Katta Elementni Topish**

**Segment Tree** — bu intervallarni saqlash va intervallar bilan bog'liq masalalarni tezkor yechish uchun ishlatiladigan tuzilma. Segment Tree odatda **qidirish** va **yangilash** operatsiyalarini samarali bajaradi.

#### **Segment Tree qanday ishlaydi?**

- **Segment Tree** intervallarni taqdim etadi va intervallarni birlashtiradi. Masalan, agar bizda **intervalni qo'shish** yoki **eng katta elementni topish** kerak bo'lsa, segment tree bu operatsiyalarni O(log⁡n)O(\log n) da bajaradi.
- **Query**: Intervaldagi minimum yoki maksimumni topish yoki intervalni qo'shish.
- **Update**: Ma'lum bir elementni yangilash.

#### **Segment Tree kodi misoli** (eng katta elementni topish):

```python
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)

        # Build the tree
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, index, value):
        index += self.n  # Treega ko'chirish
        self.tree[index] = value
        while index > 1:
            index //= 2
            self.tree[index] = max(self.tree[2 * index], self.tree[2 * index + 1])

    def query(self, left, right):
        left += self.n  # Treega ko'chirish
        right += self.n  # Treega ko'chirish
        result = float('-inf')
        while left <= right:
            if left % 2 == 1:
                result = max(result, self.tree[left])
                left += 1
            if right % 2 == 0:
                result = max(result, self.tree[right])
                right -= 1
            left //= 2
            right //= 2
        return result

# Misol
arr = [1, 3, 2, 7, 9, 11]
seg_tree = SegmentTree(arr)
print(seg_tree.query(1, 4))  # 7
seg_tree.update(2, 6)
print(seg_tree.query(1, 4))  # 7 (max(3, 6, 7, 9))
```

**Vaqt murakkabligi**:

- **Update**: O(log⁡n)O(\log n)
- **Query**: O(log⁡n)O(\log n)

---

### **3. Union-Find — Bog'lanishni Topish va Birlashtirish**

**Union-Find** (yoki **Disjoint Set Union (DSU)**) — bu ma'lumot tuzilmasi, ma'lumotlarni disjoint (bir-biridan alohida) to'plamlarga ajratish va ularga tegishli bog'lanishni aniqlashda ishlatiladi. Ko'pincha **kriminal tarmoqlar**, **komponentlarni topish** va **kriptografik masalalarda** qo'llaniladi.

#### **Union-Find qanday ishlaydi?**

- **Find**: Biror elementni qaysi to'plamga tegishli ekanligini aniqlash.
- **Union**: Ikki to'plamni birlashtirish.

**Path Compression** va **Union by Rank** kabi optimallashtirishlar orqali bu algoritmning samaradorligi yaxshilanadi.

#### **Union-Find kodi misoli**:

```python
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            # Union by rank
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

# Misol
uf = UnionFind(10)
uf.union(1, 2)
uf.union(2, 3)
print(uf.find(1))  # 3 (1 va 3 birlashtirilgan)
print(uf.find(2))  # 3
```

**Vaqt murakkabligi**:

- **Find**: Amalda O(α(n))O(\alpha(n)), bu yerda α(n)\alpha(n) — **invers Ackermann funktsiyasi**.
- **Union**: Amalda O(α(n))O(\alpha(n)).

---

### **4. Trie (Prefix Tree)**

**Trie** — bu ma'lumot tuzilmasi, asosan matnlarni (string) ishlashda, masalan, so'zlarni saqlash, qidirish yoki prefiks bo'yicha qidiruvni tezlashtirishda ishlatiladi. Trie, barcha so'zlarni o'z ichiga olgan daraxt tuzilmasini hosil qiladi.

- **Qidirish, qo'shish va o'chirish**: O(m)O(m), bu yerda mm so'z uzunligi.
- **Avtomatik tamg'alar (autocomplete)** va **prefiks bilan qidirish** kabi masalalarda foydalidir.

#### **Trie kodi misoli**:

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Misol
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))  # True
print(trie.search("app"))    # False
print(trie.starts_with("app"))  # True
```

---

### **5. Binary Search Tree (BST)**

**Binary Search Tree** (BST) — bu ma'lumotlar strukturasining boshqalaridan farqi shundaki, har bir tugun o'zidan kichik elementlar uchun chapda, kattaroq elementlar uchun esa o'ngda joylashadi. BST asosida tezkor **qidiruv**, **o'chirish** va **qo'shish** operatsiyalarini O(log⁡n)O(\log n) da bajarish mumkin, lekin eng yomon holatda (O(n)O(n)) bo'lishi mumkin.

- **Qidirish**, **Qo'shish**, **O'chirish**: O(log⁡n)O(\log n) eng yaxshi holatda.
- Agar daraxt unbalance bo'lsa, vaqt murakkabligi O(n)O(n) bo'lishi mumkin.

---

### **6. AVL Tree / Red-Black Tree**

**AVL Tree** va **Red-Black Tree** — balansiuz binar qidiruv daraxtlarining (BST) kengaytirilgan versiyalaridir. Ular **balansni saqlash** orqali tezkor qidiruv, qo'shish va o'chirish operatsiyalarini kafolatlaydi, bu esa daraxtning balansi yomon holatga kelishini oldini oladi.

- **AVL Tree**: Har bir tugunning chap va o'ng farqlari ≤1\leq 1 bo'lishi kerak.
    
- **Red-Black Tree**: Tugunlar uchun ranglarni (qizil va qora) qo'llaydi va har bir ranglar ketma-ketligini cheklaydi.
    
- **Qidirish**, **Qo'shish**, **O'chirish**: O(log⁡n)O(\log n) har doim.
    

---

### **7. B-Tree / B+ Tree**

**B-Tree** va **B+ Tree** — bu **balanslangan daraxtlar** bo'lib, ular diskda yoki boshqa tashqi xotira qurilmalarida katta ma'lumotlarni saqlash va tezkor qidirish uchun ishlatiladi. B+ Tree asosan bazalar va fayl tizimlarida qo'llaniladi.

- **Qidirish**, **Qo'shish**, **O'chirish**: O(log⁡n)O(\log n)

---

### **8. Kadane's Algorithm (Maximum Subarray Sum)**

**Kadane's Algorithm** — bu algoritm, berilgan massivda eng katta yig'indini hisoblash uchun ishlatiladi. Algoritm O(n)O(n) vaqtda ishlaydi va dinamik dasturlashning oddiy misolidir.

**Masala**:

- Berilgan massivda eng katta yopiq (subarray) yig'indini toping.

#### **Kadane's Algorithm kodi**:

```python
def max_subarray_sum(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Misol
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(nums))  # Output: 6 (subarray [4, -1, 2, 1])
```

---

### **9. Bitwise DP (Bitmasking) - Kengaytirilgan Yondashuvlar**

**Bitmasking** yordamida masalalarni samarali yechish uchun, masalan, dinamik dasturlashda (DP), juda ko'p holatlar va kombinatsiyalarni saqlash mumkin. **Bitmasking DP** — bu holatlar sonini kamaytirish uchun bitlarni saqlash va bitwise operatsiyalarini qo'llash usulidir.

Misol: **Travelling Salesman Problem (TSP)** — bu masala, barcha shaharlar orasidagi eng qisqa yo'lni topish uchun ishlatiladi va bitmasking yordamida yechiladi.

---

### **10. Knuth-Morris-Pratt (KMP) Algorithm**

**KMP algoritmi** — bu matndagi biror satrni izlashda samarali ishlovchi algoritmdir. KMP nafaqat qat'iy qidiruvni, balki **prefiks-suffix** munosabatlarini ham ishlatadi, bu esa uni an'anaviy qidiruv algoritmlaridan tezroq qiladi.

#### **KMP algoritmi kodi**:

```python
def KMPSearch(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = [0] * m
    j = 0

    # LPS (longest prefix suffix) jadvalini qurish
    def computeLPSArray():
        length = 0
        i = 1
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

    computeLPSArray()

    # Qidiruvni amalga oshirish
    i = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            print(f"Pattern found at index {i - j}")
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

# Misol
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
KMPSearch(text, pattern)
```

---

### **Xulosa**

Kengaytirilgan yondashuvlar va tuzilmalar ko'plab murakkab masalalarni samarali yechish uchun yordam beradi. Quyidagi tuzilmalar va algoritmlar:

- **Fenwick Tree**: Prefix summalar va yangilashlar uchun.
- **Segment Tree**: Interval masalalari, maksimum/minimum qidirish va qo'shish operatsiyalari.
- **Union-Find**: Birlashtirish va bog'lanishni aniqlash masalalari.
- **Trie**: Prefiks bo'yicha qidiruv va avtomatik tamg'alar (autocomplete).
- **AVL Tree / Red-Black Tree**: Balanslangan binar qidiruv daraxtlari.
- **Kadane's Algorithm**: Eng katta subarray yig'indisini topish.
- **Knuth-Morris-Pratt (KMP)**: Matnda satrni izlash.

Bularning barchasi dasturlash musobaqalarida va katta ma'lumotlar bilan ishlashda juda foydalidir.

- **Fenwick Tree** (Binary Indexed Tree) — prefix summalarini samarali hisoblash va yangilash uchun ishlatiladi, vaqti O(log⁡n)O(\log n).
- **Segment Tree** — intervallarni qo'shish, maksimumni topish yoki boshqa interval masalalarini yechishda ishlatiladi, vaqti O(log⁡n)O(\log n).
- **Union-Find** (Disjoint Set Union) — ma'lumotlarni birlashtirish va bog'lanishni aniqlashda samarali ishlaydi, vaqti O(α(n))O(\alpha(n)), bu juda tez.

Bu tuzilmalar juda samarali va katta ma'lumotlar bilan ishlashda optimallashtirilgan yondashuvlar taqdim etadi.