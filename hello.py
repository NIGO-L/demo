# fxxk = True;
#
# if fxxk:
#     print("SSSS")
# else:
#     print("false")
#
# print(fxxk);

# s = 'abcdef'
# print(s[1:5])
#
# list(s)
#
# s = {'一': '1', '个': '1', 'asd': '1', 2: '呵呵'}
#
# print(s.keys())
#
# print(s.values())

# while循环
a = 1

while a < 8:
    if a % 2 == 0:
        print(a, "是偶数")
    else:
        print(a, "是奇数")
    a += 1
else:
    print(a, "是八")

# fruits = ['banana', 'apple', 'mango']
#
# for index in range(len(fruits)):
#     print("当前水果：", fruits[index])


for letter in 'Python':  # 第一个实例
    if letter == 'y':
        break
    print('当前字母 :', letter)

for letter in 'Python':  # 第一个实例
    if letter == 'h':
        continue
    print('当前字母 :', letter)

for letter in 'wills':
    if letter == 's':
        break
    print('sss', letter)


def function(vars1):
    print("pass学习" + vars1)


var1 = '牛不牛'

function(var1)


class Test:
    def prt(self):
        print(self)
        print(self.__class__)


print("shiashdasdasda")


print("1111111")

t = Test()
t.prt()
