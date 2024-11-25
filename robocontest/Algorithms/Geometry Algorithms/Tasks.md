### **Geometriya Algoritmlari (Geometry Algorithms)**

Geometriya algoritmlari kompyuter fanlari va matematikada geometrik shakllar bilan ishlashda ishlatiladi. Ular masalan, **nuqtalar**, **chiziqlar**, **poligonlar**, **doiralar**, va **ko'pburchaklar** bilan ishlashni osonlashtiradi. Bu turdagi algoritmlar, masalan, **kompyuter grafikasida**, **geografik axborot tizimlarida (GIS)** va **robototexnikada** keng qo'llaniladi.

Quyida **geometriya algoritmlari**ning ba'zi asosiy turlari va ularning qanday ishlashi haqida batafsil tushuntirish keltirilgan.

---

### **1. Convex Hull (Konveks Qoplama)**

**Convex Hull** — bu nuqtalar to'plami bo'ylab chiziqlar chizish orqali maksimal chegarani aniqlash usulidir. Agar biz bir nechta nuqtani berilgan bo'lsa, **konveks qoplama** bu nuqtalar orasidagi eng kichik poligon bo'lib, barcha nuqtalar shu poligonning ichida bo'lishi kerak. Bu masala ko'plab **kompyuter grafikasida**, **robototexnikada** va **GIS**da qo'llaniladi.

**Graham Scan** va **Jarvis March** — bu **Convex Hull**ni topish uchun ishlatiladigan eng mashhur algoritmlar.

#### **Graham Scan Algoritmi**

**Graham Scan** algoritmi quyidagicha ishlaydi:

1. Avvalo, to'plamdagi eng past nuqta tanlanadi.
2. Keyin bu nuqtadan barcha boshqa nuqtalar burchak bo'yicha tartiblanadi.
3. Tartiblangan nuqtalardan foydalanib, konveks qoplama quriladi.

**Algoritm**ning murakkabligi: O(nlog⁡n)O(n \log n), bu yerda nn nuqtalar soni.

##### **Graham Scan Algoritmi kodni misoli**:

```python
import matplotlib.pyplot as plt

# Nuqtalarni va ularning x, y koordinatalarini kiritamiz
points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3), (1, 2)]

# Yordamchi funksiya: burchakni hisoblash
def orientation(p, q, r):
    return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

# Graham Scan algoritmi
def graham_scan(points):
    points = sorted(points, key=lambda p: (p[0], p[1]))  # Nuqtalarni x va y bo'yicha tartiblash
    hull = []

    for point in points:
        while len(hull) >= 2 and orientation(hull[-2], hull[-1], point) <= 0:
            hull.pop()  # Ortiqcha nuqtalarni olib tashlash
        hull.append(point)
    
    return hull

# Natijaviy konveks qoplamani hisoblash
convex_hull = graham_scan(points)

# Natijani vizualizatsiya qilish
x, y = zip(*points)
hx, hy = zip(*convex_hull)

plt.scatter(x, y)
plt.plot(hx + (hx[0],), hy + (hy[0],), 'r-')
plt.show()
```

#### **Jarvis March (Gift Wrapping) Algoritmi**

**Jarvis March** algoritmi konveks qoplama qurish uchun **"gift wrapping"** usulini ishlatadi. Algoritm quyidagicha ishlaydi:

1. Har bir nuqtani tekshirib chiqing va keyingi nuqtani tanlang, bunda ular orasidagi burchakni hisoblab, eng kichik burchakka ega bo'lgan nuqtani tanlash kerak.
2. Algoritm **O(n \times h)** vaqt murakkabligiga ega bo'ladi, bu yerda nn — nuqtalar soni va hh — konveks qoplamaning uzunligi.

##### **Jarvis March Algoritmi kodni misoli**:

