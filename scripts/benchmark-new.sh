#!/usr/bin/env bash

WORK_DIR=$(cd "$(dirname "$0")/.."; pwd)
export PYTHONPATH=${WORK_DIR}
CONV_MODE=v1
cd ${WORK_DIR}

for step in 2000 4000 6000 8000 10000 12000 14000; do
  CHCEKPOINT_PATH=/home/onsi/jsun/MobileVLM/outputs/mobilevlm_v2-2.finetune-1584K/checkpoint-${step}
  OUTPUT_DIR_EVAL=/home/onsi/jsun/MobileVLM/outputs/mobilevlm-3.evaluation-1584k/checkpoint-${step}
  mkdir -p ${OUTPUT_DIR_EVAL}

  echo "🧪 Evaluating checkpoint-${step}..."

  for dataset in mme gqa textvqa pope mmbench sqa; do
    case $dataset in
      mme)
        MODEL_GENERATOR=mobilevlm.eval.model_vqa_loader
        DATA_ROOT=${WORK_DIR}/dataset/benchmark_data/mme
        SPLIT_NAME=llava_mme
        ;;
      gqa)
        MODEL_GENERATOR=mobilevlm.eval.model_vqa_loader
        DATA_ROOT=${WORK_DIR}/dataset/benchmark_data/gqa
        SPLIT_NAME=llava_gqa_testdev_balanced
        ;;
      textvqa)
        MODEL_GENERATOR=mobilevlm.eval.model_vqa_loader
        DATA_ROOT=${WORK_DIR}/dataset/benchmark_data/textvqa
        SPLIT_NAME=llava_textvqa_val_v051_ocr
        ;;
      pope)
        MODEL_GENERATOR=mobilevlm.eval.model_vqa_loader
        DATA_ROOT=${WORK_DIR}/dataset/benchmark_data/pope
        SPLIT_NAME=llava_pope_test
        ;;
      mmbench)
        MODEL_GENERATOR=mobilevlm.eval.model_vqa_mmbench
        DATA_ROOT=${WORK_DIR}/dataset/benchmark_data/mmbench
        SPLIT_NAME=mmbench_dev_en_20231003
        ;;
      sqa)
        MODEL_GENERATOR=mobilevlm.eval.model_vqa_science
        DATA_ROOT=${WORK_DIR}/dataset/benchmark_data/sqa
        SPLIT_NAME=llava_test_CQM-A
        ;;
    esac

    echo "➡️  Running ${dataset}..."
    CUDA_VISIBLE_DEVICES=0,1,2,3 bash scripts/benchmark/${dataset}.sh \
      ${MODEL_GENERATOR} ${CHCEKPOINT_PATH} ${CONV_MODE} ${SPLIT_NAME} ${DATA_ROOT} ${OUTPUT_DIR_EVAL}/${dataset}
  done
done
