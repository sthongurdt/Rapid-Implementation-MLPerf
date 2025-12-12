# Result

The results were obtained by running the recipe provided in the Docker directory and using the files located in the update directory. Although the results may differ slightly from those presented in the tables, the recipe ensures that the process is reproducible and can be executed consistently across different environments. It is important to note that variations in the power supply, the temperature of the testing environment, and the effectiveness of thermal dissipation mechanisms can impact the outcomes. These factors have an even stronger influence on embedded devices, where performance is more sensitive to external conditions.

| Device   | CPU                       | RAM   | Others                                             | NET                 |
|----------|---------------------------|-------|----------------------------------------------------|---------------------|
| Laptop   | i5 10300H                 | 32 GB | 512 GB SSD, GTX 1650ti                             | 1GbE                |
| RPi      | ARM Cortex-A72            | 8 GB  | 128 GB SDcard, VideoCore VI                        | 1GbE                |
| Nano     | ARM® Cortex-A57           | 2 GB  | 128 GB SDcard, Maxwell (128 núcleos CUDA)          | 10GbE               |
| Nova     | 2 x Intel Xeon E5-2620 v4 | 64 GB | 557 GB HDD                                          | 10GbE               |
| Neowise  | AMD EPYC 7642             | 512 GB| 1788 GB SSD, 8 GPUs Radeon Instinct MI50           | 2 x 10GbE           |
| ExaDell  | 2 x AMD EPYC 9534         | 376 GB| 2 x Instinct MI210                                  | Infiniband 200Gbps  |
| ExaSM    | 2 x AMD EPYC 9554         | 376 GB| 1 x Instinct MI210                                  | Infiniband 200Gbps  |
