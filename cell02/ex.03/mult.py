#!/usr/bin/env python3
#รับค่าตัวเลข 2 ตัว
num1 = int(input("Enter the first number: ").strip())
num2 = int(input("Enter the second  number: ").strip())
#คูณกัน
result = num1 * num2
#เเสดงผลคูณกัน
print (f"{num1} × {num2} = {result}")
#เช็คค่าผลลัพธ์
if result > 0:
    print("The result is positive. ")
elif result < 0:
    print("The result  is negative. ")
else:
    print("The result is positive and negative. ")