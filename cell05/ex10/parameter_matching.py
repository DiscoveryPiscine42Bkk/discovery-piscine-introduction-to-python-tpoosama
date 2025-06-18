#!/usr/bin/env python3
import sys

# ตรวจสอบจำนวน argument ที่ส่งมา (ไม่นับ index 0 ที่เป็นชื่อไฟล์)
if len(sys.argv) != 2:
    print("none")
else:
    # รับ input จากผู้ใช้
    user_input = input("What was the parameter? ")
    
    # เปรียบเทียบกับ argument ที่ส่งเข้ามา
    if user_input == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")

