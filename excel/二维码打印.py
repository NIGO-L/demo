import pandas as pd
import qrcode
import xlrd
import PIL
import os
import barcode
import datetime
from barcode.writer import ImageWriter
from PIL import Image
from pandas import timedelta_range

# a = input("请输入什么继续测试")

#   定义 a 为 文件名称，所有的文件位于E盘开发目录下，操作步骤：
#    1，导出需要处理的二维码表格，为XLS格式
#    2，图片链接列名： 链接地址
#    参数说明：
#   定义row_max 为最大行数,row_excel 备用参数 , f 为预读的 Excel 条形码文件：
#    help(barcode.ean)

#   这里必须定义
a = "二维码_10张北京达美_Jason.xls"  # 取二维码数字的原始表
rows_excel = 0  # 第几个SHEET
rows_max = 11  # 总共多少行，总数 + 1
f = pd.read_excel(a, converters={'条码': str})  # 建立DataFrame
shop = "北京达美"  # 定义开卡门店
icon = Image.open('logo-b01.png')  # 公司LOGO
pd.set_option('display.max_columns', None)
writerS = pd.ExcelWriter('二维码套打1.11.xlsx')  # 保存方法

# 简化明细表，生成年月日列，生成地址列，前移1天
df = f[["批次名称", "条码", "卡种", "有效期", "生成日期"]]
df.loc[:, ["date"]] = pd.to_datetime(df["有效期"], format='%Y-%m-%d')
df["date"] = df["date"] + datetime.timedelta(days=-1)

# 提取年
df["年"] = df["date"].dt.year
# 提取月份
df["月"] = df["date"].dt.month
# 提取日
df["日"] = df["date"].dt.day
print(df.tail())
input("测试中断点")

df1 = df.drop("有效期", 1)
df1.columns = ["批次名称", "条码", "卡种", "生成日期", "有效期", "年", "月", "日"]
df1["开卡门店"] = shop
df1["二维码地址"] = None
df1["条码地址"] = None
df1["TEST"] = None

print(df1.tail())

input("调试使用中断")
for i in range(1, rows_max):
    text = f["条码"][i - 1]
    qr = qrcode.QRCode(
        version=6,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=13,
        border=2,
    )

    # img = qr.make(text)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image()
    img = img.convert("RGBA")
    img_w, img_h = img.size  # 获取图片的宽高
    factor = 4
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)
    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h  # 重新设置logo的尺寸
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)
    img.paste(icon, (w, h))  # 显示图片
    img.save(os.getcwd() + '/qrcode/' + str(i) + '.png')  # 将文件路径保存到表格当中
    Code1 = os.getcwd() + "\\qrcode\\" + str(i) + '.png'
    Code2 = os.getcwd() + "\\qrcode\\" + str(i) + 't.png'
    df1["二维码地址"][i - 1] = eval(repr(Code1).replace('\\', '\\\\'))  # 将 \ 转换为 \\，为邮件合并中地址
    df1["条码地址"][i - 1] = eval(repr(Code2).replace('\\', '\\\\'))

    # 保存图片至本地目录，可以设定路径  img.show()
    print("-------------二维码" + str(i) + "准备完毕， 开始准备条码---------")

    # // 创建ean13格式的条形码格式对象
    EAN = barcode.get_barcode_class('code128')
    ean = EAN(str(text), writer=ImageWriter())  # // 创建条形码对象，内容为5901234 # 123457，  保存条形码图片，并返回保存路径。图片格式为png
    ean.save(os.getcwd() + '/qrcode/' + str(i) + 't',
             {'module_height': 6,
              'quiet_zone': 2,
              'font_size': 16,
              'text_distance': 1})
    i += 1
print('二维码打印完毕 - 20210311')

df1.to_excel(writerS)
writerS.save()

# // 查看python - barcode支持的条形码格式
print(barcode.PROVIDED_BARCODES)

#   条形码 备用语句
# EAN = barcode.get_barcode_class('ean13') // 创建ean13格式的条形码格式对象
# ean = EAN('5901234123457', writer=ImageWriter()) // 创建条形码对象，内容为5901234123457
# fullname = ean.save('d:\ean13_barcode') // 保存条形码图片，并返回保存路径。图片格式为png
#
# print(fullname)
