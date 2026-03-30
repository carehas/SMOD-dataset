# YOLO 类别映射

## 类别对照表

| 原始ID | 类别名称 | YOLO ID |
|--------|----------|---------|
| 1      | person   | 0       |
| 2      | rider    | 1       |
| 3      | bicycle  | 2       |
| 4      | car      | 3       |

行人、骑行者、自行车和汽车

## YOLO 标注格式

```
<class_id> <x_center> <y_center> <width> <height>
```

其中所有坐标值都已归一化（0-1范围）。

## 文件命名

标注文件名与对应图像名一致，格式为：
- 图像: `000000_rgb.jpg`
- 标注: `000000_rgb.txt`

不带文件夹前缀（如 `day/`）。

## 输出目录

```
anno/
├── labels/
│   ├── train/  (3700 个标注文件)
│   └── test/   (2676 个标注文件)
├── new_train_annotations_rgb.json
└── new_test_annotations_rgb.json
```
