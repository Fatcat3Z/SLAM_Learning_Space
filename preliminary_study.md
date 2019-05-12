# LEARNING SLAM
## ————————————Based on ORB-SLAM2 

### ORB 
[ORB特征提取算法](https://blog.csdn.net/yang843061497/article/details/38553765)
- 特征点的选择 FAST算法
- 描述子（旋转一致性）
- 匹配
- 实现：opencv
> 虚函数的实现：静态，智能指针的用法。

### DBoW2
特征描述子和特征计算得到单词归属，map，KL树的生成，计算相似度
#### 建立Vocabulary tree
> - [相关理论](https://blog.csdn.net/lwx309025167/article/details/80524020)
> - 字典的创建、构造、图像转化为BowVector对象（特征和键值对应），计算相似度，保存字典[代码解读](https://blog.csdn.net/lwx309025167/article/details/80528179)
#### Orbdatabase回环检测
> - query计算图像间相似度规则来检索 [分析](https://blog.csdn.net/lwx309025167/article/details/80565061)

### 系统入口System
