# Xotira 16 MB Vaqt 1000 ms Qiyinchiligi 7 % 
# #Matematika #Dinamik dasturlash #Ochko'z algoritm
# 3.8
# (Baholar 52)
#  16 
# Muallif: ShoyimObloqulov
  
# Kitoblar
# Quvonchbek muhim vazifa yuklangan - u kutubxonadagi kitoblarni raqamlashi kerak, har bir kitob javonga o'z raqami bilan kitob qo'yishi kerak. n ta kitobning har biri 1 dan n gacha raqam olishi kerak va albatta, turli kitoblar har xil raqamlarni olishi kerak.

# Quvonchbek barcha kitob javondagi joylarni nomlashda qancha raqam yozishi kerakligini bilmoqchi.

# Kiruvchi ma'lumotlar:
# Birinchi qatorda butun son n
# (
# 1
# ≤
# n
# ≤
# 1
# 0
# 9
# )
# (1≤n≤10 
# 9
#  ) kiritiladi. n — kutubxonadagi kitoblar soni.

# Chiquvchi ma'lumotlar:
# Barcha kitoblarni raqamlash uchun kerakli raqamlar sonini chop eting.

# Misollar
# #	input.txt	output.txt
# 1	
# 13
# 17
# 2	
# 4
# 4
# Izoh:
# Birinchi test uchun tushuntirish. Kitoblar 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, jami 17 ta raqamdan iborat bo’ladi.

# Ikkinchi test uchun tushuntirish. Kitoblar soni 1, 2, 3, 4 bo‘ladi, bu esa 4 tagacha raqamlangan.

def count_total_digits(n):
    total_count = 0
    length = len(str(n))

    # Har bir raqamning xonalari sonini hisoblash
    for l in range(1, length):
        total_count += l * (10**l - 10**(l - 1))

    # Oxirgi raqamlar guruhi uchun
    total_count += length * (n - 10**(length - 1) + 1)
    
    return total_count

# Foydalanuvchidan musbat sonni kiritishni so'raymiz
number = int(input("Musbat sonni kiriting: "))

if number > 0:
    total_digit_count = count_total_digits(number)
    print(f"1 dan {number} gacha bo'lgan sonlarning xonalar soni: {total_digit_count}")
else:
    print("Iltimos, musbat son kiriting.")
