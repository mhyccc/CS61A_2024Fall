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


## HW04
```python
def max_path_sum(t):
    """Return the maximum root-to-leaf path sum of a tree.
    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t) # 1, 10
    11
    >>> t2 = tree(5, [tree(4, [tree(1), tree(3)]), tree(2, [tree(10), tree(3)])])
    >>> max_path_sum(t2) # 5, 2, 10
    17
    """
    "*** YOUR CODE HERE ***"
```

最开始写的代码是
```python
    def helper(t, sum):
        max_path = 0
        if is_leaf(t):
            return sum + label(t)
        for b in branches(t):
            cur_path = helper(b, sum + label(t))
            print("DEBUG: ", cur_path, max_path)
            max_path = max(max_path, cur_path)
        return max_path
    return helper(t, 0)
```

但是有点复杂，仔细想想这个函数的返回值是从根到叶节点的最大的label值和

那么就从这里出发

**base case**

如果是叶子节点，自己同时又是根节点，那么最大值就是自己的label值

**recusive case**

如果不是叶子节点，那么按照通用的方法，把上面根节点排除掉

结果应该是 `label(t) + max(....)`，排除掉的根节点下面的子节点肯定有自己的最大值，从中取最大即可

代码如下
```python
    "*** ANOTHER METHOD ***"
    if is_leaf(t):
        return label(t)
    return label(t) + max(max_path_sum(b) for b in branches(t))
```


## HW06

Q4: Mutable Mapping
第一次报错：tuple 没有 first属性
原因是没有考虑到  `ans is Link.empty`的 base case

Q5: Two List
做不到统一，自己写的代码必须先将第一个值处理好后，才能用两层for循环完成后面的操作，后面看看solutions吧
重要的是使用 cur指针（暂且叫这个名字吧）并且每次要更新cur指针.