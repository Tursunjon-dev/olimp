### Stek (Stack) va Navbat (Queue) haqida umumiy ma'lumot

**Stek (Stack)** va **Navbat (Queue)** - bu ma'lumotlar tuzilmalari bo'lib, ularni turli muammolarni yechishda ishlatish juda qulay. Ular asosan elementlarni qo'shish va o'chirish usullari bilan ajralib turadi.

---

### **Stek (Stack)**

Stek – bu **LIFO (Last In, First Out)** tamoyili asosida ishlaydi. Ya'ni, oxirgi qo'shilgan element birinchi bo'lib olinadi.

#### Stekning asosiy operatsiyalari:

1. **Push**: Stekka yangi element qo'shish.
2. **Pop**: Stekning oxiridan elementni olish.
3. **Peek (Top)**: Stekning yuqorisidagi elementni ko'rish.
4. **IsEmpty**: Stekning bo'shligini tekshirish.

#### Stek Python-da qanday ishlaydi:

Python-da stekni osonlikcha ro'yxatlar (`list`) yoki `collections.deque` yordamida amalga oshirish mumkin.

##### Misol (list yordamida):

```python
# Stekni yaratish
stack = []

# Push: Element qo'shish
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after pushes:", stack)  # [10, 20, 30]

# Pop: Oxirgi elementni olish
top_element = stack.pop()
print("Popped element:", top_element)  # 30
print("Stack after pop:", stack)  # [10, 20]

# Peek: Oxirgi elementni ko'rish
if stack:
    print("Top element:", stack[-1])  # 20
```

---

### **Navbat (Queue)**

Navbat – bu **FIFO (First In, First Out)** tamoyili asosida ishlaydi. Ya'ni, birinchi qo'shilgan element birinchi bo'lib olinadi.

#### Navbatning asosiy operatsiyalari:

1. **Enqueue**: Navbatning oxiriga yangi element qo'shish.
2. **Dequeue**: Navbatning boshidan elementni olib tashlash.
3. **Peek (Front)**: Navbatning boshidagi elementni ko'rish.
4. **IsEmpty**: Navbatning bo'shligini tekshirish.

#### Navbat Python-da qanday ishlaydi:

Python-da navbatni `collections.deque` yoki `queue.Queue` yordamida amalga oshirish mumkin.

##### Misol (deque yordamida):

```python
from collections import deque

# Navbatni yaratish
queue = deque()

# Enqueue: Element qo'shish
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue after enqueues:", list(queue))  # [10, 20, 30]

# Dequeue: Birinchi elementni olish
front_element = queue.popleft()
print("Dequeued element:", front_element)  # 10
print("Queue after dequeue:", list(queue))  # [20, 30]

# Peek: Birinchi elementni ko'rish
if queue:
    print("Front element:", queue[0])  # 20
```

---

