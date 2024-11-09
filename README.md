CS61A_2024Fall code and documents

## 为什么学这门课
- 练习题有难度，配合SICP可能能学到更多。有种说法是这门课要比SICP浅的多，目前我还没看
- 有测试用例检查结果，`python3 ok --score`，`--submit`不能提交也没关系。没有人会想写没有答案的教辅吧hh（虽然现在是有AI啦）



## 2024-11-8
目前觉得最难就是proj2:cats的problem7

需要把base case考虑周到
另外recursive case中需要想明白这三种改变单词的操作的意义，经过这次操作，下一次递归中的单词应该是什么样的

在P7的基础上 Phase4:Problem EC

首先要明白装饰器的作用，才能知道这道题自己要干嘛。

如果碰到有的case通不过，想想base case是不是少了（想不起来就看看Hint）

其实题目说明写的也很清晰了，题做不明白极有可能是有的说明没看明白或者是漏看了。


## lab04

记录下Q3:Buying Fruit的思路吧

**Recursive case**:

For each fruit in fruits_to_buy, calculate how many units can be purchased given the remaining total_amount.
Subtract the price of each unit purchased from total_amount and recursively call the function with the remaining fruits and amount.

unit: 这个应该是指这次枚举的情况是买了几个(0, max(`amount // price`))这种水果

**Base Case**:

If there are no fruits left and the total_amount is exactly 0, print the current combination of fruits.

这个打印结果也就是第三个参数，需要在递归调用中累加


