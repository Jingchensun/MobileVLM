#!/usr/bin/env bash

WORK_DIR=$(cd "$(dirname "$0")/..";pwd)
export PYTHONPATH=${WORK_DIR}
# CHCEKPOINT_PATH=/home/onsi/jsun/checkpoints/mobilevlm/MobileVLM_V2-1.7B
# CHCEKPOINT_PATH=/home/onsi/jsun/MobileVLM/outputs/mobilevlm_v2_1.7b_20250624_210606/mobilevlm_v2-1.pretrain
CHCEKPOINT_PATH=/home/onsi/jsun/MobileVLM/outputs/mobilevlm_v2_1.7b_20250702_224652/mobilevlm_v2-2.finetune/checkpoint-14000
OUTPUT_DIR_EVAL=/home/onsi/jsun/MobileVLM/outputs/mobilevlm-3.evaluation/checkpoint-14000
mkdir -p ${OUTPUT_DIR_EVAL}
CONV_MODE=v1
cd ${WORK_DIR}

DATASET_NAME=mme
MODEL_GENERATOR=mobilevlm.eval.model_vqa_loader
DATA_ROOT=${WORK_DIR}/dataset/benchmark_data/mme
SPLIT_NAME=llava_mme
CUDA_VISIBLE_DEVICES=0, bash scripts/benchmark/${DATASET_NAME}.sh \
    ${MODEL_GENERATOR} ${CHCEKPOINT_PATH} ${CONV_MODE} ${SPLIT_NAME} ${DATA_ROOT} ${OUTPUT_DIR_EVAL}/${DATASET_NAME}

DATASET_NAME=gqa
MODEL_GENERATOR=mobilevlm.eval.model_vqa_loader
DATA_ROOT=${WORK_DIR}/dataset/benchmark_data/gqa
SPLIT_NAME=llava_gqa_testdev_balanced
CUDA_VISIBLE_DEVICES=0 bash scripts/benchmark/${DATASET_NAME}.sh \
    ${MODEL_GENERATOR} ${CHCEKPOINT_PATH} ${CONV_MODE} ${SPLIT_NAME} ${DATA_ROOT} ${OUTPUT_DIR_EVAL}/${DATASET_NAME}

DATASET_NAME=textvqa
MODEL_GENERATOR=mobilevlm.eval.model_vqa_loader
DATA_ROOT=${WORK_DIR}/dataset/benchmark_data/textvqa
SPLIT_NAME=llava_textvqa_val_v051_ocr
CUDA_VISIBLE_DEVICES=0 bash scripts/benchmark/${DATASET_NAME}.sh \
    ${MODEL_GENERATOR} ${CHCEKPOINT_PATH} ${CONV_MODE} ${SPLIT_NAME} ${DATA_ROOT} ${OUTPUT_DIR_EVAL}/${DATASET_NAME}

DATASET_NAME=pope
MODEL_GENERATOR=mobilevlm.eval.model_vqa_loader
DATA_ROOT=${WORK_DIR}/dataset/benchmark_data/pope
SPLIT_NAME=llava_pope_test
CUDA_VISIBLE_DEVICES=0 bash scripts/benchmark/${DATASET_NAME}.sh \
    ${MODEL_GENERATOR} ${CHCEKPOINT_PATH} ${CONV_MODE} ${SPLIT_NAME} ${DATA_ROOT} ${OUTPUT_DIR_EVAL}/${DATASET_NAME}

DATASET_NAME=mmbench
MODEL_GENERATOR=mobilevlm.eval.model_vqa_mmbench
DATA_ROOT=${WORK_DIR}/dataset/benchmark_data/mmbench
SPLIT_NAME=mmbench_dev_en_20231003
CUDA_VISIBLE_DEVICES=0 bash scripts/benchmark/${DATASET_NAME}.sh \
    ${MODEL_GENERATOR} ${CHCEKPOINT_PATH} ${CONV_MODE} ${SPLIT_NAME} ${DATA_ROOT} ${OUTPUT_DIR_EVAL}/${DATASET_NAME}

DATASET_NAME=sqa
MODEL_GENERATOR=mobilevlm.eval.model_vqa_science
DATA_ROOT=${WORK_DIR}/dataset/benchmark_data/sqa
SPLIT_NAME=llava_test_CQM-A
CUDA_VISIBLE_DEVICES=0 bash scripts/benchmark/${DATASET_NAME}.sh \
    ${MODEL_GENERATOR} ${CHCEKPOINT_PATH} ${CONV_MODE} ${SPLIT_NAME} ${DATA_ROOT} ${OUTPUT_DIR_EVAL}/${DATASET_NAME}
