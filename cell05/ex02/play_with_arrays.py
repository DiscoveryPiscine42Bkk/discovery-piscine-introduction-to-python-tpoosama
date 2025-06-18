#!/usr/bin/env python3

# อาร์เรย์เดิม
original = [2, 8, 9, 48, 8, 22, -12, 2]

# อาร์เรย์ใหม่ (จะเก็บเฉพาะค่าที่มากกว่า 5 แล้วบวก 2)
new = []

# วนลูปใน original
for n in original:
    if n > 5:
        new.append(n + 2)

# แสดงผล
print(original)
print(new)
