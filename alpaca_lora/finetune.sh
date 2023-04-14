CUDA_VISIBLE_DEVICES=0 \
torchrun --nproc_per_node=1 \
finetune.py \
    --base_model 'decapoda-research/llama-7b-hf' \
    --data_path 'datasets/alpaca_data_cleaned.json' \
    --output_dir './workspace/exp1'