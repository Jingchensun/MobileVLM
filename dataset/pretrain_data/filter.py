import json

# 原始 JSON 文件路径
input_path = "share-captioner_coco_lcs_sam_1246k_1107.json"
# 输出 JSON 文件路径
output_path = "filtered_llava_samples.json"

# 读取原始 JSON 数据
with open(input_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# 筛选出 image 路径以 "sam/images" 开头的样本
filtered_data = [sample for sample in data if sample.get("image", "").startswith("llava/llava_pretrain/images")]

# 保存为新的 JSON 文件
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(filtered_data, f, ensure_ascii=False, indent=2)

print(f"✅ Total filtered samples: {len(filtered_data)}")
print(f"📁 Saved to {output_path}")
