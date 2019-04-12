---
title: "Technical Documentation, Docker Container | RAPIDS"
og_title: "RAPIDS Getting Started"
og_description: "Get started with RAPIDS using conda, docker, pip, or from source builds."
brand_name: ""
brand_tagline: "Learn how to use RAPIDS"
brand_button: "DOWNLOAD CHEAT SHEET"
brand_link: "assets/files/cheatsheet.pdf"
layout: default
redirect_from: "/documentation.html"
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
## Get RAPIDS

##### RAPIDS is available as conda or pip packages, docker images, and from source builds. Use the tool below to select your preferred method, packages, and environment to install RAPIDS. Certain combinations may not be possible and are dimmed automatically. Be sure to review the [prerequisites](#prerequisites) section for more details about requirements to use RAPIDS.

{% include options.html %}

{% endcapture %}
{% include sec-left-purple.html content=section_conda %}

{% capture section_container %}
## Using RAPIDS
{: .pad-top-0 .pad-bot-30 }

##### Learn how to use RAPIDS with the method of your choice.

### <br/>Conda Install

You can get a minimal conda installation with [Miniconda](https://conda.io/miniconda.html) or get the full installation with [Anaconda](https://www.anaconda.com/download).

For instructions on how to build a development conda environment, see the [cuDF README](https://github.com/rapidsai/cudf/blob/master/README.md#conda) for more information. Also refer to the [cuML README](https://github.com/rapidsai/cuml/blob/master/README.md#conda) for conda install instructions for cuML.

### <br/>Docker Container

Run the following command within the Docker container started from the command [above](#get-rapids) to launch the notebook server:

```bash
(rapids) root@container:/rapids/notebooks# bash utils/start-jupyter.sh
```
**NOTE:** This will run [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) on your host machine at port 8888.

#### Use JupyterLab to Explore the Notebooks

Notebooks can be found in two directories within the container:

* `/rapids/notebooks/cuml` - cuML demo notebooks
  * These notebooks have data pre-loaded in the container image and will be decompressed by the notebooks
* `/rapids/notebooks/mortgage` - cuDF, Dask, XGBoost demo notebook
  * This notebook requires download of [Mortgage Data](https://docs.rapids.ai/datasets/mortgage-data), see notebook `E2E.ipynb` for more details

#### Advanced Usage

See the [RAPIDS Container README](https://hub.docker.com/r/rapidsai/rapidsai) page for more information about using custom datasets. [Docker Hub](https://hub.docker.com/r/rapidsai/rapidsai/) and [NVIDIA GPU Cloud](https://ngc.nvidia.com/catalog/containers/nvidia%2Frapidsai%2Frapidsai) host RAPIDS containers with full list of available [tags](https://hub.docker.com/r/rapidsai/rapidsai#full-tag-list).

<!--  
    the breaks in the headers are necessary to space the anchor so it doesn't 
    place the header under the nav bar 
-->
### <br/>Pip Install

**NOTE:** Ubuntu 16.04's `python3` package is Python 3.5 by default. Follow the [python install](#ubuntu-1604-python-install) instructions to upgrade.
Refer to the [cuDF README](https://github.com/rapidsai/cudf/tree/master#pip) or [cuML README](https://github.com/rapidsai/cuml/tree/master#pip) for pip install instructions.

### <br/>Build From Source

Checkout the [cuDF README](https://github.com/rapidsai/cudf/tree/master#development-setup) or [cuML README](https://github.com/rapidsai/cuml/tree/master#installing-from-source) for from source build instructions.

{% endcapture %}
{% include sec-right-gray.html content=section_container %}

{% capture section_info %}
## More Information

### <br/>Prerequisites

* NVIDIA Pascal™ GPU architecture or better
* CUDA [9.2](https://developer.nvidia.com/cuda-92-download-archive) or [10.0](https://developer.nvidia.com/cuda-10.0-download-archive) compatible nvidia driver
* Ubuntu 16.04 or 18.04 
* For Docker Images
  * Docker CE v18+
  * [nvidia-docker](https://github.com/nvidia/nvidia-docker/wiki/Installation-(version-2.0)) v2+

#### <br/>Ubuntu 16.04 Python Install
By default, Ubuntu 16.04's `python3` package is Python 3.5, so you need to install Python 3.6 or 3.7 with the following steps:

**For Python 3.6**

```bash
apt-get install software-properties-common python-software-properties
add-apt-repository ppa:deadsnakes/ppa
apt update && apt install python3.6-dev
```

**For Python 3.7**

```bash
apt-get install software-properties-common python-software-properties
add-apt-repository ppa:deadsnakes/ppa
apt update && apt install python3.7-dev
```

#### Documentation

Check out the [cuDF](https://rapidsai.github.io/projects/cudf/en/latest), [cuML](https://rapidsai.github.io/projects/cuml/en/latest), and [XGBoost](https://xgboost.readthedocs.io/en/latest/) API docs.

Learn how to setup a mult-node cuDF and XGBoost data preparation and distributed training environment by following the [mortgage data example notebook and scripts](https://github.com/rapidsai/notebooks).

{% endcapture %}
{% include sec-white.html content=section_info %}

{% include cta-footer.html 
name="Join the Community" 
tagline="Learn how you can be an adopter, contributor, and more."
button="Join Today"
link="community.html"
%}
