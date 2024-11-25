### **Matematika Algoritmlari (Mathematics Algorithms)**

Matematika algoritmlari asosan raqamlar va matematik funksiyalar bilan ishlashda ishlatiladi. Bu algoritmlar nafaqat kompyuter fanlarida, balki kriptografiya, ma'lumotlarni siqish, va boshqa sohalarda ham keng qo'llaniladi. Quyida ba'zi asosiy matematika algoritmlarini va ularning qanday ishlashini ko'rib chiqamiz.

---

### **1. Sonsiz Sonlarni Modda Hisoblash (Modular Arithmetic)**

**Modular arifmetika** — bu sonlar bo'yicha hisoblash usuli bo'lib, sonlarni ma'lum bir modulga bo'lib, qolganini hisoblashni o'z ichiga oladi. Masalan, amod  ma \mod m bu aa sonining mm ga bo'lgandagi qoldig'idir. Modular arifmetika juda muhim, chunki u ko'plab kriptografik algoritmlar va ma'lumotlarni himoya qilish tizimlarida ishlatiladi.

**Asosiy operatsiyalar:**

- **Qo'shish moduli**: (a+b)mod  m(a + b) \mod m
- **Ayirish moduli**: (a−b)mod  m(a - b) \mod m
- **Ko'paytirish moduli**: (a×b)mod  m(a \times b) \mod m
- **Bo'lish moduli**: (a/b)mod  m(a / b) \mod m, agar bb ning moduli mm ga bo'linadigan bo'lsa.

#### **Modular arifmetika kodi misoli**:

```python
def modular_addition(a, b, m):
    return (a + b) % m

def modular_multiplication(a, b, m):
    return (a * b) % m

# Misol
a = 15
b = 10
m = 7
print("Qo'shish moduli:", modular_addition(a, b, m))  # (15 + 10) % 7 = 25 % 7 = 4
print("Ko'paytirish moduli:", modular_multiplication(a, b, m))  # (15 * 10) % 7 = 150 % 7 = 3
```

---

### **2. Greatest Common Divisor (GCD) va Least Common Multiple (LCM)**

- **GCD (Greatest Common Divisor)** — ikki yoki undan ortiq sonning **eng katta bo'luvchisi**.
- **LCM (Least Common Multiple)** — ikki yoki undan ortiq sonning **eng kichik ko'paytmasi**.

#### **GCDni topish algoritmi — Evklid algoritmi**:

Evklid algoritmi GCDni topishda juda samarali usuldir. Agar aa va bb sonlarining GCDsini topish kerak bo'lsa, Evklid algoritmi quyidagicha ishlaydi:

1. amod  ba \mod b ni hisoblang.
2. Agar qoldiq 00 bo'lsa, unda GCD — bb.
3. Agar qoldiq nol bo'lmasa, a=ba = b va b=amod  bb = a \mod b ga o'ting.

#### **Evklid algoritmi kodi misoli**:

```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Misol
a = 56
b = 98
print("GCD:", gcd(a, b))  # GCD(56, 98) = 14
```

#### **LCM (Least Common Multiple)**:

LCMni hisoblash uchun quyidagi formula ishlatiladi:

LCM(a,b)=∣a×b∣GCD(a,b)LCM(a, b) = \frac{|a \times b|}{GCD(a, b)}

#### **LCM kodi**:

```python
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Misol
a = 56
b = 98
print("LCM:", lcm(a, b))  # LCM(56, 98) = 392
```

---

### **3. Fast Exponentiation — Tez Quvvatlash (Modular Exponentiation)**

**Modular exponentiation** — bu katta sonlar bilan ishlashda juda samarali usul bo'lib, moduli bo'yicha quvvatlarni hisoblashni o'z ichiga oladi. Bu algoritmning asosiy maqsadi abmod  ma^b \mod m ifodasini hisoblashda **tezlikni oshirishdir**.

**Tez exponentiation** usuli (yoki **binary exponentiation**) quyidagicha ishlaydi:

1. aba^bni ab//2×ab//2a^{b // 2} \times a^{b // 2} shaklida qisqartirish.
2. Agar bb juft bo'lsa, ab//2mod  ma^{b // 2} \mod mni toping, agar toq bo'lsa, ab//2×amod  ma^{b // 2} \times a \mod mni hisoblang.

#### **Modular exponentiation kodi**:

```python
def modular_exponentiation(a, b, m):
    result = 1
    a = a % m  # Moddan kichiklashtirish
    while b > 0:
        if b % 2 == 1:  # Agar b toq bo'lsa
            result = (result * a) % m
        a = (a * a) % m  # Ayni kuchga ko'tarish
        b //= 2
    return result

# Misol
a = 3
b = 200
m = 13
print("Tez quvvatlash:", modular_exponentiation(a, b, m))  # 3^200 % 13
```

**Vaqt murakkabligi**: O(log⁡b)O(\log b), bu yerda bb — quvvat.

---

### **4. Prime Numbers va Sieve of Eratosthenes**

**Prime number** — bu faqat 11 va o'zi bo'luvchi sonlardan iborat bo'lgan son. Boshqacha aytganda, agar son pp bo'lsa, unda pp soni faqat 11 va ppga bo'linadi.

**Sieve of Eratosthenes** — bu sonlarning tubligini aniqlash uchun samarali algoritmdir. Bu algoritm orqali, berilgan oraliqdagi barcha tub sonlarni topish mumkin.

**Sieve of Eratosthenes algoritmi**:

1. 2 dan nn gacha bo'lgan barcha sonlar tub deb belgilansin.
2. Har bir tub sonni tekshirib, uning karralari bo'lgan sonlarni yo'q qiling.

#### **Sieve of Eratosthenes kodi**:

```python
def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n + 1) if primes[p]]
    return prime_numbers

# Misol
n = 50
print("Tub sonlar:", sieve_of_eratosthenes(n))  # 50 gacha bo'lgan tub sonlar
```

**Vaqt murakkabligi**: O(nlog⁡log⁡n)O(n \log \log n), bu yerda nn — maksimal son.

---

### **Xulosa**

Matematika algoritmlari turli masalalarni yechishda juda foydali:

- **Modular arifmetika** sonlarni modda bo'yicha hisoblashda ishlatiladi.
- **Evklid algoritmi** GCD ni topishda yordam beradi, va undan **LCM** ni hisoblash mumkin.
- **Tez quvvatlash (modular exponentiation)** katta sonlar bilan ishlashda samarali yechim taqdim etadi.
- **Sieve of Eratosthenes** algoritmi tub sonlarni tez aniqlashda ishlatiladi.

Ushbu algoritmlar turli xil masalalarni samarali yechishga yordam beradi va ko'plab sohalarda keng qo'llaniladi.