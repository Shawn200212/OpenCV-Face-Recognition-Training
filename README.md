# OpenCV Learning Exercises — Vision Effects & Face Recognition / OpenCV 学习练习——视觉效果与人脸识别

**English**

> **What this is:** my personal **learning exercises** for OpenCV's vision module and face-recognition
> module — a study repository, **not a production project**. I'm keeping it public as a record of how
> these fundamentals feed into my later work (YOLO pedestrian detection for the
> [Networked Cities workshop](https://github.com/Shawn200212/DigitalFutures-Workshop-Pedestrian-Activity-Prediction),
> and local TripoSR deployment via PyTorch).

The code is organized as **two modules**:

**中文**

> **项目定位：**这是我对 OpenCV 视觉模块和人脸识别模块的个人学习练习，不是生产项目。
> 公开保留它，是为了记录这些基础如何延伸到后续项目，例如
> [Networked Cities 工作营](https://github.com/Shawn200212/DigitalFutures-Workshop-Pedestrian-Activity-Prediction)
> 的 YOLO 行人检测，以及通过 PyTorch 本地部署 TripoSR。

代码分为两个模块。

## Module 1 · Vision display effects (16 progressive scripts) / 模块 1 · 视觉显示效果（16 个渐进脚本）

**English**

![Vision effects](docs/vision_effects_grid.jpg)

*Six of the operators covered, run on one training photo: grayscale conversion, Gaussian blur,
Canny edge detection, binary thresholding and the Laplacian gradient.*

| File | Topic |
| --- | --- |
| `ReadImages.py` / `ReadVideos.py` | Reading images & video streams |
| `rescale.py` | Resizing and frame rescaling |
| `draw.py` | Drawing shapes and text |
| `transformations.py` | Translation, rotation, flipping |
| `contours.py` | Contour detection |
| `Spaces.py` / `split_merge.py` | Color spaces, channel split & merge |
| `smoothing.py` / `bitwise.py` / `masking.py` | Blurring, bitwise ops, masking |
| `histogram.py` / `thresh.py` / `gradients.py` | Histograms, thresholding, edge gradients |
| `basic.py` / `test.py` | Basics & scratch tests |

**中文**

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

## Module 2 · Face recognition training (`face_recognition.py` and friends) / 模块 2 · 人脸识别训练

**English**

![Haar detection](docs/haar_detection_demo.jpg)

*Step 1 of the pipeline: the Haar cascade locates the face and crops the ROI that gets fed to
the LBPH recognizer.*

### Training set

![Training set](docs/train_set_sample.jpg)

```
Photo/Train/<person>/*.jpg          five celebrity folders, photos crawled from the web
   → haar_face.xml                  Haar cascade detects face ROIs      (face_detect.py)
   → grayscale ROIs + labels        collected per person                (Faces_train.py)
   → cv.face.LBPHFaceRecognizer     trained & persisted
   → face_trained.yml + features.npy + labels.npy
   → prediction with confidence     label + box drawn on the image      (face_recognition.py)
```

| File | Role |
| --- | --- |
| `face_detect.py` | Haar-cascade face detection on a single image |
| `Faces_train.py` | Build the training set from `Photo/Train/` and train the LBPH recognizer |
| `face_recognition.py` | Load the trained model and recognize faces with confidence scores |
| `haar_face.xml` | OpenCV frontal-face Haar cascade |

**About the training data** — `Photo/Train/` holds photos of five celebrities (Brad / Leonardo /
Tom / long zun / zhen zhang) crawled from the internet, used **only as an analysis source for this
coding exercise**. The photo set and the trained artifacts (`face_trained.yml`, `features.npy`,
`labels.npy`) are not distributed with the repo — point `Faces_train.py` at your own
`Photo/Train/<person>/` folders to reproduce.

**中文**

*流水线第一步：Haar 级联定位人脸并裁剪 ROI，再送入 LBPH 识别器。*

### 训练集


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

## Run / 运行

**English**

```bash
pip install opencv-contrib-python numpy
python Faces_train.py       # after preparing Photo/Train/<person>/
python face_recognition.py
```

---

🎨 **Portfolio — [ruixiaozhang.com](https://ruixiaozhang.com)** · game design, realtime animation, embodied AI and urban research
🎬 **YouTube — [project videos](https://www.youtube.com/channel/UCyr-ubod7eNa6XhET25vdmw)**

**中文**

```bash
pip install opencv-contrib-python numpy
python Faces_train.py       # 先准备 Photo/Train/<person>/
python face_recognition.py
```

---

🎨 **作品集：[ruixiaozhang.com](https://ruixiaozhang.com)** · 游戏设计、实时影像、具身智能与城市研究

🎬 **YouTube：[项目视频](https://www.youtube.com/channel/UCyr-ubod7eNa6XhET25vdmw)**
