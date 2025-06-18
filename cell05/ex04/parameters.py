#!/usr/bin/env python3
import sys

# sys.argv มีรายการคำสั่งและพารามิเตอร์ทั้งหมดที่รับมา
# sys.argv[0] คือชื่อไฟล์โปรแกรมเอง
# ดังนั้นจำนวนพารามิเตอร์จริงๆ คือ len(sys.argv) - 1

num_params = len(sys.argv) - 1

print(f"Number of parameters: {num_params}.")
