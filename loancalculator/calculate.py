import math
import numpy as np
#ฟังก์ชันเรียงวันเกิดให้สวยงาม
def bday(d,m,y):
  if(d < 10):
    if(m < 10):
      return ("0{}/0{}/{}".format(d,m,y))
    else:
      return ("0{}/{}/{}".format(d,m,y))  
  elif(month < 10):
    return ("{}/0{}/{}".format(d,m,y))
  else:  
    return ("{}/{}/{}".format(d,m,y))


#เริ่มโปรแกรมคำนวณเงินกู้
print("โปรแกรมคำนวณเงินกู้")

print("\nวิธีคิดดอกเบี้ยแบบไหน?")
print("1.ปกติ\n2.ลดต้นลดดอก")
tp = int(input("กรุณาเลือกวิธีการคิดดอกเบี้ย : ")) #อินพุทเลือกวิธีการคิด

#เช็คความถูกต้องของตัวเลือก
btp = (tp == 1) or (tp == 2)
while btp == False:
  print("\nError!\nกรุณาเลือกคำตอบใหม่")
  tp = int(input("กรุณาเลือกวิธีการคิดดอกเบี้ย : "))
  btp = (tp == 1) or (tp == 2)

answer = 2
#loopเพื่อกลับมาป้อนค่าอีกรอบหากต้องการเปลี่ยนข้อมูล
while answer  == 2 :
  #อินพุทข้อมูล
  loan = float(input("\nจำนวนเงินกู้ : "))
  itrst = float(input("อัตราดอกเบี้ยรายปี : "))
  t = float(input("ระยะเวลาการกู้ยืม(ปี) : "))
  print("\nกรุณากรอกวันที่เริ่มต้นการกู้เงิน")
  day = int(input("วัน (ตัวอย่าง 5 12) : "))
  month = int(input("เดือน (ตัวอย่าง 8 11) : "))
  year = int(input("ปี (ตัวอย่าง 2566) : "))
  
  #เช็คความถูกต้องของวันที่
  bld1 = day > 31
  bld2 = (month == 2) and (day > 29)
  blm1 = month > 12
  while (bld1 or bld2 or blm1) == True:
    print("\nError!\nกรุณาป้อนข้อมูลใหม่")
    day = int(input("วัน (ตัวอย่าง 5 12) : "))
    month = int(input("เดือน (ตัวอย่าง 8 11) : "))
    year = int(input("ปี (ตัวอย่าง 2566) : "))
    bld1 = day > 31
    bld2 = (month == 2) and (day > 29)
    blm1 = month > 12

  print("\n--------------------------------------------")
  print("------------ตรวจสอบข้อมูล--------------")
  print("--------------------------------------------\n")
  print("จำนวนเงินกู้ : ", round(loan,2) , "฿\nอัตราดอกเบี้ยรายปี : ", round(itrst,2) , "%\nระยะเวลาการกู้ยืม : ", int(t) )
  dt = bday(day,month,year)
  print("วันที่เริ่มต้นการกู้เงิน : {}".format(bday(day,month,year)))
  print("\n--------------------------------------------")
  print("\nข้อมูลถูกต้องใช่หรือไม่?")  #เช็คข้อมูลที่ป้อนเข้าไปว่าถูกต้องตามความต้องการหรือไม่
  answer = int(input("1.ใช่\n2.ไม่\nป้อนคำตอบ: "))
  basw1 = answer == 1
  basw2 = answer == 2
  fbasw = basw1 or basw2
  #เช็คความถูกต้องของตัวเลือก
  while fbasw == False:
    print("\nError!\nกรุณาป้อนข้อมูลใหม่")
    answer = int(input("1.ใช่\n2.ไม่\nป้อนคำตอบ: "))
    basw1 = answer == 1
    basw2 = answer == 2
    fbasw = basw1 or basw2

#เช็คว่าใช้วิธีคิดแบบไหนแล้วคำนวณการคิดดอกเบี้ยตามวิธีการที่เลือกด้านบน
if(tp == 1):
  ampm = t*12
  totalitrst = loan*((itrst/100)*t)
  cost = loan + totalitrst
  mpm = cost/ampm
elif(tp == 2):
  c = loan
  totalitrst = 0
  ampm = t*12
  i = (itrst/100)/12
  mpm = c/((1-(1/((1+i)**ampm)))/i)
  for tmp in range(int(ampm)):
    a = c * i
    b = mpm - a
    c = c - b
    totalitrst += a
  cost = loan + totalitrst

#สรุปค่าทั้งหมดที่ได้ออกมา
print("\n--------------------------------------------")
print("\nการชำระเงินรายเดือน: ",round(mpm,2),"฿")
print("จำนวนการชำระเงิน(เดือน): ",int(ampm))
print("ยอดรวมดอกเบี้ย: ",round(totalitrst,2),"฿")
print("ดอกเบี้ยต้นทุนเงินกู้: ",round(cost,2),"฿")

