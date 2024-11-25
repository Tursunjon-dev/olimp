Python bo‘yicha **graf** bilan bog‘liq masalalarni samarali va qisqa shaklda tushuntirishga harakat qilaman. Quyida amaliy jihatdan kerakli narsalar va tez ishlash uchun foydali yondashuvlarni keltiraman.

---

### **Grafni ifodalashning eng yaxshi usullari**

1. **Qo‘shnichilik ro‘yxati**:
    
    - **Xotira jihatdan samarali** va ko‘p hollarda eng samarali ifodalash usuli.
    - Masalan:
        
        ```python
        graph = {
            1: [2, 3],
            2: [4],
            3: [4, 5],
            4: [],
            5: [1]
        }
        ```
        
2. **Qo‘shnichilik matritsasi**:
    
    - Agar graf **sichqon yo‘li grafiga (sparse)** ega bo‘lsa, xotira talab qiladi.
    - Masalan:
        
        ```python
        # 1, 2, 3, 4, 5 tugunlari uchun matritsa
        graph = [
            [0, 1, 1, 0, 0],  # 1
            [0, 0, 0, 1, 0],  # 2
            [0, 0, 0, 1, 1],  # 3
            [0, 0, 0, 0, 0],  # 4
            [1, 0, 0, 0, 0]   # 5
        ]
        ```
        
3. **Qirralar ro'yxati** (og‘irlikli graflar uchun qulay):
    
    ```python
    edges = [
        (1, 2, 5),  # 1 -> 2 og‘irligi 5
        (1, 3, 2),  # 1 -> 3 og‘irligi 2
        (2, 4, 1),  # 2 -> 4 og‘irligi 1
        (3, 4, 7),  # 3 -> 4 og‘irligi 7
        (3, 5, 3)   # 3 -> 5 og‘irligi 3
    ]
    ```
    

---

### **DFS va BFS (qidiruv algoritmlari)**

#### **DFS (Depth-First Search)**:

- Chuqurlik bo‘yicha qidirish.
- **Xotira:** O(V)O(V) (rekursiya steki uchun).
- **Kod:**
    
    ```python
    def dfs(graph, node, visited):
        if node not in visited:
            visited.add(node)
            print(node, end=" ")
            for neighbor in graph[node]:
                dfs(graph, neighbor, visited)
    
    # Amalda foydalanish
    graph = {1: [2, 3], 2: [4], 3: [4, 5], 4: [], 5: [1]}
    visited = set()
    dfs(graph, 1, visited)  # Output: 1 2 4 3 5
    ```
    

#### **BFS (Breadth-First Search)**:

- Kenglik bo‘yicha qidirish.
- **Xotira:** O(V)O(V) (navbat uchun).
- **Kod:**
    
    ```python
    from collections import deque
    
    def bfs(graph, start):
        visited = set()
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                print(node, end=" ")
                queue.extend(graph[node])
    
    # Amalda foydalanish
    graph = {1: [2, 3], 2: [4], 3: [4, 5], 4: [], 5: [1]}
    bfs(graph, 1)  # Output: 1 2 3 4 5
    ```
    

---

### **Yo‘l topish (Minimal masofa topish)**

#### **Dijkstra algoritmi**:

- **Og‘irlikli graf** uchun eng samarali algoritm.
- **Vaqt murakkabligi:** O((V+E)log⁡V)O((V + E) \log V) (`heapq` bilan).
- **Kod:**
    
    ```python
    import heapq
    
    def dijkstra(graph, start):
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        priority_queue = [(0, start)]  # (masofa, tugun)
    
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
    
            if current_distance > distances[current_node]:
                continue
    
            for neighbor, weight in graph[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
    
        return distances
    
    # Amalda foydalanish
    graph = {
        1: [(2, 5), (3, 2)],
        2: [(4, 1)],
        3: [(4, 7), (5, 3)],
        4: [],
        5: [(1, 8)]
    }
    print(dijkstra(graph, 1))  # Output: {1: 0, 2: 5, 3: 2, 4: 6, 5: 5}
    ```
    

#### **BFS bilan minimal yo‘l (og‘irliksiz graf):**

- **Kod:**
    
    ```python
    from collections import deque
    
    def bfs_shortest_path(graph, start, target):
        visited = set()
        queue = deque([(start, 0)])  # (tugun, masofa)
    
        while queue:
            node, distance = queue.popleft()
            if node == target:
                return distance
            if node not in visited:
                visited.add(node)
                for neighbor in graph[node]:
                    queue.append((neighbor, distance + 1))
        return -1
    
    # Amalda foydalanish
    graph = {1: [2, 3], 2: [4], 3: [4, 5], 4: [], 5: [1]}
    print(bfs_shortest_path(graph, 1, 4))  # Output: 2
    ```
    

---

### **Graf tahlili uchun maslahatlar**

1. **Qo‘shnichilik ro‘yxati**:
    
    - Agar graf **sichqon yo‘li grafiga (sparse)** ega bo‘lsa, foydalaning. Xotira jihatdan tejamkor.
2. **Qo‘shnichilik matritsasi**:
    
    - Agar graf **to‘liq graf (dense)** bo‘lsa, foydalaning. Yoki qirralar tezkor kirish-chiqishni talab qilsa.
3. **DFS**:
    
    - **Chuqurlikdagi barcha yo‘llarni tekshirishda** yoki tsikl borligini aniqlashda yaxshi.
    - Rekursiyadan foydalanilganda sodda kod yozish imkonini beradi.
4. **BFS**:
    
    - **Minimal masofani topish** yoki birinchi topilgan yechim yetarli bo‘lgan masalalar uchun afzal.
5. **Og‘irlikli graflar**:
    
    - **Dijkstra** yoki **Bellman-Ford** algoritmlarini ishlating.
6. **Minimal qirralar yig‘indisi daraxtini (MST)** topish:
    
    - **Kruskal** yoki **Prim** algoritmlaridan foydalaning.

---

### **Xulosa**

Agar graf bo‘yicha masalalarni samarali yechmoqchi bo‘lsangiz, quyidagi usullarga amal qiling:

- Grafni **qo‘shnichilik ro‘yxati**da ifodalang.
- Oddiy qidiruv masalalari uchun **DFS** va **BFS**.
- Minimal yo‘l uchun **Dijkstra** yoki BFS.
- **Har bir masala uchun kerakli vaqt va xotira jihatlarini** hisobga oling.

Batafsil misollar yoki kodni tushuntirish kerak bo‘lsa, yozing! 😊