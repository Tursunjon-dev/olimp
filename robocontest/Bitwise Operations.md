### **Bitwise Operatsiyalar (Bitwise Operations)**

**Bitwise operatsiyalar** — bu raqamlar bilan bitlar (binary) darajasida ishlashni o'z ichiga oladi. Har bir bit uchun alohida hisoblashlarni amalga oshirish orqali tez va samarali algoritmlar yaratish mumkin. Bu operatsiyalar kompyuter arxitekturasida ko'plab optimallashtirishlarni taqdim etadi va ko'plab masalalarda qo'llaniladi, jumladan, kriptografiya, tasvirni qayta ishlash, va optimallashtirish masalalari.

#### **Bitwise operatsiyalar**

- **AND ( & )**: Har bir bitni tekshiradi, va faqat ikkala bit 1 bo'lsa, natija 1 bo'ladi.
- **OR ( | )**: Har bir bitni tekshiradi, va agar ikkala bitdan birortasi 1 bo'lsa, natija 1 bo'ladi.
- **XOR ( ^ )**: Har bir bitni tekshiradi, va agar bittalab bitlar farqli bo'lsa, natija 1 bo'ladi (ya'ni, 1 va 0).
- **NOT ( ~ )**: Boshqacha aytganda, bitni teskari qiladi, ya'ni 0 ni 1ga, 1 ni esa 0 ga aylantiradi.

---

### **1. AND ( & ) operatsiyasi**

AND operatsiyasi ikkita bitni taqqoslaydi. Agar ikkala bit ham 1 bo'lsa, natija 1 bo'ladi, aks holda 0 bo'ladi.

**Misol**:

```python
a = 5  # 0101 in binary
b = 3  # 0011 in binary
result = a & b  # 0001 in binary, which is 1
print(result)  # Output: 1
```

**Jadval**:

|a (binary)|b (binary)|a & b (binary)|a & b (decimal)|
|---|---|---|---|
|0101|0011|0001|1|
|1101|1011|1001|9|

---

### **2. OR ( | ) operatsiyasi**

OR operatsiyasi ikkala bitdan kamida bittasi 1 bo'lsa, natija 1 bo'ladi.

**Misol**:

```python
a = 5  # 0101 in binary
b = 3  # 0011 in binary
result = a | b  # 0111 in binary, which is 7
print(result)  # Output: 7
```

**Jadval**: | a (binary) | b (binary) | a | b (binary) | a | b (decimal) | |------------|------------|-------------|---------------| | 0101 | 0011 | 0111 | 7 | | 1101 | 1011 | 1111 | 15 |

---

### **3. XOR ( ^ ) operatsiyasi**

XOR operatsiyasi ikkala bit farqli bo'lsa, natija 1 bo'ladi, aks holda 0 bo'ladi.

**Misol**:

```python
a = 5  # 0101 in binary
b = 3  # 0011 in binary
result = a ^ b  # 0110 in binary, which is 6
print(result)  # Output: 6
```

**Jadval**:

|a (binary)|b (binary)|a ^ b (binary)|a ^ b (decimal)|
|---|---|---|---|
|0101|0011|0110|6|
|1101|1011|0110|6|

---

### **4. NOT (~) operatsiyasi**

NOT operatsiyasi bitni teskari qiladi. Bu, ya'ni 0 ni 1ga, 1 ni esa 0ga aylantiradi. Shuningdek, bu operatsiya o'zgaruvchining barcha bitlarini teskari qiladi (Pythonda bunday bitlar ikkilik qo'shimcha formatda saqlanadi).

**Misol**:

```python
a = 5  # 0101 in binary
result = ~a  # In Python, this will give -6
print(result)  # Output: -6
```

**Izoh**: Python'da bunday bitwise operatsiyasi ikkilik qo'shimcha tizimda ishlaydi, shuning uchun 5ning teskari qiymati -6 bo'ladi.

---

### **Bitwise DP (Bitmasking)**

**Bitmasking** — bu bitwise operatsiyalar yordamida ma'lumotlarni saqlash va manipulyatsiya qilish usulidir. Masalan, bitlar yordamida turli holatlarni yoki kombinatsiyalarni saqlash mumkin.

#### **Bitmasking asoslari**:

- **Set va unset**: Bitning ma'lum bir pozitsiyasini o'zgartirish uchun AND, OR va XOR operatsiyalaridan foydalaniladi.
- **Masking**: Faqat kerakli bitni ajratib olish uchun bitwise operatsiyalarni qo'llash.

#### **Bitmasking misol (Subsets)**

Faraz qilaylik, bizda n ta elementdan iborat bir to'plam bor va biz uning barcha bo'laklarini topmoqchimiz. Bu yerda bitmasking yordamida barcha kombinatsiyalarni topish mumkin.

**Masala**: {1, 2, 3} to'plamining barcha bo'laklarini topish.

**Bitmasking kodi**:

```python
def generate_subsets(nums):
    n = len(nums)
    subsets = []
    
    for mask in range(1 << n):  # 1 << n: 2^n
        subset = []
        for i in range(n):
            if mask & (1 << i):  # Agar i-bit 1 bo'lsa, uni qo'sh
                subset.append(nums[i])
        subsets.append(subset)
    
    return subsets

# Misol
nums = [1, 2, 3]
print(generate_subsets(nums))
```

**Izoh**:

- `mask` soni `1 << n` darajaga teng bo'ladi va har bir `mask` bir bo'lakni (subset) belgilaydi. Har bir bit o'zaro kombinatsiyalarning mavjudligini bildiradi.
- Misol: `{1, 2, 3}` to'plami uchun barcha bo'laklar:

```
[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
```

---

### **Xulosa**

Bitwise operatsiyalar raqamlar bilan ishlashda juda foydalidir. Ular tez va samarali algoritmlar yaratishga yordam beradi va ko'plab sohalarda ishlatiladi:

- **AND**, **OR**, **XOR**, va **NOT** operatsiyalarini qo'llab-quvvatlash orqali bitlar darajasida tezkor hisoblashlar amalga oshiriladi.
- **Bitmasking** yordamida masalalarni yanada samarali va ixcham yechish mumkin, ayniqsa dinamik dasturlashda, masalan, subset va kombinatsiyalarni hisoblashda.

Bitwise operatsiyalar va bitmasking, ayniqsa katta ma'lumotlar va optimallashtirish talab qiladigan masalalarda juda samarali bo'ladi.