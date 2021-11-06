import tkinter 
from tkinter import ttk
import tkinter.ttk
import os 
import ctypes
from tkinter import *
from tkinter.colorchooser import askcolor
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import time
from PIL import Image,ImageDraw, ImageFont
import imgkit
import pyperclip
user32 = ctypes.windll.user32
path = os.getcwd()


#屏幕大小
global pk
pk = user32.GetSystemMetrics(0)
#得到屏幕宽度
global pg
pg = user32.GetSystemMetrics(1)
#得到屏幕高度

#用户数据地址
path_user = path.replace('dist','user data')
path_logo = path.replace('dist','logo')
path_Temporary = path.replace('dist','Temporary data')
path_wkhtmltopdf = path.replace('dist','wkhtmltopdf')

#背景色
with open(path_user +'\\bg.txt',"r") as f:    #设置对象
    ckbg = f.read()  #读取文件内容
#字体色
with open(path_user +'\\fg.txt',"r") as f:    #设置对象
    ckfg = f.read()  #读取文件内容
#透明度
with open(path_user +'\\tm.txt',"r") as f:    #设置对象
    cktm = f.read()  #读取文件内容


#默认组
global A1
with open(path_Temporary +'\\layout color\\A1.txt',"r") as f:    #设置对象
    A1 = f.read()  #读取文件内容
    
global A2
with open(path_Temporary +'\\layout color\\A2.txt',"r") as f:    #设置对象
    A2 = f.read()  #读取文件内容
    
global A3
with open(path_Temporary +'\\layout color\\A3.txt',"r") as f:    #设置对象
    A3 = f.read()  #读取文件内容

global B1
with open(path_Temporary +'\\layout color\\B1.txt',"r") as f:    #设置对象
    B1 = f.read()  #读取文件内容
    
global B2
with open(path_Temporary +'\\layout color\\B2.txt',"r") as f:    #设置对象
    B2 = f.read()  #读取文件内容
    
global B3
with open(path_Temporary +'\\layout color\\B3.txt',"r") as f:    #设置对象
    B3 = f.read()  #读取文件内容
    
global C1
with open(path_Temporary +'\\layout color\\C1.txt',"r") as f:    #设置对象
    C1 = f.read()  #读取文件内容
    
global C2
with open(path_Temporary +'\\layout color\\C2.txt',"r") as f:    #设置对象
    C2 = f.read()  #读取文件内容
    
global C3
with open(path_Temporary +'\\layout color\\C3.txt',"r") as f:    #设置对象
    C3 = f.read()  #读取文件内容
    
global D1
with open(path_Temporary +'\\layout color\\D1.txt',"r") as f:    #设置对象
    D1 = f.read()  #读取文件内容
    
global D2
with open(path_Temporary +'\\layout color\\D2.txt',"r") as f:    #设置对象
    D2 = f.read()  #读取文件内容
    
global D3
with open(path_Temporary +'\\layout color\\D3.txt',"r") as f:    #设置对象
    D3 = f.read()  #读取文件内容


#窗口位置

def ckdx(ckk,ckg):
    global pk
    global pg
    #计算
    ckdx =str(ckk)+"x"+str(ckg)+"+"+str(int((pk-ckk) / 2))+"+"+str(int((pg-ckg) / 2))
    #返回
    return ckdx

########################################################
root_jz = tkinter.Tk()
root_jz.overrideredirect(True)
root_jz.geometry(str(610)+"x"+str(443)+"+"+str(int((user32.GetSystemMetrics(0)-610) / 2))+"+"+str(int((user32.GetSystemMetrics(1)-443) / 2)))
root_jz.wm_attributes('-alpha',int(cktm)/100)
root_jz. attributes ("-topmost",True)
root_jz.resizable(False,False)

canvas = Canvas(root_jz,width=610, height=443,bg='white')
canvas.place(x=0, y=0)
img=[]

im = Image.open(path_logo + '\\logo.gif')
# GIF图片流的迭代器
iter_ = ImageSequence.Iterator(im)
#frame就是gif的每一帧，转换一下格式就能显示了
for frame in iter_:
    pic=ImageTk.PhotoImage(frame)
    canvas.create_image((305,221.5), image=pic)
    time.sleep(0.04)
    root_jz.update_idletasks()  #刷新
    root_jz.update()
#加载

global number

number = "A"


def color16_rgb(hex_color):
    r = int('0x' + hex_color[1:3],16)   
    g = int('0x' + hex_color[3:5],16)
    b = int('0x' + hex_color[5:7],16)

    return str(r) + ',' + str(g) + ',' + str(b)
    
def rgb_color16(r,g,b):
    hex_r = hex(r)[2:].upper()
    hex_g = hex(g)[2:].upper()
    hex_b = hex(b)[2:].upper()
    
    hex_r0 = hex_r.zfill(2)   
    hex_g0 = hex_g.zfill(2)
    hex_b0 = hex_b.zfill(2)
    
    return "#" + hex_r0 + hex_g0 + hex_b0

#美观
def fh(event):
    btn_sy["bg"] = ckbg
    btn_sy["fg"] = ckfg
    btn_nr["bg"] = ckbg
    btn_nr["fg"] = ckfg
    btn_c["bg"] = ckbg
    btn_c["fg"] = ckfg
    
def b_sy(event):
    btn_sy["bg"] = ckfg
    btn_sy["fg"] = ckbg
def b_nr(event):
    btn_nr["bg"] = ckfg
    btn_nr["fg"] = ckbg
def b_c(event):
    btn_c["bg"] = ckfg
    btn_c["fg"] = ckbg

def g_sy():
    global A1
    global B1
    global C1
    global number
    
    if number == "A":
        sy = askcolor(color=A1,)
        
    if number == "B":
        sy = askcolor(color=B1,)
        
    if number == "C":
        sy = askcolor(color=C1,)
        
    if number == "D":
        sy = askcolor(color=D1,)

    if sy[1] != None:
        if number == "A":
            A1 = sy[1]
            with open(path_Temporary +'\\layout color\\A1.txt',"w") as f:
                f.write(A1)
            
        if number == "B":
            B1 = sy[1]
            with open(path_Temporary +'\\layout color\\B1.txt',"w") as f:
                f.write(B1)
            
        if number == "C":
            C1 = sy[1]
            with open(path_Temporary +'\\layout color\\C1.txt',"w") as f:
                f.write(C1)
            
        if number == "D":
            D1 = sy[1]
            with open(path_Temporary +'\\layout color\\D1.txt',"w") as f:
                f.write(D1)

        ys()
        ysz()


def g_nr():
    global A2
    global B2
    global C2
    global number
    
    if number == "A":
        nr = askcolor(color=A2,)
        
    if number == "B":
        nr = askcolor(color=B2,)
        
    if number == "C":
        nr = askcolor(color=C2,)
        
    if number == "D":
        nr = askcolor(color=D2,)

    if nr[1] != None:
        if number == "A":
            A2 = nr[1]
            with open(path_Temporary +'\\layout color\\A2.txt',"w") as f:
                f.write(A2)
            
        if number == "B":
            B2 = nr[1]
            with open(path_Temporary +'\\layout color\\B2.txt',"w") as f:
                f.write(B2)
            
        if number == "C":
            C2 = nr[1]
            with open(path_Temporary +'\\layout color\\C2.txt',"w") as f:
                f.write(C2)
            
        if number == "D":
            D2 = nr[1]
            with open(path_Temporary +'\\layout color\\D2.txt',"w") as f:
                f.write(D2)

        ys()
        ysz()
        
def g_c():
    global A3
    global B3
    global C3
    global number
    
    if number == "A":
        c = askcolor(color=A3,)
        
    if number == "B":
        c = askcolor(color=B3,)
        
    if number == "C":
        c = askcolor(color=C3,)
        
    if number == "D":
        c = askcolor(color=D3,)

    if c[1] != None:
        if number == "A":
            A3 = c[1]
            with open(path_Temporary +'\\layout color\\A3.txt',"w") as f:
                f.write(A3)
            
        if number == "B":
            B3 = c[1]
            with open(path_Temporary +'\\layout color\\B3.txt',"w") as f:
                f.write(B3)
            
        if number == "C":
            C3 = c[1]
            with open(path_Temporary +'\\layout color\\C3.txt',"w") as f:
                f.write(C3)
            
        if number == "D":
            D3 = c[1]
            with open(path_Temporary +'\\layout color\\D3.txt',"w") as f:
                f.write(D3)

        ys()
        ysz()
        
#国字布局
def g():
    global number
    number = "A"
    ysz()
    ys()
    wz()

#三字布局
def s():
    global number
    number = "B"
    ysz()
    ys()
    wz()
    
#丁字布局
def d():
    global number
    number = "C"
    ysz()
    ys()
    wz()
    
#综合布局
def z():
    global number
    number = "D"
    ysz()
    ys()
    wz()
    
