<div align="center">

# RSI MLPerf Benchmark Results

**Results Obtained Using the Proposed Docker-Based Methodology**

[![Artifact Type](https://img.shields.io/badge/Artifact-Results-blue)](#)
[![Artifact Evaluation](https://img.shields.io/badge/AE-Ready-success)](#)
[![Reproducibility](https://img.shields.io/badge/Reproducibility-High-brightgreen)](#)
[![MLPerf](https://img.shields.io/badge/Benchmark-MLPerf-orange)](https://mlcommons.org/en/mlperf/)
[![Docker](https://img.shields.io/badge/Container-Docker-informational)](https://www.docker.com/)

</div>

---

## Overview of the Results

This document presents the **results obtained from a series of MLPerf inference benchmarks** executed using the **methodology proposed in the `docker/` directory**, together with the **Dockerfiles and dataset configuration provided in the `update/` directory**.
Although the numerical values obtained during execution may differ slightly from those reported in the tables, the proposed recipe ensures that the **benchmarking process is reproducible, consistent, and portable** across different environments and devices.
Minor variations in results are expected due to external and environmental factors, including:
- Power supply stability  
- Ambient temperature during execution  
- Thermal dissipation efficiency  
These factors have a **stronger impact on embedded and edge devices**, where performance and energy consumption are more sensitive to external conditions.

---

## Glossary
- **HW** – Hardware  
- **ORT** – ONNX Runtime  
- **TF** – TensorFlow  
- **MOB** – MobileNet  
- **RES** – ResNet50  

---

## Methodological Context
The results should be interpreted as part of a **multi-layered benchmarking methodology** designed to evaluate not only performance, but also the **environmental cost of AI inference at the edge and fog layers**.
The methodology consists of the following stages.

---

## 1. Hardware Selection
The experiments were conducted on multiple hardware platforms representing different levels of the **Edge–Fog–HPC continuum**.
- **Low-Power CPU (Edge)**  
  Raspberry Pi 4 (RPI), representing widely available and low-cost IoT hardware.
- **Entry-Level GPU (Edge AI)**  
  NVIDIA Jetson Nano 2GB, selected to evaluate hardware optimized for AI inference at the edge.
- **High-Performance CPU/GPU (Fog / Edge / HPC)**  
  PU-based systems, representing upper-tier fog computing resources, advanced edge devices, and HPC-class environments.
**Table 1** summarizes the main characteristics of the evaluated devices.

Table 1. Description of the Devices Evaluated
| Device   | CPU                       | RAM   | Others                                             | NET                 |
|----------|---------------------------|-------|----------------------------------------------------|---------------------|
| Laptop   | i5 10300H                 | 32 GB | 512 GB SSD, GTX 1650ti                             | 1GbE                |
| RPi      | ARM Cortex-A72            | 8 GB  | 128 GB SDcard, VideoCore VI                        | 1GbE                |
| Nano     | ARM® Cortex-A57           | 2 GB  | 128 GB SDcard, Maxwell (128 núcleos CUDA)          | 10GbE               |
| Nova     | 2 x Intel Xeon E5-2620 v4 | 64 GB | 557 GB HDD                                          | 10GbE               |
| Neowise  | AMD EPYC 7642             | 512 GB| 1788 GB SSD, 8 GPUs Radeon Instinct MI50           | 2 x 10GbE           |
| ExaDell  | 2 x AMD EPYC 9534         | 376 GB| 2 x Instinct MI210                                  | Infiniband 200Gbps  |
| ExaSM    | 2 x AMD EPYC 9554         | 376 GB| 1 x Instinct MI210                                  | Infiniband 200Gbps  |


---

## 2. Model Selection (Workload)
Two neural network architectures were selected to represent different computational complexities:
- **MobileNet (MOB)**  
  A lightweight model designed for mobile and embedded computer vision tasks.
- **ResNet50 (RES)**  
  A deeper and more computationally intensive model commonly used for complex image recognition workloads.
This selection allows analysis of how model complexity impacts performance, energy consumption, and carbon footprint across devices.

---

## 3. Software Framework Implementation
To avoid bias toward a single inference engine, each model was executed using two different frameworks:
- **TensorFlow (TF)**  
  A widely adopted framework for training and deploying machine learning models.
- **ONNX Runtime (ORT)**  
  A high-performance inference engine optimized for efficient execution across heterogeneous hardware platforms.

---

## 4. Configuration Setup (Traffic Profile)
Following MLPerf inference specifications, benchmarks were executed under two operational scenarios:
- **Single-Stream (SS)**  
  Processes one input at a time, primarily measuring **latency**.
- **Multi-Stream (MS)**  
  Processes multiple inputs concurrently, focusing on **throughput**.
These scenarios reflect different real-world deployment conditions.

---

## 5. Measurement and Data Collection
During benchmark execution, specialized monitoring tools were used to collect energy-related metrics:
- **Energy Consumption (kWh)**  
  The total electrical energy consumed during inference.
- **Carbon Footprint (kg CO₂eq)**  
  Computed using the measured energy consumption, combined with:
  - Local Carbon Intensity (CI) of the power grid  
  - Power Usage Effectiveness (PUE) of the execution environment  
This approach enables a consistent estimation of environmental impact across devices.

---

## 6. Statistical Validation
To ensure reliability and reproducibility:
- Each experiment was executed multiple times.
- **Mean (average)** and **standard deviation** were calculated.
- This statistical treatment reduces the influence of transient system behavior and outliers.

---

## Results Summary
- **Table 2** presents the results obtained in the **Single-Stream scenario** across all evaluated devices.
- **Table 3** presents the results obtained in the **Multi-Stream scenario** across all evaluated devices.
Tables 2 and 3 present the results in the different multi-device test configurations.

Table 2. Results Obtained from Devices in the SingleStream Scenario
| Layer | Device  | HW   | Framework | Model | Avg qps | Mean Avg ms | Time Avg s | Avg Watts | Avg dist Watts | Queries | P50 Latency (ms) | P99 Latency (ms) | Energy (kWh) | CO2 (Kg eq) |
|-------|---------|------|-----------|-------|---------|--------------|-------------|------------|------------------|---------|-------------------|-------------------|----------------|--------------|
| Edge | Laptop | CPU | TF  | MOB | 116.78 | 8.37 | 600.39 | 74.97 | 0.92 | 70111.0 | 8.37 | 8.67 | 0.01250 | 0.00375 |
| Edge | Laptop | CPU | TF  | RES | 26.99 | 36.83 | 600.35 | 78.53 | 1.53 | 16203.7 | 36.80 | 38.23 | 0.01309 | 0.00393 |
| Edge | Laptop | CPU | ORT | MOB | 235.87 | 3.93 | 494.79 | 60.20 | 0.52 | 120001.0 | 3.90 | 6.00 | 0.00830 | 0.00249 |
| Edge | Laptop | CPU | ORT | RES | 42.96 | 23.10 | 600.35 | 60.87 | 0.44 | 25791.3 | 23.00 | 25.63 | 0.01016 | 0.00305 |
| Edge | Laptop | GPU | TF  | MOB | 386.97 | 2.50 | 310.10 | 79.27 | 0.79 | 120001.0 | 2.50 | 2.60 | 0.00682 | 0.00205 |
| Edge | Laptop | GPU | TF  | RES | 98.35 | 10.10 | 600.13 | 88.20 | 0.74 | 59020.0 | 10.10 | 10.30 | 0.01470 | 0.00441 |
| Edge | Laptop | GPU | ORT | MOB | 536.02 | 1.80 | 224.15 | 88.27 | 0.89 | 120001.0 | 1.80 | 1.80 | 0.00550 | 0.00165 |
| Edge | Laptop | GPU | ORT | RES | 127.03 | 7.80 | 600.12 | 90.00 | 0.89 | 76232.3 | 7.80 | 7.90 | 0.01500 | 0.00450 |
| Edge | RPi | CPU | TF  | MOB | 5.18 | 190.90 | 602.52 | 5.10 | 0.17 | 3122.0 | 196.33 | 214.93 | 0.00085 | 16.519 |
| Edge | RPi | CPU | TF  | RES | 1.11 | 892.33 | 603.44 | 4.53 | 0.17 | 672.7 | 929.57 | 957.13 | 0.00076 | 14.673 |
| Edge | RPi | CPU | ORT | MOB | 4.90 | 202.13 | 602.01 | 4.53 | 0.17 | 2950.0 | 209.40 | 236.90 | 0.00076 | 14.673 |
| Edge | RPi | CPU | ORT | RES | 1.15 | 887.43 | 603.16 | 5.23 | 0.16 | 676.3 | 914.17 | 968.83 | 0.00088 | 16.940 |
| Edge | Nano | CPU | TF  | MOB | 11.72 | 84.97 | 600.39 | 5.71 | 0.93 | 7038.0 | 57.77 | 68.60 | 0.00095 | 18.495 |
| Edge | Nano | CPU | TF  | RES | 2.24 | 451.00 | 601.50 | 6.48 | 1.16 | 1346.7 | 448.83 | 469.23 | 0.00109 | 20.989 |
| Edge | Nano | CPU | ORT | MOB | 11.10 | 88.87 | 601.15 | 6.47 | 0.93 | 6717.7 | 87.23 | 104.20 | 0.00108 | 20.956 |
| Edge | Nano | CPU | ORT | RES | 2.82 | 355.47 | 601.55 | 6.56 | 1.23 | 1696.3 | 354.57 | 370.73 | 0.00110 | 21.248 |
| Fog | Nova | CPU | TF  | MOB | 86.60 | 0.011 | 600.13 | 28.45 | 5.310 | 51972 | 7.89 | 13.27 | 0.00474 | 0.00171 |
| Fog | Nova | CPU | TF  | RES | 25.78 | 0.039 | 600.16 | 28.11 | 4.533 | 15472 | 38.30 | 42.07 | 0.00469 | 0.00169 |
| Fog | Nova | CPU | ORT | MOB | 311.72 | 0.003 | 385.02 | 28.67 | 5.707 | 120001 | 3.03 | 3.57 | 0.00307 | 0.00110 |
| Fog | Nova | CPU | ORT | RES | 62.00 | 0.016 | 600.15 | 27.59 | 5.537 | 37210 | 15.50 | 18.27 | 0.00460 | 0.00166 |
| Fog | Neowise | CPU | TF  | MOB | 130.69 | 0.008 | 600.11 | 64.71 | 6.860 | 78425 | 7.53 | 8.00 | 0.01079 | 0.00388 |
| Fog | Neowise | CPU | TF  | RES | 33.09 | 0.030 | 600.12 | 65.22 | 5.613 | 19856 | 29.53 | 33.37 | 0.01087 | 0.00391 |
| Fog | Neowise | CPU | ORT | MOB | 283.49 | 0.003 | 423.32 | 64.38 | 6.797 | 120001 | 3.37 | 3.60 | 0.00757 | 0.00273 |
| Fog | Neowise | CPU | ORT | RES | 75.92 | 0.013 | 600.11 | 64.79 | 7.537 | 45558 | 12.87 | 15.10 | 0.01080 | 0.00389 |
| Cloud | ExaDell | CPU | TF  | MOB | - | - | - | - | - | - | - | - | 0.00474 | 0.00175 |
| Cloud | ExaDell | CPU | TF  | RES | - | - | - | - | - | - | - | - | 0.00469 | 0.00173 |
| Cloud | ExaDell | CPU | ORT | MOB | - | - | - | - | - | - | - | - | 0.00307 | 0.00113 |
| Cloud | ExaDell | CPU | ORT | RES | - | - | - | - | - | - | - | - | 0.00460 | 0.00170 |
| Cloud | ExaSM | CPU | TF  | MOB | - | - | - | - | - | - | - | - | 0.01079 | 0.00399 |
| Cloud | ExaSM | CPU | TF  | RES | - | - | - | - | - | - | - | - | 0.01087 | 0.00402 |
| Cloud | ExaSM | CPU | ORT | MOB | - | - | - | - | - | - | - | - | 0.00757 | 0.00280 |
| Cloud | ExaSM | CPU | ORT | RES | - | - | - | - | - | - | - | - | 0.01080 | 0.00399 |

Table 3. Results Obtained from Devices in the MultiStream Scenario
| Layer | Device  | HW   | Framework | Model | Avg qps | Mean Avg ms | Time Avg s | Avg Watts | Avg dist Watts | Queries | P50 Latency (ms) | P99 Latency (ms) | Energy (kWh) | CO2 (Kg eq) |
|-------|---------|------|-----------|-------|---------|--------------|-------------|------------|------------------|---------|-------------------|-------------------|----------------|--------------|
| Edge | Laptop | CPU | TF  | MOB | 19.39 | 508.10 | 600.26 | 81.97 | 1.65 | 11640.0 | 50.70 | 53.17 | 0.01367 | 0.00410 |
| Edge | Laptop | CPU | TF  | RES | 4.02 | 247.93 | 600.51 | 85.20 | 0.82 | 2414.3 | 247.80 | 252.00 | 0.01423 | 0.00427 |
| Edge | Laptop | CPU | ORT | MOB | 28.05 | 34.90 | 534.92 | 66.20 | 1.55 | 15001.0 | 34.60 | 50.83 | 0.00986 | 0.00296 |
| Edge | Laptop | CPU | ORT | RES | 5.21 | 191.30 | 600.42 | 65.97 | 1.49 | 3126.3 | 188.50 | 318.93 | 0.01100 | 0.00330 |
| Edge | Laptop | GPU | TF  | MOB | 78.46 | 12.17 | 191.20 | 83.20 | 1.49 | 15001.0 | 12.20 | 12.40 | 0.00441 | 0.00132 |
| Edge | Laptop | GPU | TF  | RES | 23.67 | 41.67 | 600.10 | 92.97 | 1.77 | 14206.0 | 41.60 | 42.13 | 0.01549 | 0.00465 |
| Edge | Laptop | GPU | ORT | MOB | 84.98 | 11.20 | 176.51 | 90.20 | 1.75 | 15001.0 | 11.10 | 11.27 | 0.00442 | 0.00133 |
| Edge | Laptop | GPU | ORT | RES | 25.24 | 39.03 | 594.26 | 93.23 | 1.86 | 15001.0 | 39.00 | 39.27 | 0.01539 | 0.00462 |
| Edge | RPi | CPU | TF  | MOB | 0.94 | 1061.77 | 707.46 | 4.80 | 0.17 | 662.0 | 1090.77 | 1177.47 | 0.00094 | 15.547 |
| Edge | RPi | CPU | TF  | RES | 0.17 | 5916.03 | 3921.07 | 4.63 | 0.17 | 662.0 | 5894.93 | 6122.60 | 0.00505 | 14.997 |
| Edge | RPi | CPU | ORT | MOB | 0.76 | 1328.63 | 870.51 | 4.63 | 0.17 | 662.0 | 1439.40 | 1597.97 | 0.00112 | 14.997 |
| Edge | RPi | CPU | ORT | RES | 0.17 | 6111.40 | 4052.95 | 5.30 | 0.18 | 662.0 | 6613.67 | 6994.73 | 0.00596 | 17.167 |
| Edge | Nano | CPU | TF  | MOB | 2.11 | 468.90 | 600.57 | 6.08 | 0.93 | 1184.3 | 461.47 | 486.63 | 0.00101 | 19.693 |
| Edge | Nano | CPU | TF  | RES | 0.35 | 2081.57 | 1820.15 | 6.72 | 1.04 | 662.0 | 2079.33 | 2152.03 | 0.00340 | 21.766 |
| Edge | Nano | CPU | ORT | MOB | 1.52 | 658.93 | 600.92 | 6.60 | 0.93 | 908.0 | 656.80 | 678.37 | 0.00110 | 21.377 |
| Edge | Nano | CPU | ORT | RES | 0.37 | 2696.77 | 1786.64 | 6.71 | 1.33 | 662.0 | 2690.63 | 2756.77 | 0.00333 | 21.734 |
| Fog | Nova | CPU | TF  | MOB | 28.44 | 0.034 | 527.57 | 86.14 | 10.843 | 15001 | 33.43 | 36.87 | 0.01262 | 0.00454 |
| Fog | Nova | CPU | TF  | RES | 7.26 | 0.136 | 600.24 | 95.37 | 9.413 | 4355 | 136.13 | 146.83 | 0.01590 | 0.00572 |
| Fog | Nova | CPU | ORT | MOB | 35.41 | 0.027 | 427.24 | 94.50 | 3.907 | 15001 | 26.60 | 34.03 | 0.01122 | 0.00404 |
| Fog | Nova | CPU | ORT | RES | 8.29 | 0.120 | 600.21 | 97.60 | 3.420 | 4972 | 123.00 | 158.83 | 0.01627 | 0.00586 |
| Fog | Neowise | CPU | TF  | MOB | 30.50 | 0.033 | 500.36 | 158.71 | 15.497 | 15001 | 33.83 | 37.43 | 0.02206 | 0.00794 |
| Fog | Neowise | CPU | TF  | RES | 10.91 | 0.091 | 600.17 | 177.14 | 8.520 | 6550 | 90.43 | 100.97 | 0.02953 | 0.01063 |
| Fog | Neowise | CPU | ORT | MOB | 80.95 | 0.012 | 185.32 | 199.07 | 6.980 | 15001 | 10.63 | 27.53 | 0.01025 | 0.00369 |
| Fog | Neowise | CPU | ORT | RES | 22.04 | 0.045 | 600.12 | 208.32 | 3.530 | 13225 | 41.00 | 82.37 | 0.03473 | 0.01250 |
| Cloud | ExaDell | CPU | TF  | MOB | - | - | - | - | - | - | - | - | 0.01262 | 0.00467 |
| Cloud | ExaDell | CPU | TF  | RES | - | - | - | - | - | - | - | - | 0.01590 | 0.00588 |
| Cloud | ExaDell | CPU | ORT | MOB | - | - | - | - | - | - | - | - | 0.01122 | 0.00415 |
| Cloud | ExaDell | CPU | ORT | RES | - | - | - | - | - | - | - | - | 0.01627 | 0.00602 |
| Cloud | ExaSM | CPU | TF  | MOB | - | - | - | - | - | - | - | - | 0.02206 | 0.00816 |
| Cloud | ExaSM | CPU | TF  | RES | - | - | - | - | - | - | - | - | 0.02953 | 0.01092 |
| Cloud | ExaSM | CPU | ORT | MOB | - | - | - | - | - | - | - | - | 0.01025 | 0.00379 |
| Cloud | ExaSM | CPU | ORT | RES | - | - | - | - | - | - | - | - | 0.03473 | 0.03473 |

Together, these tables provide a comparative view of performance, energy consumption, and environmental impact.

---

## Energy Measurement Sources
The `EDGE/` and `FOG/` directories contain the raw energy consumption data collected during the experiments:
- **Edge Devices**  
  Measurements were obtained using a smart power outlet (VTA-84630).
- **Fog Devices**  
  Measurements were collected using the Kwollect monitoring tool.
This separation reflects the practical constraints and measurement capabilities of each class of device.

---

## Reproducibility Statement
The results presented in this document were generated using:
- The Docker-based recipe provided in `docker/`
- The Dockerfiles and datasets defined in `update/`
- Scripted and repeatable execution workflows
While absolute values may vary slightly across environments, the **methodology and relative comparisons remain reproducible**, making this artifact suitable for academic evaluation and result verification.

---
