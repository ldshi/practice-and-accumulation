1. 基础算法
  - 顺序查找
  - 二分查找
  - 插值查找
  - 斐波那契查找
  - 树表查找
    - 二叉查找树
    - 平衡查找树之 2-3查找树 (2-3 Tree)
    - 平衡查找树之 红黑树 (Red-Black Tree)
    - B Tree
    - B+ Tree
  - 分块查找
  - 哈希查找

2. SQL `order by` statement

3. 机器学习常见算法
  - 朴素贝叶斯
    - Laplace校验
  - 逻辑回归和线性回归
    - 梯度下降
  - KNN
    - KD树
    - SVM、SMO
    - 对偶求解
  - 决策树
    - ID3
    - C4.5
    - Cart
    - 随机森林RF
  - GBDT
  - BP
  - 最下二乘法
  - EM
  - Bagging
  - Boosting
  - 凸优化

4. [TCP 3次握手 4次挥手 node.js cluster module以及并发测试siege](https://mp.weixin.qq.com/s?__biz=MzAwNDcyNjI3OA==&mid=2650838731&idx=1&sn=6a9d5dcf551e5a8fa9d694c7f70edc4a&scene=1&srcid=0514QYF3RMYITR2PjiA8jajN&pass_ticket=BaLMQWAuJq4FFKR3ZNoy4MvsNqu2idSDlLn%2FdI9hGpd2ITk%2B4LYBI5bPRmN9l2tJ#rd)

5. [傅立叶变换 vs 小波分析](https://mp.weixin.qq.com/s?__biz=MzI2NjA3NTc4Ng==&mid=2652077976&idx=1&sn=4de57da48ace3c2c17a0177b1e90e684&scene=1&srcid=05145FOIDXXLls2TQJxab1kd&pass_ticket=BaLMQWAuJq4FFKR3ZNoy4MvsNqu2idSDlLn%2FdI9hGpd2ITk%2B4LYBI5bPRmN9l2tJ#rd)

6. [从随机过程到马尔科夫链蒙特卡洛方法](https://mp.weixin.qq.com/s?__biz=MzI2NjA3NTc4Ng==&mid=2652077972&idx=1&sn=707be5926dc6012166f49e1d5a9ce2bd&scene=1&srcid=0514LwyMCeioIJx66TuzHOVX&pass_ticket=BaLMQWAuJq4FFKR3ZNoy4MvsNqu2idSDlLn%2FdI9hGpd2ITk%2B4LYBI5bPRmN9l2tJ#rd)

7. [数学之美：平凡又神奇的贝叶斯方法](https://mp.weixin.qq.com/s?__biz=MzI2NjA3NTc4Ng==&mid=2652077970&idx=1&sn=be062f2cfb9a0ec5662c0b68591a414f&scene=1&srcid=0514tfF2RaNolivGc1ypChb2&pass_ticket=BaLMQWAuJq4FFKR3ZNoy4MvsNqu2idSDlLn%2FdI9hGpd2ITk%2B4LYBI5bPRmN9l2tJ#rd)

8. [如何用简单易懂的例子解释隐马尔可夫模型？](https://mp.weixin.qq.com/s?__biz=MzI2NjA3NTc4Ng==&mid=2652077944&idx=1&sn=d17758f0aed8670ba0f5f41e481f0205&scene=1&srcid=0514FMmwVk3FkOjjEm4XWcxW&pass_ticket=BaLMQWAuJq4FFKR3ZNoy4MvsNqu2idSDlLn%2FdI9hGpd2ITk%2B4LYBI5bPRmN9l2tJ#rd)

9. [Python验证码识别：利用pytesser识别简单图形验证码](https://mp.weixin.qq.com/s?__biz=MzA5ODUzOTA0OQ==&mid=2651688035&idx=1&sn=c8ad383215ed11a11a847933c54e0ee6&scene=1&srcid=0514hcQT3NiZdELz5Q1jTit5&pass_ticket=BaLMQWAuJq4FFKR3ZNoy4MvsNqu2idSDlLn%2FdI9hGpd2ITk%2B4LYBI5bPRmN9l2tJ#rd)

10. [Python验证码识别：利用pytesser识别简单图形验证码](https://mp.weixin.qq.com/s?__biz=MzA5ODUzOTA0OQ==&mid=2651688035&idx=1&sn=c8ad383215ed11a11a847933c54e0ee6&scene=1&srcid=0514hcQT3NiZdELz5Q1jTit5&pass_ticket=BaLMQWAuJq4FFKR3ZNoy4MvsNqu2idSDlLn%2FdI9hGpd2ITk%2B4LYBI5bPRmN9l2tJ#rd)

11. Microsoft fast and Microsoft fast search

12. LexaLytics

13. [kofax](http://www.kofax.com/data-integration-extraction)

14. [kapow](http://www.infoworld.com/article/2630604/applications/kapow-focuses-on-web-data-services.html)

15. [Apache mahout](http://mahout.apache.org/)

16. [Apache Lucene](https://lucene.apache.org/core/)

17. [Apache Solr](http://lucene.apache.org/solr/)

18. [Apache OpenNLP](https://opennlp.apache.org/)

19. [Construct real time advertisement building system](http://www.kiosked.com/) - Generate the advertisement in real time according to the page content.

20. [Producer–consumer problem](https://en.wikipedia.org/wiki/Producer%E2%80%93consumer_problem)

  ```
  int itemCount = 0;

  procedure producer() {
    while (true) {
      item = produceItem();

      if (itemCount == BUFFER_SIZE) {
        sleep();
      }

      putItemIntoBuffer(item);
      itemCount = itemCount + 1;

      if (itemCount == 1) {
        wakeup(consumer);
      }
    }
  }

  procedure consumer() {
    while (true) {

      if (itemCount == 0) {
        sleep();
      }

      item = removeItemFromBuffer();
      itemCount = itemCount - 1;

      if (itemCount == BUFFER_SIZE - 1) {
        wakeup(producer);
      }

      consumeItem(item);
    }
  }
  ```

21. FC
  - 真实人虚拟人的对应
  - 生活的location
  - 最近时间段关注的东西、问题、事物

22. [promise](http://www.html-js.com/article/2589)

23. [React](http://mp.weixin.qq.com/s?__biz=MzAwNDcyNjI3OA==&mid=2650838823&idx=1&sn=a82c47024e8746e0e89c18dc7e4a75fb&scene=0#wechat_redirect)

24. [Vue](http://mp.weixin.qq.com/s?__biz=MzAwNDcyNjI3OA==&mid=2650838823&idx=1&sn=a82c47024e8746e0e89c18dc7e4a75fb&scene=0#wechat_redirect)

25. [Web Component and React 组件](http://mp.weixin.qq.com/s?__biz=MzAwNDcyNjI3OA==&mid=2650838823&idx=1&sn=a82c47024e8746e0e89c18dc7e4a75fb&scene=0#wechat_redirect)

26. [Writing fast, memory-efficient JavaScript](http://mp.weixin.qq.com/s?__biz=MzAwNDcyNjI3OA==&mid=2650838822&idx=1&sn=d57fdff91022804b03c64cad900a79fe&scene=0#wechat_redirect)

27. [Kernels of browsers](http://mp.weixin.qq.com/s?__biz=MzAwNDcyNjI3OA==&mid=2650838792&idx=1&sn=d0c711ee3d75d483cade36e988ecf90a&scene=0#wechat_redirect)

28. [使用Python进行无线攻击：Dnspwn攻击](http://mp.weixin.qq.com/s?__biz=MzA5ODUzOTA0OQ==&mid=2651688040&idx=1&sn=b0110aaf293323af41a283699d4fe136&scene=0#wechat_redirect)

29. [Python程序的执行原理](http://mp.weixin.qq.com/s?__biz=MzA5ODUzOTA0OQ==&mid=2651688033&idx=1&sn=3e52e2139a458f4f05dd3b1f777fb904&scene=0#wechat_redirect)

30. [MySQL学习笔记：插件式存储引擎](http://mp.weixin.qq.com/s?__biz=MzI3NDA4OTk1OQ==&mid=2649900741&idx=1&sn=e40e0b44c1bb90530d5dd853b004a83d&scene=0#wechat_redirect)

31. [实际项目中的常见算法](http://mp.weixin.qq.com/s?__biz=MzI2NjA3NTc4Ng==&mid=2652077993&idx=1&sn=978241052af8be2e86367dfff38f7511&scene=0#wechat_redirect)

32. [Linux入侵检测基础 ](http://mp.weixin.qq.com/s?__biz=MzIyMDEzMTA2MQ==&mid=2651147543&idx=1&sn=fbc00c0bf3b211d2dca912f1e3558fd5&scene=0#wechat_redirect)

33. [如何用简单易懂的例子解释隐马尔可夫模型?](https://www.zhihu.com/question/20962240)

34. [MySQL学习笔记：SQL服务器模式汇总](http://mp.weixin.qq.com/s?__biz=MzI3NDA4OTk1OQ==&mid=2649900742&idx=1&sn=fc31795856f7c2e5e91772585d85e712&scene=0#wechat_redirect)

35. [正态分布的由来, 高斯与误差正态分布, 戈塞特与T检验](http://mp.weixin.qq.com/s?__biz=MzAxMjcyNjE5MQ==&mid=2650486591&idx=1&sn=16bfcde2e691528b38604449a5b23e72&scene=0#wechat_redirect)

36. [机器学习中的相似性度量：距离](http://mp.weixin.qq.com/s?__biz=MzAxMjcyNjE5MQ==&mid=2650486595&idx=1&sn=024f66f8d2fa69d62fbef5e184600fde&scene=0#wechat_redirect)

37. [波斯公主选驸马： 关于算法和重大决策](http://mp.weixin.qq.com/s?__biz=MzI2NjA3NTc4Ng==&mid=2652078072&idx=1&sn=0fd0440c9578057abdcb779735f02031&scene=0#wechat_redirect)

38. [JavaEE中遗漏的10个最重要的安全控制](http://mp.weixin.qq.com/s?__biz=MzIyMDEzMTA2MQ==&mid=2651147580&idx=1&sn=5bde4606b0bb17fce6e7c85188ca74ee&scene=0#wechat_redirect)

39. [Blockchain](https://www.zhihu.com/question/27687960)

40. [Creating Desktop Applications With AngularJS and GitHub Electron](https://scotch.io/tutorials/creating-desktop-applications-with-angularjs-and-github-electron)

41. [A Tour of Go](https://tour.golang.org/welcome/1)

42. Bitcoin & the Byzantine Generals Problem
  - [Bitcoin & the Byzantine Generals Problem](https://web.archive.org/web/20140603221234/http://expectedpayoff.com/blog/2013/03/22/bitcoin-and-the-byzantine-generals-problem/)
  - [比特币与拜占庭将军问题](http://www.8btc.com/bitcoin-and-the-byzantine-generals-problem)

43. Making Sense of Bitcoin Transaction Fees
  - [Making Sense of Bitcoin Transaction Fees](http://bitzuma.com/posts/making-sense-of-bitcoin-transaction-fees/)
  - [理解比特币交易费用](http://www.8btc.com/making-sense-of-bitcoin-transaction-fee)

44. [15年双11手淘前端技术巡演： H5性能最佳实践](http://mp.weixin.qq.com/s?__biz=MzAwNDcyNjI3OA==&mid=2650838912&idx=1&sn=2bca14e8ca4228172de9cf727f0f130b&scene=0#wechat_redirect)

45. [从BAT面试题说起：前端面试解题思路](http://mp.weixin.qq.com/s?__biz=MzAwNDcyNjI3OA==&mid=2650838909&idx=1&sn=089a315c006ced68db4ac6582c3bd68f&scene=0#wechat_redirect)

46. [堆：神奇的优先队列](http://mp.weixin.qq.com/s?__biz=MzI2NjA3NTc4Ng==&mid=2652078111&idx=1&sn=ac486400d4ad4fd9681e20707805ca6b&scene=0#wechat_redirect)

47. [遗传算法(Genetic Algorithm)概述](http://mp.weixin.qq.com/s?__biz=MzI2NjA3NTc4Ng==&mid=2652078127&idx=1&sn=3b1d8ea6d77814cef848b3e710158cc2&scene=0#wechat_redirect)

48. [Linear Algebra](http://mp.weixin.qq.com/s?__biz=MzI2NjA3NTc4Ng==&mid=2652078129&idx=1&sn=bd8ed571759c1af375dffb0cbe744586&scene=0#wechat_redirect)

49. [RabbitMQ or Apache Kafka](http://mp.weixin.qq.com/s?__biz=MzA4ODgwNjk1MQ==&mid=403597527&idx=1&sn=a242e50735b2d5203b24d6f4edf2915c&scene=21#wechat_redirect)

50. [How does HTTPs work?](http://mp.weixin.qq.com/s?__biz=MzIyMDEzMTA2MQ==&mid=2651147614&idx=1&sn=cc8a41e4f157918a7a69031cfe81e4a7&scene=0#wechat_redirect)

51. [Why is float type number not accurate?](http://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513140&idx=1&sn=565517e977ac56904305a4a9f9d65012&scene=0#wechat_redirect)