def sz():
    global sz_bg
    sz_bg = ckbg
    global sz_fg
    sz_fg = ckfg
    def xgfg():
        xgf = askcolor(color=ckfg, title='字体颜色修改')
        if xgf[1] != None:
            global sz_fg
            sz_fg = xgf[1]
            
            lb_zt_1["text"] = xgf[1]
            lb_zt_1["fg"] = xgf[1]
            lb_bg_1["fg"] = xgf[1]

    def xgbg():
        xgb = askcolor(color=ckbg, title='背景颜色修改')
        if xgb[1] != None:
            global sz_bg
            sz_bg = xgb[1]

            lb_bg_1["text"] = xgb[1]
            lb_bg_1["bg"] = xgb[1]
            lb_zt_1["bg"] = xgb[1]
            
    def qd():
        ans = tkinter.messagebox.askyesno("提示", "修改后，请重启软件")
        if ans:

            global sz_bg
            with open(path_user +'\\bg.txt',"w") as f:
                f.write(str(sz_bg))
                
            global sz_fg
            with open(path_user +'\\fg.txt',"w") as f:
                f.write(str(sz_fg))
                
            with open(path_user +'\\tm.txt',"w") as f:
                f.write(str(sca1.get()))
            
            root_sz.destroy()
        
        else:
            return 0
        
    def qx():
        ans = tkinter.messagebox.askyesno("提示", "退出后，修改信息不会保留")
        if ans:
            
            root_sz.destroy()
        
        else:
            return 0
        
    def zt_b(event):
        btn_zt["bg"] = ckfg
        btn_zt["fg"] = ckbg
        
    def bg_b(event):
        btn_bg["bg"] = ckfg
        btn_bg["fg"] = ckbg
        
    def qd_b(event):
        btn_qd["bg"] = ckfg
        btn_qd["fg"] = ckbg
        
    def qx_b(event):
        btn_qx["bg"] = ckfg
        btn_qx["fg"] = ckbg


    def fh(event):
        btn_zt["bg"] = ckbg
        btn_zt["fg"] = ckfg
        btn_bg["bg"] = ckbg
        btn_bg["fg"] = ckfg
        btn_qd["bg"] = ckbg
        btn_qd["fg"] = ckfg
        btn_qx["bg"] = ckbg
        btn_qx["fg"] = ckfg

    root_sz = tkinter.Tk()
    root_sz.title("设置")
    root_sz.geometry(ckdx(500,400))
    root_sz.iconbitmap(path_logo+"\\logo.ico")
    root_sz.wm_attributes('-alpha',int(cktm)/100)
    root_sz.configure(bg=ckbg)
    root_sz.resizable(False,False)

    lb_zt = Label(root_sz, text="字体颜色修改:",bg=ckbg,fg=ckfg,font=('楷体', 18),)
    lb_zt.grid(row=1, column=1, padx=20, pady=20)

    btn_zt = tkinter.Button(root_sz, text="字体颜色",bg=ckbg,fg=ckfg,font=('楷体', 18),command=xgfg)
    btn_zt.bind("<Enter>", zt_b)
    btn_zt.bind("<Leave>", fh)
    btn_zt.grid(row=1, column=2,padx=20, pady=20)

    lb_zt_1 = Label(root_sz, text=ckfg,bg=ckbg,fg=ckfg,font=('楷体', 18),)
    lb_zt_1.grid(row=1, column=3, padx=20, pady=20)

    lb_bg = Label(root_sz, text="背景颜色修改:",bg=ckbg,fg=ckfg,font=('楷体', 18),)
    lb_bg.grid(row=2, column=1, padx=20, pady=20)

    btn_bg = tkinter.Button(root_sz, text="背景颜色",bg=ckbg,fg=ckfg,font=('楷体', 18),command=xgbg)
    btn_bg.bind("<Enter>", bg_b)
    btn_bg.bind("<Leave>", fh)
    btn_bg.grid(row=2, column=2,padx=20, pady=20)

    lb_bg_1 = Label(root_sz, text=ckbg,bg=ckbg,fg=ckfg,font=('楷体', 18),)
    lb_bg_1.grid(row=2, column=3, padx=20, pady=20)

    lb_tm = Label(root_sz, text="窗口不透明度:",bg=ckbg,fg=ckfg,font=('楷体', 18),)
    lb_tm.grid(row=3, column=1, padx=20, pady=20)

    sca1 = tkinter.Scale(root_sz, from_=1, to=100,bg=ckbg,fg=ckfg,font=('楷体', 18))
    sca1.set(int(cktm))
    sca1.grid(row=3, column=2, padx=20, pady=20)

    btn_qd = tkinter.Button(root_sz, text="确定",bg=ckbg,fg=ckfg,font=('楷体', 18),command=qd)
    btn_qd.bind("<Enter>", qd_b)
    btn_qd.bind("<Leave>", fh)
    btn_qd.grid(row=4, column=2,padx=20, pady=20)

    btn_qx = tkinter.Button(root_sz, text="取消",bg=ckbg,fg=ckfg,font=('楷体', 18),command=qx)
    btn_qx.bind("<Enter>", qx_b)
    btn_qx.bind("<Leave>", fh)
    btn_qx.grid(row=4, column=3,padx=20, pady=20)




    root_sz.mainloop()
    
def dbys():
    def t(event):
        btn["bg"] = ckfg
        btn["fg"] = ckbg

    def fh(event):
        btn["bg"] = ckbg
        btn["fg"] = ckfg

    def zt():
        color = com.get()
        lb11["fg"] = "%s"%(color)
        lb12["fg"] = "%s"%(color)
        lb13["fg"] = "%s"%(color)
        lb14["fg"] = "%s"%(color)
        lb15["fg"] = "%s"%(color)
        lb16["fg"] = "%s"%(color)
        lb21["fg"] = "%s"%(color)
        lb22["fg"] = "%s"%(color)
        lb23["fg"] = "%s"%(color)
        lb24["fg"] = "%s"%(color)
        lb25["fg"] = "%s"%(color)
        lb26["fg"] = "%s"%(color)
        lb31["fg"] = "%s"%(color)
        lb32["fg"] = "%s"%(color)
        lb33["fg"] = "%s"%(color)
        lb34["fg"] = "%s"%(color)
        lb35["fg"] = "%s"%(color)
        lb36["fg"] = "%s"%(color)
        lb37["fg"] = "%s"%(color)
        lb38["fg"] = "%s"%(color)
        lb40["fg"] = "%s"%(color)
        lb41["fg"] = "%s"%(color)
        lb42["fg"] = "%s"%(color)
        lb43["fg"] = "%s"%(color)
        lb44["fg"] = "%s"%(color)
        lb45["fg"] = "%s"%(color)
        lb46["fg"] = "%s"%(color)
        lb47["fg"] = "%s"%(color)
        lb48["fg"] = "%s"%(color)
        lb49["fg"] = "%s"%(color)
        lb50["fg"] = "%s"%(color)
        btn["fg"] = "%s"%(color)
        sca1["fg"] = "%s"%(color)
        sca2["fg"] = "%s"%(color)
        sca3["fg"] = "%s"%(color)
        sca4["fg"] = "%s"%(color)
        sca5["fg"] = "%s"%(color)
        sca6["fg"] = "%s"%(color)
        
    def tsp(e):
        r = sca1.get()
        g = sca2.get()
        b = sca3.get()
        R = sca4.get()
        G = sca5.get()
        B = sca6.get()
        lb31["text"] = "%s"%(r)
        lb32["text"] = "%s"%(g)
        lb33["text"] = "%s"%(b)
        lb34["text"] = "%s"%(R)
        lb35["text"] = "%s"%(G)
        lb36["text"] = "%s"%(B)
        hex_r = hex(r)[2:].upper()   #10进制转16进制，并去掉16进制前面的“0x”，再把得出的结果转为大写
        hex_g = hex(g)[2:].upper()
        hex_b = hex(b)[2:].upper()
        hex_r0 = hex_r.zfill(2)   #位数不足2位时补“0”
        hex_g0 = hex_g.zfill(2)
        hex_b0 = hex_b.zfill(2)
        l = '#' + hex_r0 + hex_g0 + hex_b0
        lb38["text"] = "%s"%(l)
        hex_R = hex(R)[2:].upper()   #10进制转16进制，并去掉16进制前面的“0x”，再把得出的结果转为大写
        hex_G = hex(G)[2:].upper()
        hex_B = hex(B)[2:].upper()
        hex_R0 = hex_R.zfill(2)   #位数不足2位时补“0”
        hex_G0 = hex_G.zfill(2)
        hex_B0 = hex_B.zfill(2)
        y = '#' + hex_R0 + hex_G0 + hex_B0
        lb37["text"] = "%s"%(y)
        lb1["bg"] = "%s"%(y)
        lb2["bg"] = "%s"%(y)
        lb3["bg"] = "%s"%(y)
        lb4["bg"] = "%s"%(y)
        lb5["bg"] = "%s"%(l)
        lb6["bg"] = "%s"%(y)
        lb7["bg"] = "%s"%(y)
        lb8["bg"] = "%s"%(y)
        lb9["bg"] = "%s"%(y)

    quit = tkinter.messagebox.askokcancel('提示', '背景色不要使用深色')
    
    root_ys = tkinter.Tk()
    root_ys.title("调色盘")
    root_ys.geometry(ckdx(700,450))
    root_ys.iconbitmap(path_logo+"\\cclogo.ico")
    root_ys.wm_attributes('-alpha',int(cktm)/100)
    root_ys.configure(bg=ckbg)
    root_ys. attributes ("-topmost",True)
    root_ys.resizable(False,False)
    


    #显示区
    lb1 = tkinter.Label(root_ys, text = "",width = 10,height = 4,bg = "black")
    lb1.grid(row=1, column=4)

    lb2 = tkinter.Label(root_ys, text = "",width = 10,height = 4,bg = "black")
    lb2.grid(row=1, column=5)

    lb3 = tkinter.Label(root_ys, text = "",width = 10,height = 4,bg = "black")
    lb3.grid(row=1, column=6)

    lb4 = tkinter.Label(root_ys, text = "",width = 10,height = 4,bg = "black")
    lb4.grid(row=2, column=4)

    lb5 = tkinter.Label(root_ys, text = "",width = 10,height = 4,bg = "black")
    lb5.grid(row=2, column=5)           #中间

    lb6 = tkinter.Label(root_ys, text = "",width = 10,height = 4,bg = "black")
    lb6.grid(row=2, column=6)

    lb7 = tkinter.Label(root_ys, text = "",width = 10,height = 4,bg = "black")
    lb7.grid(row=3, column=4)

    lb8 = tkinter.Label(root_ys, text = "",width = 10,height = 4,bg = "black")
    lb8.grid(row=3, column=5)

    lb9 = tkinter.Label(root_ys, text = "",width = 10,height = 4,bg = "black")
    lb9.grid(row=3, column=6)
    #显示框
    lb11 = tkinter.Label(root_ys, text = "中间R",bg = ckbg,fg = ckfg)
    lb11.grid(row=1, column=1,padx=10, pady=10)

    lb12 = tkinter.Label(root_ys, text = "中间G",bg = ckbg,fg = ckfg)
    lb12.grid(row=2, column=1,padx=10, pady=10)

    lb13 = tkinter.Label(root_ys, text = "中间B",bg = ckbg,fg = ckfg)
    lb13.grid(row=3, column=1,padx=10, pady=10)

    lb14 = tkinter.Label(root_ys, text = "外面R",bg = ckbg,fg = ckfg)
    lb14.grid(row=1, column=7,padx=10, pady=10)

    lb15 = tkinter.Label(root_ys, text = "外面G",bg = ckbg,fg = ckfg)
    lb15.grid(row=2, column=7,padx=10, pady=10)

    lb16 = tkinter.Label(root_ys, text = "外面B",bg = ckbg,fg = ckfg)
    lb16.grid(row=3, column=7,padx=10, pady=10)

    lb21 = tkinter.Label(root_ys, text = "：",bg = ckbg,fg = ckfg)
    lb21.grid(row=1, column=2,padx=10, pady=10)

    lb22 = tkinter.Label(root_ys, text = "：",bg = ckbg,fg = ckfg)
    lb22.grid(row=2, column=2,padx=10, pady=10)

    lb23 = tkinter.Label(root_ys, text = "：",bg = ckbg,fg = ckfg)
    lb23.grid(row=3, column=2,padx=10, pady=10)

    lb24 = tkinter.Label(root_ys, text = "：",bg = ckbg,fg = ckfg)
    lb24.grid(row=1, column=8,padx=10, pady=10)

    lb25 = tkinter.Label(root_ys, text = "：",bg = ckbg,fg = ckfg)
    lb25.grid(row=2, column=8,padx=10, pady=10)

    lb26 = tkinter.Label(root_ys, text = "：",bg = ckbg,fg = ckfg)
    lb26.grid(row=3, column=8,padx=10, pady=10)

    lb31 = tkinter.Label(root_ys, text = "0",bg = ckbg,fg = ckfg)
    lb31.grid(row=1, column=3,padx=10, pady=10)

    lb32 = tkinter.Label(root_ys, text = "0",bg = ckbg,fg = ckfg)
    lb32.grid(row=2, column=3,padx=10, pady=10)

    lb33 = tkinter.Label(root_ys, text = "0",bg = ckbg,fg = ckfg)
    lb33.grid(row=3, column=3,padx=10, pady=10)

    lb34 = tkinter.Label(root_ys, text = "0",bg = ckbg,fg = ckfg)
    lb34.grid(row=1, column=9,padx=10, pady=10)

    lb35 = tkinter.Label(root_ys, text = "0",bg = ckbg,fg = ckfg)
    lb35.grid(row=2, column=9,padx=10, pady=10)

    lb36 = tkinter.Label(root_ys, text = "0",bg = ckbg,fg = ckfg)
    lb36.grid(row=3, column=9,padx=10, pady=10)

    lb37 = tkinter.Label(root_ys, text = "#000000",bg = ckbg,fg = ckfg)
    lb37.grid(row=0, column=9,padx=10, pady=10)

    lb38 = tkinter.Label(root_ys, text = "#000000",bg = ckbg,fg = ckfg)
    lb38.grid(row=0, column=3,padx=10, pady=10)

    #标签
    lb40 = tkinter.Label(root_ys, text = "中间R",bg = ckbg,fg = ckfg)
    lb40.grid(row=4, column=1,padx=10, pady=10)

    lb41 = tkinter.Label(root_ys, text = "中间G",bg = ckbg,fg = ckfg)
    lb41.grid(row=4, column=2,padx=10, pady=10)

    lb42 = tkinter.Label(root_ys, text = "中间B",bg = ckbg,fg = ckfg)
    lb42.grid(row=4, column=3,padx=10, pady=10)

    lb43 = tkinter.Label(root_ys, text = "外面R",bg = ckbg,fg = ckfg)
    lb43.grid(row=4, column=7,padx=10, pady=10)

    lb44 = tkinter.Label(root_ys, text = "外面G",bg = ckbg,fg = ckfg)
    lb44.grid(row=4, column=8,padx=10, pady=10)

    lb45 = tkinter.Label(root_ys, text = "外面B",bg = ckbg,fg = ckfg)
    lb45.grid(row=4, column=9,padx=10, pady=10)

    lb46 = tkinter.Label(root_ys, text = "中间16进制",bg = ckbg,fg = ckfg)
    lb46.grid(row=0, column=1,padx=10, pady=10)

    lb47 = tkinter.Label(root_ys, text = "外面16进制",bg = ckbg,fg = ckfg)
    lb47.grid(row=0, column=7,padx=10, pady=10)

    lb48 = tkinter.Label(root_ys, text = "字体",bg = ckbg,fg = ckfg)
    lb48.grid(row=0, column=4,padx=10, pady=10)

    lb49 = tkinter.Label(root_ys, text = "：",bg = ckbg,fg = ckfg)
    lb49.grid(row=0, column=2,padx=10, pady=10)

    lb50 = tkinter.Label(root_ys, text = "：",bg = ckbg,fg = ckfg)
    lb50.grid(row=0, column=8,padx=10, pady=10)
    #拉条区
    sca1 = tkinter.Scale(root_ys, from_=255, to=0,command=tsp,bg = ckbg,fg = ckfg)
    sca1.grid(row=5, column=1,padx=10, pady=10)

    sca2 = tkinter.Scale(root_ys, from_=255, to=0,command=tsp,bg = ckbg,fg = ckfg)
    sca2.grid(row=5, column=2,padx=10, pady=10)

    sca3 = tkinter.Scale(root_ys, from_=255, to=0,command=tsp,bg = ckbg,fg = ckfg)
    sca3.grid(row=5, column=3,padx=10, pady=10)

    sca4 = tkinter.Scale(root_ys, from_=255, to=0,command=tsp,bg = ckbg,fg = ckfg)
    sca4.grid(row=5, column=7,padx=10, pady=10)

    sca5 = tkinter.Scale(root_ys, from_=255, to=0,command=tsp,bg = ckbg,fg = ckfg)
    sca5.grid(row=5, column=8,padx=10, pady=10)

    sca6 = tkinter.Scale(root_ys, from_=255, to=0,command=tsp,bg = ckbg,fg = ckfg)
    sca6.grid(row=5, column=9,padx=10, pady=10)



    #皮肤
    com = tkinter.ttk.Combobox(root_ys, width=7)
    com["value"] = ("red","blue", "yellow", "orange", "black","green","pink","purple","white","gray","brown","silver","gold","teal","khaki","chocolate","cyan","maroon","navy","coral","azure","bisque","salmon","wheat",)
    com.current(4)
    com["state"]="readonly" #状态为只读
    com.grid(row=0, column=5)

    btn = tkinter.Button(root_ys, text="确定",bg=ckbg,fg = ckfg,command=zt)
    btn.bind("<Enter>", t)
    btn.bind("<Leave>", fh)
    btn.grid(row=0, column=6,padx=10, pady=10)
    
    

    root_ys.mainloop()
    
    

