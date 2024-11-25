### **Dynamic Programming (DP)**

**Dynamic Programming (DP)** — bu **takrorlanadigan sub-masalalarni** yechish orqali **kengaytirilgan kombinatorka masalalarini** samarali yechish usulidir. DP yordamida masalalarni yechishda bir nechta sub-masalaning yechimlari saqlanib, qayta ishlatiladi, shu bilan vaqt murakkabligi sezilarli darajada kamayadi.

DP asosan quyidagi shartlarga ega bo'lgan masalalar uchun samarali ishlaydi:

- Masala takrorlanuvchi sub-masalalarga bo'linishi kerak.
- Sub-masalaning yechimi boshqa sub-masalaning yechimiga bog'liq bo'ladi (optimallik sharti).
- Sub-masalalarni bir marta yechib, ularning natijalarini saqlab qo‘yish kerak (bu **memoization** yoki **tabulation** yordamida amalga oshiriladi).

### **DP ning Asosiy Konseptsiyalari**

1. **Optimal substructure**: Masalaning umumiy yechimi sub-masalalarning optimal yechimlariga asoslanadi.
2. **Overlapping subproblems**: Masala ko'plab takrorlanuvchi sub-masalalarga bo'linadi, ya'ni bir xil sub-masalalarni bir necha bor yechishga to'g'ri keladi.

### **Asosiy metodlar**

- **Memoization (Top-down)**: Rekursiv usulda masala yechiladi va har bir sub-masala natijasi saqlanadi.
- **Tabulation (Bottom-up)**: Sub-masalalarni iteratsiya yordamida yechish, natijalar jadvalda saqlanadi.

---

### **Kengaytirilgan Kombinatorika Masalalari (DP orqali yechish)**

#### **1. Fibonacci Sonlari**

**Fibonacci sonlari** — bu masalada, har bir son oldingi ikki sondan iborat bo'ladi:

- F(0)=0F(0) = 0
- F(1)=1F(1) = 1
- F(n)=F(n−1)+F(n−2)F(n) = F(n-1) + F(n-2)

DP yordamida Fibonacci sonlarini hisoblashning ikki asosiy usuli mavjud:

- **Memoization** — rekursiv tarzda, takroriy hisoblashlardan qochish.
- **Tabulation** — iteratsiya orqali hisoblash.

##### **Tabulation (Bottom-up)**:

```python
def fibonacci(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# Misol:
n = 10
print(f"Fibonacci {n}-chi soni: {fibonacci(n)}")
```

##### **Memoization (Top-down)**:

```python
def fibonacci_memo(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

# Misol:
n = 10
print(f"Fibonacci {n}-chi soni (Memoization): {fibonacci_memo(n)}")
```

**Vaqt murakkabligi**:

- **Tabulation va Memoization**: O(n)O(n)

---

#### **2. Knapsack Problemi (0/1 Knapsack)**

**Knapsack** masalasi quyidagicha ta'riflanadi:

- Sizda ma'lum og'irlikdagi buyumlar bor va ular ma'lum qiymatga ega. Sizda **og'irlikni cheklovchi sumka** mavjud, uning maksimal og'irligi WW.
    
- Vazifa: maksimal qiymatni olish uchun qaysi buyumlarni tanlash kerak?
    
- **DP Yechimi**: Bu masala **0/1 knapsack** deb nomlanadi va DP yordamida yechiladi.
    

##### **DP Yechimi**:

```python
def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]

# Misol:
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
W = 5  # Sumka og'irligi
print(f"Maximal qiymat: {knapsack(weights, values, W)}")
```

**Vaqt murakkabligi**:

- **DP**: O(n×W)O(n \times W), bu yerda nn — buyumlar soni, WW — maksimal og'irlik.

---

#### **3. Longest Common Subsequence (LCS)**

**Longest Common Subsequence (LCS)** — bu ikki satrda eng uzun umumiy ketma-ketlikni topish masalasi.

- **DP Yechimi**: Har bir sub-masalani saqlash va qayta ishlatish orqali yechimni topish.

##### **DP Yechimi**:

```python
def lcs(X, Y):
    m = len(X)
    n = len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

# Misol:
X = "AGGTAB"
Y = "GXTXAYB"
print(f"Longest Common Subsequence uzunligi: {lcs(X, Y)}")
```

**Vaqt murakkabligi**:

- **DP**: O(m×n)O(m \times n), bu yerda mm va nn — ikki satr uzunligi.

