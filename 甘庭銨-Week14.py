# 給數字串列,將數字串列中的元素加總。
## 數字串列的初值、終值、遞增值
start = int(input('請輸入加總開始值?'))
end = int(input('請輸入加總終止值?'))
step = int(input('請輸入遞增減值?'))
## 用for迴圈做加總 + range()
sum = 0 #初始條件
for i in range(start, end, step): #判斷條件
    sum = sum + i #更新條件
    print('i為', i, '時,累加結果為', sum)