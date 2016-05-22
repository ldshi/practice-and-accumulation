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


