m=0
j1=0
#保存（存在程序所在处）
import json
with open("number saved.json","r") as jj:
    tt=json.load(jj)
def saved(quqi,p):
    c=str(input("您是否要保存计算结果？（是按1，不是按2）"))
    if c=="1":
        ww=[]
        if tt=="0":
            with open("reply.json","w") as z:
                json.dump("*",z)
            with open("number saved.json","w") as zz:
                json.dump("1",zz)
        with open("reply.json","r") as g:
            ee=json.load(g)
            ww.append(ee)
            ww.append(quqi)
            ww.append(p)
        with open("reply.json","w") as f:
            json.dump(ww,f)
        print("完成，已存至reply.json")
    if c=="2":
        z=1
#前端        
while m<1:
    import string
    import math
    if j1>0:
        a = input("请输入需要选择的功能的代码(输入shutdown关闭程序，输入help查看使用指南)")
    else:
        a = input("请输入需要选择的功能的代码(0是生成质数表，1是翻倍运算，2是计算算数平方根，3是计算圆周率，4是求n次方，5是四则运算，6是生成斐波那契数列，7是计算黄金分割率，输入shutdown关闭程序，输入help查看使用指南")
        j1+=1
    #生成质数表
    if a=="0":
        b = int(input("请输入您要生成的质数表范围：（注意要加一）:"))
        def prime(b):
            number = (b)
            if number == 1:
                print(number, "不是质数")
                return False
            for c in range(2, int(math.sqrt(number))+1):
                if number % c == 0:
                    return False
            return True

        d = []
        for e in range(2, b):
            if prime(e):
                d.append(e)
        print("共找到", len(d), "个质数")
        print(d)
        saved("the reply from fuction 0",d)
    #翻倍运算
    if a=="1":
        e = int(input("请输入您需要翻倍的数值"))
        f = int(input("请输入您需要翻倍的次数"))
        j = 0
        h = 0
        for i in range(f):
            j= e*2
            h += 1
            e = j
            print("现在数值为", j, ",这是第", h, "次翻倍.")
            w=j
        saved("the reply from fuction 1",w)
    #计算算数平方根
    if a=="2":
        x = float(input("请输入需要求算术平方根的数："))
        b = 0
        z = 0
        v = z+1
        k = 1
        w = 0
        d = int(input("需要的精确度（输入的整数数值越高计算无限小数型的算术平方根数值越精确，如果不能确定是否为无限不循环小数，推荐输入10000）："))
        u = []
        e = 0
        pre=0
        for y in range(d):
            for i in range(10):
                b = v*v
                if b < x:
                    v = v+k
                    d = d+1000
                if b > x:
                    print("这个数的算术平方根是无限小数，现在精确到：", v)
                    w = v
                    v = v/10
                    k = k/10
                if b == x:
                    u.append(v)
                    e = len(u)
                    for q in range(e-1):
                        u.pop()
            if u == []:
                print()
            else:
                pre = u[0]
                print("这个数的算术平方根是：", pre)
        saved("the reply from fuction 2",pre)
        saved("genhao",x)
    #计算圆周率
    if a =="3":
        c=int(input("请选择使用代数法还是几何法（代数法按1，几何法按2）"))
        if c==1:#代数法
            a=0
            b=1
            d=0
            e=int(input("请输入您需要的范围（10的倍数）"))
            for c in range(1,e):
                d=2*c-1
                if b==1:
                    a+=1/d
                else:
                    a-=1/d
                print("圆周率约等于",4*a)
                b=b*-1
                d=4*a
            saved("the reply from fuction 3",d)
        if c==2:#几何法
            import turtle
            myPen = turtle.Pen()
            Pos = []
            o = 0
            k = 0
            c = 0
            j = int(input("请输入需要的精度（10的倍数）"))
            r = 360*j
            py = r/2
            myPen.speed(0)
            for i in range(int(py)):
                print(i+1)
                myPen.forward(0.0001)
                myPen.left(1/j)
                o = o+1
                if o == r/2:
                    Pos.append(myPen.pos())
            print(Pos)
            m = float(input("请将显示的是信息中后一个数字输入"))
            q1=r/10000
            t = q1/m
            print("圆周率约等于",t)
            saved("the reply from fuction 3",t)
            
    #求n次方
    if a=="4":
        s = int(input("请输入底数"))
        h = int(input("请输入指数"))
        o=0
        w=s
        l=h-1
        ll=0
        for i in range(l):
            s=s*w   
        print("结果是", s)
        saved("the reply from fuction 4",s)
        ll=ll+1
        saved("^",h)
        saved("=",s)
    #四则运算
    if a=="5":
        s = int(input("请输入您选择的模式（1代表加法运算,2代表减法运算,3代表除法运算,4代表乘法运算）"))
        if s == 1:
            b = int(input("请输入一个加数"))
            c = int(input("请输入另一个加数"))
            d = c+b
            print("结果是", d)
            ee=0
            saved("the reply from fuction 5[1]",b)
            ee=ee+1
            saved("+",c)
            saved("=",d)
            ee=0
        if s == 2:
            e = int(input("请输入被减数"))
            f = int(input("请输入减数"))
            g = e-f
            print("结果是", g)
            ff=0
            saved("the reply from fuction 5[2]",e)
            ff=ff+1
            saved("-",f)
            saved("=",g)
            ff=0
        if s == 3:
            h = int(input("请输入被除数"))
            j = int(input("请输入除数"))
            if j == 0:
                print("您输入的除数是0，0不能作为除数")
            else:
                k = h/j
                print("结果是", k)
            jj=0
            saved("the reply from fuction 5[3]",h)
            jj=jj+1
            saved("/",j)
            saved("=",k)
            jj=0
        if s == 4:
            l = int(input("请输入一个乘数"))
            m = int(input("请输入另一个乘数"))
            n = l*m
            print("结果是", n)
            gg=0
            saved("the reply from fuction 5[4]",l)
            gg=gg+1
            saved("*",m)
            saved("=",n)
            gg=0
    #生成斐波那契数列
    if a =="6":
        a = (int(input("请输入范围")))
        b = 1
        c = 0
        d = []
        for i in range(2):
            d.append(b)
        for e in range(a):
            f = d[e]+d[e+1]
            d.append(f)
        print(d)
        saved("the reply from fuction 6",d)
    #计算黄金分割率
    if a =="7":
        a = (int(input("请输入范围")))
        b = 1
        c = 0
        d = []
        for i in range(2):
            d.append(b)
        for e in range(a):
            f = d[e]+d[e+1]
            d.append(f)
        s=len(d)
        v=d[s-2]/d[s-1]
        print("黄金分割率约为",v)
        saved("the reply from fuction 7",v)
#帮助
    if a=="help":
        print("0是生成质数表，1是翻倍运算，2是计算算数平方根，3是计算圆周率，4是求n次方，5是四则运算，6是生成斐波那契数列，7是计算黄金分割率，输入shutdown关闭程序")
#终止运行
    if a =="shutdown":
        m=2

