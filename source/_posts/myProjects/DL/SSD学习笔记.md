---
title: 深度学习目标检测之SSD模型
toc: true
categories:
- DeepLearning
tag:
- DeepLearning
---

[toc]

# SSD模型总结

## 概述

SD论文的中心思想：

> Our improvements include using a small convolutional filter to predict object categories and offsets in bounding box locations, using separate predictors (filters) for different aspect ratio detections, and applying these filters to multiple feature maps from the later stages of a network in order to perform detection at multiple scales.

核心：

- 用小的卷积核预测目标分类和offsets；
- 对使用不同aspect ratio的检测使用不同的卷积核；
- 将这些卷积核用于不同大小的feature maps，使得模型能够处理不同尺度的目标检测；
  

其主要贡献：

- 提出新的OD方法SSD，比YOLO快和准。保证速度的同时，其结果的 `mAP `可与使用 region proposals 技术的方法（如 [Faster R-CNN](https://arxiv.org/abs/1506.01497)）相媲美；
- SSD 方法的核心就是 **predict** object（目标预测），以及其归属类别的 score（得分）；同时，在 feature map 上使用小的卷积核，去 **predict** 一系列 bounding boxes 的 box offsets（预测结果的bboxes相对于default boxes的offsets）；
- 本文中为了得到高精度的检测结果，在不同层次的 feature maps 上进行预测和分类，同时，还得到不同 aspect ratio 的 predictions来更好地贴合ground truths。
- 本文的这些改进设计，能够在当输入分辨率较低的图像时，保证检测的精度。同时，这个整体 end-to-end 的设计，训练也变得简单。在检测速度、检测精度之间取得较好的 **trade-off**。
- 本文提出的模型（model）在不同的数据集上，如 [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/)、[MS COCO](http://mscoco.org/home/)、[ILSVRC](http://image-net.org/index)， 都进行了测试。在检测时间（timing）、检测精度（accuracy）上，均与目前物体检测领域 state-of-art 的检测方法进行了比较。

## SSD框架及训练方法

SSD输出：一系列固定大小的bboxes，以及每个box的score（包含物体实例的可能性），我们看到的图片中标注出的boxes是经过非极大值抑制（Non-maximum suppression）的结果，即选择IOU大于某个阈值的所有boxes中，score最高的box，得到最终的predictions。

### SSD Model

- base network：

  用于图像分类的标准架构，作用是提取浅层特征；

- Multi-scale feature  maps for detection

  在base network之后添加的额外卷积层，大小逐层递减，用于在多尺度下进行预测；

- Convolutional predictors for detection

  对每一个feature map，使用一系列卷积核产生一系列固定大小的predictions

- Default boxes and aspect ratios

  相对于与其对应的 feature map cell 的位置是固定的。在每一个 feature map cell 中，我们要 predict 得到的 box 与 default box 之间的 offsets，以及每一个 box 中包含物体的 score（每一个类别概率都要计算出）。因此，对于一个位置上的 k 个boxes 中的每一个 box，我们需要计算出 c 个类，每一个类的 score，还有这个 box 相对于它的默认 box 的 4 个偏移值（offsets）。于是，在 feature map 中的每一个 feature map cell 上，就需要有$ (c+4)×k(c+4)×k $个 filters。对于一张 $m×n$ 大小的 feature map，即会产生 $(c+4)×k×m×n$ 个输出结果。

## 训练

SSD训练集当中人工标注的ground truths需要绑定到固定输出的boxes上，即以：fixed-size bounding boxes + offsets的形式输出。

### Matching strategy

在输入的时候，将具有`best jaccard overlap`（即最大交并比）的一对groundtruth box和default box匹配，用匹配的default box表示GT；然后将每一个default box与任何jaccard overlap大于一个阈值的所有GT配对，简化了训练（这里没太懂，之后再回来看）；

### Training objective

根据上面的Matching strategy，一个default box可能匹配多个GT，反过来，一个GT也可能对应多个default boxes，那么总的目标损失函数定义如下：
$$
\begin{equation}
L(x, c, l, g)=\frac{1}{N}\left(L_{c o n f}(x, c)+\alpha L_{l o c}(x, l, g)\right)
\end{equation}
$$
其中：

- N是与GT匹配的 default boxes 个数
- $L_{loc}$代表localization loss (loc)，Smooth L1 Loss，用于回归bounding boxes 的参数
- $\begin{equation}L_{c o n f}(x, c)\end{equation}$代表 confidence loss (conf)，是 softmax loss，输入为每一类的置信度$c$
- $\alpha$为权重项，SSD原文中设置为1

### Choosing scales and aspect ratios for default boxes

大部分 CNN 网络在越深的层，feature map 的尺寸（size）会越来越小。这样做不仅仅是为了减少计算与内存的需求，还有个好处就是，最后提取的 feature map 就会有某种程度上的平移与尺度不变性[^1]。

[^1]:由于conv层的卷积核对于特定的特征才会有较大激活值，所以不论 上一层特征图谱（feature map）中的某一特征平移到何处，卷积核都会找到该特征并在此处呈现较大的激活值。这应该就是“等变性”。而所谓的“尺度不变性”，是由类似于SSD这种对不同尺寸（分辨率）的feature map作相同的处理得到的。CNN本身并不具备尺度不变性。

同时为了处理不同尺度的物体，一些文章将图像转换成不同的尺度，将这些图像独立地通过 CNN 网络处理，再将这些不同尺度的图像结果进行综合。

而SSD同时使用lower feature maps, upper feature maps 来对目标进行预测。事实上，使用同一个网络中的、不同层上的 feature maps，也可以达到相同的效果，同时在所有物体尺度中共享参数。

一般来说，一个 CNN 网络中不同的 layers 有着不同尺寸的感受野（receptive fields）[^2]。在目标检测任务中，需要GT来进行回归与分类任务，而 GT 对应着 feature map 中的default boxes，然而只有被选定的 feature maps 需要执行回归与分类任务，因此也只有选定的 feature maps 需要 default boxes，那么如何选择每个 feature map 中的 default boxes 尺寸呢？

为了使模型可以处理不同尺度的对象，SSD设计 feature map 中的特定位置来负责图像中特定区域、特定物体尺寸的检测，解释如下：浅层的 feature map，尺寸较大，而感受野较小，因而采用小的 scale 可以使该特定位置检测原图像中一个较小的区域；反之，在深层的 feature map 中采用较大的 scale 可以检测很大的目标。

SSD同时还在 feature map 的同一位置设置了多个aspect ratio 的default boxes 用于贴合 GT 的形状。

### Hard negative mining

在生成一系列的 predictions 之后，会产生很多个匹配 ground truth box 的 predictions boxes，但同时，不匹配 ground truth boxes 也很多，而且这个 negative boxes，远多于 positive boxes。这会造成 negative boxes、positive boxes 之间的不均衡。训练时难以收敛。

因此，SSD 在训练中的做法是，对一个目标的所有 predictions 的负样本根据对应类别的  score 进行排序，保留 score 最高的几个，这背后的逻辑是保留最难检测的负样本（最容易被检测为正样本的负样本），保证最后正负样本的比例为$3:1$。

原文中通过实验发现，这样的比例可以更快的优化，训练也更稳定。

[^2]:卷积神经网络（CNN）中每层的卷积特征图（feature map）上的像素点在原始图像中映射的区域大小，也就相当于高层的特征图中的像素点受原图多大区域的影响。

### Data augmentation

原文中还对数据做了数据增广，对于每一张训练图像，随机地进行如下几种选择：

- 使用原始图像
- 采样一个 patch，使得它与 object 间的最小 jaccard overlap 为：0.1， 0.3， 0.5， 0.7， 0.9
- 随机采样一个 patch

采样的 patch 与原图的比例在 $[0.1,1]$之间，aspect ratio 在 $[0.5,2]$之间。

当 groundtruth box 的中心（center）在采样的 patch 中时，我们保留重叠部分。

在这些采样步骤之后，每一个采样的 patch 被 **resize** 到固定的大小，并且以 0.5 的概率被随机地水平翻转（horizontally flipped）。