人工智能学习笔记

2023.0301
跟李沐,把主要的代码跑一遍.

列表:
神经元
多层神经网络
rnn
cnn
lstm



机器学习需要大量数学基础与数学推导.
深度学习基于神经网络,偏向应用层.需要大量实践,需要动手.

我们现在以深度学习为主.偶尔推一推机器 学习的基础理论.




购买带有n卡的机器
安装win10
安装cuda 11.7
nvidia-smi

不必安装anaconda

安装带有cuda的pytorch



pip 安装 jupitor d2l

https://www.bilibili.com/video/BV18K411w7Vs/
测试残差网络




基础数据操作

我们一般使用32位浮点数.




太磨叽了.
现在理论的部分,看快一点,或者直接跳过不看了.快点进入代码阶段.


进入算法了

线性回归
单层神经网络 pxmx

np问题.

梯度下降,没有显式解

sgd




3090 3090ti 这两个是目前适合的显卡.
90的优点
便宜,便宜就是王道


90ti的优点
新,计算力强
散热好
矿卡的程度轻.没出多久就没法挖矿了


我打算买个便宜的或者流行的.
比如映众就很便宜,电竞叛客
火神比较流行.

水神算了,现在不会考虑任何水冷的卡,
听说涡轮比较吵,但更适合多卡.还不了解 .


想要一张90ti的火神.

你要问他,什么时候出厂的.
你一般用显卡干什么.

越新越好.
打游戏最好.
视频剪辑次之
和我一样深度学习最差.

因为打游戏时间最少,
深度学习和挖矿基本差不多...

现在6200的90ti火神会被人抢,就是这么个局势.
超过7000就可以别买了,没必要.

没有sn....
什么奇葩都有.

目前看来90ti最便宜是7000的.
映众的便宜100多,还是算了吧.还是火神吧.

我c,他那个7000元的也是无条码的.看来还是刚才那个6200的爽啊.
可惜无论如何 ,我现在都不买,就当来探路的.

滚去学习.



今天,数学看 太少了.这是个可惜的地方.
好的地方是,重新把方向调整向了动手学深度学习.本来想看理论的,想推机器 学习的,但发现还是造轮子.本来机器 学习的理论就不太重要.

我们的学习,终于要走上正轨了.




一千两千的也别纠结了.我们现在是从事很尊贵的行业.没必要磨磨唧唧地浪费时间.
不如随便买显卡回来,赶紧跑项目.这才是重点.



数学是理论,但不要忘了，深度学习是应用学科.一定要考虑机器是否适应你的算法..搞那么复杂 的计算,gpu可能 会吃不消,就适得其反了.


所以,并行计算,多搞数字运算,少写if 判断(switch也是一样,本质 是jmp指令,指令寄存器跳转)也就是说,尽量纯粹地使用alu,而不使用各种花里胡哨的功能寄存器




softmax 分类
之前只是回归



09课
这节课要多听几遍,没认真听
https://www.bilibili.com/video/BV1K64y1Q7wu/?p=5&spm_id_from=pageDriver&vd_source=88a8cff72324a68b12af164215c67b12


怎么跑个深度学习我cpu占满了啊...

现在买一万多的机器还是太难了.我只有这么些钱了
要不买个便宜的卡吧.2060?



感知机 perceptron{

    二分类问题




    收敛定理

    感知机的缺陷
    不能拟合 xor函数
    导致第一次ai寒冬..

    等价于使用批量大小为1的梯度下降


}

多层感知机
mlp{

    
}


如何设计mlp的结构要靠经验.
一般先扩展一下,再均匀地压缩.
cnn也有时会先压缩再扩展.

超参数,我感觉就是不由机器训练出来的参数,而是由人提前决定的,比如层数,每层的容量.




为什么mlp用得更多?而不是svm
因为方便改装成cnn transformer等各种复杂 的模型.



我们需要泛化误差最小的模型容量.
先足够大,再往下降


我们现在用的深度学习,基于mlp 多层感知机.而不是其它的算法(svm)


李沐说神经网络是语言...

权重衰退

我现在的问题是一个基础的,为什么模型参数不大的时候,模型复杂度就不会大呢?
模型参数的个数少,模型就简单,这个我能理解 .因为网络太简单，表达不出复杂的结构 .比如单个元表达不出异或.

大概明白了.李沐的qa不错啊.解决了我的问题.



确实这个 lamda怎么调整呢.



vc已经白学了

dropout好像又白学了..
现在主流是用正则,好像是在输入时把某些输入变成0

问怎么调,答瞎jb调.

解决过拟合问题,
如果你进行模型缩小时,只是超参数,而不是参数的话,有屁用.还是要我来调,你应该把它设计成参数,这样才能训练 啊.