---

#### **4. Coin Change Problemi**

**Coin Change** masalasi quyidagicha ta'riflanadi:

- Sizda **turli nominaldagi tangalar** mavjud va ma'lum bir qiymatni olish kerak.
- Vazifa: qaysi tangalardan foydalanib, berilgan qiymatni to'lash uchun minimal tangalar sonini toping.

##### **DP Yechimi**:

```python
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

# Misol:
coins = [1, 2, 5]
amount = 11
print(f"Minimal tangalar soni: {coin_change(coins, amount)}")
```

**Vaqt murakkabligi**:

- **DP**: O(n×m)O(n \times m), bu yerda nn — qiymat, mm — tangalar soni.

---

#### **5. Matrix Chain Multiplication**

**Matrix Chain Multiplication** masalasi, bir nechta matritsalarni birlashtirishda minimal ko‘paytirish operatsiyalarini hisoblashga yordam beradi. Bu masala uchun **DP** yordamida yechim topiladi.

##### **DP Yechimi**:

```python
def matrix_chain_order(dimensions):
    n = len(dimensions) - 1
    dp = [[0] * n for _ in range(n)]

    for chain_len in range(2, n + 1):  # chain_len - matritsa zanjirining uzunligi
        for i in range(n - chain_len + 1):
            j = i + chain_len - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                q = dp[i][k] + dp[k + 1][j] + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                dp[i][j] = min(dp[i][j], q)

    return dp[0][n - 1]

# Misol:
dimensions = [10, 20
```

, 30, 40, 30] print(f"Minimal ko'paytirish soni: {matrix_chain_order(dimensions)}")

```

**Vaqt murakkabligi**:
- **DP**: \( O(n^3) \), bu yerda \(n\) — matritsalar soni.

---

### **Xulosa**

**Dynamic Programming** kengaytirilgan kombinatorika masalalarini samarali yechish uchun muhim vosita hisoblanadi. DP yordamida:
- **Vaqt murakkabligi** sezilarli darajada kamayadi.
- Masalalar yanada tez va samarali yechiladi, ayniqsa katta kirish ma'lumotlari bilan ishlaganda.

**DP** nafaqat musobaqalarda, balki haqiqiy hayotdagi ko'plab masalalarni yechishda ham juda foydalidir.
```
### **6. Floyd-Warshall algoritmi (Grafdagi eng qisqa yo‘lni topish)**

**Floyd-Warshall algoritmi** — grafdagi barcha juftlar orasidagi eng qisqa yo‘llarni hisoblash uchun ishlatiladi.

- **Muammo**: Har bir juft nuqtalar orasidagi eng qisqa yo‘llarni topish.
- **Vaqt murakkabligi**: O(V3)O(V^3), bu yerda VV — grafdagi tugunlar soni.

#### **Kod**:

```python
def floyd_warshall(graph):
    V = len(graph)
    dist = [row[:] for row in graph]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# Misol:
graph = [
    [0, 3, float('inf'), float('inf')],
    [2, 0, float('inf'), 1],
    [float('inf'), 7, 0, 2],
    [6, float('inf'), 4, 0]
]
result = floyd_warshall(graph)
for row in result:
    print(row)
```

---

### **Taqqoslash va Yechimlar**:

|**Muammo**|**Vaqt murakkabligi**|**Afzalliklar**|**Kamchiliklar**|
|---|---|---|---|
|**Fibonacci sonlari**|O(n)O(n)|Oddiy va aniq, ko‘p ishlatiladi|Rekursiv usulda samarali emas|
|**Knapsack**|O(n×W)O(n \times W)|Maksimal foy||

da olish uchun samarali | Katta W uchun xotira talab qiladi | | **LCS** | O(n×m)O(n \times m) | Ikki satr o‘rtasidagi eng uzun umumiy ketma-ketlikni topish | Katta satrlar uchun sekin | | **Coin Change** | O(n×W)O(n \times W) | Minimal tangalar sonini topish | Katta qiymatlar bilan sekinlashadi | | **Matrix Chain Multiplication** | O(n3)O(n^3) | Matritsalar ko‘paytmasi uchun samarali | Ko‘p matritsalar bilan qiyin | | **Floyd-Warshall** | O(V3)O(V^3) | Grafdagi barcha juftlar orasidagi eng qisqa yo‘llar | Katta graflarda yomon ishlaydi |

Bu algoritmlar sizni musobaqalar va masalalar yechishda juda samarali qiladi!