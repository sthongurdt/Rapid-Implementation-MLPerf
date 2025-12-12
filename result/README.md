# Result

The results were obtained by running the recipe provided in the Docker directory and using the files located in the update directory. Although the results may differ slightly from those presented in the tables, the recipe ensures that the process is reproducible and can be executed consistently across different environments. It is important to note that variations in the power supply, the temperature of the testing environment, and the effectiveness of thermal dissipation mechanisms can impact the outcomes. These factors have an even stronger influence on embedded devices, where performance is more sensitive to external conditions.

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

