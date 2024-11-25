### **Bubble Sort, Selection Sort, Insertion Sort**

Bu uchta algoritm oddiy va tushunish oson bo‘lib, **kichik hajmli ma’lumotlarni** saralashda ishlatiladi. Har biri **O(n²)** vaqt murakkabligiga ega, ammo ba’zi hollarda boshqalariga qaraganda samaraliroq ishlaydi.

---

### **1. Bubble Sort**

**Prinsip**: Qo‘shni elementlarni taqqoslab, ularni tartibga keltirish.

- **Asosiy xususiyatlari**:
    - Eng katta (yoki eng kichik) elementni oxirga (yoki boshiga) “ko‘taradi”.
    - Har bir iteratsiyada **qism tartiblangan qismni** kengaytiradi.
- **Vaqt murakkabligi**:
    - Eng yaxshi holat: O(n)O(n) (Agar massiv allaqachon tartiblangan bo‘lsa).
    - Eng yomon va o‘rtacha holat: O(n2)O(n^2).

#### **Kod**:

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):  # Har bir iteratsiyada oxirgi element qaralmaydi
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Elementlarni joyini almashtirish
                swapped = True
        if not swapped:  # Agar iteratsiya davomida hech narsa almashtirilmagan bo‘lsa
            break

# Misol:
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Bubble Sort:", arr)  # [11, 12, 22, 25, 34, 64, 90]
```

---

### **2. Selection Sort**

**Prinsip**: Har bir iteratsiyada eng kichik (yoki eng katta) elementni tanlab, uni kerakli joyiga qo‘yadi.

- **Asosiy xususiyatlari**:
    - Har bir iteratsiyada **massivning tartiblangan qismini kengaytiradi**.
    - O‘z joyida ishlaydi va qo‘shimcha xotira talab qilmaydi.
- **Vaqt murakkabligi**:
    - Eng yaxshi, eng yomon va o‘rtacha holat: O(n2)O(n^2).

#### **Kod**:

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):  # Eng kichik elementni qidirish
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Joyini almashtirish

# Misol:
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Selection Sort:", arr)  # [11, 12, 22, 25, 64]
```

---

### **3. Insertion Sort**

**Prinsip**: Har bir elementni o‘zidan oldingi tartiblangan qismga kiritadi.

- **Asosiy xususiyatlari**:
    - **Qo‘shish va siljitish** amallariga asoslangan.
    - Kichik va qisman tartiblangan massivlar uchun samarali.
- **Vaqt murakkabligi**:
    - Eng yaxshi holat: O(n)O(n) (Agar massiv allaqachon tartiblangan bo‘lsa).
    - Eng yomon va o‘rtacha holat: O(n2)O(n^2).

#### **Kod**:

```python
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Tartiblangan qismni kengaytirish uchun elementlarni surish
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Misol:
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Insertion Sort:", arr)  # [5, 6, 11, 12, 13]
```

---

### **Taqqoslash**

|**Algoritm**|**Murakkablik**|**Afzalliklari**|**Kamchiliklari**|
|---|---|---|---|
|**Bubble Sort**|O(n2)O(n^2)|Oson tushuniladi, qisman tartiblangan massiv uchun qulay|Yomon samaradorlik katta massivlarda|
|**Selection Sort**|O(n2)O(n^2)|Minimal almashishlar, qo‘shimcha xotira talab qilmaydi|Ko‘proq qiyoslashlar, yirik massivlarda sust|
|**Insertion Sort**|O(n2)O(n^2), yaxshi: O(n)O(n)|Kichik yoki qisman tartiblangan massivlar uchun tezkor|Elementlarni ko‘chirish talab qiladi|

---

### **Amaliy masalalar uchun maslahatlar**

1. **Kichik hajmdagi massiv**lar uchun bu algoritmlar yaxshi, lekin katta hajmda **merge sort yoki quick sort**ni ko‘rib chiqing.
2. **Insertion Sort** qisman tartiblangan massivlarda yaxshi ishlaydi.
3. O‘zingiz yozgan kodlarni tezlikni sinash uchun vaqt o‘lchash moduli (`time`) bilan tekshirib ko‘ring.

Agar qaysidir algoritmni chuqurroq tushuntirish yoki yangi masalalar kerak bo‘lsa, yozing! 😊