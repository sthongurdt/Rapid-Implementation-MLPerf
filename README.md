<div align="center">
<h1>RSI MLPerf</h1>
</div>

**Rapid Simple Implementation of MLPerf**

RSI MLPerf is a rapid and simple recipe for implementing MLPerf on different devices in a short series of steps.

<div align="justify">

<h2>Overview</h2>
This work presents a rapid and simple recipe for implementing MLPerf on different types of devices, including edge, fog, and traditional computing platforms. The main objective is to simplify the deployment and execution process, reducing the technical complexity usually associated with MLPerf benchmarks.

The proposed recipe is designed to support reproducibility of experiments, allowing researchers to obtain comparable and verifiable results with minimal configuration effort. By standardizing the main steps—environment preparation, benchmark execution, and result collection—the approach helps ensure consistency across devices and test runs.

This solution is especially intended for researchers with limited time or resources, who need to validate performance results efficiently without performing a full manual setup. As a result, the recipe lowers the entry barrier to MLPerf benchmarking while preserving methodological rigor and experimental reliability.

<h2>How to Use</h2>
There are different ways to run benchmarks in MLPerf, Docker is one of the most widely used tools due to its ease of integration and automation. <b>Docker</b> allows you to package and distribute MLPerf test environments as portable containers (Rapid deployment), simplifying the installation of dependencies and ensuring consistent environments. This option is ideal for users seeking rapid configuration or working in infrastructures where container-based virtualization is standard. With Docker, you can obtain official MLCommons images or build custom containers tailored to specific hardware or software needs.
</div>

- In the **`docker`** directory you will find a recipe for a rapid x86-64 deployment.
- In the **`update`** directory you will find the different `dockerfiles` for different devices and a `.sh` file to configure a simple dataset.
- In the **`result`** directory you will find the results of different tests on different devices for different scenarios.

