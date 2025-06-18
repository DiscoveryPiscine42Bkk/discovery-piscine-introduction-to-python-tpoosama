#!/usr/bin/env python3
import sys

# ตรวจสอบจำนวนพารามิเตอร์
if len(sys.argv) != 2:
    print("none")
    sys.exit()

input_str = sys.argv[1]

# นับจำนวนตัว 'z' ตัวเล็กเท่านั้น (ตามตัวอย่าง)
count_z = input_str.count('z')

if count_z == 0:
    print("none")
else:
    # แสดงตัว 'z' ซ้ำตามจำนวนที่เจอ
    print("z" * count_z)
