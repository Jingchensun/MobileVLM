import os
import re
import pandas as pd

# 设置包含所有 distill-checkpoint-* 的根目录路径
root_dir = "/home/onsi/jsun/MobileVLM/outputs/mobilevlm-3.evaluation-1584k"

# 定义各项指标名称映射
metrics = ["MME", "GQA", "TextVQA", "POPE", "MMBench", "SQA"]
metric_map = {
    "MME": "MME",
    "GQA": "GQA",
    "TextVQA": "Text-VQA",
    "POPE": "POPE",
    "MMBench": "MMB",
    "SQA": "ScienceQA"
}

data = []

# 遍历所有 checkpoint 文件夹
for subdir in sorted(os.listdir(root_dir)):
    if subdir.startswith("checkpoint-"):
        result_path = os.path.join(root_dir, subdir, "results.txt")
        if os.path.exists(result_path):
            with open(result_path, "r") as f:
                lines = f.readlines()
            row = {"checkpoint": subdir}
            for line in lines:
                match = re.search(r"(\w+) metric:\s*([\d.]+)", line)
                if match:
                    metric, value = match.groups()
                    mapped_metric = metric_map.get(metric)
                    if mapped_metric:
                        row[mapped_metric] = float(value)
            # 如果所有指标都存在，则计算平均值
            values = [row.get(metric_map[m], None) for m in metrics]
            if all(v is not None for v in values):
                row["Avg."] = sum(values) / len(values)
            data.append(row)

# 构建 DataFrame 并保存为 CSV
df = pd.DataFrame(data)
columns_order = ["checkpoint", "MME", "GQA", "Text-VQA", "POPE", "MMB", "ScienceQA", "Avg."]
df = df.reindex(columns=columns_order)
df = df.sort_values("checkpoint")
df.to_csv("distill_eval_results.csv", index=False)

print("✅ Results saved to distill_eval_results.csv")