```python
def jarvis_march(points):
    def orientation(p, q, r):
        return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

    n = len(points)
    if n < 3:
        return []

    leftmost = min(points, key=lambda p: p[0])
    hull = [leftmost]
    point = leftmost

    while True:
        next_point = points[0]
        for q in points[1:]:
            if q == point:
                continue
            o = orientation(point, next_point, q)
            if o < 0 or (o == 0 and distance(point, q) > distance(point, next_point)):
                next_point = q
        point = next_point
        if point == leftmost:
            break
        hull.append(point)

    return hull

# Natijaviy konveks qoplamani hisoblash
convex_hull_jarvis = jarvis_march(points)

# Natijani vizualizatsiya qilish
hx_jarvis, hy_jarvis = zip(*convex_hull_jarvis)
plt.scatter(x, y)
plt.plot(hx_jarvis + (hx_jarvis[0],), hy_jarvis + (hy_jarvis[0],), 'g-')
plt.show()
```

---

### **2. Line Intersection (Chiziqlar Kesishishi)**

**Chiziqlar kesishishi** masalasi ikkita chiziqning kesishish nuqtasini topishdan iborat. Agar chiziqlar parallel bo'lmasa, ular kesishadi, aks holda kesishmaydi. Har bir chiziq ikki nuqtadan iborat bo'ladi.

#### **Chiziqlar kesishishini aniqlash algoritmi (2D)**:

1. Chiziqlarni parametrik shaklda ifodalash.
2. Chiziqlarni tekshirish va ular kesishishining aniq nuqtasini topish.

##### **Chiziqlar kesishishining algoritmi (Python)**:

```python
def on_segment(p, q, r):
    return q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1])

def orientation(p, q, r):
    return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

def do_intersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and on_segment(p1, p2, q1): return True
    if o2 == 0 and on_segment(p1, q2, q1): return True
    if o3 == 0 and on_segment(p2, p1, q2): return True
    if o4 == 0 and on_segment(p2, q1, q2): return True

    return False

# Chiziqlar: (x1, y1) dan (x2, y2) gacha
p1 = (1, 1)
q1 = (10, 1)
p2 = (1, 2)
q2 = (10, 2)

print("Kesishadi!" if do_intersect(p1, q1, p2, q2) else "Kesishmaydi.")
```

**Vaqt murakkabligi**: O(1)O(1) — bir chiziqni tekshirish uchun.

---

### **3. Point in Polygon (Poligonda Nuqta)**

**Point in Polygon** masalasi, nuqtaning berilgan poligon ichida yoki tashqarisida ekanligini aniqlashdan iborat. Bu masala **Ray-Casting algoritmi** yoki **Winding Number** usullari orqali yechiladi.

#### **Ray-Casting algoritmi**:

1. Nuqtaga **gorizontal chiziq** chiziladi.
2. Chiziqni poligon qirralari bilan kesishgan joylari sanaladi.
3. Agar kesishlar soni **toq** bo'lsa, nuqta poligon ichida, aks holda tashqarida.

##### **Point in Polygon (Ray-Casting) Algoritmi**:

```python
def is_point_in_polygon(polygon, point):
```

```
x, y = point
n = len(polygon)
inside = False

p1x, p1y = polygon[0]
for i in range(n + 1):
    p2x, p2y = polygon[i % n]
    if y > min(p1y, p2y):
        if y <= max(p1y, p2y):
            if x <= max(p1x, p2x):
                if p1y != p2y:
                    xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                if p1x == p2x or x <= xinters:
                    inside = not inside
    p1x, p1y = p2x, p2y

return inside
```

polygon = [(1, 1), (1, 3), (3, 3), (3, 1)] point = (2, 2) print("Nuqta poligonda:", is_point_in_polygon(polygon, point))



---

### **Xulosa**

Geometriya algoritmlari ko'plab sohalarda foydali. **Konveks qoplama** yordamida to'plamdagi eng kichik poligonni topish mumkin, **chiziqlar kesishishi** va **nuqtalarni poligonda aniqlash** masalalari esa grafiklar va geografik tizimlarda juda keng qo'llaniladi.
