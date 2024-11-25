### **Heaps (Uyumlar)**

**Heap** — bu maxsus ma'lumotlar tuzilmasi bo‘lib, **ikki asosiy turi** mavjud:

1. **Min-Heap**: Har bir tugun o‘z bolalaridan **kichikroq yoki teng** qiymatga ega.
2. **Max-Heap**: Har bir tugun o‘z bolalaridan **katta yoki teng** qiymatga ega.

Heaps **Priority Queue** (ustuvorlik navbati)ni amalga oshirish uchun keng qo‘llaniladi, chunki u **tezkor kirish va o‘zgartirish imkoniyatlarini** taqdim etadi.

---

### **Heapning asosiy hususiyatlari**

- **Vaqt murakkabligi**:
    - **Kiritish (Insert)**: O(log⁡N)O(\log N)
    - **Eng ustuvor elementni olish (Peek)**: O(1)O(1)
    - **Eng ustuvor elementni olib tashlash (Extract)**: O(log⁡N)O(\log N)
- **Tartibli bo‘lishi kerak**, lekin **to‘liq (binary tree)** tuzilmasida saqlanadi.
- **Amalda foydalanish** uchun Python’da `heapq` moduli ishlatiladi.

---

### **Min-Heap va Max-Heap** (Python misollar)

#### **Min-Heap**

Min-Heap elementlarni **eng kichik qiymatni ustun** qilib saqlaydi.

```python
import heapq

# Min-Heap yaratish
min_heap = []
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 8)
heapq.heappush(min_heap, 1)

print("Min-Heap:", min_heap)  # [1, 3, 8, 5]

# Eng kichik elementni olish (peek)
print("Min element:", min_heap[0])  # 1

# Eng kichik elementni olib tashlash
print("Extract Min:", heapq.heappop(min_heap))  # 1
print("Min-Heap after extraction:", min_heap)  # [3, 5, 8]
```

#### **Max-Heap**

Python’da `heapq` faqat **Min-Heap**ni ta'minlaydi, ammo **Max-Heap**ni yaratish uchun qiymatlarni **salbiy (-)** qilib saqlash mumkin.

```python
import heapq

# Max-Heap yaratish
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -8)
heapq.heappush(max_heap, -1)

# Salbiy qiymatlarni qaytarib o‘qib ko‘ramiz
print("Max-Heap:", [-x for x in max_heap])  # [8, 5, 3, 1]

# Eng katta elementni olish (peek)
print("Max element:", -max_heap[0])  # 8

# Eng katta elementni olib tashlash
print("Extract Max:", -heapq.heappop(max_heap))  # 8
print("Max-Heap after extraction:", [-x for x in max_heap])  # [5, 3, 1]
```

---

### **Priority Queue (Ustuvorlik navbati)**

Priority Queue navbatda elementlarni ularning **ustuvorligi** bo‘yicha boshqaradi. `heapq` moduli Priority Queue’ni amalga oshirish uchun juda mos.

```python
import heapq

# Priority Queue yaratish
priority_queue = []
heapq.heappush(priority_queue, (2, "Task 2"))  # (ustuvorlik, vazifa)
heapq.heappush(priority_queue, (1, "Task 1"))
heapq.heappush(priority_queue, (3, "Task 3"))

print("Priority Queue:", priority_queue)
# [(1, 'Task 1'), (2, 'Task 2'), (3, 'Task 3')]

# Eng yuqori ustuvorlikdagi vazifani olish
print("Next Task:", heapq.heappop(priority_queue))  # (1, 'Task 1')
```

---

### **Max-Heap bilan Priority Queue**

Max-Heap asosida Priority Queue uchun qiymatlarni **salbiy (-)** qilib saqlash mumkin.

```python
import heapq

# Max Priority Queue yaratish
max_priority_queue = []
heapq.heappush(max_priority_queue, (-2, "Task 2"))
heapq.heappush(max_priority_queue, (-1, "Task 1"))
heapq.heappush(max_priority_queue, (-3, "Task 3"))

print("Max Priority Queue:", [(-x[0], x[1]) for x in max_priority_queue])
# [(3, 'Task 3'), (1, 'Task 1'), (2, 'Task 2')]

# Eng yuqori ustuvorlikdagi vazifani olish
priority = heapq.heappop(max_priority_queue)
print("Next Task:", (-priority[0], priority[1]))  # (3, 'Task 3')
```

---

### **Heap amaliy ishlash uchun maslahatlar**

1. **Tezkor element kiritish va chiqarish** uchun `heapq`dan foydalaning. Bu **to‘liq uyum (complete binary tree)** sifatida ishlaydi.
2. **Max-Heap** kerak bo‘lsa, salbiy qiymatlar qo‘llang.
3. **Katta hajmli massivdan k-element topish** uchun `heapq.nlargest` va `heapq.nsmallest` qulay.

---

### **Amaliy masalalar va yechimlar**

#### **Masala 1: Eng kichik kk-ta elementni topish**

Berilgan massivdan eng kichik kk-ta elementni toping.

```python
import heapq

arr = [7, 10, 4, 3, 20, 15]
k = 3

# Top 3 eng kichik element
result = heapq.nsmallest(k, arr)
print("Eng kichik 3 ta element:", result)  # [3, 4, 7]
```

#### **Masala 2: Eng katta kk-ta elementni topish**

```python
# Top 3 eng katta element
result = heapq.nlargest(k, arr)
print("Eng katta 3 ta element:", result)  # [20, 15, 10]
```

#### **Masala 3: Har doim eng kichik elementni chiqaruvchi navbat**

```python
stream = [10, 5, 3, 8]
heap = []

for num in stream:
    heapq.heappush(heap, num)
    print("Eng kichik element:", heap[0])
```

#### **Masala 4: Sliding Window Median**

Massivdagi oyna hajmi kk uchun har bir oynaning median qiymatini toping (murakkab).

---

### **Xulosa**

- **Min-Heap va Max-Heap**:
    
    - Tezroq ishlash uchun massivni `heapq` bilan boshqaring.
    - Og'irlik yoki ustuvorlik asosida navbatni yaratishda juda qulay.
- **Priority Queue**:
    
    - Vazifalarni ustuvorlik bilan tartiblab boshqarish uchun ishlatiladi.

**Amaliyot uchun har bir qadamni kod orqali sinab ko‘ring va murakkab masalalar bilan ishlang!** 😊