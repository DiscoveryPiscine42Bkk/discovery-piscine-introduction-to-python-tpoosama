#!/usr/bin/env python3
import sys

# ตรวจว่ามีพารามิเตอร์มากกว่า 0 หรือไม่
if len(sys.argv) > 1:
    print(sys.argv[1])
else:
    print("none")
