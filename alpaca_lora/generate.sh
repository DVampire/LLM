CUDA_VISIBLE_DEVICES=0 \
python generate.py \
  --base_model 'decapoda-research/llama-7b-hf' \
  --lora_weights 'output_dir/mcwiki'