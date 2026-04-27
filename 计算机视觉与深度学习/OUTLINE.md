# 计算机视觉与深度学习 · 课程大纲

参考：Stanford CS231N — Convolutional Neural Networks for Visual Recognition

## 前置工具章

| # | 章 | 内容 |
|---|-----|------|
| 00A | NumPy 基础 | 张量创建/变形/索引、广播、线性代数、随机数 |
| 00B | PyTorch 基础 | Tensor、Autograd、nn.Module、DataLoader、GPU 使用 |
| 00C | 训练流程实战 | MNIST 全流程：数据加载 → 模型定义 → 训练循环 → 验证 → 可视化 |

## 正文章节

| # | 章 | 内容 |
|---|-----|------|
| 01 | 图像分类与数据驱动方法 | kNN 分类器、线性分类器、损失函数 |
| 02 | 反向传播与计算图 | 链式法则、计算图、自动微分 |
| 03 | 卷积神经网络 (CNN) | 卷积层、池化层、全连接层、感受野 |
| 04 | CNN 架构演进 | AlexNet → VGG → GoogLeNet → ResNet → EfficientNet |
| 05 | 训练技巧 | BN、Dropout、数据增强、学习率调度、迁移学习 |
| 06 | 目标检测 | R-CNN 家族、YOLO、SSD、mAP 指标 |
| 07 | 图像分割 | FCN、U-Net、DeepLab、语义/实例分割 |
| 08 | 生成模型 | VAE、GAN、扩散模型简介 |
| 09 | 自监督学习与对比学习 | SimCLR、MoCo、MAE |
| 10 | Vision Transformer | ViT、Swin Transformer、多模态 (CLIP) |
