# from huggingface_hub import hf_hub_download

# # 下载 ShareGPT4V 数据集中的 LFS 文件
# file_path = hf_hub_download(
#     repo_id="Lin-Chen/ShareGPT4V",
#     filename="share-captioner_coco_lcs_sam_1246k_1107.json",
#     repo_type="dataset",
#     local_dir="downloads",  # 可选：本地保存目录
#     local_dir_use_symlinks=False
# )

# print(f"✅ File downloaded to: {file_path}")

# from huggingface_hub import hf_hub_download

# file_path = hf_hub_download(
#     repo_id="liuhaotian/LLaVA-Pretrain",
#     filename="images.zip",                 # 文件名必须精确匹配
#     repo_type="dataset",                  # 指定为 dataset 类型
#     local_dir="./my_llava_data",          # 你希望保存的目录
#     local_dir_use_symlinks=False          # 避免使用符号链接，直接下载文件
# )

# print(f"✅ File downloaded to: {file_path}")


import json

# 指定文件路径（修改为你的实际路径）
file_path = "share-captioner_coco_lcs_sam_1246k_1107.json"

# file_path = "filtered_sam_samples.json"

# 读取 JSON 文件内容（假设是一个 JSON list 格式）
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# 统计总样本数量
total_samples = len(data)
print(f"✅ Total samples: {total_samples}\n")

# 打印前三个样本
print("🔹 First 3 samples:")
for sample in data[:3]:
    print(json.dumps(sample, indent=2, ensure_ascii=False))

# 打印最后三个样本
print("\n🔹 Last 3 samples:")
for sample in data[-3:]:
    print(json.dumps(sample, indent=2, ensure_ascii=False))
