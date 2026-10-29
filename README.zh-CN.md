[English](README.md) | [简体中文](README.zh-CN.md)

<a id="opencv-learning-exercises--vision-effects--face-recognition--opencv-学习练习视觉效果与人脸识别"></a>
<a id="opencv-learning-exercises--vision-effects--face-recognition"></a>
<a id="opencv-学习练习视觉效果与人脸识别"></a>

# OpenCV 学习练习——视觉效果与人脸识别

> **项目定位：**这是我对 OpenCV 视觉模块和人脸识别模块的个人学习练习，不是生产项目。
> 公开保留它，是为了记录这些基础如何延伸到后续项目，例如
> [Networked Cities 工作营](https://github.com/Shawn200212/DigitalFutures-Workshop-Pedestrian-Activity-Prediction)
> 的 YOLO 行人检测，以及通过 PyTorch 本地部署 TripoSR。

代码分为两个模块。

<a id="module-1--vision-display-effects-16-progressive-scripts--模块-1--视觉显示效果16-个渐进脚本"></a>
<a id="module-1--vision-display-effects-16-progressive-scripts"></a>
<a id="模块-1--视觉显示效果16-个渐进脚本"></a>

## 模块 1 · 视觉显示效果（16 个渐进脚本）

*同一训练照片上的六种处理：灰度转换、高斯模糊、Canny 边缘检测、二值阈值与
Laplacian 梯度等。*

| 文件 | 主题 |
|---|---|
| `ReadImages.py` / `ReadVideos.py` | 读取图像与视频流 |
| `rescale.py` | 调整图像和视频帧尺寸 |
| `draw.py` | 绘制形状与文字 |
| `transformations.py` | 平移、旋转与翻转 |
| `contours.py` | 轮廓检测 |
| `Spaces.py` / `split_merge.py` | 色彩空间、通道拆分与合并 |
| `smoothing.py` / `bitwise.py` / `masking.py` | 模糊、位运算与遮罩 |
| `histogram.py` / `thresh.py` / `gradients.py` | 直方图、阈值与边缘梯度 |
| `basic.py` / `test.py` | 基础练习与临时测试 |

![视觉效果](docs/vision_effects_grid.jpg)

<a id="module-2--face-recognition-training-face_recognitionpy-and-friends--模块-2--人脸识别训练"></a>
<a id="module-2--face-recognition-training-face_recognitionpy-and-friends"></a>
<a id="模块-2--人脸识别训练"></a>

## 模块 2 · 人脸识别训练

*流水线第一步：Haar 级联定位人脸并裁剪 ROI，再送入 LBPH 识别器。*

### 训练集

![训练集](docs/train_set_sample.jpg)

```text
Photo/Train/<person>/*.jpg          五位名人的文件夹，照片来自网络
   → haar_face.xml                  Haar 级联检测人脸 ROI
   → 灰度 ROI + 标签                按人物收集
   → cv.face.LBPHFaceRecognizer     训练并持久化
   → face_trained.yml + features.npy + labels.npy
   → 带置信度的预测                 在图像上绘制标签与边框
```

| 文件 | 作用 |
|---|---|
| `face_detect.py` | 对单张图像执行 Haar 级联人脸检测 |
| `Faces_train.py` | 从 `Photo/Train/` 构建训练集并训练 LBPH 识别器 |
| `face_recognition.py` | 加载模型，以置信度识别人脸 |
| `haar_face.xml` | OpenCV 正面人脸 Haar 级联 |

**关于训练数据：**`Photo/Train/` 使用从网络获取的五位名人照片，只作为本编程练习的分析来源。
仓库不分发照片集和训练制品（`face_trained.yml`、`features.npy`、`labels.npy`）。
如需复现，请把 `Faces_train.py` 指向自己的 `Photo/Train/<person>/` 文件夹。

![Haar 检测](docs/haar_detection_demo.jpg)

<a id="run--运行"></a>
<a id="run"></a>
<a id="运行"></a>

## 运行

```bash
pip install opencv-contrib-python numpy
python Faces_train.py       # 先准备 Photo/Train/<person>/
python face_recognition.py
```

---

🎨 **作品集：[ruixiaozhang.com](https://ruixiaozhang.com)** · 游戏设计、实时影像、具身智能与城市研究

🎬 **YouTube：[项目视频](https://www.youtube.com/channel/UCyr-ubod7eNa6XhET25vdmw)**