def tpbc():
    global number
    
    ptpbc = tkinter.filedialog.askdirectory()
    if ptpbc == "":
        return 0
    
    if number == "A":
        img_1 = Image.new("RGB", (100, 100), A1)
        img_2 = Image.new("RGB", (100, 100), A2)
        img_3 = Image.new("RGB", (100, 100), A3)
        
    if number == "B":
        img_1 = Image.new("RGB", (100, 100), B1)
        img_2 = Image.new("RGB", (100, 100), B2)
        img_3 = Image.new("RGB", (100, 100), B3)
        
    if number == "C":
        img_1 = Image.new("RGB", (100, 100), C1)
        img_2 = Image.new("RGB", (100, 100), C2)
        img_3 = Image.new("RGB", (100, 100), C3)
        
    if number == "D":
        img_1 = Image.new("RGB", (100, 100), D1)
        img_2 = Image.new("RGB", (100, 100), D2)
        img_3 = Image.new("RGB", (100, 100), D3)
    
    img_1.save(path_Temporary+"\\1.png")
    img_2.save(path_Temporary+"\\2.png")
    img_3.save(path_Temporary+"\\3.png")
    
    p=0
    if int('0x' + ckfg[1:3],16) >= 128:
        p = 1
    if int('0x' + ckfg[3:5],16) >= 128:
        p = 1
    if int('0x' + ckfg[5:7],16) >= 128:
        p = 1
        
    if p == 1:
        bg=Image.open(path_logo + "\\pf2.png")
    else :
        bg=Image.open(path_logo + "\\pf1.png")
        
    
    if number == "A":#国字布局
        tp1_1 =Image.open(path_Temporary+ "\\1.png")
        tp2_1 =Image.open(path_Temporary+ "\\2.png")
        tp3_1 =Image.open(path_Temporary+ "\\3.png")

        tp2_2 = tp2_1.resize((2000,1500))
        bg.paste(tp2_2, (241,255))

        tp3_2 = tp3_1.resize((400,1500))
        bg.paste(tp3_2, (241,255))
        bg.paste(tp3_2, (1841,255))

        tp1_2 = tp1_1.resize((2000,200))
        bg.paste(tp1_2, (241,255))
        bg.paste(tp1_2, (241,1555))

        draw = ImageDraw.Draw(bg)
        ttfront = ImageFont.truetype("simhei.ttf",200)
        draw.text((841,10),"国字布局",fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((741,2000),"页头/脚条:",fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((941,2150),"RGB:"+color16_rgb(A1),fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((941,2300),"16进制:"+A1,fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((741,2500),"左/右侧:",fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((941,2650),"RGB:"+color16_rgb(A3),fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((941,2800),"16进制:"+A3,fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((741,3000),"内容:",fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((941,3150),"RGB:"+color16_rgb(A2),fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((941,3300),"16进制:"+A2,fill = ckfg,font = ttfront)
    
    if number == "B":#三字布局
        tp1_1 =Image.open(path_Temporary+ "\\1.png")
        tp2_1 =Image.open(path_Temporary+ "\\2.png")
        tp3_1 =Image.open(path_Temporary+ "\\3.png")

        tp2_2 = tp2_1.resize((2000,1500))
        bg.paste(tp2_2, (241,255))

        tp3_2 = tp3_1.resize((2000,200))
        bg.paste(tp3_2, (241,1555))


        tp1_2 = tp1_1.resize((2000,200))
        bg.paste(tp1_2, (241,255))

        draw = ImageDraw.Draw(bg)
        ttfront = ImageFont.truetype("simhei.ttf",200)
        draw.text((841,10),"三字布局",fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((741,2000),"页头条:",fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((941,2150),"RGB:"+color16_rgb(B1),fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((941,2300),"16进制:"+B1,fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((741,2500),"页脚条:",fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((941,2650),"RGB:"+color16_rgb(B3),fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((941,2800),"16进制:"+B3,fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((741,3000),"内容:",fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((941,3150),"RGB:"+color16_rgb(B2),fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((941,3300),"16进制:"+B2,fill = ckfg,font = ttfront)

    if number == "C":#综合布局
        tp1_1 =Image.open(path_Temporary+ "\\1.png")
        tp2_1 =Image.open(path_Temporary+ "\\2.png")
        tp3_1 =Image.open(path_Temporary+ "\\3.png")

        tp2_2 = tp2_1.resize((2000,1500))
        bg.paste(tp2_2, (241,255))

        tp3_2 = tp3_1.resize((1000,1500))
        bg.paste(tp3_2, (241,255))

        tp1_2 = tp1_1.resize((2000,400))
        bg.paste(tp1_2, (241,255))

        draw = ImageDraw.Draw(bg)
        ttfront = ImageFont.truetype("simhei.ttf",200)
        draw.text((841,10),"综合布局",fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((741,2000),"页头条:",fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((941,2150),"RGB:"+color16_rgb(C1),fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((941,2300),"16进制:"+C1,fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((741,2500),"左侧:",fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((941,2650),"RGB:"+color16_rgb(C3),fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((941,2800),"16进制:"+C3,fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((741,3000),"右侧:",fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((941,3150),"RGB:"+color16_rgb(C2),fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((941,3300),"16进制:"+C2,fill = ckfg,font = ttfront)
    
    if number == "D":#丁字布局
        tp1_1 =Image.open(path_Temporary+ "\\1.png")
        tp2_1 =Image.open(path_Temporary+ "\\2.png")
        tp3_1 =Image.open(path_Temporary+ "\\3.png")

        tp2_2 = tp2_1.resize((2000,1500))
        bg.paste(tp2_2, (241,255))

        tp3_2 = tp3_1.resize((400,1500))
        bg.paste(tp3_2, (241,255))

        tp1_2 = tp1_1.resize((2000,200))
        bg.paste(tp1_2, (241,255))




        draw = ImageDraw.Draw(bg)
        ttfront = ImageFont.truetype("simhei.ttf",200)
        draw.text((841,10),"丁字布局",fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((741,2000),"页头条:",fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((941,2150),"RGB:"+color16_rgb(D1),fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((941,2300),"16进制:"+D1,fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((741,2500),"左侧:",fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((941,2650),"RGB:"+color16_rgb(D3),fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((941,2800),"16进制:"+D3,fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((741,3000),"内容:",fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((941,3150),"RGB:"+color16_rgb(D2),fill = ckfg,font = ttfront)

        ttfront = ImageFont.truetype("simhei.ttf",100)
        draw.text((941,3300),"16进制:"+D2,fill = ckfg,font = ttfront)

    bg.save(ptpbc+"\\ Color adjustment.png")
    ans = tkinter.messagebox.askyesno("提示", "保存成功")
    
    
def hqwy():
    global pA1
    pA1 = ckfg
    global pA2
    pA2 = ckfg
    global pA3
    pA3 = ckfg
    global pA4
    pA4 = ckfg
    global pA5
    pA5 = ckfg
    global pA6
    pA6 = ckfg
    global pA7
    pA7 = ckfg
    global pA8
    pA8 = ckfg

    def hqqd():
        global pA1
        global pA2
        global pA3
        global pA4
        global pA5
        global pA6
        global pA7
        global pA8
        wbk = E1.get()
        
        path_wkimg = path_wkhtmltopdf+'\\bin\\wkhtmltoimage.exe'  # 工具路径
        cfg = imgkit.config(wkhtmltoimage=path_wkimg)

        try:
            imgkit.from_url(wbk, path_Temporary+'\\ip.jpg', config=cfg)
        except Exception:
            ans = tkinter.messagebox.showerror('错误','发生了一些错误，请使用截图')
            root_hq.destroy()
            return 0
        
        def get_dominant_colors(infile):
            image = Image.open(infile)
            
            # 缩小图片，否则计算机压力太大
            small_image = image.resize((80, 80))
            result = small_image.convert(
                "P", palette=Image.ADAPTIVE, colors=10
            )  

            # 找到主要的颜色
            palette = result.getpalette()
            color_counts = sorted(result.getcolors(), reverse=True)
            colors = list()

            for i in range(8):
                palette_index = color_counts[i][1]
                dominant_color = palette[palette_index * 3 : palette_index * 3 + 3]
                colors.append(tuple(dominant_color))

            # print(colors)
            return colors

        image_path = path_Temporary+"\\ip.jpg"
        color = get_dominant_colors(image_path)
                
        pA1 = rgb_color16(color[0][0],color[0][1],color[0][2])
        pA2 = rgb_color16(color[1][0],color[1][1],color[1][2])
        pA3 = rgb_color16(color[2][0],color[2][1],color[2][2])
        pA4 = rgb_color16(color[3][0],color[3][1],color[3][2])
        pA5 = rgb_color16(color[4][0],color[4][1],color[4][2])
        pA6 = rgb_color16(color[5][0],color[5][1],color[5][2])
        pA7 = rgb_color16(color[6][0],color[6][1],color[6][2])
        pA8 = rgb_color16(color[7][0],color[7][1],color[7][2])
        
        lb_pA1 ["bg"] = pA1
        lb_pA2 ["bg"] = pA2
        lb_pA3 ["bg"] = pA3
        lb_pA4 ["bg"] = pA4
        lb_pA5 ["bg"] = pA5
        lb_pA6 ["bg"] = pA6
        lb_pA7 ["bg"] = pA7
        lb_pA8 ["bg"] = pA8




    def A1(event):
        global pA1
        lb_t ["bg"] = pA1
        lb_t_rbg16 ["text"] = "RBG:"+color16_rgb(pA1)+"\n \n16进制:"+pA1

    def A2(event):
        global pA2
        lb_t ["bg"] = pA2
        lb_t_rbg16 ["text"] = "RBG:"+color16_rgb(pA2)+"\n \n16进制:"+pA2

    def A3(event):
        global pA3
        lb_t ["bg"] = pA3
        lb_t_rbg16 ["text"] = "RBG:"+color16_rgb(pA3)+"\n \n16进制:"+pA3
        
    def A4(event):
        global pA4
        lb_t ["bg"] = pA4
        lb_t_rbg16 ["text"] = "RBG:"+color16_rgb(pA4)+"\n \n16进制:"+pA4
        
    def A5(event):
        global pA5
        lb_t ["bg"] = pA5
        lb_t_rbg16 ["text"] = "RBG:"+color16_rgb(pA5)+"\n \n16进制:"+pA5
        
    def A6(event):
        global pA6
        lb_t ["bg"] = pA6
        lb_t_rbg16 ["text"] = "RBG:"+color16_rgb(pA6)+"\n \n16进制:"+pA6
        
    def A7(event):
        global pA7
        lb_t ["bg"] = pA7
        lb_t_rbg16 ["text"] = "RBG:"+color16_rgb(pA7)+"\n \n16进制:"+pA7
        
    def A8(event):
        global pA8
        lb_t ["bg"] = pA8
        lb_t_rbg16 ["text"] = "RBG:"+color16_rgb(pA8)+"\n \n16进制:"+pA8

    def h(event):
        lb_t ["bg"] = ckfg
        lb_t_rbg16 ["text"] = "RBG:\n \n16进制:"


    def bs(event):
        btn["bg"] = ckfg
        btn["fg"] = ckbg

    def hh(event):
        btn["bg"] = ckbg
        btn["fg"] = ckfg

    root_hq = tkinter.Tk()
    root_hq.title("网页颜色")
    root_hq.geometry(ckdx(1209,687))
    root_hq.iconbitmap(path_logo+"\\logo.ico")
    root_hq.wm_attributes('-alpha',int(cktm)/100)
    root_hq.resizable(False,False)
    root_hq.configure(bg=ckbg)

    E1 = tkinter.Entry(root_hq, bd =5,width = 75,bg=ckbg,fg=ckfg)
    E1.grid(row=1, column=1,padx=20, pady=20)

    btn = tkinter.Button(root_hq, text="确定",bg=ckbg,fg=ckfg,font=('楷体', 18),command=hqqd)
    btn.bind("<Enter>", bs)
    btn.bind("<Leave>", hh)
    btn.grid(row=1, column=2)

    lb_tm = Label(root_hq, text="*必须使用http或https开头",bg=ckbg,fg=ckfg,font=('楷体', 10),)
    lb_tm.grid(row=2, column=1,)

    lb_pA = tkinter.Label(root_hq, text = "↖左上角为出现\n次数最多的顺时\n针依次减少",width = 20,height = 8,bg = ckbg,fg = ckfg,font=('楷体', 12))
    lb_pA.bind("<Enter>", h)
    lb_pA.grid(row=5, column=4)

    lb_pA1 = tkinter.Label(root_hq, text = "",width = 25,height = 10,bg = pA1)
    lb_pA1.bind("<Enter>", A1)
    lb_pA1.grid(row=4, column=3)

    lb_pA2 = tkinter.Label(root_hq, text = "",width = 25,height = 10,bg = pA2)
    lb_pA2.bind("<Enter>", A2)
    lb_pA2.grid(row=4, column=4)

    lb_pA3 = tkinter.Label(root_hq, text = "",width = 25,height = 10,bg = pA3)
    lb_pA3.bind("<Enter>", A3)
    lb_pA3.grid(row=4, column=5)

    lb_pA4 = tkinter.Label(root_hq, text = "",width = 25,height = 10,bg = pA4)
    lb_pA4.bind("<Enter>", A4)
    lb_pA4.grid(row=5, column=5)

    lb_pA5 = tkinter.Label(root_hq, text = "",width = 25,height = 10,bg = pA5)
    lb_pA5.bind("<Enter>", A5)
    lb_pA5.grid(row=6, column=5)

    lb_pA6 = tkinter.Label(root_hq, text = "",width = 25,height = 10,bg = pA6)
    lb_pA6.bind("<Enter>", A6)
    lb_pA6.grid(row=6, column=4)

    lb_pA7 = tkinter.Label(root_hq, text = "",width = 25,height = 10,bg = pA7)
    lb_pA7.bind("<Enter>", A7)
    lb_pA7.grid(row=6, column=3)

    lb_pA8 = tkinter.Label(root_hq, text = "",width = 25,height = 10,bg = pA7)
    lb_pA8.bind("<Enter>", A8)
    lb_pA8.grid(row=5, column=3)

    #调色显示
    lb_t = tkinter.Label(root_hq, text = "",width = 50,height = 5,bg = pA1)
    lb_t.grid(row=4, column=1)

    lb_t_rbg16 = tkinter.Label(root_hq, text = "RBG:\n \n16进制:",bg = ckbg,fg = ckfg,font=('楷体', 30))
    lb_t_rbg16.grid(row=5, column=1)

#截图网页
def jtwy():
    global pB1
    pB1 = ckfg
    global pB2
    pB2 = ckfg
    global pB3
    pB3 = ckfg
    global pB4
    pB4 = ckfg
    global pB5
    pB5 = ckfg
    global pB6
    pB6 = ckfg
    global pB7
    pB7 = ckfg
    global pB8
    pB8 = ckfg
    global hqptp

    def hqqd():
        global hqptp
        global pB1
        global pB2
        global pB3
        global pB4
        global pB5
        global pB6
        global pB7
        global pB8
        
        try:
            f = open(hqptp, 'rb')  # rb 以二进制读取
            data = f.read()  # 先把图片读出来
            f1 = open(path_Temporary+'\\ip.jpg', 'wb')  # 创建一个新的文件

            f1.write(data)  # 写入a.jpg

            f.close()
            f1.close()
        except Exception:
            ans = tkinter.messagebox.showerror('错误','发生了一些错误')
            root_hq.destroy()
            return 0
        
        
        
        def get_dominant_colors(infile):
            image = Image.open(infile)
            
            # 缩小图片，否则计算机压力太大
            small_image = image.resize((80, 80))
            result = small_image.convert(
                "P", palette=Image.ADAPTIVE, colors=10
            )  

            # 找到主要的颜色
            palette = result.getpalette()
            color_counts = sorted(result.getcolors(), reverse=True)
            colors = list()

            for i in range(8):
                palette_index = color_counts[i][1]
                dominant_color = palette[palette_index * 3 : palette_index * 3 + 3]
                colors.append(tuple(dominant_color))

            # print(colors)
            return colors

        image_path = hqptp
        color = get_dominant_colors(image_path)
                
        pB1 = rgb_color16(color[0][0],color[0][1],color[0][2])
        pB2 = rgb_color16(color[1][0],color[1][1],color[1][2])
        pB3 = rgb_color16(color[2][0],color[2][1],color[2][2])
        pB4 = rgb_color16(color[3][0],color[3][1],color[3][2])
        pB5 = rgb_color16(color[4][0],color[4][1],color[4][2])
        pB6 = rgb_color16(color[5][0],color[5][1],color[5][2])
        pB7 = rgb_color16(color[6][0],color[6][1],color[6][2])
        pB8 = rgb_color16(color[7][0],color[7][1],color[7][2])
        
        lb_pB1 ["bg"] = pB1
        lb_pB2 ["bg"] = pB2
        lb_pB3 ["bg"] = pB3
        lb_pB4 ["bg"] = pB4
        lb_pB5 ["bg"] = pB5
        lb_pB6 ["bg"] = pB6
        lb_pB7 ["bg"] = pB7
        lb_pB8 ["bg"] = pB8
        
        
    def xzlj():
        global hqptp
        hqptp = tkinter.filedialog.askopenfilename()
        print(hqptp)
        lb_lj ["text"] = hqptp
        



    def B1(event):
        global pB1
        lb_t ["bg"] = pB1
        lb_t_rbg16 ["text"] = "RBG:"+color16_rgb(pB1)+"\n \n16进制:"+pB1

    def B2(event):
        global pB2
        lb_t ["bg"] = pB2
        lb_t_rbg16 ["text"] = "RBG:"+color16_rgb(pB2)+"\n \n16进制:"+pB2

    def B3(event):
        global pB3
        lb_t ["bg"] = pB3
        lb_t_rbg16 ["text"] = "RBG:"+color16_rgb(pB3)+"\n \n16进制:"+pB3
        
    def B4(event):
        global pB4
        lb_t ["bg"] = pB4
        lb_t_rbg16 ["text"] = "RBG:"+color16_rgb(pB4)+"\n \n16进制:"+pB4
        
    def B5(event):
        global pB5
        lb_t ["bg"] = pB5
        lb_t_rbg16 ["text"] = "RBG:"+color16_rgb(pB5)+"\n \n16进制:"+pB5
        
    def B6(event):
        global pB6
        lb_t ["bg"] = pB6
        lb_t_rbg16 ["text"] = "RBG:"+color16_rgb(pB6)+"\n \n16进制:"+pB6
        
    def B7(event):
        global pB7
        lb_t ["bg"] = pB7
        lb_t_rbg16 ["text"] = "RBG:"+color16_rgb(pB7)+"\n \n16进制:"+pB7
        
    def B8(event):
        global pB8
        lb_t ["bg"] = pB8
        lb_t_rbg16 ["text"] = "RBG:"+color16_rgb(pB8)+"\n \n16进制:"+pB8

    def h(event):
        lb_t ["bg"] = ckfg
        lb_t_rbg16 ["text"] = "RBG:\n \n16进制:"

    def xz(event):
        btn_xz["bg"] = ckfg
        btn_xz["fg"] = ckbg

    def bs(event):
        btn["bg"] = ckfg
        btn["fg"] = ckbg

    def hh(event):
        btn["bg"] = ckbg
        btn["fg"] = ckfg
        btn_xz["bg"] = ckbg
        btn_xz["fg"] = ckfg

    root_hq = tkinter.Tk()
    root_hq.title("网页颜色")
    root_hq.geometry(ckdx(1209,687))
    root_hq.iconbitmap(path_logo+"\\logo.ico")
    root_hq.wm_attributes('-alpha',int(cktm)/100)
    root_hq.resizable(False,False)
    root_hq.configure(bg=ckbg)

    lb_lj = Label(root_hq, text="",bd =5,width = 75,bg=ckbg,fg=ckfg,font=('楷体', 10),)
    lb_lj.grid(row=1, column=1,)

    btn = tkinter.Button(root_hq, text="确定",bg=ckbg,fg=ckfg,font=('楷体', 18),command=hqqd)
    btn.bind("<Enter>", bs)
    btn.bind("<Leave>", hh)
    btn.grid(row=1, column=2, padx=5, pady=5)

    btn_xz = tkinter.Button(root_hq, text="选择文件",bg=ckbg,fg=ckfg,font=('楷体', 18),command=xzlj)
    btn_xz.bind("<Enter>", xz)
    btn_xz.bind("<Leave>", hh)
    btn_xz.grid(row=1, column=3, padx=5, pady=5)

    lb_tm = Label(root_hq, text="*必须使用png或jpg图片,截图不要截到浏览器",bg=ckbg,fg=ckfg,font=('楷体', 10),)
    lb_tm.grid(row=2, column=1,)

    lb_pB = tkinter.Label(root_hq, text = "↖左上角为出现\n次数最多的顺时\n针依次减少",width = 20,height = 8,bg = ckbg,fg = ckfg,font=('楷体', 12))
    lb_pB.bind("<Enter>", h)
    lb_pB.grid(row=5, column=4)

    lb_pB1 = tkinter.Label(root_hq, text = "",width = 25,height = 10,bg = pB1)
    lb_pB1.bind("<Enter>", B1)
    lb_pB1.grid(row=4, column=3)

    lb_pB2 = tkinter.Label(root_hq, text = "",width = 25,height = 10,bg = pB2)
    lb_pB2.bind("<Enter>", B2)
    lb_pB2.grid(row=4, column=4)

    lb_pB3 = tkinter.Label(root_hq, text = "",width = 25,height = 10,bg = pB3)
    lb_pB3.bind("<Enter>", B3)
    lb_pB3.grid(row=4, column=5)

    lb_pB4 = tkinter.Label(root_hq, text = "",width = 25,height = 10,bg = pB4)
    lb_pB4.bind("<Enter>", B4)
    lb_pB4.grid(row=5, column=5)

    lb_pB5 = tkinter.Label(root_hq, text = "",width = 25,height = 10,bg = pB5)
    lb_pB5.bind("<Enter>", B5)
    lb_pB5.grid(row=6, column=5)

    lb_pB6 = tkinter.Label(root_hq, text = "",width = 25,height = 10,bg = pB6)
    lb_pB6.bind("<Enter>", B6)
    lb_pB6.grid(row=6, column=4)

    lb_pB7 = tkinter.Label(root_hq, text = "",width = 25,height = 10,bg = pB7)
    lb_pB7.bind("<Enter>", B7)
    lb_pB7.grid(row=6, column=3)

    lb_pB8 = tkinter.Label(root_hq, text = "",width = 25,height = 10,bg = pB7)
    lb_pB8.bind("<Enter>", B8)
    lb_pB8.grid(row=5, column=3)

    #调色显示
    lb_t = tkinter.Label(root_hq, text = "",width = 50,height = 5,bg = pB1)
    lb_t.grid(row=4, column=1)

    lb_t_rbg16 = tkinter.Label(root_hq, text = "RBG:\n \n16进制:",bg = ckbg,fg = ckfg,font=('楷体', 30))
    lb_t_rbg16.grid(row=5, column=1)
    
def wjbcfh():
    if number == "A":#国字布局
        na = "国字布局"
        jq_1 = "页头/脚条:"
        jq_2 = "内容:"
        jq_3 = "左/右侧:"
        fz_t1 = A1
        fz_t2 = A2
        fz_t3 = A3
        
    if number == "B":#三字布局
        na = "三字布局"
        jq_1 = "页头条:"
        jq_2 = "内容:"
        jq_3 = "页脚条:"
        fz_t1 = B1
        fz_t2 = B2
        fz_t3 = B3
        
    if number == "C":#综合布局
        na = "综合布局"
        jq_1 = "页头条:"
        jq_2 = "右侧:"
        jq_3 = "左侧:"
        fz_t1 = C1
        fz_t2 = C2
        fz_t3 = C3
        
    if number == "D":#丁字布局
        na = "丁字布局"
        jq_1 = "页头条:"
        jq_2 = "内容:"
        jq_3 = "左侧:"
        fz_t1 = D1
        fz_t2 = D2
        fz_t3 = D3
        
    return na+"\n"+jq_1+"\n"+"    16进制:"+fz_t1+"\n"+"    RGB:"+color16_rgb(fz_t1)+"\n"+jq_2+"\n"+"    16进制:"+fz_t2+"\n"+"    RGB:"+color16_rgb(fz_t2)+"\n"+jq_3+"\n"+"    16进制:"+fz_t3+"\n"+"    RGB:"+color16_rgb(fz_t3)

    

def fz():
            

    pyperclip.copy(wjbcfh())
    spam = pyperclip.paste()
    
    ans = tkinter.messagebox.showinfo('提示','复制成功')
    
def wbwd():
    
    ptpbc = tkinter.filedialog.askdirectory()
    if ptpbc == "":
        return 0
    
    f=open(ptpbc+"\\ Color adjustment.txt","w+")
    f.write(wjbcfh())
    
    ans = tkinter.messagebox.showinfo('提示','保存成功')


def ysz():
    global number
    global A1
    global B1
    global C1
    global A2
    global B2
    global C2
    global A3
    global B3
    global C3
    global A4
    global B4
    global C4
    
    if number == "A":
        lb_sy_16_fl ["text"] = A1
        lb_sy_16_rgb ["text"] = color16_rgb(A1)
        lb_nr_16_fl ["text"] = A2
        lb_nr_16_rgb ["text"] = color16_rgb(A2)
        lb_c_16_fl ["text"] = A3
        lb_c_16_rgb ["text"] = color16_rgb(A3)
        
    if number == "B":
        lb_sy_16_fl ["text"] = B1
        lb_sy_16_rgb ["text"] = color16_rgb(B1)
        lb_nr_16_fl ["text"] = B2
        lb_nr_16_rgb ["text"] = color16_rgb(B2)
        lb_c_16_fl ["text"] = B3
        lb_c_16_rgb ["text"] = color16_rgb(B3)
        
    if number == "C":
        lb_sy_16_fl ["text"] = C1
        lb_sy_16_rgb ["text"] = color16_rgb(C1)
        lb_nr_16_fl ["text"] = C2
        lb_nr_16_rgb ["text"] = color16_rgb(C2)
        lb_c_16_fl ["text"] = C3
        lb_c_16_rgb ["text"] = color16_rgb(C3)
        
    if number == "D":
        lb_sy_16_fl ["text"] = D1
        lb_sy_16_rgb ["text"] = color16_rgb(D1)
        lb_nr_16_fl ["text"] = D2
        lb_nr_16_rgb ["text"] = color16_rgb(D2)
        lb_c_16_fl ["text"] = D3
        lb_c_16_rgb ["text"] = color16_rgb(B3)
        
    print("调用显示刷新")

def ys():
    global number
    global A1
    global B1
    global C1
    global A2
    global B2
    global C2
    global A3
    global B3
    global C3
    global A4
    global B4
    global C4
    if number == "A":#国字布局
        root.title("国字布局")
        lb1_A1 ['bg'] = A1
        lb1_A2 ['bg'] = A1
        lb1_A3 ['bg'] = A1
        lb1_A4 ['bg'] = A1
        lb1_A5 ['bg'] = A1
        lb1_A6 ['bg'] = A1
        lb1_A7 ['bg'] = A1
        lb1_A8 ['bg'] = A1
        lb1_A9 ['bg'] = A1
        lb1_A10 ['bg'] = A1
        lb1_A11 ['bg'] = A1
        lb1_A12 ['bg'] = A1
        lb1_B1 ['bg'] = A3
        lb1_B2 ['bg'] = A3
        lb1_B3 ['bg'] = A2
        lb1_B4 ['bg'] = A2
        lb1_B5 ['bg'] = A2
        lb1_B6 ['bg'] = A2
        lb1_B7 ['bg'] = A2
        lb1_B8 ['bg'] = A2
        lb1_B9 ['bg'] = A2
        lb1_B10 ['bg'] = A2
        lb1_B11 ['bg'] = A3
        lb1_B12 ['bg'] = A3
        lb1_C1 ['bg'] = A3
        lb1_C2 ['bg'] = A3
        lb1_C3 ['bg'] = A2
        lb1_C4 ['bg'] = A2
        lb1_C5 ['bg'] = A2
        lb1_C6 ['bg'] = A2
        lb1_C7 ['bg'] = A2
        lb1_C8 ['bg'] = A2
        lb1_C9 ['bg'] = A2
        lb1_C10 ['bg'] = A2
        lb1_C11 ['bg'] = A3
        lb1_C12 ['bg'] = A3
        lb1_D1 ['bg'] = A3
        lb1_D2 ['bg'] = A3
        lb1_D3 ['bg'] = A2
        lb1_D4 ['bg'] = A2
        lb1_D5 ['bg'] = A2
        lb1_D6 ['bg'] = A2
        lb1_D7 ['bg'] = A2
        lb1_D8 ['bg'] = A2
        lb1_D9 ['bg'] = A2
        lb1_D10 ['bg'] = A2
        lb1_D11 ['bg'] = A3
        lb1_D12 ['bg'] = A3
        lb1_E1 ['bg'] = A3
        lb1_E2 ['bg'] = A3
        lb1_E3 ['bg'] = A2
        lb1_E4 ['bg'] = A2
        lb1_E5 ['bg'] = A2
        lb1_E6 ['bg'] = A2
        lb1_E7 ['bg'] = A2
        lb1_E8 ['bg'] = A2
        lb1_E9 ['bg'] = A2
        lb1_E10 ['bg'] = A2
        lb1_E11 ['bg'] = A3
        lb1_E12 ['bg'] = A3
        lb1_F1 ['bg'] = A3
        lb1_F2 ['bg'] = A3
        lb1_F3 ['bg'] = A2
        lb1_F4 ['bg'] = A2
        lb1_F5 ['bg'] = A2
        lb1_F6 ['bg'] = A2
        lb1_F7 ['bg'] = A2
        lb1_F8 ['bg'] = A2
        lb1_F9 ['bg'] = A2
        lb1_F10 ['bg'] = A2
        lb1_F11 ['bg'] = A3
        lb1_F12 ['bg'] = A3
        lb1_G1 ['bg'] = A3
        lb1_G2 ['bg'] = A3
        lb1_G3 ['bg'] = A2
        lb1_G4 ['bg'] = A2
        lb1_G5 ['bg'] = A2
        lb1_G6 ['bg'] = A2
        lb1_G7 ['bg'] = A2
        lb1_G8 ['bg'] = A2
        lb1_G9 ['bg'] = A2
        lb1_G10 ['bg'] = A2
        lb1_G11 ['bg'] = A3
        lb1_G12 ['bg'] = A3
        lb1_H1 ['bg'] = A3
        lb1_H2 ['bg'] = A3
        lb1_H3 ['bg'] = A2
        lb1_H4 ['bg'] = A2
        lb1_H5 ['bg'] = A2
        lb1_H6 ['bg'] = A2
        lb1_H7 ['bg'] = A2
        lb1_H8 ['bg'] = A2
        lb1_H9 ['bg'] = A2
        lb1_H10 ['bg'] = A2
        lb1_H11 ['bg'] = A3
        lb1_H12 ['bg'] = A3
        lb1_I1 ['bg'] = A1
        lb1_I2 ['bg'] = A1
        lb1_I3 ['bg'] = A1
        lb1_I4 ['bg'] = A1
        lb1_I5 ['bg'] = A1
        lb1_I6 ['bg'] = A1
        lb1_I7 ['bg'] = A1
        lb1_I8 ['bg'] = A1
        lb1_I9 ['bg'] = A1
        lb1_I10 ['bg'] = A1
        lb1_I11 ['bg'] = A1
        lb1_I12 ['bg'] = A1

    if number == "B":#三字布局
        root.title("三字布局")
        lb1_A1 ['bg'] = B1
        lb1_A2 ['bg'] = B1
        lb1_A3 ['bg'] = B1
        lb1_A4 ['bg'] = B1
        lb1_A5 ['bg'] = B1
        lb1_A6 ['bg'] = B1
        lb1_A7 ['bg'] = B1
        lb1_A8 ['bg'] = B1
        lb1_A9 ['bg'] = B1
        lb1_A10 ['bg'] = B1
        lb1_A11 ['bg'] = B1
        lb1_A12 ['bg'] = B1
        lb1_B1 ['bg'] = B2
        lb1_B2 ['bg'] = B2
        lb1_B3 ['bg'] = B2
        lb1_B4 ['bg'] = B2
        lb1_B5 ['bg'] = B2
        lb1_B6 ['bg'] = B2
        lb1_B7 ['bg'] = B2
        lb1_B8 ['bg'] = B2
        lb1_B9 ['bg'] = B2
        lb1_B10 ['bg'] = B2
        lb1_B11 ['bg'] = B2
        lb1_B12 ['bg'] = B2
        lb1_C1 ['bg'] = B2
        lb1_C2 ['bg'] = B2
        lb1_C3 ['bg'] = B2
        lb1_C4 ['bg'] = B2
        lb1_C5 ['bg'] = B2
        lb1_C6 ['bg'] = B2
        lb1_C7 ['bg'] = B2
        lb1_C8 ['bg'] = B2
        lb1_C9 ['bg'] = B2
        lb1_C10 ['bg'] = B2
        lb1_C11 ['bg'] = B2
        lb1_C12 ['bg'] = B2
        lb1_D1 ['bg'] = B2
        lb1_D2 ['bg'] = B2
        lb1_D3 ['bg'] = B2
        lb1_D4 ['bg'] = B2
        lb1_D5 ['bg'] = B2
        lb1_D6 ['bg'] = B2
        lb1_D7 ['bg'] = B2
        lb1_D8 ['bg'] = B2
        lb1_D9 ['bg'] = B2
        lb1_D10 ['bg'] = B2
        lb1_D11 ['bg'] = B2
        lb1_D12 ['bg'] = B2
        lb1_E1 ['bg'] = B2
        lb1_E2 ['bg'] = B2
        lb1_E3 ['bg'] = B2
        lb1_E4 ['bg'] = B2
        lb1_E5 ['bg'] = B2
        lb1_E6 ['bg'] = B2
        lb1_E7 ['bg'] = B2
        lb1_E8 ['bg'] = B2
        lb1_E9 ['bg'] = B2
        lb1_E10 ['bg'] = B2
        lb1_E11 ['bg'] = B2
        lb1_E12 ['bg'] = B2
        lb1_F1 ['bg'] = B2
        lb1_F2 ['bg'] = B2
        lb1_F3 ['bg'] = B2
        lb1_F4 ['bg'] = B2
        lb1_F5 ['bg'] = B2
        lb1_F6 ['bg'] = B2
        lb1_F7 ['bg'] = B2
        lb1_F8 ['bg'] = B2
        lb1_F9 ['bg'] = B2
        lb1_F10 ['bg'] = B2
        lb1_F11 ['bg'] = B2
        lb1_F12 ['bg'] = B2
        lb1_G1 ['bg'] = B2
        lb1_G2 ['bg'] = B2
        lb1_G3 ['bg'] = B2
        lb1_G4 ['bg'] = B2
        lb1_G5 ['bg'] = B2
        lb1_G6 ['bg'] = B2
        lb1_G7 ['bg'] = B2
        lb1_G8 ['bg'] = B2
        lb1_G9 ['bg'] = B2
        lb1_G10 ['bg'] = B2
        lb1_G11 ['bg'] = B2
        lb1_G12 ['bg'] = B2
        lb1_H1 ['bg'] = B2
        lb1_H2 ['bg'] = B2
        lb1_H3 ['bg'] = B2
        lb1_H4 ['bg'] = B2
        lb1_H5 ['bg'] = B2
        lb1_H6 ['bg'] = B2
        lb1_H7 ['bg'] = B2
        lb1_H8 ['bg'] = B2
        lb1_H9 ['bg'] = B2
        lb1_H10 ['bg'] = B2
        lb1_H11 ['bg'] = B2
        lb1_H12 ['bg'] = B2
        lb1_I1 ['bg'] = B3
        lb1_I2 ['bg'] = B3
        lb1_I3 ['bg'] = B3
        lb1_I4 ['bg'] = B3
        lb1_I5 ['bg'] = B3
        lb1_I6 ['bg'] = B3
        lb1_I7 ['bg'] = B3
        lb1_I8 ['bg'] = B3
        lb1_I9 ['bg'] = B3
        lb1_I10 ['bg'] = B3
        lb1_I11 ['bg'] = B3
        lb1_I12 ['bg'] = B3


    if number == "C":#综合布局
        root.title("综合布局")
        lb1_A1 ['bg'] = C1
        lb1_A2 ['bg'] = C1
        lb1_A3 ['bg'] = C1
        lb1_A4 ['bg'] = C1
        lb1_A5 ['bg'] = C1
        lb1_A6 ['bg'] = C1
        lb1_A7 ['bg'] = C1
        lb1_A8 ['bg'] = C1
        lb1_A9 ['bg'] = C1
        lb1_A10 ['bg'] = C1
        lb1_A11 ['bg'] = C1
        lb1_A12 ['bg'] = C1
        lb1_B1 ['bg'] = C1
        lb1_B2 ['bg'] = C1
        lb1_B3 ['bg'] = C1
        lb1_B4 ['bg'] = C1
        lb1_B5 ['bg'] = C1
        lb1_B6 ['bg'] = C1
        lb1_B7 ['bg'] = C1
        lb1_B8 ['bg'] = C1
        lb1_B9 ['bg'] = C1
        lb1_B10 ['bg'] = C1
        lb1_B11 ['bg'] = C1
        lb1_B12 ['bg'] = C1
        lb1_C1 ['bg'] = C3
        lb1_C2 ['bg'] = C3
        lb1_C3 ['bg'] = C3
        lb1_C4 ['bg'] = C3
        lb1_C5 ['bg'] = C3
        lb1_C6 ['bg'] = C3
        lb1_C7 ['bg'] = C2
        lb1_C8 ['bg'] = C2
        lb1_C9 ['bg'] = C2
        lb1_C10 ['bg'] = C2
        lb1_C11 ['bg'] = C2
        lb1_C12 ['bg'] = C2
        lb1_D1 ['bg'] = C3
        lb1_D2 ['bg'] = C3
        lb1_D3 ['bg'] = C3
        lb1_D4 ['bg'] = C3
        lb1_D5 ['bg'] = C3
        lb1_D6 ['bg'] = C3
        lb1_D7 ['bg'] = C2
        lb1_D8 ['bg'] = C2
        lb1_D9 ['bg'] = C2
        lb1_D10 ['bg'] = C2
        lb1_D11 ['bg'] = C2
        lb1_D12 ['bg'] = C2
        lb1_E1 ['bg'] = C3
        lb1_E2 ['bg'] = C3
        lb1_E3 ['bg'] = C3
        lb1_E4 ['bg'] = C3
        lb1_E5 ['bg'] = C3
        lb1_E6 ['bg'] = C3
        lb1_E7 ['bg'] = C2
        lb1_E8 ['bg'] = C2
        lb1_E9 ['bg'] = C2
        lb1_E10 ['bg'] = C2
        lb1_E11 ['bg'] = C2
        lb1_E12 ['bg'] = C2
        lb1_F1 ['bg'] = C3
        lb1_F2 ['bg'] = C3
        lb1_F3 ['bg'] = C3
        lb1_F4 ['bg'] = C3
        lb1_F5 ['bg'] = C3
        lb1_F6 ['bg'] = C3
        lb1_F7 ['bg'] = C2
        lb1_F8 ['bg'] = C2
        lb1_F9 ['bg'] = C2
        lb1_F10 ['bg'] = C2
        lb1_F11 ['bg'] = C2
        lb1_F12 ['bg'] = C2
        lb1_G1 ['bg'] = C3
        lb1_G2 ['bg'] = C3
        lb1_G3 ['bg'] = C3
        lb1_G4 ['bg'] = C3
        lb1_G5 ['bg'] = C3
        lb1_G6 ['bg'] = C3
        lb1_G7 ['bg'] = C2
        lb1_G8 ['bg'] = C2
        lb1_G9 ['bg'] = C2
        lb1_G10 ['bg'] = C2
        lb1_G11 ['bg'] = C2
        lb1_G12 ['bg'] = C2
        lb1_H1 ['bg'] = C3
        lb1_H2 ['bg'] = C3
        lb1_H3 ['bg'] = C3
        lb1_H4 ['bg'] = C3
        lb1_H5 ['bg'] = C3
        lb1_H6 ['bg'] = C3
        lb1_H7 ['bg'] = C2
        lb1_H8 ['bg'] = C2
        lb1_H9 ['bg'] = C2
        lb1_H10 ['bg'] = C2
        lb1_H11 ['bg'] = C2
        lb1_H12 ['bg'] = C2
        lb1_I1 ['bg'] = C3
        lb1_I2 ['bg'] = C3
        lb1_I3 ['bg'] = C3
        lb1_I4 ['bg'] = C3
        lb1_I5 ['bg'] = C3
        lb1_I6 ['bg'] = C3
        lb1_I7 ['bg'] = C2
        lb1_I8 ['bg'] = C2
        lb1_I9 ['bg'] = C2
        lb1_I10 ['bg'] = C2
        lb1_I11 ['bg'] = C2
        lb1_I12 ['bg'] = C2
        print("颜色刷新")

    if number == "D":#丁字布局
        root.title("丁字布局")
        lb1_A1 ['bg'] = D1
        lb1_A2 ['bg'] = D1
        lb1_A3 ['bg'] = D1
        lb1_A4 ['bg'] = D1
        lb1_A5 ['bg'] = D1
        lb1_A6 ['bg'] = D1
        lb1_A7 ['bg'] = D1
        lb1_A8 ['bg'] = D1
        lb1_A9 ['bg'] = D1
        lb1_A10 ['bg'] = D1
        lb1_A11 ['bg'] = D1
        lb1_A12 ['bg'] = D1
        lb1_B1 ['bg'] = D3
        lb1_B2 ['bg'] = D3
        lb1_B3 ['bg'] = D2
        lb1_B4 ['bg'] = D2
        lb1_B5 ['bg'] = D2
        lb1_B6 ['bg'] = D2
        lb1_B7 ['bg'] = D2
        lb1_B8 ['bg'] = D2
        lb1_B9 ['bg'] = D2
        lb1_B10 ['bg'] = D2
        lb1_B11 ['bg'] = D2
        lb1_B12 ['bg'] = D2
        lb1_C1 ['bg'] = D3
        lb1_C2 ['bg'] = D3
        lb1_C3 ['bg'] = D2
        lb1_C4 ['bg'] = D2
        lb1_C5 ['bg'] = D2
        lb1_C6 ['bg'] = D2
        lb1_C7 ['bg'] = D2
        lb1_C8 ['bg'] = D2
        lb1_C9 ['bg'] = D2
        lb1_C10 ['bg'] = D2
        lb1_C11 ['bg'] = D2
        lb1_C12 ['bg'] = D2
        lb1_D1 ['bg'] = D3
        lb1_D2 ['bg'] = D3
        lb1_D3 ['bg'] = D2
        lb1_D4 ['bg'] = D2
        lb1_D5 ['bg'] = D2
        lb1_D6 ['bg'] = D2
        lb1_D7 ['bg'] = D2
        lb1_D8 ['bg'] = D2
        lb1_D9 ['bg'] = D2
        lb1_D10 ['bg'] = D2
        lb1_D11 ['bg'] = D2
        lb1_D12 ['bg'] = D2
        lb1_E1 ['bg'] = D3
        lb1_E2 ['bg'] = D3
        lb1_E3 ['bg'] = D2
        lb1_E4 ['bg'] = D2
        lb1_E5 ['bg'] = D2
        lb1_E6 ['bg'] = D2
        lb1_E7 ['bg'] = D2
        lb1_E8 ['bg'] = D2
        lb1_E9 ['bg'] = D2
        lb1_E10 ['bg'] = D2
        lb1_E11 ['bg'] = D2
        lb1_E12 ['bg'] = D2
        lb1_F1 ['bg'] = D3
        lb1_F2 ['bg'] = D3
        lb1_F3 ['bg'] = D2
        lb1_F4 ['bg'] = D2
        lb1_F5 ['bg'] = D2
        lb1_F6 ['bg'] = D2
        lb1_F7 ['bg'] = D2
        lb1_F8 ['bg'] = D2
        lb1_F9 ['bg'] = D2
        lb1_F10 ['bg'] = D2
        lb1_F11 ['bg'] = D2
        lb1_F12 ['bg'] = D2
        lb1_G1 ['bg'] = D3
        lb1_G2 ['bg'] = D3
        lb1_G3 ['bg'] = D2
        lb1_G4 ['bg'] = D2
        lb1_G5 ['bg'] = D2
        lb1_G6 ['bg'] = D2
        lb1_G7 ['bg'] = D2
        lb1_G8 ['bg'] = D2
        lb1_G9 ['bg'] = D2
        lb1_G10 ['bg'] = D2
        lb1_G11 ['bg'] = D2
        lb1_G12 ['bg'] = D2
        lb1_H1 ['bg'] = D3
        lb1_H2 ['bg'] = D3
        lb1_H3 ['bg'] = D2
        lb1_H4 ['bg'] = D2
        lb1_H5 ['bg'] = D2
        lb1_H6 ['bg'] = D2
        lb1_H7 ['bg'] = D2
        lb1_H8 ['bg'] = D2
        lb1_H9 ['bg'] = D2
        lb1_H10 ['bg'] = D2
        lb1_H11 ['bg'] = D2
        lb1_H12 ['bg'] = D2
        lb1_I1 ['bg'] = D3
        lb1_I2 ['bg'] = D3
        lb1_I3 ['bg'] = D2
        lb1_I4 ['bg'] = D2
        lb1_I5 ['bg'] = D2
        lb1_I6 ['bg'] = D2
        lb1_I7 ['bg'] = D2
        lb1_I8 ['bg'] = D2
        lb1_I9 ['bg'] = D2
        lb1_I10 ['bg'] = D2
        lb1_I11 ['bg'] = D2
        lb1_I12 ['bg'] = D2
        print("颜色刷新")
    print("调用颜色刷新")

        

def wz():
    global number
    if number == "A":#国字布局
        lb_sy['text'] = "页头/脚条:"
        lb_nr['text'] = "内容:"
        lb_c['text'] = "左/右侧:"
        print("文字刷新")
    if number == "B":#三字布局
        lb_sy['text'] = "页头条:"
        lb_nr['text'] = "内容:"
        lb_c['text'] = "页脚条:"
        print("文字刷新")
    if number == "C":#综合布局
        lb_sy['text'] = "页头条:"
        lb_nr['text'] = "右侧:"
        lb_c['text'] = "左侧:"
        print("文字刷新")
    if number == "D":#丁字布局
        lb_sy['text'] = "页头条:"
        lb_nr['text'] = "内容:"
        lb_c['text'] = "左侧:"
        print("文字刷新")
    print("调用文字刷新")



root_jz.destroy()
root = tkinter.Tk()
root.title("国字布局")
root.geometry(ckdx(1209,687))
root.iconbitmap(path_logo+"\\logo.ico")
root.wm_attributes('-alpha',int(cktm)/100)
root.resizable(False,False)
root.configure(bg=ckbg)

def callback():
    print("~被调用了~")
 
# 创建一个顶级菜单
menubar = tk.Menu(root)
 
# 创建一个下拉菜单“文件”，然后将它添加到顶级菜单中
filemenu = tk.Menu(menubar, tearoff=False)
#filemenu.add_command(label="打开", command=callback)
#filemenu.add_command(label="打开", command=callback)
filemenu.add_command(label="保存文本", command=wbwd)
filemenu.add_command(label="保存图片", command=tpbc)
filemenu.add_separator()
filemenu.add_command(label="复制", command=fz)
menubar.add_cascade(label="文件", menu=filemenu)
 
editmenu = tk.Menu(menubar, tearoff=False)
editmenu.add_command(label="国字布局", command=g)
editmenu.add_command(label="三字布局", command=s)
editmenu.add_command(label="综合布局", command=d)
editmenu.add_command(label="丁字布局", command=z)
menubar.add_cascade(label="布局", menu=editmenu)

menubar.add_cascade(label="设置", command=sz)

gj = tk.Menu(menubar, tearoff=False)
gj.add_command(label="颜色对比", command=dbys)
gj.add_separator()
gj.add_command(label="网址获取网页颜色", command=hqwy)
gj.add_command(label="截图获取网页颜色", command=jtwy)
'''
gj.add_command(label="综合布局", command=z)
'''
menubar.add_cascade(label="工具", menu=gj)

 
# 显示菜单
root.config(menu=menubar)

lb_sy = Label(root, text="页头/脚条:",bg=ckbg,fg=ckfg,font=('楷体', 18),width = 10,)
lb_sy.grid(row=2, column=1, padx=5, pady=5)

btn_sy = tkinter.Button(root, text="修改",bg=ckbg,fg=ckfg,font=('楷体', 18),command=g_sy)
btn_sy.bind("<Enter>", b_sy)
btn_sy.bind("<Leave>", fh)
btn_sy.grid(row=2, column=2,padx=5, pady=5)

lb_sy_16 = Label(root, text="16进制:",bg=ckbg,fg=ckfg,font=('楷体', 18),)
lb_sy_16.grid(row=3, column=1, padx=5, pady=5)

lb_sy_16_fl = Label(root, text=A1,bg=ckbg,fg=ckfg,font=('楷体', 18),)
lb_sy_16_fl.grid(row=3, column=2, padx=5, pady=5)

lb_sy_rgb = Label(root, text="RGB进制:",bg=ckbg,fg=ckfg,font=('楷体', 18),)
lb_sy_rgb.grid(row=4, column=1, padx=5, pady=5)

lb_sy_16_rgb = Label(root, text=color16_rgb(A1),bg=ckbg,fg=ckfg,font=('楷体', 18),width = 12)
lb_sy_16_rgb.grid(row=4, column=2, padx=5, pady=5)


lb_nr = Label(root, text="内容:",bg=ckbg,fg=ckfg,font=('楷体', 18),)
lb_nr.grid(row=5, column=1, padx=5, pady=5)

btn_nr = tkinter.Button(root, text="修改",bg=ckbg,fg=ckfg,font=('楷体', 18),command=g_nr)
btn_nr.bind("<Enter>", b_nr)
btn_nr.bind("<Leave>", fh)
btn_nr.grid(row=5, column=2,padx=5, pady=5)

lb_nr_16 = Label(root, text="16进制:",bg=ckbg,fg=ckfg,font=('楷体', 18),)
lb_nr_16.grid(row=6, column=1, padx=5, pady=5)

lb_nr_16_fl = Label(root, text=A2,bg=ckbg,fg=ckfg,font=('楷体', 18),)
lb_nr_16_fl.grid(row=6, column=2, padx=5, pady=5)

lb_nr_rgb = Label(root, text="RGB进制:",bg=ckbg,fg=ckfg,font=('楷体', 18),)
lb_nr_rgb.grid(row=7, column=1, padx=5, pady=5)

lb_nr_16_rgb = Label(root, text=color16_rgb(A2),bg=ckbg,fg=ckfg,font=('楷体', 18),)
lb_nr_16_rgb.grid(row=7, column=2, padx=5, pady=5)


lb_c = Label(root, text="左/右侧:",bg=ckbg,fg=ckfg,font=('楷体', 18),)
lb_c.grid(row=8, column=1, padx=5, pady=5)

btn_c = tkinter.Button(root, text="修改",bg=ckbg,fg=ckfg,font=('楷体', 18),command=g_c)
btn_c.bind("<Enter>", b_c)
btn_c.bind("<Leave>", fh)
btn_c.grid(row=8, column=2,padx=5, pady=5)

lb_c_16 = Label(root, text="16进制:",bg=ckbg,fg=ckfg,font=('楷体', 18),)
lb_c_16.grid(row=9, column=1, padx=5, pady=5)

lb_c_16_fl = Label(root, text=A3,bg=ckbg,fg=ckfg,font=('楷体', 18),)
lb_c_16_fl.grid(row=9, column=2, padx=5, pady=5)

lb_c_rgb = Label(root, text="RGB进制:",bg=ckbg,fg=ckfg,font=('楷体', 18),)
lb_c_rgb.grid(row=10, column=1, padx=5, pady=5)

lb_c_16_rgb = Label(root, text=color16_rgb(A3),bg=ckbg,fg=ckfg,font=('楷体', 18),)
lb_c_16_rgb.grid(row=10, column=2, padx=5, pady=5)















#显示



lb1_A1 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A1,)
lb1_A1.grid(row=2, column=5)

lb1_A2 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A1,)
lb1_A2.grid(row=2, column=6)

lb1_A3 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A1,)
lb1_A3.grid(row=2, column=7)

lb1_A4 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A1,)
lb1_A4.grid(row=2, column=8)

lb1_A5 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A1,)
lb1_A5.grid(row=2, column=9)

lb1_A6 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A1,)
lb1_A6.grid(row=2, column=10)

lb1_A7 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A1,)
lb1_A7.grid(row=2, column=11)

lb1_A8 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A1,)
lb1_A8.grid(row=2, column=12)

lb1_A9 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A1,)
lb1_A9.grid(row=2, column=13)

lb1_A10 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A1,)
lb1_A10.grid(row=2, column=14)

lb1_A11 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A1,)
lb1_A11.grid(row=2, column=15)

lb1_A12 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A1,)
lb1_A12.grid(row=2, column=16)

lb1_B1 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A3,)
lb1_B1.grid(row=3, column=5)

lb1_B2 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A3,)
lb1_B2.grid(row=3, column=6)

lb1_B3 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_B3.grid(row=3, column=7)

lb1_B4 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_B4.grid(row=3, column=8)

lb1_B5 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_B5.grid(row=3, column=9)

lb1_B6 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_B6.grid(row=3, column=10)

lb1_B7 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_B7.grid(row=3, column=11)

lb1_B8 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_B8.grid(row=3, column=12)

lb1_B9 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_B9.grid(row=3, column=13)

lb1_B10 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_B10.grid(row=3, column=14)

lb1_B11 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A3,)
lb1_B11.grid(row=3, column=15)

lb1_B12 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A3,)
lb1_B12.grid(row=3, column=16)

lb1_C1 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A3,)
lb1_C1.grid(row=4, column=5)

lb1_C2 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A3,)
lb1_C2.grid(row=4, column=6)

lb1_C3 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_C3.grid(row=4, column=7)

lb1_C4 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_C4.grid(row=4, column=8)

lb1_C5 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_C5.grid(row=4, column=9)

lb1_C6 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_C6.grid(row=4, column=10)

lb1_C7 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_C7.grid(row=4, column=11)

lb1_C8 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_C8.grid(row=4, column=12)

lb1_C9 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_C9.grid(row=4, column=13)

lb1_C10 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_C10.grid(row=4, column=14)

lb1_C11 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A3,)
lb1_C11.grid(row=4, column=15)

lb1_C12 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A3,)
lb1_C12.grid(row=4, column=16)

lb1_D1 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A3,)
lb1_D1.grid(row=5, column=5)

lb1_D2 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A3,)
lb1_D2.grid(row=5, column=6)

lb1_D3 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_D3.grid(row=5, column=7)

lb1_D4 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_D4.grid(row=5, column=8)

lb1_D5 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_D5.grid(row=5, column=9)

lb1_D6 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_D6.grid(row=5, column=10)

lb1_D7 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_D7.grid(row=5, column=11)

lb1_D8 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_D8.grid(row=5, column=12)

lb1_D9 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_D9.grid(row=5, column=13)

lb1_D10 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_D10.grid(row=5, column=14)

lb1_D11 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A3,)
lb1_D11.grid(row=5, column=15)

lb1_D12 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A3,)
lb1_D12.grid(row=5, column=16)

lb1_E1 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A3,)
lb1_E1.grid(row=6, column=5)

lb1_E2 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A3,)
lb1_E2.grid(row=6, column=6)

lb1_E3 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_E3.grid(row=6, column=7)

lb1_E4 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_E4.grid(row=6, column=8)

lb1_E5 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_E5.grid(row=6, column=9)

lb1_E6 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_E6.grid(row=6, column=10)

lb1_E7 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_E7.grid(row=6, column=11)

lb1_E8 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_E8.grid(row=6, column=12)

lb1_E9 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_E9.grid(row=6, column=13)

lb1_E10 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_E10.grid(row=6, column=14)

lb1_E11 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A3,)
lb1_E11.grid(row=6, column=15)

lb1_E12 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A3,)
lb1_E12.grid(row=6, column=16)

lb1_F1 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A3,)
lb1_F1.grid(row=7, column=5)

lb1_F2 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A3,)
lb1_F2.grid(row=7, column=6)

lb1_F3 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_F3.grid(row=7, column=7)

lb1_F4 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_F4.grid(row=7, column=8)

lb1_F5 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_F5.grid(row=7, column=9)

lb1_F6 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_F6.grid(row=7, column=10)

lb1_F7 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_F7.grid(row=7, column=11)

lb1_F8 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_F8.grid(row=7, column=12)

lb1_F9 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_F9.grid(row=7, column=13)

lb1_F10 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_F10.grid(row=7, column=14)

lb1_F11 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A3,)
lb1_F11.grid(row=7, column=15)

lb1_F12 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A3,)
lb1_F12.grid(row=7, column=16)

lb1_G1 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A3,)
lb1_G1.grid(row=8, column=5)

lb1_G2 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A3,)
lb1_G2.grid(row=8, column=6)

lb1_G3 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_G3.grid(row=8, column=7)

lb1_G4 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_G4.grid(row=8, column=8)

lb1_G5 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_G5.grid(row=8, column=9)

lb1_G6 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_G6.grid(row=8, column=10)

lb1_G7 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_G7.grid(row=8, column=11)

lb1_G8 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_G8.grid(row=8, column=12)

lb1_G9 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_G9.grid(row=8, column=13)

lb1_G10 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_G10.grid(row=8, column=14)

lb1_G11 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A3,)
lb1_G11.grid(row=8, column=15)

