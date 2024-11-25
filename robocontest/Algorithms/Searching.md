### **Linear Search, Binary Search, va Interpolation Search**

Qidirish algoritmlari — ma'lum bir elementni massiv yoki qator ichida topish uchun ishlatiladi. Har bir algoritmning o‘ziga xos ishlash prinsipi, samaradorligi va ishlatilishi mavjud. Quyida har bir algoritm haqida qisqacha tushuncha va kodni ko‘rib chiqamiz.

---

### **1. Linear Search (Qatorni birma-bir tekshirish)**

**Prinsip**: Har bir elementni tekshirib, kerakli qiymatni topish.

- **Asosiy xususiyatlar**:
    - **Tartibga solinmagan massivlarda ishlaydi**.
    - O‘zgartirish yoki indekslash talab qilinmaydi.
    - **Eng yomon holat**: Massivdagi barcha elementlarni tekshirishga to‘g‘ri keladi.
- **Vaqt murakkabligi**:
    - **Eng yaxshi holat**: O(1)O(1) (element birinchi o‘rinda bo‘lsa).
    - **Eng yomon holat**: O(n)O(n) (elementni oxiridan topish yoki massivda bo‘lmasligi).

#### **Kod**:

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Element topildi, indeksini qaytarish
    return -1  # Element topilmadi

# Misol:
arr = [5, 3, 7, 2, 8]
target = 7
result = linear_search(arr, target)
print("Linear Search: Element topildi indeks:", result)  # 2
```

---

### **2. Binary Search (Saralangan massivda tez qidirish)**

**Prinsip**: Saralangan massivni ikki qismga bo‘lib, **o‘rtacha elementni** tekshiradi. Agar topilmasa, kerakli qismni qayta tekshiradi. **Divide and Conquer** usuliga asoslangan.

- **Asosiy xususiyatlar**:
    - **Tartiblangan massivda ishlaydi** (massivni oldindan saralash talab etiladi).
    - **Tizimli va samarali** (har bir qadamda massivni yarmini istisno qiladi).
    - **Eng yaxshi holat**: O‘rtadagi element topilganda O(1)O(1).
- **Vaqt murakkabligi**:
    - **Eng yaxshi, o‘rtacha va eng yomon holat**: O(log⁡n)O(\log n).

#### **Kod**:

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Element topildi, indeksini qaytarish
        elif arr[mid] < target:
            low = mid + 1  # O'ng qismni tekshirish
        else:
            high = mid - 1  # Chap qismni tekshirish

    return -1  # Element topilmadi

# Misol:
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
result = binary_search(arr, target)
print("Binary Search: Element topildi indeks:", result)  # 3
```

---

### **3. Interpolation Search (O'zgaruvchilar yoki tartiblanmagan massivlar uchun)**

**Prinsip**: **Binary Search**ga o‘xshash, lekin bu algoritm **xususiyatlar**ga asoslanadi: elementlarning qiymati o‘rtacha o‘rinda emas, balki taqsimlanishiga qarab qidirishni optimallashtiradi. Ya'ni, agar siz qidirayotgan qiymat pastga yoki yuqoriga qarab joylashgan bo‘lsa, bu algoritm uni to‘g‘ri joyda qidirishga yordam beradi.

- **Asosiy xususiyatlar**:
    - **Tartiblangan massivda ishlaydi**.
    - Yaxshi taqsimlangan massivlarda samaraliroq.
    - **Yomon holat**: Massivdagi elementlar juda noaniq taqsimlangan bo‘lsa, algoritm samarali ishlamaydi.
- **Vaqt murakkabligi**:
    - **O‘rtacha holat**: O(log⁡log⁡n)O(\log \log n).
    - **Yomon holat**: O(n)O(n) (elementlar noto‘g‘ri taqsimlanganda).

#### **Kod**:

```python
def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1

        # Interpolation formulasi
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        # Agar topilsa, indeksini qaytarish
        if arr[pos] == target:
            return pos

        if arr[pos] < target:
            low = pos + 1  # O'ng qismni tekshirish
        else:
            high = pos - 1  # Chap qismni tekshirish

    return -1  # Element topilmadi

# Misol:
arr = [10, 12, 15, 18, 20, 25, 30]
target = 18
result = interpolation_search(arr, target)
print("Interpolation Search: Element topildi indeks:", result)  # 3
```

---

### **Taqqoslash**

|**Algoritm**|**Murakkablik**|**Tartiblangan Massivga Ehtiyoj**|**Afzalliklari**|**Kamchiliklari**|
|---|---|---|---|---|
|**Linear Search**|O(n)O(n)|Yo‘q|Oddiy, qo‘shimcha xotira talab qilmaydi|Katta massivlarda sekin ishlaydi|
|**Binary Search**|O(log⁡n)O(\log n)|Ha|Tez, samarali (katta massivlarda ishlaydi)|Faqat tartiblangan massivlar uchun ishlaydi|
|**Interpolation Search**|O(log⁡log⁡n)O(\log \log n)|Ha|Yaxshi taqsimlangan massivlar uchun tez|Yomon taqsimlangan massivlarda samarasiz|

---

### **Amaliy Masalalar uchun maslahatlar**:

1. **Linear Search**: Agar massiv kichik bo‘lsa yoki tartiblanmagan bo‘lsa, ishlatish oson va samarali.
2. **Binary Search**: Katta hajmdagi tartiblangan massivlar uchun eng yaxshi tanlov.
3. **Interpolation Search**: Yaxshi taqsimlangan massivlarda, masalan, qiymatlar teng yoki ko‘payib borayotgan holatlarda ishlash uchun yaxshi.

Agar masalalar bo‘yicha batafsil tushuncha kerak bo‘lsa yoki qo‘shimcha savollar bo‘lsa, yozing! 😊