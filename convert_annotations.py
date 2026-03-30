import json


def convert_coco_to_yolo(bbox, img_width, img_height):
    x, y, w, h = bbox
    center_x = (x + w / 2) / img_width
    center_y = (y + h / 2) / img_height
    normalized_w = w / img_width
    normalized_h = h / img_height
    return center_x, center_y, normalized_w, normalized_h


def convert_file_name(file_name):
    return file_name.replace("/", "_").replace(".jpg", ".txt")


def convert_annotations(json_file, output_dir):
    with open(json_file, "r") as f:
        data = json.load(f)

    images = {img["id"]: img for img in data["images"]}
    categories = {cat["id"]: cat["name"] for cat in data["categories"]}

    image_annotations = {}
    for ann in data["annotations"]:
        image_id = ann["image_id"]
        if image_id not in image_annotations:
            image_annotations[image_id] = []
        image_annotations[image_id].append(ann)

    for img_id, img_info in images.items():
        file_name = img_info["file_name"]
        width = img_info["width"]
        height = img_info["height"]

        txt_file_name = convert_file_name(file_name)
        output_path = f"{output_dir}/{txt_file_name}"

        with open(output_path, "w") as f:
            if img_id in image_annotations:
                for ann in image_annotations[img_id]:
                    category_id = ann["category_id"]
                    class_id = category_id - 1
                    bbox = ann["bbox"]
                    center_x, center_y, w, h = convert_coco_to_yolo(bbox, width, height)
                    f.write(
                        f"{class_id} {center_x:.6f} {center_y:.6f} {w:.6f} {h:.6f}\n"
                    )

    print(f"Converted {len(images)} images from {json_file}")


convert_annotations(
    "/mnt/win11/e/files/SMOD-dataset/anno/new_train_annotations_rgb.json",
    "/home/yms/workspace/files/SMOD-dataset/labels/train",
)

convert_annotations(
    "/mnt/win11/e/files/SMOD-dataset/anno/new_test_annotations_rgb.json",
    "/home/yms/workspace/files/SMOD-dataset/labels/test",
)