lb1_G12 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A3,)
lb1_G12.grid(row=8, column=16)

lb1_H1 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A3,)
lb1_H1.grid(row=9, column=5)

lb1_H2 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A3,)
lb1_H2.grid(row=9, column=6)

lb1_H3 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_H3.grid(row=9, column=7)

lb1_H4 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_H4.grid(row=9, column=8)

lb1_H5 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_H5.grid(row=9, column=9)

lb1_H6 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_H6.grid(row=9, column=10)

lb1_H7 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_H7.grid(row=9, column=11)

lb1_H8 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_H8.grid(row=9, column=12)

lb1_H9 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_H9.grid(row=9, column=13)

lb1_H10 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A2,)
lb1_H10.grid(row=9, column=14)

lb1_H11 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A3,)
lb1_H11.grid(row=9, column=15)

lb1_H12 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A3,)
lb1_H12.grid(row=9, column=16)

lb1_I1 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A1,)
lb1_I1.grid(row=10, column=5)

lb1_I2 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A1,)
lb1_I2.grid(row=10, column=6)

lb1_I3 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A1,)
lb1_I3.grid(row=10, column=7)

lb1_I4 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A1,)
lb1_I4.grid(row=10, column=8)

lb1_I5 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A1,)
lb1_I5.grid(row=10, column=9)

lb1_I6 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A1,)
lb1_I6.grid(row=10, column=10)

lb1_I7 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A1,)
lb1_I7.grid(row=10, column=11)

lb1_I8 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A1,)
lb1_I8.grid(row=10, column=12)

lb1_I9 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A1,)
lb1_I9.grid(row=10, column=13)

lb1_I10 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A1,)
lb1_I10.grid(row=10, column=14)

lb1_I11 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A1,)
lb1_I11.grid(row=10, column=15)

lb1_I12 = tkinter.Label(root, text = "",width = 10,height = 4,fg = ckfg,bg = A1,)
lb1_I12.grid(row=10, column=16)

root.mainloop()

























