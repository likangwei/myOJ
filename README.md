

# 算法心得
---

## 大纲
  解算法 = 思路->思路验证->直译->结果验证
  
  进步 = 解算法->看高手答案->临摹->形成后续TODO

## 我的毛病

1. 容易跑偏，要直译，要直译，要直译！重要的事情说三遍。No.43
2. 爱用缓存，特别是lst。很多都是可以直接求出来的，或者不用中间层就可以算好的。No.43
3. 极速返回结果的特殊情况，多考虑一下 No.43


## 总结套路
0. vs自己
   1）多次答案改进，为什么没一开始想到

1. vs高手
    a) 命名
    b) 行数
    c) 思路
    d) 技巧
    e) 可读性
    f) 此题感悟

2. 此题其它感悟


## 感悟

* 提前优化是万恶之源 # leetcode. No(34, )
* 直译思路，遇到困难，或者难翻译的地方不要想着跳过去  # leetcode.No(40, )

### 算法思路

* 不要怕破坏原始结构，例如排序、图edges            # 旷视面试
* 正着循环的算法 看看可以根据情况倒着来吗

##### 思路正确性

* 在手动验证算法思路时，要根据testcase的多个维度制造，比如nums []int, 要从排序，长度等维度来造几个数据

### 算法速度
* 不用递归 No.44(wildcard matching) No.55 (jump game)
* 缩小对比范围
* 尽可能减少缓存。如list, map等。 No.55 (jump game)
   1） 查看规律，能用数字表示或者idx来控制的话就不再生成一个list

* 算法类用while比较快，因为range和xrange都有开销
* 用最直接的方式来实现需求，不用过早的想着优化加一些map来cache，或者用map[int]int的方式，lst的遍历是很耗时的
* 排序后的数组，可以多想想怎么快速跳过index
* 多用内置算法，内置的都是C写的，肯定比我的快

##### 内置算法快
  * for range
  * == 

### 更清晰的翻译
* 直译自己的思路，每一句代码在编写时要对照自己的解题思路，特别注意边界判断，idx判断等等，有一些地方用 <= 比 < 更能清晰的表达index界限
* target 与 data[index] 相比较时，最好target在前面比较清晰
* 在做index操作时，可以用弧线来表现到底跳动了几次
* 可以用纸笔来协助记忆思考
* 直译自己的思路，有一些不太好翻译的地方，不要绕过去，而是想办法直译，因为毕竟有很多代码模式自己没见过

### 小技巧
* 数组可以想象成算盘，多个index代表某一个算盘珠
* for 循环时，有很多缓存的参数，比如i为当前轮询值，走到for loop 最后，要进行i++供下次使用，其他参数同理


### 数据结构总结
* list。 特点
* LinkList。 特点： 插入,删除 O(1), 可以加个map来实现快速定位
* Map。 特点： 快速定位
* BinaryTree
* RedBlackTree
* Dag
* Graph

### 命名积累
```
  index 用 i, j, k
  len 用m, n
  position: 二维的idx
  options: 选项
  occupied: 占据的， unoccupied: 未被占据的
  hi, lo 来代表高低位
  first, last 来用于前后出现的位置. tail表示尾巴，最后一段， last是最后一个
```

---



