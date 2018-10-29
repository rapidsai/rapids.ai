---
title: Technical Documentation, Docker Container | RAPIDS
og_title: RAPIDS Technical Documentation
og_description: Get started with RAPIDS. Find docker container details, download and installation details, and more.
brand_name: DOCUMENTATION
brand_tagline: Getting started with RAPIDS
brand_button: DOWNLOAD CHEAT SHEET
brand_link: assets/files/cheatsheet.pdf
layout: docs
---

## Introduction to RAPIDS

##### The RAPIDS data science framework includes a collection of libraries for executing end-to-end data science pipelines completely in the GPU. It is designed to have a familiar look and feel to data scientists working in Python. Here’s a code snippet where we read in a CSV file and output some descriptive statistics.

```python
import cudf
gdf = cudf.read_csv(‘path/to/file.csv’)
for column in gdf.columns:
    print(column.mean())
```

RAPIDS uses optimized NVIDIA® CUDA® primitives and high-bandwidth GPU memory to accelerate data preparation and machine learning. The goal of RAPIDS is not only to accelerate the individual parts of the typical data science workflow, but to accelerate the complete end-to-end workflow.

We suggest that you take a look at the sample workflow in our Docker container (described below), which illustrates just how straightforward a basic XGBoost model training and testing looks in RAPIDS.


## Install Conda Package

##### The fastest way to use cuDF is through conda.

### Prerequisites

* NVIDIA Pascal™ GPU architecture or better
* CUDA [9.2](https://developer.nvidia.com/cuda-92-download-archive) or [10.0](https://developer.nvidia.com/cuda-downloads)
* Ubuntu 16.04 or 18.04

### Conda Install

You can get a minimal conda installation with [Miniconda](https://conda.io/miniconda.html) or get the full installation with [Anaconda](https://www.anaconda.com/download). Install and update cuDF using the conda command:

```bash
$ conda install -c numba -c conda-forge -c rapidsai -c defaults cudf=0.2.0
```

For instructions on how to build a development conda environment, see the [cuDF README](https://github.com/rapidsai/cudf#conda) for more information.


## Run the RAPIDS Container

##### The RAPIDS Docker containers are configured to run RAPIDS and provide example data/notebooks to get started quickly.

### Prerequisites

* NVIDIA Pascal™ GPU architecture or better
* CUDA [9.2](https://developer.nvidia.com/cuda-92-download-archive) or [10.0](https://developer.nvidia.com/cuda-downloads)
* Ubuntu 16.04 or 18.04
* Docker CE v18+
* [nvidia-docker](https://github.com/nvidia/nvidia-docker/wiki/Installation-(version-2.0)) v2+

### Start Container and Notebook Server

```bash
$ docker pull rapidsai/rapidsai:ubuntu1604_cuda92_py35
$ docker run --runtime=nvidia \
        --rm -it \
        -p 8888:8888 \
        -p 8787:8787 \
        -p 8786:8786 \
        rapidsai/rapidsai:ubuntu1604_cuda92_py35
jupyter@container:/$ cd rapids && source activate gdf
(gdf) jupyter@container:/$ tar -xzvf data/mortgage.tar.gz --directory=data
(gdf) jupyter@container:/$ bash utils/start_jupyter.sh
```
**NOTE:** This will run [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) on port 8888 on your host machine with a default token/password of `rapids`.

### Advanced Usage

See the [Docker README](https://hub.docker.com/r/rapidsai/rapidsai/) on Docker Hub.
