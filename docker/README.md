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
