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

## Dataset curation
- Pick Prior data and put into dataset folder
- The remaining data should also be kept in a csv file, shuffled and perhaps split into validation (testing) and unlabeled data using the 

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

   NOTE: USERS NEED TO MODIFY gpmodel_class.py to reflect the training columns they have for their day. In our case, it has been X1-X4 /X5 in our case.
   
4. **Evaluate PPO model**
   ```bash
   python3 evaluate.py

5. **Get best training data**
   - pick the idx from best_prior_eval.csv based on user level of accuracy and amount of training data
   - put this list into of export_prior_from_idx.py and the same batch size used in training
   - run and get the final training data
   ```bash
   python export_prior_from_idx.py



