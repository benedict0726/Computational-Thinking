#習題一
print("一件上衣300元，一件褲子350元，一件背心400元")
a=int(input("上衣購買數量:"))
b=int(input("褲子購買數量:"))
c=int(input("背心購買數量:"))
s=a*300+b*350+c*400
print("總金額:%d" %(s))
#習題二
print("一罐20一打200，不足一打則個別賣")
a=int(input("購買數量:"))
if(a<12):
    s=a*20
else:
    x=a%12
    y=(a-x)/12
    s=x*20+y*200
print("總數量:%d" %(a), "總金額:%d" %(s))
#習題三
a=int(input("第一次期中考:"))
b=int(input("第二次期中考:"))
c=int(input("第三次期中考:"))
x=a+b+c
y=(a+b+c)/3
print("總分為%d" %(x), "平均為:%8.2f" %(y))