#!/bin/bash
#$ -q long
#$ -N QuaternaryPPO
#$ -pe smp 16

#module load python
#export TF_GPU_ALLOCATOR=cuda_malloc_async
python3 train.py > output_train.txt