#เช็คว่าคิดแบบ1หรือ2
if(tp == 1):
  print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
  print("ครั้งที่\t\t\tวันที่ชำระเงิน\t\t\tยอดคงเหลือ\t\t\tการชำระเงิน\t\t\tเงินต้น\t\t\tดอกเบี้ย\t\t\tยอดสิ้นสุด")
  print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
  a = loan
  #loopแสดงค่าทั้งหมด ครั้งที่ วันที่ต้องชำระ ยอดคงเหลือ จำนวนที่ต้องชำระ เงินต้น ดอกเบี้ย ยอดสิ้นสุดในครั้งนั้นๆ
  for i in range(int(ampm)):
    i = i+1
    y = mpm - (((itrst/100)*loan)/12)
    x = a - y
    
    z = ((itrst/100)*loan)/12
    date = bday(day,month,year)
    #เช็คความยาวของสตริงแต่ละค่าแล้วลด/เพิ่มจำนวนtab
    if(len(str((round(a,2))))  > 9):
      print("{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t{}\t\t\t{}".format(str(i),str(date),str(round(a,2)),str(round(mpm,2)),str(round(y,2)),str(round(z,2)),str(round(x,2))))
    elif(len(str((round(y,2)))) < 5):
      if(len(str((round(z,2)))) < 5):
        print("{}\t\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}".format(str(i),str(date),str(round(a,2)),str(round(mpm,2)),str(round(y,2)),str(round(z,2)),str(round(x,2))))
      else:
        print("{}\t\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t{}".format(str(i),str(date),str(round(a,2)),str(round(mpm,2)),str(round(y,2)),str(round(z,2)),str(round(x,2))))
    elif(len(str((round(z,2)))) < 5):
      print("{}\t\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t{}\t\t\t\t{}".format(str(i),str(date),str(round(a,2)),str(round(mpm,2)),str(round(y,2)),str(round(z,2)),str(round(x,2))))
    else:
      print("{}\t\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t{}\t\t\t{}".format(str(i),str(date),str(round(a,2)),str(round(mpm,2)),str(round(y,2)),str(round(z,2)),str(round(x,2))))
    a = x
    #เช็คเดือนถ้าเกิน12แล้วให้บวกปีเพิ่มแล้ววนมาที่เดือนแรก
    month = month + 1
    if(month > 12):
      month = 1
      year = year + 1
elif(tp == 2):
  print("\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
  print("ครั้งที่\t\t\tวันที่ชำระเงิน\t\t\tยอดคงเหลือ\t\t\tการชำระเงิน\t\t\tเงินต้น\t\t\tดอกเบี้ย\t\t\tยอดสิ้นสุด")
  print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
  a = loan
  #loopแสดงค่าทั้งหมด ครั้งที่ วันที่ต้องชำระ ยอดคงเหลือ จำนวนที่ต้องชำระ เงินต้น ดอกเบี้ย ยอดสิ้นสุดในครั้งนั้นๆ
  for i in range(int(ampm)):
    i = i+1
    y = mpm - (((itrst/100)*a)/12)
    x = a - y
    z = ((itrst/100)*a)/12
    date = bday(day,month,year)
    bif = len(str((round(y,2)))) < 5  and  len(str((round(z,2)))) < 5
    #เช็คความยาวของสตริงแต่ละค่าแล้วลด/เพิ่มจำนวนtab
    if(len(str((round(a,2))))  > 9):
      print("{}\t\t\t{}\t\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t{}\t\t\t{}".format(str(i),str(date),str(round(a,2)),str(round(mpm,2)),str(round(y,2)),str(round(z,2)),str(round(x,2))))
    elif(len(str((round(y,2)))) < 5):
      if(len(str((round(z,2)))) < 5):
        print("{}\t\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}".format(str(i),str(date),str(round(a,2)),str(round(mpm,2)),str(round(y,2)),str(round(z,2)),str(round(x,2))))
      else:
        print("{}\t\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t{}".format(str(i),str(date),str(round(a,2)),str(round(mpm,2)),str(round(y,2)),str(round(z,2)),str(round(x,2))))
    elif(len(str((round(z,2)))) < 5):
      print("{}\t\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t{}\t\t\t\t{}".format(str(i),str(date),str(round(a,2)),str(round(mpm,2)),str(round(y,2)),str(round(z,2)),str(round(x,2))))
    else:
      print("{}\t\t\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t{}\t\t\t{}".format(str(i),str(date),str(round(a,2)),str(round(mpm,2)),str(round(y,2)),str(round(z,2)),str(round(x,2))))
    a = x
    #เช็คเดือนถ้าเกิน12แล้วให้บวกปีเพิ่มแล้ววนมาที่เดือนแรก
    month = month + 1
    if(month > 12):
      month = 1
      year = year + 1
