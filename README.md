<div align="center">
RSI MLPerf
</div>

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Artifact Type](https://img.shields.io/badge/Artifact-Evaluation-blue)](#)
[![Reproducibility](https://img.shields.io/badge/Reproducibility-High-success)](#)
[![MLPerf](https://img.shields.io/badge/Benchmark-MLPerf-orange)](https://mlcommons.org/en/mlperf/)

**Rapid and Simple Implementation of MLPerf**

---

## Overview
RSI MLPerf provides a **rapid and simple recipe** for implementing **MLPerf benchmarks** on a wide range of devices, including **edge**, **fog**, and **traditional computing platforms**. The primary goal of this repository is to **simplify deployment, execution, and result collection**, reducing the technical overhead typically required to run MLPerf workloads.

The proposed approach focuses on **reproducibility and ease of use**, enabling researchers to obtain **comparable, verifiable, and repeatable results** with minimal configuration effort. By standardizing the main stages of the benchmarking process—environment preparation, benchmark execution, and result collection—RSI MLPerf ensures consistency across different devices and experimental runs.

This repository is particularly intended for **researchers with limited time or resources**, such as those performing experimental validation, comparative analysis, or artifact evaluation. The recipe lowers the entry barrier to MLPerf benchmarking while preserving **methodological rigor**, making it suitable for academic experimentation and reproducibility-focused research.

---

## Scope and Objectives
The main objectives of RSI MLPerf are:
- To provide a **lightweight and fast setup** for MLPerf benchmarking.
- To support **heterogeneous devices** and architectures.
- To improve **experiment reproducibility** through standardized workflows.
- To reduce manual configuration and environment inconsistencies.
- To facilitate **Artifact Evaluation (AE)** and experimental validation.

---

## Repository Structure
The repository is organized as follows:
```
.
├── docker/
│   └── Rapid deployment recipes for x86-64 platforms
│
├── update/
│   ├── Dockerfiles for different devices and architectures
│   └── Shell scripts for basic dataset configuration
│
├── result/
│   ├── Benchmark results for multiple devices and scenarios
│   ├── CSV files with power consumption measurements
│   └── Scripts for energy consumption and carbon footprint analysis
│
└── README.md
```

## How to Use
MLPerf benchmarks can be executed using different approaches. In this repository, Docker-based execution is the recommended method due to its portability, automation capabilities, and reproducibility.
Docker allows MLPerf environments to be packaged as containers, simplifying dependency management and ensuring consistent runtime conditions across devices. This approach is especially suitable for:
- Rapid experimentation
- Automated benchmarking pipelines
- Container-based research infrastructures
- Artifact evaluation and result validation

Users can either:
- Use predefined Docker recipes provided in this repository, or
- Build custom Docker images tailored to specific hardware or software requirements.
Detailed instructions and scripts are provided in each directory to guide users through the execution process.

---

## Reproducibility and Artifact Evaluation
This repository is designed with reproducibility as a core principle:
- All benchmark workflows are scripted.
- Results are stored in structured and machine-readable formats (CSV).
- Energy and carbon footprint measurements are explicitly supported.
- Configuration steps are minimized and documented.
These characteristics make RSI MLPerf suitable for academic artifacts, including submissions requiring Artifact Evaluation (AE), experimental replication, and performance comparison studies.

---

## Requirements
- Docker (recommended)
- Linux-based operating system
- Supported hardware (CPU, GPU, edge, or fog devices depending on the recipe)
- MLPerf-compatible datasets (configured via provided scripts)

---

## License
This project is released under the MIT License.

---

## Citation
If you use this repository in your research, please cite it as follows:
```
RSI MLPerf: Rapid and Simple Implementation of MLPerf. Repository: https://github.com/sthongurdt/Rapid-Implementation-MLPerf
```

---

## Acknowledgements
This work builds upon the MLPerf benchmarking suite provided by MLCommons and aims to contribute a simplified and reproducibility-oriented workflow for academic research.
