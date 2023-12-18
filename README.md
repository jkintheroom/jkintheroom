<h2>目录</h2>
<h3>一、[python使用功能介绍]<br/><br/>
二、[Java 示例]</h3>
本程序支持注释
<h3 id='index1'>python使用功能介绍</h3>
<p>python示例</p>
<p>
本程序支持注释
运行代码会生成python代码到t.py文件当中 同时生成c.cmd文件直接通过os.system执行 
可以在下方面控制台板上看到t.py文件的打印输出</p>

```
sn = 0 5 3 3 1
e sn #其中 e 代表foreach 类似 for n in sn
    n++ #添加 n++ 功能
    n+=5
    p n
#or you can
n = 0 4 5 3 2
def sh(sn):
    e sn #默认for n in sn 其中 n 是内置默认的 无法更改
        p n 
sh(n)
```

最新功能示例
```
w = 0w0 0o0 0v0 0u0 0j0 0-0 0_0 0n0 0m0 0A0 QvQ :D ヾ(≧▽≦*)o （￣︶￣）↗　#等于号后加空格
s = /0 w 0 2 "ok" #s=[0,w,0,2,"ok"]
r; #替换为def r(): 例如 r;x,y 为 def r(x,y):
    p "yp "
e w
    r #替换为 r() 例如: r x 替换为 r(x)
    p n
p str(i "y=")
p [n e w]
```
函数应用
```
erjinzhi;
    o=0
    po=[["0" e 3]e 8]
    e 8
        p po
        u=bin(n)
        s=str(u).rp("0b","")
        i=0
        e s
            po[o][i+3-s.l()]=n
            p i,o
            i++
        o++
        p s,po
    p po
```
随机应用示例
```python
from random import randint as 随
骰;s
    return s[随(0,s.l()-1)]
时代1 = 夏 商 周
时代2 = 春秋 战国 两晋 南北朝 三国
p 骰(时代1)+"and"+骰(时代2)

all = en int fn
m = /1 3 3 5 6 9
e i_all #e循环 i从0到all.__len__()
    p n,i
```
函数参数自调用
```python
all = en int fn
cgs = u n m
cg;x,y
    return y,x
=cg(all,cgs)# all,cgs=cg(all,cgs)
p cgs,all
```
最新功能展示<br>
直接可以将user.txt文件内容复制到[name]所在位置 其中"["符号在最左侧或左侧只有空格
```python
[pygame] #下面的代码可以直接接在pygame的while循环中
    p=150 150 300 300 #分别代表x y w h
    rc(p)#画一个rect 在p 默认存在外部color参数 内部p w
```
其中 user.txt文件内容<br>
"{}"内的内容可以编辑
```python
{ #此处匹配\n 必要回车
import pygame
import sys
from pygame.draw import *
from pygame.locals import *
pygame.init()                                   #初始化pygame
screen = pygame.display.set_mode((1200,700),RESIZABLE)     #获取显示系统访问，创建600*500窗口
pygame.display.set_caption("Drawing shape")   #窗口的名字
color = [255,255,255]
def rc(p=[0,0,100,100],w=0):
    rect(surface=screen, color=color, rect=p,width=w)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            try:
                key=event.key
                keydown() #保证如果上部分有定义keydown的话，将直接作为keydown事件使用
            except:
                None
        if event.type == pygame.KEYUP:
            try:
                keyup() #保证如果上部分有定义keyup的话，将直接作为keyup事件使用
            except:
                None
    pygame.display.update()
}>>[pygame]
```
同时user.txt兼容新语种<br>
新代码块命名没有上下次序，存放位置随意,只是>>[]内不能重名<br>
更改smp类中的n = 4可修改编译迭代次数
```python
{
keydown;
    p key
    if key==32:
        erjinzhi()
[erjinzhi]
[pygame]
    po=200 200 100 100
    rc(po)
}>>[play0]
```

最新功能展示<br>
"/"代表"!=";"="代表"==";"!"代表"not "<br>
if 用之后的冒号代替<br> 
T代表True; F代表False; 只在":"号前生效
```python
fin;a,b #if a in b
    e a
        n in b: #if 用之后的冒号代替 
            return True
        n=0:: #elif 的用法
            p 0
    return False
```
<p>代码中将cg = {".rp": ".replace", ".sp": ".strip", ".id": ".index", ".sl": ".split",".l":".__len__",".fd":".find"}
这些功能进行替换 例如a=1b13 a=a.rp("1","0") 则a为0b03</p>

<h3 id='index2'>Java 示例</h3>
<p>本程序支持注释 代码：</p>

```
n = ["s","ff","gg"]#自动生成 String[] n=["fsd","sdf"]
void sh(S[] sn){#S会替换为String
    e 6#for(i=0;i<6;i++)
    {
        p sn[i] #print(sn[i]);分号自动加
    }
}
sh(n);#未定义功能不会加分号
```
<p>最新功能展示</p>

```
public class t{
    void cg(int x,int y)
    {
       int c=x;
       x=y;
       y=c;
       p x,y
    }
    main:
    {
    m = 0 2 3
    t t=new t();
    t.cg(m[0],m[2]);
    p m[0],m[2]
    }
}
```
