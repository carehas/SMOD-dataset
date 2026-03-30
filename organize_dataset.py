import os
import shutil
from pathlib import Path

src_day = "/mnt/win11/e/files/SMOD-dataset/day"
src_night = "/mnt/win11/e/files/SMOD-dataset/night"
dst_infrared = "/home/yms/workspace/files/SMOD-dataset/images/infrared"
dst_visible = "/home/yms/workspace/files/SMOD-dataset/images/visible"

os.makedirs(dst_infrared, exist_ok=True)
os.makedirs(dst_visible, exist_ok=True)

for src_dir, prefix in [(src_day, "day"), (src_night, "night")]:
    for fname in os.listdir(src_dir):
        src_path = os.path.join(src_dir, fname)
        name, ext = os.path.splitext(fname)
        new_name = f"{prefix}_{name}{ext}"
        if name.endswith("_tir"):
            shutil.copy2(src_path, os.path.join(dst_infrared, new_name))
        elif name.endswith("_rgb"):
            shutil.copy2(src_path, os.path.join(dst_visible, new_name))

print("Done")
