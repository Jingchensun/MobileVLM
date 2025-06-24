import json

# 设置文件路径
file_path = 'MobileVLM_V2_FT_Mix2M.json'  # 原始文件路径
output_path = 'filtered_sam_images.json'  # 输出保存路径

# 读取 JSON 文件
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 过滤出 image 字段以 'sam/images' 开头的样本
filtered_data = [sample for sample in data if str(sample.get("image", "")).startswith("sam/images")]

# 保存过滤后的数据
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(filtered_data, f, ensure_ascii=False, indent=2)

# 输出结果信息
print(f"✅ Number of filtered samples (image starts with 'sam/images'): {len(filtered_data)}")
if filtered_data:
    print("\n🔹 First 3 filtered samples:")
    for i, sample in enumerate(filtered_data[:3], 1):
        print(f"\nSample {i}:\n{json.dumps(sample, indent=2, ensure_ascii=False)}")
