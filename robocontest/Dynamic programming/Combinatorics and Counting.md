### **1. Nishonlash (Permutation) va Kombinatsiya (Combination)**

**Kombinatorika** — bu ob'ektlarning turli xil tartiblangan yoki tartiblanmagan guruhlarini hisoblash bilan shug'ullanadi. Nishonlash (permutation) va kombinatsiya (combination) bu sohaning asosiy tushunchalari.

#### **Nishonlash (Permutation)**

Nishonlash — bu ob'ektlarning tartiblangan to'plamidir. Masalan, nn ta elementdan rr tasini tartiblash.

- **Formulasi**: P(n,r)=n!(n−r)!P(n, r) = \frac{n!}{(n - r)!}
    - n!n! — n sonining faktoriali.
    - P(n,r)P(n, r) — n elementdan r tasini tartiblashning soni.

#### **Kombinatsiya (Combination)**

Kombinatsiya — bu ob'ektlarning tartibsiz to'plamidir. Masalan, nn ta elementdan rr tasini tanlash, tartibga ahamiyat bermay.

- **Formulasi**: C(n,r)=n!r!(n−r)!C(n, r) = \frac{n!}{r!(n - r)!}
    - C(n,r)C(n, r) — n elementdan r tasini tanlashning soni.

#### **Kod (Nishonlash va Kombinatsiya)**:

```python
import math

# Nishonlash (Permutation)
def permutation(n, r):
    return math.factorial(n) // math.factorial(n - r)

# Kombinatsiya (Combination)
def combination(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

# Misollar
n = 5
r = 3
print(f"Nishonlash P({n}, {r}) = {permutation(n, r)}")
print(f"Kombinatsiya C({n}, {r}) = {combination(n, r)}")
```

#### **Misol**:

- **Nishonlash**: 5 ta kitobdan 3 tasini qanday tartiblash mumkin? (P(5,3)P(5, 3))
    - Javob: P(5,3)=5!(5−3)!=1202=60P(5, 3) = \frac{5!}{(5 - 3)!} = \frac{120}{2} = 60.
- **Kombinatsiya**: 5 ta kitobdan 3 tasini qanday tanlash mumkin? (C(5,3)C(5, 3))
    - Javob: C(5,3)=5!3!(5−3)!=1206×2=10C(5, 3) = \frac{5!}{3!(5 - 3)!} = \frac{120}{6 \times 2} = 10.

---

### **2. Modular Arifmetika**

**Modular arifmetika** — bu sonlarni ma'lum bir modulga nisbatan hisoblash usulidir. Bu ko'plab dasturlash va matematik masalalarda (masalan, hashing, kriptografiya va algoritmlar) ishlatiladi.

- **Modulni hisoblash**: amod  ma \mod m — bu aa ning mm ga bo'lingan qoldig‘ini anglatadi.
- **Asosiy operatsiyalar**:
    - **Qo'shish**: (a+b)mod  m=((amod  m)+(bmod  m))mod  m(a + b) \mod m = ((a \mod m) + (b \mod m)) \mod m
    - **Ko'paytirish**: (a×b)mod  m=((amod  m)×(bmod  m))mod  m(a \times b) \mod m = ((a \mod m) \times (b \mod m)) \mod m
    - **Eksponentatsiya**: abmod  ma^b \mod m

#### **Modular eksponentatsiya** (tez hisoblash)

Modular eksponentatsiya algoritmi tez hisoblash uchun ishlatiladi, masalan, abmod  ma^b \mod m hisoblashda.

#### **Kod (Modular Arifmetika)**:

```python
# Modular qo'shish, ko'paytirish va eksponentatsiya

def mod_add(a, b, m):
    return (a + b) % m

def mod_multiply(a, b, m):
    return (a * b) % m

def mod_exponentiation(a, b, m):
    result = 1
    a = a % m
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        a = (a * a) % m
        b //= 2
    return result

# Misollar
a = 5
b = 3
m = 7

print(f"{a} + {b} mod {m} = {mod_add(a, b, m)}")
print(f"{a} * {b} mod {m} = {mod_multiply(a, b, m)}")
print(f"{a}^{b} mod {m} = {mod_exponentiation(a, b, m)}")
```

#### **Misol**:

- 5+3mod  7=15 + 3 \mod 7 = 1
- 5×3mod  7=15 \times 3 \mod 7 = 1
- 53mod  7=65^3 \mod 7 = 6

---

### **3. Backtracking — Qaytadan Tekshirish Usuli**

**Backtracking** — bu muammoni yechishda barcha imkoniyatlarni tekshirish va teskari (orqaga) qaytib, boshqa yo‘lni sinab ko‘rish usulidir. U ko‘plab kombinatorik masalalarda, masalan, **N-queens**, **subset sum**, **permutation** va **combination** kabi masalalarda ishlatiladi.

#### **Asosiy g‘oya**:

- Har bir qadamda imkoniyatlarni sinab ko‘rib, agar yechimga olib kelmasa, orqaga qaytish.
- **Branch and Bound** yoki **DFS** tarzida ishlaydi.

#### **Kod (Backtracking)**:

Masalan, **N-queens** muammosini yechishda backtrackingdan foydalanamiz.

```python
def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens(board, col, n):
    if col >= n:
        return True
    
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if solve_n_queens(board, col + 1, n):
                return True
            board[i][col] = 0  # Backtrack
    
    return False

def print_solution(board):
    for row in board:
        print(" ".join(["Q" if cell else "." for cell in row]))

# N-queens misoli
n = 4  # 4x4 taxta
board = [[0 for _ in range(n)] for _ in range(n)]

if solve_n_queens(board, 0, n):
    print_solution(board)
else:
    print("Ye solution mavjud emas!")
```

#### **Misol**:

- **N-queens muammosi**: n=4n = 4 bo‘lganda 4 ta malikani 4x4 taxtaga joylashtirish.
- Algoritm **backtracking** yordamida har bir malikani joylashtirishni tekshiradi va agar noaniqlik yuzaga kelsa, orqaga qaytadi.

---

### **Taqqoslash va Yechimlar**

|**Kechirish usuli**|**Vaqt murakkabligi**|**Afzalliklar**|**Kamchiliklar**|
|---|---|---|---|
|**Nishonlash**|O(n!)O(n!)|Elementlarni tartibda joylash|Katta n uchun juda sekin|
|**Kombinatsiya**|O(n!)O(n!)|Ob'ektlar tanlashda foydalidir|Katta n uchun tezlik muammolari|
|**Modular arifmetika**|O(log⁡b)O(\log b)|Tez hisoblash, katta sonlar bilan ishlash|Kichik xatolarni kuzatish kerak|
|**Backtracking**|O(bm)O(b^m)|Kombinatsion yechimlar bilan ishlash|Katta masalalar uchun sekinlashadi|

---

Bu usullar musobaqalarda yuqori samaradorlikni ta'minlash uchun foydalidir va ko'plab dasturlash masalalarida ishlatiladi.