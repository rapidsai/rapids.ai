---
title: "Technical Documentation, Docker Container | RAPIDS"
og_title: "RAPIDS Getting Started"
og_description: "Get started with RAPIDS using conda, docker, pip, or from source builds."
brand_name: ""
brand_tagline: "Learn How To Use RAPIDS"
brand_button: "LAUNCH NOW IN COLAB"
brand_link: "https://colab.research.google.com/drive/1XTKHiIcvyL5nuldx0HSL_dUa8yopzy_Y#forceEdit=true&offline=true&sandboxMode=true"
layout: default
redirect_from: "/documentation.html"
---

{% capture start_left %}
# Getting Started
{: .section-title-halfs}

The RAPIDS data science framework includes a collection of libraries for executing end-to-end data science pipelines completely in the GPU. It is designed to have a familiar look and feel to data scientists working in Python. Here’s a code snippet where we read in a CSV file and output some descriptive statistics:

```python
import cudf
gdf = cudf.read_csv('path/to/file.csv')
for column in gdf.columns:
    print(gdf[column].mean())
```

## <i class="fas fa-bolt"></i> Try Now In Colaboratory
Jump right into a GPU powered RAPIDS notebook with **[Colabratory](https://colab.research.google.com/notebooks/welcome.ipynb){: target="_blank"}** for free. **[Go to example notebook <i class="fas fa-angle-double-right"></i>](https://colab.research.google.com/drive/1XTKHiIcvyL5nuldx0HSL_dUa8yopzy_Y#forceEdit=true&offline=true&sandboxMode=true){: target="_blank"}**

{% endcapture %}

{% capture start_right %}
## GPU Powered Data Science 
{: .section-subtitle-top-1}

RAPIDS uses optimized **[NVIDIA CUDA®](https://developer.nvidia.com/cuda-toolkit){: target="_blank"}** primitives and high-bandwidth GPU memory to accelerate data preparation and machine learning. The goal of RAPIDS is not only to accelerate the individual parts of the typical data science workflow, but to accelerate the complete end-to-end workflow.

We suggest that you take a look at the sample workflow in our Docker container (described below), which illustrates just how straightforward a basic XGBoost model training and testing workflow looks in RAPIDS.

## Prerequisites 
<i class="fas fa-exclamation-triangle text-purple"></i> NVIDIA Pascal™ GPU architecture or better

<i class="fas fa-exclamation-triangle text-purple"></i> **[CUDA 9.2](https://developer.nvidia.com/cuda-92-download-archive){: target="_blank"}** or **[CUDA 10.0](https://developer.nvidia.com/cuda-10.0-download-archive){: target="_blank"}** compatible NVIDIA driver

<i class="fas fa-exclamation-triangle text-purple"></i> Ubuntu 16.04 or 18.04 

<i class="fas fa-exclamation-triangle text-purple"></i> **For Docker Images:** Docker CE v18+ and **[NVIDIA-docker v2+](https://github.com/nvidia/nvidia-docker/wiki/Frequently-Asked-Questions#how-do-i-install-20-if-im-not-using-the-latest-docker-version){: target="_blank"}** 
{% endcapture %}

{% include section-halfs.html
    background="background-white" 
    padding-top="0" padding-bottom="2" 
    content-left-half=start_left
    content-right-half=start_right
%} 


{% capture get_content %}
# RAPIDS Flavor Selector
{: .section-title-full}

RAPIDS is available as conda or pip packages, docker images, and from source builds. Use the tool below to select your preferred method, packages, and environment to install RAPIDS. Certain combinations may not be possible and are dimmed automatically. Be sure you've met the **requirements above**. 
{% endcapture %}

{% include slopecap.html 
    background="background-purple" 
    position="top" 
    slope="down" 
%}

{% include section-single.html
    background="background-purple" 
    padding-top="0" padding-bottom="0" 
    content-single=get_content
%}
{% include options.html  
	background="background-purple"
	padding-top="0" padding-bottom="1" 
%}
{% include slopecap.html 
    background="background-purple" 
    position="bottom" 
    slope="up" 
%}


{% capture use_left %}
## <i class="fas fa-laptop-code"></i> Conda Install
You can get a minimal conda installation with **[Miniconda](https://conda.io/miniconda.html){: target="_blank"}** or get the full installation with **[Anaconda](https://www.anaconda.com/download){: target="_blank"}**.

For instructions on how to build a development conda environment, see the **[cuDF README](https://github.com/rapidsai/cudf/blob/master/README.md#conda){: target="_blank"}** for more information. Also refer to the **[cuML README](https://github.com/rapidsai/cuml/blob/master/README.md#conda){: target="_blank"}** for conda install instructions for cuML.

## <i class="far fa-file-code"></i> Build From Source
{: .section-subtitle-top-2}

Checkout the **[cuDF README](https://github.com/rapidsai/cudf/tree/master#development-setup){: target="_blank"}** or **[cuML README](https://github.com/rapidsai/cuml/tree/master#installing-from-source){: target="_blank"}** for from-source build instructions.

## <i class="fas fa-laptop-code"></i> Where is Pip?
{: .section-subtitle-top-2}

Refer to this **[Blog Post](###){: target="_blank"}** for details on why we no longer support PIP installs. 

{% endcapture %}

{% capture use_right %}
## <i class="fab fa-docker"></i> Docker Container

Run the following command within the Docker container started from the copied Docker command above to launch the notebook server.

**NOTE:** This will run **[JupyterLab](https://jupyterlab.readthedocs.io/en/stable/){: target="_blank"}** on your host machine at port 8888.

```bash
(rapids) root@container:/rapids/notebooks# bash utils/start-jupyter.sh
```

### Use JupyterLab to Explore the Notebooks

Notebooks can be found in two directories within the container:

<i class="far fa-folder-open"></i> **`/rapids/notebooks/cuml`** <br> These cuML demo notebooks have data preloaded in the container image and will be decompressed by the notebooks.

<i class="far fa-folder-open"></i> **`/rapids/notebooks/mortgage`** <br> This cuDF, Dask, XGBoost demo notebook requires the download of **[Mortgage Data](https://docs.rapids.ai/datasets/mortgage-data){: target="_blank"}**, see notebook **`E2E.ipynb`** for more details.

### Advanced Usage

See the **[RAPIDS Container README](https://hub.docker.com/r/rapidsai/rapidsai){: target="_blank"}** page for more information about using custom datasets. **[Docker Hub](https://hub.docker.com/r/rapidsai/rapidsai/){: target="_blank"}** and **[NVIDIA GPU Cloud](https://ngc.nvidia.com/catalog/containers/nvidia%2Frapidsai%2Frapidsai){: target="_blank"}** host RAPIDS containers with full list of available **[tags](https://hub.docker.com/r/rapidsai/rapidsai#full-tag-list){: target="_blank"}**.

{% endcapture %}

{% include section-halfs.html
    background="background-gray" 
    padding-top="1" padding-bottom="2" 
    content-left-half=use_left 
    content-right-half=use_right
%} 


{% include slopecap.html 
    background="background-darkpurple" 
    position="top" 
    slope="up"
%}
{% include cta-footer.html 
name="Join the Community" 
button="LAUNCH NOW IN COLAB"
link="https://colab.research.google.com/drive/1XTKHiIcvyL5nuldx0HSL_dUa8yopzy_Y#forceEdit=true&offline=true&sandboxMode=true"
%}


