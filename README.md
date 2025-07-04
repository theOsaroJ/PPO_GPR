# PPO_GPR

**PPO_GPR** implements a Proximal Policy Optimization (PPO) reinforcement-learning agent combined with Gaussian Process Regression (GPR) for value-function approximation and uncertainty quantification.

## Overview
This project provides:
- **`scripts/`** – Python scripts for data preprocessing, model training (PPO & GPR), and evaluation.
- **`dataset/`** – Raw and processed data files used by the training scripts.
- **`Examples/`** – Jupyter notebooks demonstrating end-to-end workflows.

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
