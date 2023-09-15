#รับข้อมูลจำนวนเต็ม 5 จำนวนจากผู้ใช้ และคนนวณหาผลรวม และค่าเฉลี่ยของข้อมูลที่รับเข้ามาเป้นเท่าใด แล้วแสดงผลทางหน้าจอ
#ขอ 4 ฟังก์ชั้น ดังนั้นหาให้ได้ 4 feature

# ========================
# Program Average 5 Number
#===============================
# Enter number 1 : <input>
# Enter number 1 : <input>
# Enter number 1 : <input>
# Enter number 1 : <input>
# Enter number 1 : <input>
#===========================
# Sun of 5 number is : <output>
# Average of 5 number is : <output>
#=================================

#1.รับค่า number 2.คำนวณผมรวม ของnumber 3.คำนวณหาค่าเฉลี่ยของnumber 4.แสดงผลทางหน้าจอ
def inputData( ) :
    number1 = float(input( 'โปรดป้อนค่าตัวที่ 1 :' ))
    number2 = float(input( 'โปรดป้อนค่าตัวที่ 2 :' ))
    number3 = float(input( 'โปรดป้อนค่าตัวที่ 3 :' ))
    number4 = float(input( 'โปรดป้อนค่าตัวที่ 4 :' ))
    number5 = float(input( 'โปรดป้อนค่าตัวที่ 5 :' ))
    return number1,number2,number3,number4,number5

def calSumOfNumber(number1,number2,number3,number4,number5 ) :
    sumOfNumber = number1+number2+number3+number4+number5
    return sumOfNumber

def calAverageOfNumber( number1,number2,number3,number4,number5) :
    averageOfNumber = ((number1+number2+number3+number4+number5)/5)
    return averageOfNumber

def showDataAndSumAndAverageOfNumber( number1,number2,number3,number4,number5,sumOfNumber,averageOfNumber) :
    print(f'number 1 is {number1}')
    print(f'number 2 is {number2}')
    print(f'number 3 is {number3}')
    print(f'number 4 is {number4}')
    print(f'number 5 is {number5}')
    print('=================================')
    print(f'Sum of 5 number is {sumOfNumber}')
    print(f'Average of 5 number is {averageOfNumber:.4f}')

print('==========================================')
print('         Program Average 5 Number         ')
print('==========================================')
number1,number2,number3,number4,number5 = inputData( )
sumOfNumber = calSumOfNumber(number1,number2,number3,number4,number5 )
averageOfNumber = calAverageOfNumber( number1,number2,number3,number4,number5)
print('==========================================')
showDataAndSumAndAverageOfNumber(number1,number2,number3,number4,number5,sumOfNumber,averageOfNumber)
print('==========================================')