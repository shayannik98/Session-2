import math


op=input("enter op(+,-,*,/,tan,sin,cos,cot,factorial,radical)")
num1= int(input("enter num1: "))
num2= int(input("enter num2: "))
num3= int(input("enter num3: "))
if op== "+":
    result= num1+num2
if op== "*":
    result= num1*num2
if op== "/":
    if num2==0:
        result = "error"
    else:
        result=num1/num2 
    
if op== "-":
      
    result=num1-num2
if op== "sin":
    print(math.sin(math.radians(num3)))
if op== "cos":
    print(math.cos(math.radians(num3)))
if op== "tan":
    print(math.tan(math.radians(num3))) 
if op== "cot":
    if math.tan(num3)!=0:
           print(1/math.tan(math.radians(num3)))
else: 
           result= ("not valid!")          
if op== "factorial":
     if num3>=0:
          result= (math.factorial(num3))
if op== "radical":
     if num3>=0:
          result= (math.sqrt(num3))
     else:
             print("not valid") 
else:
     print("invalid number !")                       
