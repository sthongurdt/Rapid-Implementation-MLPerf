<div align="center">

# Testing Using Docker

**Rapid Execution of MLPerf Inference Benchmarks**

[![Artifact Type](https://img.shields.io/badge/Artifact-Methodology-blue)](#)
[![Reproducibility](https://img.shields.io/badge/Reproducibility-High-success)](#)
[![MLPerf](https://img.shields.io/badge/Benchmark-MLPerf-orange)](https://mlcommons.org/en/mlperf/)
[![Docker](https://img.shields.io/badge/Container-Docker-informational)](https://www.docker.com/)

</div>

---

## Purpose of This Document

This document describes the **methodology used to execute MLPerf inference tests** using Docker-based workflows.  
It is intended to serve as **methodological documentation** for a series of experiments and as supporting material for **Artifact Evaluation (AE)**.

The goal of this recipe is to enable **rapid, reproducible, and device-agnostic execution** of MLPerf tests, especially for researchers who need to validate results with limited setup time.

---

## Scope of the Methodology

This recipe focuses on:

- MLPerf **inference benchmarks**
- **CPU-based execution** as a baseline
- Multiple frameworks (TensorFlow and ONNX Runtime)
- Synthetic and real datasets
- Docker-based isolation for reproducibility

Although the example targets CPU execution, the same methodology can be adapted to **edge, fog, and accelerator-based devices** with minimal changes.

---

## System Requirements

The following requirements must be satisfied before starting:

- Linux-based operating system
- Docker installed and properly configured
- Internet access to download models and datasets
- Basic command-line tools

Install basic dependencies:

```bash
dnf install vim git -y
```

---

## Step 1 – Clone the MLPerf Inference Repository
Create a working directory and clone the MLPerf inference repository with submodules:
```bash
mkdir mlperf && cd mlperf/
git clone --recurse-submodules https://github.com/mlcommons/inference.git --depth 1
```
This repository provides the official MLPerf inference workloads and tools.

---

## Step 2 – Prepare Model Directories
Create directories to store models for different frameworks:
```bash
mkdir models && cd models/
mkdir tf onnx
```

---

## Step 3 – Download TensorFlow Models
Move to the TensorFlow directory and download the required models:
```bash
cd tf/
wget -q https://zenodo.org/record/2535873/files/resnet50_v1.pb
wget -q https://zenodo.org/record/2269307/files/mobilenet_v1_1.0_224.tgz
```
Decompress the MobileNet model:
```bash
tar -xzf mobilenet_v1_1.0_224.tgz ./mobilenet_v1_1.0_224_frozen.pb -C .
```

---

## Step 4 – Download ONNX Runtime Models
Move to the ONNX directory and download the models:
```bash
cd ../onnx
wget -q https://zenodo.org/record/4735647/files/resnet50_v1.onnx
wget -q https://zenodo.org/record/4735651/files/mobilenet_v1_1.0_224.onnx
```

---

## Step 5 – Prepare Dataset Directory
Create a directory to store datasets:
```bash
cd ../.. && mkdir data/
```

---

## Step 6 – Generate a Synthetic Dataset
Move to the MLPerf tools directory:
```bash
cd inference/vision/classification_and_detection/tools/
```
Backup the original script:
```bash
cp -p make_fake_imagenet.sh make_fake_imagenet.sh.$(date +%Y%m%d-%H%M%S)
```
Replace the contents of make_fake_imagenet.sh with the version provided in:
```bash
update/tools/make_fake_image.sh
```
Generate the dataset and move it to the data directory:
```bash
./make_fake_imagenet.sh
mv fake_imagenet/ ~/mlperf/data/
```

---

## Step (Optional) - Use Alternative Datasets
If real datasets are required, the following tools can be used:
```bash
./openimages_mlperf.sh -d <DOWNLOAD_PATH> -m <MAX_IMAGES>
./openimages_calibration_mlperf.sh -d <DOWNLOAD_PATH>
```
Example:
```bash
./openimages_mlperf.sh -d ../../../../data/openimages -m 100
./openimages_calibration_mlperf.sh -d ../../../../data/openimages
```

---

## Step 7 – Configure Environment Variables
Return to the inference directory:
```bash
cd ..
```
Set the model directory according to the framework:
### TensorFlow
```bash
export MODEL_DIR=../../../models/tf
```
### ONNX Runtime
```bash
export MODEL_DIR=../../../models/onnx
```
### Fake ImageNet Dataset
```bash
export DATA_DIR=../../../data/fake_imagenet/
```
### Other Datasets
```bash
export DATA_DIR=<DOWNLOAD_PATH>
```

---

## Step 8 – Adapt Dockerfiles and Execution Scripts
Before running the benchmark, the following files must be adapted:
- Dockerfile.*
- run_and_time.sh
Updated versions for each supported device are provided in:
```bash
update/docker/
```
These modifications ensure compatibility with different architectures, runtimes, and resource constraints.

---

## Step 9 – Run the MLPerf Inference Test
Execute the benchmark using the adapted script:
```bash
./run_and_time.sh onnxruntime mobilenet cpu --accuracy
```

---

# Notes on Execution Variability
The exact command, Docker configuration, and runtime parameters may vary depending on the target device, such as:
- CPU vs GPU
- Edge or fog devices
- ARM vs x86 architectures
- Memory and power constraints
For this reason, the test launch procedure should be adapted per device, while preserving the same methodological steps described in this document.
This flexibility is intentional and supports reproducibility across heterogeneous platforms.

---

# Reproducibility Statement
This methodology is designed to be:
- Script-based
- Deterministic in setup
- Portable across devices
- Suitable for academic artifact evaluation
Any deviations from the described steps should be documented alongside experimental results.

---

# Disclaimer
Initial executions may fail if the original MLPerf scripts are used without modification.
Ensure that the run_and_time.sh file is replaced with the version provided in this repository before running the tests.




```bash
```
