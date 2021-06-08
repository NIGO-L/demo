import tkinter as tk

import panda as pd

# 思路：
# 测试读取文件的内容，跨行刷数，用到的功能: map(),  applymap() 等函数完成
# 测试文件：  PY考勤明细表   关注人员有： 徐艺庭，刘海，何星辰
# tkinter 制作 一个框，有文字提示   窗口，画布，按钮，多选框，提示文字，得到输入值


# df = pd.read_excel("PY考勤明细表V1.05.xlsx", engine = "openpyxl")
# print(df.head())

mywindow = tk.Tk()
mywindow.title("计算工具")
mywindow.geometry("600x400")  # 窗口宽 x 高

# 制作一个输入框， 并得到输入的值

text_A1 = "请输入A表名称（查找值）  xlsx 类型格式文件"
text_A2 = "请输入A表SHEET名称"
text_A3 = "请输入A表中查找的 字段 名称"
text_B1 = "请输入B表名称（匹配区域） xlsx 类型格式文件"
text_B2 = "请输入B表SHEET名称"
text_B3 = "请输入B表中匹配的 字段 名称"
text_01 = "正在将B表合并到A表"
a1, a2, a3, b1, b2, b3 = 0, 0, 0, 0, 0, 0
on_hit = False

mywin_text_A1 = tk.Label(mywindow, text="A1. " + text_A1, bg='grey', height=2)
mywin_text_A1.place(x=100, y=100)
mywin_text_A1.pack()
t1 = tk.StringVar(mywindow, value="公文流水")
mywin_keyin_A1 = tk.Entry(mywindow, textvariable=t1)
mywin_keyin_A1.pack()
A1 = mywin_keyin_A1.get()

mywin_text_A2 = tk.Label(mywindow, text="A2. " + text_A2, height=2)
mywin_text_A2.place(x=100, y=150)
mywin_text_A2.pack()

t2 = tk.StringVar(mywindow, value="公文项目明细")
mywin_keyin_A2 = tk.Entry(mywindow, textvariable=t2)
mywin_keyin_A2.pack()
A2 = mywin_keyin_A2.get()

mywin_text_A3 = tk.Label(mywindow, text="A3. " + text_A3, height=2)
mywin_text_A3.place(x=100, y=200)
mywin_text_A3.pack()
t3 = tk.StringVar(mywindow, value="使用部门")
mywin_keyin_A3 = tk.Entry(mywindow, textvariable=t3)
mywin_keyin_A3.place(x=100, y=250)
mywin_keyin_A3.pack()
A3 = mywin_keyin_A3.get()

mywin_text_B1 = tk.Label(mywindow, text="B1. " + text_B1, bg='grey', height=2)
mywin_text_B1.pack()
t11 = tk.StringVar(mywindow, value="门店匹配20210415a")
mywin_keyin_B1 = tk.Entry(mywindow, textvariable=t11)
mywin_keyin_B1.pack()
B1 = mywin_keyin_B1.get()

mywin_text_B2 = tk.Label(mywindow, text="B2. " + text_B2, height=2)
mywin_text_B2.pack()
t12 = tk.StringVar(mywindow, value="Sheet1")
mywin_keyin_B2 = tk.Entry(mywindow, textvariable=t12)
mywin_keyin_B2.pack()
B2 = mywin_keyin_B2.get()

mywin_text_B3 = tk.Label(mywindow, text="B3. " + text_B3, height=2)
mywin_text_B3.pack()
t13 = tk.StringVar(mywindow, value="使用部门")
mywin_keyin_B3 = tk.Entry(mywindow, textvariable=t13)
mywin_keyin_B3.pack()
B3 = mywin_keyin_B3.get()


# input("测试中断")

# 定义按钮开始运算  先定义计算的函数
def test(a):
    return print("这个值是" + str(a))


def cal_vl01(a):
    var1 = a.get()
    return var1


def cal_vl02(a1, a3, b1, b3):
    # ppp = False
    # if ppp = False:
    #     "请"
    df1 = pd.read_excel(a1 + ".xlsx", engine="openpyxl")
    df2 = pd.read_excel(b1 + ".xlsx", engine="openpyxl")
    df = pd.merge(df1, df2, left_on=a3, right_on=b3, how="left")
    df.to_excel("test01.xlsx")


def cal_vl03():
    global on_hit
    a1, a2, a3, b1, b2, b3 = A1, A2, A3, B1, B2, B3
    df1 = pd.read_excel(a1 + ".xlsx", sheet_name=a2, engine="openpyxl")
    df2 = pd.read_excel(b1 + ".xlsx", sheet_name=b2, engine="openpyxl")
    if on_hit == False:
        on_hit = True
        df = pd.merge(df1, df2, left_on=a3, right_on=b3, how="left")
        df.to_excel("test01.xlsx")
        var.set("开始合并")
    else:
        on_hit = False
        var.set("请点击开始")
        print("继续")


def hit_me(a1, a2, a3, b1, b2, b3):
    global on_hit
    a1 = A1
    a2 = A2
    a3 = A3
    b1 = B1
    b2 = B2
    b3 = B3

    if on_hit == False:
        on_hit = True
        df1 = pd.read_excel(a1 + ".xlsx", engine="openpyxl")
        df2 = pd.read_excel(b1 + ".xlsx", engine="openpyxl")
        df = pd.merge(df1, df2, left_on=a3, right_on=b3, how="left")
        df.to_excel("test01.xlsx")

        var.set("You hit me!")

    else:
        on_hit = False
        var.set("")
        print("继续")


test01 = mywin_keyin_A1.get()
print(test01)
print(A2)

var = tk.StringVar()
l = tk.Label(mywindow, textvariable=var, width=50, height=2)
l.pack()

cal_a = tk.Button(mywindow, text="开始匹配", command=cal_vl03, height=2)
cal_a.pack()

mywindow.mainloop()
