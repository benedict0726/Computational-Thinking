#資料容器List



## 混合串列

list1 = [1,2,3,4,5]

## 索引 position index - 0

list1[0] # 1
list1[4] # 5
list1[-1] # 5

## **切片**
list1[1:4] # [2, 3, 4]


list = [1,2,3,4,5]

list2 = range(1,10000,1) # [1,2,3,4,5]

list3 = range(1,6,2) # [1,3,5]

# range(start, stop, step)
#[0,1,2,3,4,5,6,7,8,9]
##star = 0, step = 1, stop = 10
range(0,10,1)

#2+4+6+8+10=?
sum = 0
for i in range(2,11,2):
    sum = sum + i
print("Total is", sum)
    