### **Hash-Set va Hash-Map (Dictionary)**

Python’da **Hash-Set** va **Hash-Map** — bu **hash funksiyalaridan** foydalanadigan ma'lumotlar tuzilmalari bo‘lib, ular **tezkor qidirish, qo‘shish va o‘chirish** amallarini amalga oshirish uchun ishlatiladi.

---

### **Hash-Set**

- Takrorlanmas elementlarni saqlash uchun ishlatiladi.
- **Vaqt murakkabligi**:
    - **Qo‘shish, qidirish va o‘chirish**: O(1)O(1) (o‘rtacha holda).
    - **Saqlash tartibi yo‘q**.
- **Misol**:
    
    ```python
    # Set yaratish
    my_set = {1, 2, 3}
    my_set.add(4)        # Qo‘shish
    print(my_set)        # {1, 2, 3, 4}
    
    # Qidirish
    print(2 in my_set)   # True
    print(5 in my_set)   # False
    
    # Elementni o‘chirish
    my_set.remove(3)     # Agar yo‘q bo‘lsa, xato beradi
    my_set.discard(5)    # Yo‘q bo‘lsa xato bermaydi
    print(my_set)        # {1, 2, 4}
    
    # Elementlar o‘rtasida operatsiyalar
    another_set = {3, 4, 5}
    print(my_set | another_set)  # Union: {1, 2, 3, 4, 5}
    print(my_set & another_set)  # Intersection: {4}
    print(my_set - another_set)  # Difference: {1, 2}
    ```
    

---

### **Hash-Map (Dictionary)**

Python’da **Dictionary**:

- Kalit-qiymat (key-value) juftlarini saqlash uchun ishlatiladi.
- **Vaqt murakkabligi**:
    - **Qo‘shish, qidirish va o‘chirish**: O(1)O(1) (o‘rtacha holda).
- **Kalitlar unikalligi (takrorlanmasligi)** ta’minlanadi.

#### **Asosiy operatsiyalar**

```python
# Dictionary yaratish
my_dict = {"a": 1, "b": 2, "c": 3}

# Element qo‘shish yoki o‘zgartirish
my_dict["d"] = 4  # Yangi juft
my_dict["a"] = 10 # Mavjud juftni o‘zgartirish
print(my_dict)    # {'a': 10, 'b': 2, 'c': 3, 'd': 4}

# Elementni qidirish
print(my_dict["b"])        # 2
print(my_dict.get("e", 0)) # 0 (kalit topilmasa, standart qiymat)

# Elementni o‘chirish
my_dict.pop("b")           # 'b' ni o‘chirish
print(my_dict)             # {'a': 10, 'c': 3, 'd': 4}

# Kalitlar va qiymatlar
print(my_dict.keys())      # dict_keys(['a', 'c', 'd'])
print(my_dict.values())    # dict_values([10, 3, 4])
print(my_dict.items())     # dict_items([('a', 10), ('c', 3), ('d', 4)])
```

---

### **Amaliy Masalalar**

#### **Masala 1: Takrorlanmas elementlarni topish**

Berilgan massivdagi barcha takrorlanmas elementlarni toping.

```python
nums = [1, 2, 2, 3, 4, 4, 5]
unique = set(nums)  # Hash-Set
print(unique)       # {1, 2, 3, 4, 5}
```

#### **Masala 2: Har bir elementning chiqish sonini hisoblash**

Massiv elementlarining chastotasini hisoblang.

```python
nums = [1, 2, 2, 3, 4, 4, 5]
freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1

print(freq)  # {1: 1, 2: 2, 3: 1, 4: 2, 5: 1}
```

#### **Masala 3: Har bir so‘zning chastotasini hisoblash**

Matndagi so‘zlarni qanchalik tez-tez uchrayotganini toping.

```python
text = "apple banana apple orange banana apple"
words = text.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)  # {'apple': 3, 'banana': 2, 'orange': 1}
```

#### **Masala 4: Hash-Set bilan bir xil elementlarni topish**

Ikki massivning umumiy elementlarini toping.

```python
arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]

common = set(arr1) & set(arr2)
print(common)  # {3, 4}
```

#### **Masala 5: Hash-Set bilan unikal qiymatlar sonini hisoblash**

Massivda nechta turli element borligini aniqlang.

```python
nums = [1, 2, 2, 3, 4, 4, 5]
unique_count = len(set(nums))
print(unique_count)  # 5
```

---

### **Hash-Set va Hash-Mapning afzalliklari**

1. **Tezkor amallar**:
    - Qidirish, qo‘shish va o‘chirish uchun O(1)O(1).
2. **Hash-Set**:
    - Takrorlanmas elementlarni boshqarish uchun ideal.
3. **Hash-Map**:
    - Kalit-qiymat juftliklarini saqlash uchun kuchli vosita.

---

### **Amaliy maslahatlar**

1. **Set**ni foydalaning:
    - Agar sizga **takrorlanmas elementlarni** saqlash yoki ularni tezda solishtirish kerak bo‘lsa.
    - Misol: Listni tozalash, umumiy elementlarni topish.
2. **Dictionary**dan foydalaning:
    - Agar sizga ma’lumotlarni kalit asosida boshqarish yoki indeksatsiya qilish kerak bo‘lsa.
    - Misol: So‘z chastotasini topish, konfiguratsiyalarni saqlash.
3. **Memory va tezlik** jihatidan Hash-Set va Hash-Map juda samarali.

**Qo‘shimcha masalalar kerak bo‘lsa, yozing! 😊**