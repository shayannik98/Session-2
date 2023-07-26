name= input("enter name:")
family=input ("enter family name:")
point1=int(input ("enter math number"))
point2=int(input ("enter physic number"))
point3=int(input ("enter art number"))
b = point1+point2+point3
avrage= b / 3
if avrage<12:
    print("Fail")
if 12<avrage < 17 :
    print("Normal")
if avrage >=17:
    print("Great")    

print("your name","is", name,family,"your","avrage","is",avrage)