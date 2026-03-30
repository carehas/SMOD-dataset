import os
import re
from pathlib import Path

def rename_images_recursive(folder_path):
    """
    支持以下格式重命名：
        day_000001_tir.jpg   → day_000001.jpg
        day_000001_rgb.jpg   → day_000001.jpg
        night_000000_tir.jpg → night_000000.jpg
        night_000000_rgb.jpg → night_000000.jpg
    """
    # 正确的正则表达式
    pattern = re.compile(r'^(day|night)_(\d{6})_(tir|rgb)\.(\w+)$', re.IGNORECASE)
    
    renamed_count = 0
    skipped_count = 0
    
    print(f"开始递归处理文件夹: {folder_path}\n")
    
    for root, dirs, files in os.walk(folder_path):
        current_folder = Path(root)
        
        for filename in files:
            file_path = current_folder / filename
            
            match = pattern.match(filename)
            if match:
                prefix = match.group(1)   # day 或 night
                number = match.group(2)   # 000001
                suffix = match.group(3)   # tir 或 rgb
                ext = match.group(4)      # jpg
                
                base_name = f"{prefix}_{number}"
                new_filename = f"{base_name}.{ext}"
                new_file_path = file_path.with_name(new_filename)
                
                # 防止覆盖已有文件
                if new_file_path.exists():
                    print(f"⚠️  跳过（目标已存在）: {file_path.relative_to(folder_path)}")
                    skipped_count += 1
                else:
                    try:
                        file_path.rename(new_file_path)
                        print(f"✅ 重命名成功: {filename} → {new_filename}")
                        renamed_count += 1
                    except Exception as e:
                        print(f"❌ 重命名失败: {filename} → 错误: {e}")
                        skipped_count += 1
            else:
                # 只显示可能的图片文件跳过信息，避免输出太多无关文件
                if file_path.suffix.lower() in {'.jpg', '.jpeg', '.png', '.tiff', '.bmp', '.webp'}:
                    print(f"⏭️  跳过（格式不匹配）: {file_path.relative_to(folder_path)}")
                skipped_count += 1   # 所有不匹配的文件都计入跳过
    
    print("\n" + "="*70)
    print(f"处理完成！")
    print(f"成功重命名: {renamed_count} 个文件")
    print(f"跳过文件: {skipped_count} 个")
    print("="*70)


# ====================== 使用 ======================
if __name__ == "__main__":
    # ==================== 修改这里 ====================
    folder = r"/home/yms/workspace/files/SMOD/images/visible"     # ←←← 把你的实际路径填在这里
    
    # 如果想每次运行时输入路径，可以把上面一行注释掉，取消下面一行的注释：
    # folder = input("请输入文件夹完整路径: ").strip().strip('"')
    
    if os.path.exists(folder):
        rename_images_recursive(folder)
    else:
        print(f"错误：文件夹不存在 → {folder}")