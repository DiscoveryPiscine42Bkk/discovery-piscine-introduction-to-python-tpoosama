#!/usr/bin/env python3

original = [2, 8, 9, 48, 8, 22, -12, 2]

new = []
for n in original:
    if n > 5:
        new.append(n + 2)

# แสดง original เป็น list ตามเดิม
print(original)

# แสดง new เป็น set เพื่อเอาค่าซ้ำออก
print(set(new))
