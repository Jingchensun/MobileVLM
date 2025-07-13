#!/bin/bash

# SLURM job directives
#SBATCH --job-name=mob-train                     # 作业名称
#SBATCH --output=train.out                   # 输出日志文件
#SBATCH --error=train.err                    # 错误日志文件
#SBATCH --ntasks=1                             # 启动 1 个任务
#SBATCH --cpus-per-task=8                      # 每个任务 8 个 CPU 核心
#SBATCH --mem-per-cpu=24GB                     # 每个 CPU 核心分配 16GB 内存
#SBATCH --time=1-18:00:00                        # 运行时间（1小时）
#SBATCH --partition=prod_long                       # 分区设置（prod 分区）
#SBATCH --gres=shard:16                           # 请求 4 个 GPU


# 加载 Conda 环境
export PATH=/usr/local/cuda-11.8/bin:$PATH   #
export CUDA_HOME=/usr/local/cuda-11.8   # 
export CUDA=1
export PATH=/home/onsi/jsun/miniconda3/envs/mobilevlm/bin:$PATH  # Conda 环境路径
source /home/onsi/jsun/miniconda3/bin/activate mobilevlm         # 激活 Conda 环境

LANGUAGE_MODEL=mtgv/MobileLLaMA-1.4B-Chat  # or 2.7B
VISION_MODEL=openai/clip-vit-large-patch14-336
# bash run.sh mobilevlm_v2_1.7b pretrain-finetune-test ${LANGUAGE_MODEL} ${VISION_MODEL}
bash run.sh mobilevlm_v2_1.7b finetune ${LANGUAGE_MODEL} ${VISION_MODEL}
bash run.sh mobilevlm_v2_1.7b test ${LANGUAGE_MODEL} ${VISION_MODEL}