import pandas as pd

myDataset = {'sites': ["Google", "Runoob", "Wiki"],
             'number': [1, 2, 3]}

myVar = pd.DataFrame(myDataset, index=["d", "f", "1"])

print(myVar)

print(myVar.loc["f"])

print("这是一条测试语句")

myCsv = pd.read_csv("nba.csv")

print(myCsv)

print(myCsv.info())









