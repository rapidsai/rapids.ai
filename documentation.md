---
title: "Technical Documentation, Docker Container | RAPIDS"
og_title: "RAPIDS Technical Documentation"
og_description: "Get started with RAPIDS. Find docker container details, download and installation details, and more."
brand_name: "DOCUMENTATION"
brand_tagline: "Getting started with RAPIDS"
brand_button: "DOWNLOAD CHEAT SHEET"
brand_link: "assets/files/cheatsheet.pdf"
layout: default
---
{% capture section_intro %}
## Introduction to RAPIDS

##### The RAPIDS data science framework includes a collection of libraries for executing end-to-end data science pipelines completely in the GPU. It is designed to have a familiar look and feel to data scientists working in Python. Here’s a code snippet where we read in a CSV file and output some descriptive statistics.

```python
import cudf
gdf = cudf.read_csv('path/to/file.csv')
for column in gdf.columns:
    print(gdf[column].mean())
```

RAPIDS uses optimized NVIDIA® CUDA® primitives and high-bandwidth GPU memory to accelerate data preparation and machine learning. The goal of RAPIDS is not only to accelerate the individual parts of the typical data science workflow, but to accelerate the complete end-to-end workflow.

We suggest that you take a look at the sample workflow in our Docker container (described below), which illustrates just how straightforward a basic XGBoost model training and testing looks in RAPIDS.
{% endcapture %}
{% include sec-white.html content=section_intro %}

{% capture section_conda %}
## Install Conda Package

##### The fastest way to use cuDF is through conda.

#### Prerequisites

* NVIDIA Pascal™ GPU architecture or better
* CUDA [9.2](https://developer.nvidia.com/cuda-92-download-archive) or [10.0](https://developer.nvidia.com/cuda-downloads)
* Ubuntu 16.04 or 18.04

#### Conda Install

You can get a minimal conda installation with [Miniconda](https://conda.io/miniconda.html) or get the full installation with [Anaconda](https://www.anaconda.com/download). Install and update cuDF using the conda command:

```bash
$ conda install -c numba -c nvidia -c rapidsai -c conda-forge -c defaults cudf=0.5
```

For instructions on how to build a development conda environment, see the [cuDF README](https://github.com/rapidsai/cudf/blob/master/README.md#conda) for more information. Also refer to the [cuML README](https://github.com/rapidsai/cuml/blob/master/README.md#conda) for conda install instructions for cuML.
{% endcapture %}
{% include sec-left-gray.html content=section_conda %}

{% capture section_pip %}
## Install Python Package with Pip

##### You can also quickly install cuDF using pip

#### Prerequisites

* NVIDIA Pascal™ GPU architecture or better
* CUDA [9.2](https://developer.nvidia.com/cuda-92-download-archive) or [10.0](https://developer.nvidia.com/cuda-downloads)
* Ubuntu 16.04 or 18.04

#### Python Install

##### Ubuntu 16.04
By default, Ubuntu 16.04's `python3` package is Python 3.5, so you need to install Python 3.6 or 3.7 with the following steps:

```bash
$ apt-get install software-properties-common python-software-properties
$ add-apt-repository ppa:jonathonf/python-3.6 #Or 3.7
$ apt update && apt install python3.6 #Or 3.7
```

##### Ubuntu 18.04

Simply install the `python3.6` or `python3.7` package:

```bash
apt install python3.6 #Or 3.7
```

#### Pip Install

You can install and update cuDF for CUDA 9.2 using the command:

```bash
$ python3.6 -m pip install cudf-cuda92=0.5
```

You can install and update cuDF for CUDA 10.0 using the command:

```bash
$ python3.6 -m pip install cudf-cuda100=0.5
```


Also refer to the [cuML README](https://github.com/rapidsai/cuml/tree/master#pip) for pip install instructions for cuML.
{% endcapture %}
{% include sec-left-gray.html content=section_pip %}

{% capture section_container %}
## Run the RAPIDS Container

##### The RAPIDS Docker containers are configured to run RAPIDS and provide example data/notebooks to get started quickly.

#### Prerequisites

* NVIDIA Pascal™ GPU architecture or better
* CUDA [9.2](https://developer.nvidia.com/cuda-92-download-archive) or [10.0](https://developer.nvidia.com/cuda-downloads) compatible nvidia driver
* Ubuntu 16.04 or 18.04
* Docker CE v18+
* [nvidia-docker](https://github.com/nvidia/nvidia-docker/wiki/Installation-(version-2.0)) v2+

#### Start Container and Notebook Server

```bash
$ docker pull rapidsai/rapidsai:cuda9.2-runtime-ubuntu16.04
$ docker run --runtime=nvidia \
        --rm -it \
        -p 8888:8888 \
        -p 8787:8787 \
        -p 8786:8786 \
        rapidsai/rapidsai:cuda9.2-runtime-ubuntu16.04
root@container:/rapids/notebooks/$ source activate rapids
(rapids) root@container:/rapids/notebooks/$ bash utils/start_jupyter.sh
```
**NOTE:** This will run [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) on port 8888 on your host machine.

#### Use JupyterLab to Explore the Notebooks

Notebooks can be found in two directories within the container:

* `/rapids/notebooks/cuml` - cuML demo notebooks
  * These notebooks have data pre-loaded in the container image and requires the following command to be run for decompression: `cd /rapids/notebooks/cuml/data && gunzip mortgage.npy.gz`
* `/rapids/notebooks/mortgage` - cuDF, Dask, XGBoost demo notebook
  * This notebook requires download of [Mortgage Data](datasets/mortgage-data), see notebook `E2E.ipynb` for more details

#### Custom Data and Advanced Usage


See the [RAPIDS Container README](https://hub.docker.com/r/rapidsai/rapidsai) page for more information about using custom datasets. 

[Docker Hub](https://hub.docker.com/r/rapidsai/rapidsai/) and [NVIDA GPU Cloud](https://ngc.nvidia.com/catalog/containers/nvidia%2Frapidsai%2Frapidsai) host RAPIDS containers with full list of available [tags](https://hub.docker.com/r/rapidsai/rapidsai#full-tag-list).

## More Information

Check out the [cuDF](https://rapidsai.github.io/projects/cudf/en/latest), [cuML](https://rapidsai.github.io/projects/cuml/en/latest), and [XGBoost](https://xgboost.readthedocs.io/en/latest/) API docs.

Learn how to setup a mult-node cuDF and XGBoost data preparation and distributed training environment by following the [mortgage data example notebook and scripts](https://github.com/rapidsai/notebooks).

{% endcapture %}
{% include sec-white.html content=section_container %}

{% include cta-footer.html 
name="Join the Community" 
tagline="Learn how you can be an adopter, contributor, and more."
button="Join Today"
link="community.html"
%}
