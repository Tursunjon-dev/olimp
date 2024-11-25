### **Merge Sort, Quick Sort, Heap Sort**

Bu algoritmlar murakkab **saralash muammolarini** hal qilish uchun samarali bo‘lib, katta hajmdagi ma’lumotlar ustida ishlashga mo‘ljallangan. Ularning **murakkabligi O(nlog⁡n)O(n \log n)** bo‘lib, amaliyotda ko‘p ishlatiladi.

---

### **1. Merge Sort**

**Prinsip**: **Divide and Conquer** uslubiga asoslangan:

1. Massivni ikkiga ajratadi (rekursiv).
2. Har bir bo‘lakni saralaydi.
3. Ikki bo‘lakni birlashtirib saralangan massiv hosil qiladi.

- **Asosiy xususiyatlari**:
    - Tizimli, **barqaror (stable)**.
    - **Qo‘shimcha xotira** talab qiladi (O(n)O(n)).
- **Vaqt murakkabligi**:
    - Har doim: O(nlog⁡n)O(n \log n).

#### **Kod**:

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Rekursiv bo‘linish
        merge_sort(left)
        merge_sort(right)

        # Birlashtirish
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Qolgan elementlarni qo‘shish
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Misol:
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Merge Sort:", arr)  # [3, 9, 10, 27, 38, 43, 82]
```

---

### **2. Quick Sort**

**Prinsip**: **Divide and Conquer** uslubiga asoslangan:

1. Pivot (tayanch) elementni tanlaydi.
2. Massivni pivotdan kichik va katta qismlarga ajratadi.
3. Har bir qismni rekursiv saralaydi.

- **Asosiy xususiyatlari**:
    - **O‘z joyida ishlaydi (in-place)**.
    - Pivot tanlash usuliga bog‘liq.
- **Vaqt murakkabligi**:
    - O‘rtacha: O(nlog⁡n)O(n \log n).
    - Eng yomon: O(n2)O(n^2) (yomon pivot tanlashda).

#### **Kod**:

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Tayanch element
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Rekursiv qayta saralash
    return quick_sort(left) + middle + quick_sort(right)

# Misol:
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)
print("Quick Sort:", sorted_arr)  # [1, 5, 7, 8, 9, 10]
```

---

### **3. Heap Sort**

**Prinsip**: **Binary Heap**ga asoslangan:

1. Max-Heap yoki Min-Heapni quradi.
2. Eng katta (yoki eng kichik) elementni oxirga olib boradi.
3. Qolgan qismini qayta tartiblaydi.

- **Asosiy xususiyatlari**:
    - O‘z joyida ishlaydi (O(1)O(1) qo‘shimcha xotira).
    - Barqaror emas.
- **Vaqt murakkabligi**:
    - Har doim: O(nlog⁡n)O(n \log n).

#### **Kod**:

```python
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Chap va o‘ng bolalar bilan taqqoslash
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Agar eng katta o‘zgarib qolsa, joyini almashtirish
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Max-Heap qurish
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Elementlarni birma-bir chiqarish
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Eng kattani oxirga qo‘yish
        heapify(arr, i, 0)

# Misol:
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Heap Sort:", arr)  # [5, 6, 7, 11, 12, 13]
```

---

### **Taqqoslash**

|**Algoritm**|**Murakkablik (Vaqt)**|**Barqarorlik**|**Xotira talablar**|**Afzalliklari**|**Kamchiliklari**|
|---|---|---|---|---|---|
|**Merge Sort**|O(nlog⁡n)O(n \log n)|Ha|O(n)O(n)|Katta massivlarda barqaror|Qo‘shimcha xotira talab qiladi|
|**Quick Sort**|O(nlog⁡n)O(n \log n)|Yo‘q|O(log⁡n)O(\log n)|O‘z joyida ishlaydi, tez|Eng yomon holatda O(n2)O(n^2)|
|**Heap Sort**|O(nlog⁡n)O(n \log n)|Yo‘q|O(1)O(1)|O‘z joyida ishlaydi|Amaliyotda Quick Sort’dan sustroq|

---

### **Qaysi birini tanlash kerak?**

1. **Tezlik va kam xotira** uchun: `Quick Sort` (ammo yomon pivot tanlashdan ehtiyot bo‘ling).
2. **Barqarorlik kerak bo‘lsa**: `Merge Sort`.
3. **Qo‘shimcha xotira ishlatmaslik kerak bo‘lsa**: `Heap Sort`.

Amaliyot uchun har bir algoritmni yozib ko‘ring va murakkabligi katta bo‘lgan massivlarda ularning tezligini sinab ko‘ring. 😊