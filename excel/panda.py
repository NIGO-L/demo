import pandas as pd

mydataset = {'sites': ["Google", "Runoob", "Wiki"],
             'number': [1, 2, 3]}

myvar = pd.DataFrame(mydataset, index=["d", "f", "1"])

print(myvar)

print(myvar.loc["f"])


print("测试语句，git")
