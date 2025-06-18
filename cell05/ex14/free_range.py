#!/usr/bin/env python3
import sys

# ตรวจสอบว่ามีพารามิเตอร์ 2 ตัว
if len(sys.argv) != 3:
    print("none")
else:
    try:
        # แปลงพารามิเตอร์เป็นตัวเลข
        start = int(sys.argv[1])
        end = int(sys.argv[2])

        # สร้าง list ด้วย range โดยรวม end ด้วย
        result = list(range(start, end + 1)) if start <= end else list(range(start, end - 1, -1))

        # แสดงผลลัพธ์
        print(result)
    except ValueError:
        print("none")
