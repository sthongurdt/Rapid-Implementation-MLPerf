<div align="center">

# MLPerf Implementation Guide

**Multi-Device Testing with a Synthetic Dataset**

[![Artifact Type](https://img.shields.io/badge/Artifact-Methodology-blue)](#)
[![Artifact Evaluation](https://img.shields.io/badge/AE-Ready-success)](#)
[![Reproducibility](https://img.shields.io/badge/Reproducibility-High-brightgreen)](#)
[![MLPerf](https://img.shields.io/badge/Benchmark-MLPerf-orange)](https://mlcommons.org/en/mlperf/)
[![Docker](https://img.shields.io/badge/Container-Docker-informational)](https://www.docker.com/)

</div>

---

## Purpose of This Repository

This repository provides a **practical guide for running MLPerf inference benchmarks** on **different types of devices** using Docker-based workflows and a **synthetic dataset**.  
It is designed to support **experimental reproducibility**, **rapid validation**, and **Artifact Evaluation (AE)** in academic contexts.

The main objective is to **reduce setup complexity** while preserving a clear and repeatable methodology across heterogeneous platforms.

---

## What Is Included

This repository is organized around two main components that support multi-device testing and dataset preparation.

### Directory Structure

```text
.
├── device/
│   └── Dockerfiles adapted for different devices and architectures
│
├── tools/
│   └── Shell script for generating a synthetic dataset
│
└── README.md
```

---

## Device-Specific Configuration
The `device/` directory contains Dockerfiles customized for each tested device.
These Dockerfiles account for differences in:
- Hardware architecture (e.g., x86, ARM)
- Available compute resources (CPU, GPU, edge devices)
- Framework support and runtime dependencies
- Operating system constraints
Each Dockerfile follows the same logical structure but may include device-specific optimizations or limitations to ensure correct execution and reproducibility.

---

## Synthetic Dataset Configuration
The `tools/` directory contains a shell script used to generate a synthetic dataset compatible with MLPerf inference benchmarks.
Key characteristics of this dataset:
- Provides approximately 90% accuracy
- Enables fast and lightweight testing
- Reduces storage and download requirements
- Is suitable for functional validation and comparative analysis
This dataset is intended for rapid experimentation and artifact evaluation.
For higher accuracy or production-grade experiments, users are encouraged to consult the official MLPerf documentation and generate or download custom datasets.

---

# Recommended Workflow
The recommended workflow for using this repository is as follows:
- Select the appropriate Dockerfile from the `device/` directory based on the target hardware.
- Build the Docker image using the selected Dockerfile.
- Use the script in the `tools/` directory to generate the synthetic dataset.
- Mount the dataset into the Docker container.
- Execute the MLPerf inference benchmark inside the container.
This workflow ensures consistency across experiments while allowing controlled variation across devices.

---

# Notes on Test Execution
The method used to launch the MLPerf tests may vary depending on the target device.
Differences may include:
- Execution command syntax
- Runtime parameters
- Resource allocation (CPU cores, memory, accelerators)
- Framework-specific options
These variations are expected and necessary due to hardware heterogeneity.
However, the overall methodology, dataset, and evaluation criteria remain consistent, ensuring comparability and reproducibility across devices.

---

## Reproducibility and Artifact Evaluation
This repository is designed to support:
- Scripted and repeatable workflows
- Container-based isolation
- Transparent device-specific adaptations
- Academic artifact evaluation and result verification
Any deviations from the provided workflow should be clearly documented when reporting results.

---

## Disclaimer
The provided synthetic dataset is intended for rapid testing and validation.
It does not replace official MLPerf datasets for full compliance or leaderboard submissions.
