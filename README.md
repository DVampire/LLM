# Introduction
Currently only alpaca-lora, official code reference https://github.com/tloen/alpaca-lora

# Train

## step1: Start Container
`docker run -it --gpus=all --name llm --shm-size="100g" --rm --cpus=32 -t llm:0.0.1 /bin/bash`

Note: `--name` <container_name>, you should pick a container name that no one else uses

## step2: Prepare Dataset
This JSON file is a list of dictionaries, each dictionary contains the following fields:
- `instruction`: `str`, describes the task the model should perform. Each of the instructions is unique.
- `input`: `str`, optional context or input for the task.
- `output`: `str`, the answer to the instruction.

Example:
```
{
    "instruction": "Use the given data to calculate the median.",
    "input": "[2, 3, 7, 8, 10]",
    "output": "The median of the given data is 7."
}
```
Reference: [alpaca_data_cleaned.json](alpaca_lora%2Fdatasets%2Falpaca_data_cleaned.json)
Then put it in the `alpaca_lora/datasets` directory

## Step3: Start Train
Modify the run script:

`CUDA_VISIBLE_DEVICES=0 torchrun --nproc_per_node=1 finetune.py --base_model 'decapoda-research/llama-7b-hf' --data_path 'datasets/alpaca_data_cleaned.json' --output_dir './workspace/exp1'`

`--data_path` should be the relative path to the json file of your data.

Then,

`sh finetune.sh`