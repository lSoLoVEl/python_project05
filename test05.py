#คำนวณหาภาษีที่ต้องจ่าย และเงินเดือนสุทธิของพนักงานแล้วแสดงผลทางหน้าจอ โดยรับค่ารหัสพนักงาน ชื่อพนักงาน และเงินเดือนปกติของพนักงานทางแป้นพิมพ์
#ทั้งนี้เงินเดืออนสุทธิของพนักงานนั้นจะต้องหักค้าภาษีและเบี้ยประกันสังคมออกจากเงินเดือนเสียก่อน โดยที่พนักงานต้องเสียถาษี 7% ของเงินเดือนปกติและจ่ายค่าเบี้ยประกันสังคม 500 บาท

#ขอ 5 ฟังก์ชั้น

#=============================
#       คำนวณเงินเดือนพนักงาน
#=============================
#ป้อนรหัสพนักงาน : <input>
#ป้อนชื่อพนักงาน : <input>
#ป้อนเงินเดือนปกติ : <input> บาท
#=========================================
#ภาษีเป็นเงิน : <output บาท (ของทศนิยม 2 ตำแหน่ง)
#เงินเดือนสุทธิเป็นเงิน : <output> บาท (ขอทศนิยม 2 ตำแหน่ง)
#=============================================

#1.รับค่าข้อมูลจากพนักงาน 2.คำนวณเงินเดือนพนักงานสุทธิ 3.คำนวณหาค่าภาษีของพนักงาน 4.คำนวณประกันสังคม   5.แสดงผล

def inputData( ) :
    id = str(input( 'โปรดป้อนรหัสพนักงาน : ' ))
    name = str(input( 'โปรดป้อนชื่อพนักงาน : '))
    salary = float(input( 'โปรดป้อนเงินเดือน : '))
    return id,name,salary

def calTax(salary ) :
    tax = salary*(7/100)
    return tax

def socialSecurity( ) :
    socialSecurity = 500
    return socialSecurity

def calNetsalary(salary,tax,socialSecurity ) :
    netsalary = salary - tax- socialSecurity
    return netsalary

def showSalaryTaxSocialSecurityAndNetsalary(salary,tax,socialSecurity,netsalary) :
    print(f'ภาษีเป็นเงิน {tax:.2f} บาท')
    print(f'เบี้ยประกันสังคม {socialSecurity:.2f} บาท')
    print(f'เงินเดือนสุทธิเป็นเงิน {netsalary:.2f} บาท')
    
print('==========================================================')
print('                   คำนวณเงินเดือนพนักงาน               ')
print('==========================================================')
id,name,salary = inputData( )
tax = calTax( salary)
socialSecurity = socialSecurity( )
netsalary = calNetsalary(salary,tax,socialSecurity )
showSalaryTaxSocialSecurityAndNetsalary(salary,tax,socialSecurity,netsalary)
print('==========================================================')