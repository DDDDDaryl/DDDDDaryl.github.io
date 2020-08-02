---
title: YOLOv4
date: 2020-05-27 15:49:22
categories:
- DeepLearning
tags:
- YOLO
---

# YOLOv4 学习笔记

论文地址：https://arxiv.org/abs/2004.10934

## TODO

- CBN
- SAM

## 概述

论文主要贡献：

1. 以提升生产系统中目标检测器的速度以及优化并行计算，而不是优化 BFLOPS（十亿次浮点数运算）。构建的目标检测模型降低了训练对硬件的限制；
2. 检测器训练时，验证了最先进的Bag-of Freebies and Bag-of-Specials目标检测方法的影响。
3. 对一些先进的方法进行修改，包括CBN、PAN、SAM，使得它们更加的高效并适合单GPU运算。

> A modern detector is usually composed of two parts, a backbone which is pre-trained on ImageNet and a head which is used to predict classes and bounding boxes of objects.

当前的检测器通常由两部分组成：

- 在 ImageNet 上预训练的主干网络 (backbone)
- 用来预测物体类别以及 bbox 的头部

运行在不同平台上的模型所常用的 backbone：

- GPU 平台：
  - VGG
  - ResNet
  - ResNeXt
  - DenseNet
- CPU 平台
  - SqueezeNet
  - MobileNet
  - ShuffleNet

检测头一般分为单阶段和双阶段目标检测器：

- 双阶段：
  - fast R-CNN
  - faster R-CNN
  - R-FCN
  - Libra R-CNN
- 单阶段：
  - YOLO
  - SSD
  - RetinaNet

近年来，目标检测器通常是在头部和主干网络之间加入一些层，这些层被用来收集不同阶段的特征图。采用这种机制的网络包括 FPN, PAN, BiFPN 和 NAS-FPN。

> Usually, a conventional object detector is trained offline. Therefore, researchers always like to take this advantage and develop better training methods which can make the object detector receive better accuracy without increasing the inference cost. We call these methods that only change the training strategy or only increase the training cost as “bag of freebies.” 

只改变训练策略或者仅仅增加训练强度的方法叫做 bag of freebies。

比如：

- 数据增强，data augmentation
- hard negative example mining，focal loss 等解决正负样本不平衡
- BBox regression 中的 IoU loss，避免 l1 loss 和 l2 loss 对 scale 的敏感性

> For those plugin modules and post-processing methods that only increase the inference cost by a small amount but can signiﬁcantly improve the accuracy of object detection, we call them “bag of specials”. Generally speaking, these plugin modules are for enhancing certain attributes in a model, such as enlarging receptive ﬁeld, introducing attention mechanism, or strengthening feature integration capability, etc., and post-processing is a method for screening model prediction results. 

只增加小幅推理成本（正向传播）但是可以显著提高目标检测准确度的，增加模块或者预处理的方法叫做 bag of specials。