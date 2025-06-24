# from huggingface_hub import hf_hub_download

# # 下载到 Downloads 文件夹
# file_path = hf_hub_download(
#     repo_id="mtgv/MobileVLM_V2_FT_Mix2M",          # 仓库名
#     filename="MobileVLM_V2_FT_Mix2M.json",         # 文件名
#     repo_type="dataset",                           # 类型是 dataset
#     local_dir="Downloads",                         # 下载到本地的 Downloads 目录
#     local_dir_use_symlinks=False                   # 避免软链接，直接复制文件
# )

# print(f"✅ File saved to: {file_path}")

import json

# 设置文件路径
file_path = 'MobileVLM_V2_FT_Mix2M.json'  # 根据实际路径修改

# 读取 JSON 文件
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 统计总样本数量
total_samples = len(data)
print(f"📊 Total number of samples: {total_samples}")

# 打印前三个样本
print("\n🔹 First 3 samples:")
for i, sample in enumerate(data[:3], 1):
    print(f"\nSample {i}:\n{json.dumps(sample, indent=2, ensure_ascii=False)}")

# 打印后三个样本
print("\n🔸 Last 3 samples:")
for i, sample in enumerate(data[-3:], total_samples - 2):
    print(f"\nSample {i}:\n{json.dumps(sample, indent=2, ensure_ascii=False)}")
