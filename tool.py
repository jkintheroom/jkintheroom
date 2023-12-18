import os

rng=[r"""
e 5
    p n
""","""

"""]

s = rng[1]+rng[0]
rootl="" #File path
# fli=open(rootl+"tool.smp","r+",encoding="utf-8")
# s=fli.read() #if need read other file
# s=r"""
# """
#python??pyr() Java?? jvr
class smp:
    filetool=""
    cg = {".rp": ".replace", ".rm":".remove",".sp": ".strip", ".id": ".index", ".sl": ".split",".l":".__len__",".fd":".find",".rfd":".rfind",".ap":".append"}
    cf = {"i ":"input","p ":"print"}
    f = []
    mk = []
    n = 7
    @classmethod
    def fin(self, a, b):
        for n in a:
            if n in b:
                return True
        return False
    @classmethod
    def __init__(self):
        self.l=[]
        self.f = []
        print("0")
    @classmethod
    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            pass
    @classmethod
    def mpy(self, cds,s):
        kw = ["try", "if ", "for", "except", "while", "case", "class", "elif", "else", "def"]
        y = s.split("\n")
        ls=-1
        lk = False
        for x in y:
            ls+=1
            if x != '':
                b = ""
                bl = False
                if "'''" in x:
                    lk=not lk
                if lk:
                    cds+=x+"\n"
                    continue
                if "#" in x:
                    b = x[x.find("#")-1:]
                    x = x[:x.find("#")-1]
                if "=" in x and " e " not in x and "==" not in x and ";" + str(ls)!=self.mk and "." not in x and "," not in x and "not " not in x and "\"" not in x[:x.index("=")] and "\'" not in x[:x.index("=")] and "(" not in x[:x.index("=")] and ":"!=x[x.__len__()-1]:
                    d = x[x.index("=")+1:]
                    d = d.strip(" ")
                    if "\n[" not in s:
                        self.ln(";" + str(ls), self.mk)
                    if "/" in d and " " in d:
                        sl = d.split(" ")
                        sl[0] = sl[0].replace("/","")
                        d = x[:x.index("=") + 1] + " ["
                        for i in sl:
                            d += i + ","
                        d = d[0:d.__len__() - 1] + "]"
                    elif "|" in d and self.is_number(d.split(" ")[0]):
                        sd=d.split("|")
                        d = x[:x.index("=") + 1] + " ["
                        for s in sd:
                            d+="["
                            sl = s.split(" ")
                            for i in sl:
                                d+=i+","
                            d =d[0:d.__len__() - 1]+ "],"
                        d = d[0:d.__len__() - 1] + "]"
                    elif "|" in d and " " in d:
                        sd=d.split("|")
                        d = x[:x.index("=") + 1] + " ["
                        for s in sd:
                            d+="[\""
                            sl = s.split(" ")
                            for i in sl:
                                d+=i+"\",\""
                            d =d[0:d.__len__() - 3]+ "\"],"
                        d = d[0:d.__len__() - 1] + "]"
                    elif " " in d and "\"" not in d and "\'" not in d and "[" not in d and "(" not in d:
                        if self.is_number(d.replace(" ","")):
                            sl = d.split(" ")
                            d = x[:x.index("=")+1]+" ["
                            for i in sl:
                                d += i + ","
                            d = d[0:d.__len__()-1]+"]"
                        else:
                            sl = d.split(" ")
                            d = x[:x.index("=") + 1] + " [\""
                            for i in sl:
                                d += i + "\",\""
                            d = d[0:d.__len__() - 2] + "]"
                    elif x[:x.index("=")].strip(" ")=="":
                        d = x[x.index("(")+1:x.index(")")]+x
                    else:
                        d = x
                    cds += d
                    self.ln("="+str(ls),self.mk)
                elif "e " in x and (x.find("e ")==0 or ord(x[x.find("e ")-1])<97 or ord(x[x.find("e ")-1])>122):
                    # self.ln("e" + str(ls), self.mk)
                    # and "e"+str(ls) not in self.mk
                    d = x.replace("e ", "")
                    if self.is_number(x[x.index("e")+2:x.index("e")+3]) or x[x.find("e ")+2]=="/":
                        x=x.replace("/","")
                        if x[:x.index("e")].strip(" ")=="":
                            md=x[x.index("e")+2:]
                            d = x.replace("e "+md, "for n in range("+ md + "):")
                        else:
                            md = ""
                            if "]" in x[x.index("e "):]:
                                md = x[x.index("e ") + 2:x.index("]",x.index("e "))]
                                d = x.replace("e " + md, "for n in range(" + md + ")")
                            else:
                                md = x[x.index("e ") + 2:]
                            d = x.replace("e " + md, "for n in range(" + md +")")
                    else:
                        if x[:x.index("e ")].strip(" ")=="":
                            if x.find("_")!=-1:
                                c=x[x.find("e ")+2:x.find("_")]
                                d = x.replace("e "+c+"_", c+"=-1\n"+x[:x.index("e ")]+"for n in ") + ":\n"+x[:x.index("e ")]+"    "+c+"+=1"
                            else:
                                d = x.replace("e ", "for n in ") + ":"
                        else:
                            d = x.replace("e ", "for n in ")
                    cds = cds + d
                elif ";" in x:
                    d = x[:x.find(";")]
                    if "\n[" not in s:
                        self.ln(";"+str(ls),self.mk)
                    if d not in self.f:
                        self.ln(d,self.f)
                    d = d.replace(d.strip(" "),"")+"def "+d.strip(" ")+"("+x[x.find(";")+1:]+"):"
                    cds += d
                elif x.strip(" ").__len__()>0 and x.strip(" ")[0]=="[":
                    # and "e"+str(ls) not in self.mk
                    self.mk=[]
                    f = open(self.filetool, "r+",encoding="utf-8")
                    s = f.read()
                    if s.find(">>" + x.strip(" "))!=-1:
                        d = s[s[:s.find(">>"+x.strip(" "))].rfind("\n{\n") + 2:s[:s.find(">>"+x.strip(" "))].rfind("}")]
                        s=x.replace(x.strip(" "),"")
                        d=d.replace("\n","\n"+s)
                        cds = cds + d + "\n"
                    else:
                        cds = cds + x
                elif x.replace(" ","").__len__()>0 and ":" == x.replace(" ","")[x.replace(" ","").__len__()-1] and  not self.fin(kw,x) and ":"+str(ls) not in self.mk:
                    if "\n[" not in s:
                        self.ln(":" + str(ls), self.mk)
                    f = '\''
                    if '\"' in x:
                        f = "\""
                    cs = x[x.find(f):x.find(f, x.find(f) + 1) + 1]
                    if cs!='':
                        d = x.replace(cs, "????")
                        d = d.replace("<=", "<~")
                    else:
                        d = x.replace("<=", "<~")
                    d = d.replace("!=", "/-/")
                    d = d.replace("<=", "*-*")
                    d = d.replace(">=", "-*-")
                    d = d.replace("==", "=")
                    d = d.replace("=", "==")
                    d = d.replace("<~", "<=")
                    # d=d.replace("True","T")
                    # d = d.replace("False", "F")
                    # d = d.replace("F", "False")
                    # d = d.replace("T", "True")
                    d=d.replace("!","not ")
                    d = d.replace("/-/", "!=")
                    d = d.replace("*-*","<=")
                    d = d.replace("-*-",">=")
                    d = d.replace("&", " and ")
                    d = d.replace("|", " or ")
                    if cs != '':
                        d = d.replace("????", cs)
                    if "::" in d:
                        d=d.replace("::",":")
                        cds += d.replace(d.strip(" "), "elif " + d.strip(" ")) + "\n"
                    else:
                        cds+=d.replace(d.strip(" "),"if "+d.strip(" "))+"\n"
                else:
                    bl=True
                    for f in self.cf:
                        if f in x and "\"" not in x[:x.find("p ")]:
                            d = x.replace(f, self.cf[f]+"(", 1) + ")"
                            cds = cds + d
                            bl = False
                            break
                    if bl:
                        for f in self.f:
                            if f == x.replace(" ",""):
                                d = x.replace(f, f + "(", 1) + ")"
                                cds = cds + d
                                bl = False
                                break
                            elif f+" " in x and "def" not in x and "=" not in x:
                                d = x.replace(f+" ", f + "(", 1) + ")"
                                cds = cds + d
                                bl = False
                                break
                if bl: #last
                    if "." in x:
                        dot=-1
                        while True:
                            if x.find(".",dot+1)==-1:
                                break
                            if x[x.index(".", dot + 1):x.find("(", x.index(".", dot + 1))] in self.cg and "\"" not in x[:x.index(".", dot + 1)] and "\'" not in x[:x.index(".", dot + 1)]:
                                d = x[x.index(".", dot + 1):x.find("(", x.index(".", dot + 1))]
                                d = x.replace(d, self.cg[d])
                                bl = False
                            dot = x.find(".",dot+1)
                        if not bl:
                            cds += d
                    if bl:
                        if "++" in x:
                            x = x.replace("++", "+=1")
                            cds = cds + x
                        elif "--" in x:
                            x = x.replace("--", "-=1")
                            cds = cds + x
                        else:
                            cds = cds + x
                cds = cds + b + "\n"
        return cds
    @classmethod
    def ln(self, x, o):
        if x not in o:
            o.append(x)
            return True
        return False
    #tck(str,"[")
    @classmethod
    def tck(self, s,m):
        l=0
        mx=0
        for c in s:
            if c == m:
                l+=1
            else:
                l=0
            if l>mx:
                mx = l
        return mx
    @classmethod
    def mjv(self, cds):
        self.l=[]
        y = s.split("\n")
        ls = 0
        for x in y:
            if x != '':
                ls+=1
                b = ""
                if "//" in x:
                    b = x[x.find("//")-1:]
                    x = x[:x.find("//")-1]
                if "=" in x and "="+str(ls) not in self.mk and ";" not in x:
                    self.ln("=" + str(ls), self.mk)
                    # d = x[x.index(" ")-1:x.index("=")-1]
                    if self.ln(d,self.l):#???????
                        d = x[x.index("=") + 1:]
                        d = d.strip(" ")
                        if "/" in d:
                            sl = d.split(" ")
                            sl[0] = sl[0].replace("/", "")
                            d = "Object[] "+x[:x.index("=") + 1] + "{"
                            for i in sl:
                                d += i + ","
                            d = d[0:d.__len__() - 1] + "}"
                        elif " " in d and "\"" not in d and "\'" not in d and "[" not in d:
                            if self.is_number(d.replace(" ", "")):
                                sl = d.split(" ")
                                d = x.replace(x.strip(" "),"")+"int[] " +x[:x.find("=")+1].strip(" ")+ "{"
                                for i in sl:
                                    d += i + ","
                                d = d[0:d.__len__() - 1] + "}"
                            else:
                                sl = d.split(" ")
                                d = x[:x.index("=") + 1] + " [\""
                                for i in sl:
                                    d += i + "\",\""
                                d = d[0:d.__len__() - 2] + "]"
                        elif "[" in x :
                            d = x[:x.index("=") + 1]
                            if "\"" in x:
                                d = "String"+"[]"*self.tck(x,"[")+" " + d.replace(' ', '') + x[x.index("=") + 2:].replace("[","{").replace("]","}")
                            else:
                                d = "int"+"[]"*self.tck(x,"[")+" " + d.replace(' ', '') + x[x.index("=") + 2:].replace("[","{").replace("]","}")
                        elif "\"" in x:
                            d = x[:x.index("=")+1]
                            d = "String "+d.replace(' ','') + x[x.index("=")+2:]
                        elif x[:x.index("=")].strip(" ") == "":
                            d = x[x.find("(") + 1:x.find(")")] + x
                        else:
                            d = x[:x.index("=") + 1]
                            d = x.replace(x.strip(" "),"")+"int " + d.replace(' ', '') + x[x.index("=") + 2:]
                    else:
                        d = x
                    cds = cds + d + ";"
                elif "S" in x:
                    cds = cds + x.replace("S","String")
                elif "e " in x and "="+str(ls) not in self.mk:
                    self.ln("=" + str(ls), self.mk)
                    d = x[x.index("e ")+2:]
                    if self.is_number(d):
                        cds += x.replace(x.strip(" "),"")+"for(int i=0;i<"+d+";i++)"
                    else:
                        cds += x.replace(x.strip(" "),"")+"for(Object i:"+d+")"
                elif "p " in x:
                    if "," in x and "\"" not in x:
                        x = x.replace(",","+\",\"+")
                    d = x.replace("p ", "")
                    d = d.replace(d.strip(' '), "") + "System.out.println(" + d.strip(' ') + ");"
                    cds = cds + d
                elif "main" in x:
                    d=x.replace("main:","public static void main(String args[])")
                    cds += d
                else:
                    cds = cds + x
                cds = cds + b + "\n"
        return cds
    @classmethod
    def jvr(self, s):
        cds = ""
        cds = self.mjv(cds)
        fl = open("t.java", "w+", encoding="utf-8")
        fl.write(cds)
        fl.close()
        fl = open("c.cmd", "w+", encoding="utf-8")
        fl.write("javac t.java\njava t")
        fl.close()
        os.system("c.cmd")
    @classmethod
    def pyr(self, s):
        cds=s
        for i in range(0,self.n):#????
            cds = self.mpy("",cds)
        # print(cds)
        fl = open(rootl+"t.py", "w+", encoding="utf-8")
        fl.write(cds)
        fl.close()
        fl = open("c.cmd", "w+", encoding="utf-8")
        fl.write("cd "+rootl+"\npython t.py")
        fl.close()
        os.system("c.cmd")
    @classmethod
    def listall(self):
        f = open(self.filetool, "r+",encoding="utf-8")
        s = f.read().split("\n")
        for a in s:
            if ">>" in a:
                print(a)

smp.filetool=r"tool.txt"
# smp.listall()
smp.pyr(s)