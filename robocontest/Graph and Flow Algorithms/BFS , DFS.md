BFS (Breadth-First Search), DFS (Depth-First Search)
### DFS va BFS algoritmlarida Stek va Navbat

#### **DFS (Depth First Search)**:

DFS algoritmi chuqurlik bo'yicha qidirish uchun ishlatiladi va bunda **stek**dan foydalaniladi. Stek yordamida tugunlar ketma-ket ko'rib chiqiladi.

##### DFS Misol (rekursiya bilan stek analogiyasi):

```python
def dfs(graph, start, visited=set()):
    if start not in visited:
        print(start, end=" ")  # Hozirgi tugunni chop etish
        visited.add(start)
        for neighbor in graph[start]:
            dfs(graph, neighbor, visited)

# Grafni belgilash
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

print("DFS Traversal:")
dfs(graph, 'A')  # Output: A B D E C F
```

##### DFS Misol (iterativ, stek bilan):

```python
def dfs_iterative(graph, start):
    stack = [start]  # Stekni boshlash
    visited = set()

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            stack.extend(graph[node])  # Qo'shnilarni stekka qo'shish

# DFSni ishlatish
print("\nDFS Traversal (Iterative):")
dfs_iterative(graph, 'A')  # Output: A C F B E D
```

---

#### **BFS (Breadth First Search)**:

BFS algoritmi kenglik bo'yicha qidirish uchun ishlatiladi va bunda **navbat**dan foydalaniladi.

##### BFS Misol (navbat bilan):

```python
def bfs(graph, start):
    queue = deque([start])  # Navbatni boshlash
    visited = set()

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])  # Qo'shnilarni navbatga qo'shish

# BFSni ishlatish
print("\nBFS Traversal:")
bfs(graph, 'A')  # Output: A B C D E F
```

---

Quyidagi jadvalga **vaqt murakkabligi** va **eng yomon holatlar**ni qo'shgan holda DFS va BFSni taqqoslab ko'rsatamiz:
### Farqi:

|**Xususiyat**|**DFS**|**BFS**|
|---|---|---|
|**Yondashuv**|Chuqurlik bo'yicha qidiradi|Kenglik bo'yicha qidiradi|
|**Ma'lumot tuzilmasi**|Stek (yoki rekursiya)|Navbat|
|**Qo'llanilishi**|Xavfsizlik yo'lini topish, Murakkab graf analizlari|Minimal yo'lni topish|
|**Xotira ishlatish**|Kamroq|Ko'proq|
|**Vaqt murakkabligi**|O(V+E)O(V + E)|O(V+E)O(V + E)|
|**Xotira murakkabligi**|O(V)O(V) rekursiya uchun yoki stek uchun|O(V)O(V) navbat uchun|
|**Yo'l topish**|Minimal yo'lni kafolatlamaydi|Minimal yo'lni kafolatlaydi|
|**Eng yomon holat**|Graflar chuqur bo'lganda samarador|Graflar keng bo'lganda samarador|

Bu yerda:

- VV - graflarning tugunlar soni.
- EE - graflarning qirralar soni.

#### Qo'shimcha tushuntirish:

1. **Vaqt murakkabligi O(V+E)O(V + E):**
    
    - DFS va BFS ikkalasi ham barcha tugunlar va ularning qirralarini bir marta ko'rib chiqadi. Shu sababli, ular bir xil vaqt murakkabligiga ega.
2. **Xotira murakkabligi:**
    
    - DFS stek yoki rekursiya uchun O(V)O(V) xotiradan foydalanadi.
    - BFS navbat uchun O(V)O(V) xotiradan foydalanadi, ayniqsa graflar keng bo'lsa, bu ko'p joy talab qiladi.
3. **Minimal yo'lni topish:**
    
    - **BFS** kenglik bo'yicha qidirishi sababli, bir xil og'irlikdagi grafda (masalan, yo'l og'irliklari teng bo'lsa) minimal yo'lni kafolatlaydi.
    - **DFS** esa chuqurlik bo'yicha qidiradi, bu esa minimal yo'lni har doim kafolatlamaydi.

### DFS va BFSni tanlashda vaqt va xotira jihatlarini hisobga olish kerak:

- DFS graflar chuqur bo'lsa, lekin keng bo'lmasa samaraliroq.
- BFS esa graflar keng bo'lsa samarali, lekin bu xotira talabini oshiradi.