# PPO_GPR

**PPO_GPR** implements a Proximal Policy Optimization (PPO) reinforcement-learning agent combined with Gaussian Process Regression (GPR) for value-function approximation and uncertainty quantification.

## Overview
This project provides:
- **`scripts/`** – Python scripts for data preprocessing, model training (PPO & GPR), and evaluation.
- **`dataset/`** – Raw and processed data files used by the training scripts.


## Prerequisites
- **Python 3.8+**  
- Unix-like OS (Linux/macOS) or Windows with WSL  
- **CUDA** (optional, for GPU acceleration)  
- ≥ 8 GB RAM and ≥ 10 GB free disk space  

## Installation
1. **Clone the repository**  
   ```bash
   git clone https://github.com/theOsaroJ/PPO_GPR.git
   cd PPO_GPR

2. **Install requirements**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt

3. **Train the PPO agent**
   ```bash
   python train.py [users can modify the configurations in the train.py file], for example:
   
   config = {
    'GPR_batch': 10,
    'total_timesteps': 2000,
    'n_steps': 10,
    'checkpoint': 100,}

   Also edit data path in file with this function:
   def train(wandb_usage=False):
    prior_path = '../dataset/Prior.csv'
    test_path = '../dataset/Test.csv'
    best_train_prior_path = '../results/best_prior_train.csv'
   
4. **Evaluate PPO model**
   ```bash
   python3 evaluate.py
