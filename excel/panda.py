import pandas as pd

mydataset = {'sites': ["Google", "Runoob", "Wiki"],
             'number': [1, 2, 3]}

myvar = pd.DataFrame(mydataset, index=["d", "f", "1"])

print(myvar)

print(myvar.loc["f"])


print("这是一条测试语句")
