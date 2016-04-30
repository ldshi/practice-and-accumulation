- 机器学习关注的问题
  1. 分类问题
    - 根据数据样本上抽取的特征，判定其属于有限个类别中的哪一个。
    - 如：
      - 垃圾邮件识别（1、垃圾邮件；2、正常邮件；）
      - 文本情感褒贬判定（1、褒；2、贬；）
      - 图像内容识别（1、喵星人；2、汪星人；3、人类；4、都不是）

  2. 回归问题
    - 根据数据样本上抽取的特征，预测一个连续值的结果。
    - 如：
      - 电影的票房
      - 某个地区多长时间后的房价

  3. 聚类问题
    - 根据数据样本上提取的特征，让样本抱团（相近、相关的样本抱团）
    - 如：
      - Google的新闻分类
      - 用户群体划分

- 学习路径
  1. 数学基础
    - 微积分
    - 线性代数
    - 概率论与数理统计

  2. 典型算法
    - 处理分类问题的常用算法包括：
      - 逻辑回归（工业界最常用）
      - 支持向量机
      - 随机森林
      - 朴素贝叶斯（NLP中常用）
      - 深度神经网络（视频、图片、语音等多媒体数据中使用）
    - 处理回归问题的常用算法包括：
      - 线性回归
      - 普通最小二乘回归（Ordinary Least Squares Regression）
      - 逐步回归（Stepwise Regression）
      - 多元自适应回归样条（Multivariate Adaptive Regression Splines）
    - 处理聚类问题的常用的算法包括：
      - K均值（K－means）
      - 基于密度聚类
      - LDA
    - 降维的常用算法包括：
      - 主成分分析（PCA）
      - 奇异值分解（SVD）
    - 推荐系统常用的算法：
      - 协同过滤
    - 模型融合（model ensemble）和提升（boosting）的算法包括：
      - bagging
      - adaboost
      - GBDT
      - GBRT
    - EM算法

- 应该了解的一些库：
  1. scikit-learn
  2. libsvm
  3. keras/TensorFlow（深度学习，方便搭建自己的神经网络）
  4. 自然语言处理方面的：
    - nltk
  5. 交互式环境：
    - ipython notebook

- 基本工作流程
  1. 抽象成数学问题
  2. 获取数据
  3. 特征预处理与特征提取
  4. 训练模型与调优
  5. 模型诊断
  6. 模型融合
  7. 上线运行

- 如何积累最初始的项目经验
  1. Kaggle
  2. DataCastle
  3. 阿里天池

- 相关参考资料
  - 微积分相关
    - [Calculus: Single Variable](https://www.coursera.org/learn/single-variable-calculus)
    - [Multivariable Calculus](http://ocw.mit.edu/courses/mathematics/18-02sc-multivariable-calculus-fall-2010/)

  - 线性代数
    - [Linear Algebra](http://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/)
  
  - 概率论与数理统计
    - [Introduction to Statistics: Descriptive Statistics](https://www.edx.org/course/introduction-statistics-descriptive-uc-berkeleyx-stat2-1x)
    - [Probabilistic Systems Analysis and Applied Probability](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-041-probabilistic-systems-analysis-and-applied-probability-fall-2010/)
  
  - 机器学习方法
    - [Statistical Learning(R)](https://lagunita.stanford.edu/courses/HumanitiesandScience/StatLearning/Winter2015/about)
    - [machine learning](https://www.coursera.org/learn/machine-learning) 强烈推荐，Andrew Ng老师的课程
    - [机器学习基石](https://www.coursera.org/course/ntumlone)
    - [机器学习技术](https://www.coursera.org/course/ntumltwo) 林轩田老师的课相对更有深度一些，把作业做完会对提升对机器学习的认识
    - [自然语言处理](https://class.coursera.org/nlp/lecture) 斯坦福大学课程

  - 有源代码的教程
    - [scikit-learn](http://scikit-learn.org/stable/auto_examples/index.html)
    - 《机器学习实战》 有中文版，并附有python源代码。
    - [《The Elements of Statistical Learning (豆瓣)》](http://book.douban.com/subject/3294335/) 这本书有对应的中文版：《统计学习基础 (豆瓣)》（http://book.douban.com/subject/1152126/）。书中配有R包。可以参照着代码学习算法。网盘中有中文版。
    - 《Natural Language Processing with Python (豆瓣)》（http://book.douban.com/subject/3696989/） NLP 经典，其实主要是讲 python的NLTK 这个包。网盘中有中文版。
    - 《Neural Networks and Deep Learning》（http://neuralnetworksanddeeplearning.com/） Michael Nielsen的神经网络教材，浅显易懂。国内有部分翻译，不全，建议直接看原版。
    - 统计学习方法 (豆瓣) 》（http://book.douban.com/subject/10590856/）：李航经典教材。
    - 《Pattern Recognition And Machine Learning (豆瓣) 》（http://book.douban.com/subject/2061116/）：经典中教材。 
    - 《统计自然语言处理》自然语言处理经典教材 
    - 《Applied predictive modeling》：英文版，注重工程实践的机器学习教材 
    - 《UFLDL教程》（http://ufldl.stanford.edu/wiki/index.php/UFLDL%E6%95%99%E7%A8%8B）：神经网络经典教材 
    - 《deeplearningbook》（http://www.deeplearningbook.org/）:深度学习经典教材。

  - 工具书
    - 《SciPy and NumPy (豆瓣) 》 （http://book.douban.com/subject/10561724/）
    - 《Python for Data Analysis (豆瓣) 》作者是Pandas这个包的作者（http://book.douban.com/subject/10760444/）
    - 机器学习(Machine Learning)与深度学习(Deep Learning)资料汇总（http://blog.csdn.net/zhongwen7710/article/details/45331915）


