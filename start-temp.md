---
title: "Getting Started"
description: "Get started with RAPIDS using conda, docker, or from source builds."
tagline: "Get RAPIDS Now"
button_text: "SELECT RELEASE"
button_link: "#get-rapids"
layout: default
redirect_from: "/documentation.html" # redirect from old page to ensure existing links still work
---

{% capture start_left %}

# Getting Started
{: .section-title-halfs}

The RAPIDS data science framework includes a collection of libraries for executing **end-to-end data science pipelines completely in the GPU**. It is designed to have a familiar look and feel to data scientists working in Python. Here's a code snippet where we read in a CSV file and output some descriptive statistics:

```python
import cudf
df = cudf.read_csv('path/to/file.csv')
for column in df.columns:
    print(df[column].mean())
```

RAPIDS uses optimized **[NVIDIA CUDA®](https://developer.nvidia.com/cuda-toolkit){: target="_blank"}** primitives and high-bandwidth GPU memory to accelerate data preparation and machine learning. The goal of RAPIDS is not only to accelerate the individual parts of the typical data science workflow, but to accelerate the complete end-to-end workflow.

{% endcapture %}
{% capture start_right %}

## <i class="fas fa-bolt"></i> Test Drive RAPIDS Now!
{: .section-subtitle-top-1}

Jump right into a GPU powered RAPIDS notebook, online, with either **[SageMaker Studio Lab](https://studiolab.sagemaker.aws/)** or **[Colab](https://colab.research.google.com/){: target="_blank"} [(v21.12 only)](https://docs.rapids.ai/notices/rsn0014/)**:

[![SageMaker Studio Lab]({{ site.baseurl }}{% link /assets/images/Open-StudioLab.png%})](smsl.html){: target="_blank"}

[![Colab]({{ site.baseurl }}{% link /assets/images/Open-Colab.png%})](https://colab.research.google.com/drive/1rY7Ln6rEE1pOlfSHCYOVaqt8OvDO35J0#forceEdit=true&offline=true&sandboxMode=true){: target="_blank"}

{% endcapture %}

{% include section-halfs.html
    background="background-white"
    padding-top="1em" padding-bottom="10em"
    content-left-half=start_left
    content-right-half=start_right
%}


{% capture gs_overview %}
# Install Overview
{: .section-title-halfs}

Easily install RAPIDS on an **on-prem computer** with a CUDA enabled GPU or a CUDA enabled GPU **cloud instance** with either **[Conda](#rapids-conda)** or **[Docker](#rapids-docker)**. For some advanced use cases, RAPIDS can also be **[built from source](#env-rapids)**.

{% endcapture %}
{% include slopecap.html
    background="background-gray"
    position="top"
    slope="down"
%}
{% include section-single.html
    background="background-gray"
    padding-top="1em" padding-bottom="1em"
    content-single=gs_overview
%}

{% capture req_left %}
## Use RAPIDS on a Cloud Provisioned System
{: .section-title-halfs}

Learn how to deploy RAPIDS on **[Cloud Service Providers <i class="fa fa-angle-double-right" aria-hidden="true"></i>](https://rapids.ai/cloud){: target="_blank"}**

<div class="container-logo-flex padding-top-{{ include.padding-top }} padding-bottom-{{ include.padding-bottom }}">
    <div class="logo-flex">
        <a href="cloud.html#aws" target="_blank"> <img src="{{ site.baseurl }}{% link /assets/images/AWS-logo.png %}" alt="AWS"> </a>
    </div>
    <div class="logo-flex">
        <a href="cloud.html#azure" target="_blank"> <img src="{{ site.baseurl }}{% link /assets/images/azure-ml.png %}" alt="Azure ML"> </a>
    </div>
    <div class="logo-flex">
        <a href="cloud.html#googlecloud" target="_blank"> <img src="{{ site.baseurl }}{% link /assets/images/GCP-logo.png %}" alt="GCP"> </a>
    </div>
    <div class="logo-flex">
        <a href="https://www.paperspace.com/gpu-cloud" target="_blank"> <img src="{{ site.baseurl }}{% link /assets/images/paperspace_small.png %}" alt="Paperspace"> </a>
    </div>
</div>

## Use RAPIDS on a Local Provisioned System
{: .section-subtitle-top-1}

Aside from the system requirments, other considerations for best performance include:
{: .no-tb-margins }g
- SSD drive (NVMe preferred)
- Approximately **2:1** ratio of host RAM to total GPU Memory (especially useful for Dask)
- With 2x or more GPUs, **[NVLink](https://www.nvidia.com/en-us/data-center/nvlink/)** between GPUs

We suggest taking a look at the sample workflow in our Docker container, which illustrates how straightforward a basic XGBoost model training and testing workflow runs with RAPIDS.

{% endcapture %}
{% capture req_right %}

<div id="req"></div>
## System Requirements
{: .section-title-halfs}

All provisioned systems need to be RAPIDS capable. Here's what is required:

<i class="fas fa-microchip text-purple"></i> **GPU:** NVIDIA Pascal™ or better with **[compute capability](https://developer.nvidia.com/cuda-gpus){: target="_blank"}** 6.0+, **[More details here](https://medium.com/dropout-analytics/which-gpus-work-with-rapids-ai-f562ef29c75f){: target="_blank"}**

<i class="fas fa-desktop text-purple"></i> **OS:** Ubuntu 18.04/20.04 or CentOS 7/8 with <code>gcc/++</code> 9.0+
{: .no-tb-margins }
- <i class="fas fa-bullhorn text-purple"></i> See **[RDN 8](https://docs.rapids.ai/notices/rdn0008){: target="_blank"}** for recent changes to <code>gcc/++</code> 9.0 requirements<br/>
- <i class="fas fa-info-circle text-purple"></i> RHEL 7/8 support is provided through CentOS 7/8 builds/installs

<i class="fas fa-desktop text-purple"></i> **Experimental** WSL2 with Windows 11: For details [see this separate install guide](https://developer.nvidia.com/blog/run-rapids-on-microsoft-windows-10-using-wsl-2-the-windows-subsystem-for-linux/){: target="_blank"}**

<i class="fas fa-download text-purple"></i> **CUDA & NVIDIA Drivers:** One of the following supported versions:
{: .no-tb-margins }

- <i class="fas fa-check-circle text-purple"></i> [11.0](https://developer.nvidia.com/cuda-11.0-update1-download-archive){: target="_blank"} & v450.80.02+
- <i class="fas fa-check-circle text-purple"></i> [11.2](https://developer.nvidia.com/cuda-11.2.0-download-archive){: target="_blank"} & v460.27.03+
- <i class="fas fa-check-circle text-purple"></i> [11.4](https://developer.nvidia.com/cuda-11-4-0-download-archive){: target="_blank"} & v470.42.01+
- <i class="fas fa-check-circle text-purple"></i> [11.5](https://developer.nvidia.com/cuda-11-5-0-download-archive){: target="_blank"} & v495.29.05+

{% endcapture %}
{% include section-halfs.html
    background="background-gray"
    padding-top="1em" padding-bottom="1em"
    content-left-half=req_left
    content-right-half=req_right
%}




<!--- MOVE -->

<div id="get-rapids"></div>




{% include selector.html
	background="background-purple"
	padding-top="1em" padding-bottom="1em"
%}
{% include selector-commands-stable.html %}
{% include selector-commands-nightly.html %}

{% capture options_details %}
## details below <br> <i class="fas fa-chevron-down"></i>
{: .section-title-full}

{% endcapture %}

{% include section-single.html
    background="background-purple"
    padding-top="0em" padding-bottom="3em"
    content-single=options_details
%}
{% include slopecap.html
    background="background-purple"
    position="bottom"
    slope="up"
%}


{% capture use_left %}
## <i class="fas fa-laptop-code"></i> Conda Install
You can get a minimal conda installation with **[Miniconda](https://conda.io/miniconda.html){: target="_blank"}** or get the full installation with **[Anaconda](https://www.anaconda.com/download){: target="_blank"}**.

For instructions on how to build a development conda environment, see the **[cuDF README](https://github.com/rapidsai/cudf/blob/main/README.md#conda){: target="_blank"}** for more information. Also refer to the **[cuML README](https://github.com/rapidsai/cuml/blob/main/README.md#conda){: target="_blank"}** for conda install instructions for cuML.

## <i class="far fa-file-code"></i> Build From Source
{: .section-subtitle-top-2}

Checkout the **[cuDF README](https://github.com/rapidsai/cudf/tree/main#development-setup){: target="_blank"}**, **[cuML README](https://github.com/rapidsai/cuml/tree/main#installing-from-source){: target="_blank"}**, or **[cuGraph README](https://github.com/rapidsai/cugraph/tree/main#build-from-source-and-contributing){: target="_blank"}** for from-source build instructions.

## <i class="fas fa-laptop-code"></i> Where is Pip?
{: .section-subtitle-top-2}

Refer to our **[RAPIDS 0.7 Release Drops PIP Packages — and sticks with Conda](https://medium.com/rapids-ai/rapids-0-7-release-drops-pip-packages-47fc966e9472){: target="_blank"}** post for details on why we no longer support PIP installs.

{% endcapture %}

<div id="details"></div>

{% capture use_right %}
## <i class="fab fa-docker"></i> Docker Container

The copied Docker command above should auto-run a notebook server. If it does not, run the following command within the Docker container to launch the notebook server.

```bash
bash /rapids/utils/start-jupyter.sh
```

**NOTE:** This will run **[JupyterLab](https://jupyterlab.readthedocs.io/en/stable/){: target="_blank"}** on your host machine at port 8888.

### Legacy Docker Users
Docker CE v18 & [nvidia-docker2](https://github.com/NVIDIA/nvidia-docker/wiki/Installation-(version-2.0)) users will need to replace the following for compatibility:
```bash
'docker run --gpus all' with 'docker run --runtime=nvidia'
```

### Use JupyterLab to Explore the Notebooks

Notebooks can be found in notebooks directory within the container:

<i class="far fa-folder-open"></i> **`/rapids/notebooks/cuml`** (cuML demos)
{: .no-tb-margins }

<i class="far fa-folder-open"></i> **`/rapids/notebooks/cugraph`** (cuGraph demos)
{: .no-tb-margins }

<i class="far fa-folder-open"></i> **`/rapids/notebooks/xgboost`** (XGBoost demo)
{: .no-tb-margins }

### Advanced Usage

See the **[RAPIDS Container README](https://hub.docker.com/r/rapidsai/rapidsai){: target="_blank"}** page for more information about using custom datasets. **[Docker Hub](https://hub.docker.com/r/rapidsai/rapidsai/){: target="_blank"}** and **[NVIDIA GPU Cloud](https://ngc.nvidia.com/catalog/containers/nvidia:rapidsai:rapidsai){: target="_blank"}** host RAPIDS containers with full list of available **[tags](https://hub.docker.com/r/rapidsai/rapidsai#full-tag-list){: target="_blank"}**.

{% endcapture %}

{% include section-halfs.html
    background="background-gray"
    padding-top="5em" padding-bottom="10em"
    content-left-half=use_left
    content-right-half=use_right
%}


{% include slopecap.html
    background="background-darkpurple"
    position="top"
    slope="up"
%}

{% include cta-footer.html
    name="TRY RAPIDS NOW ONLINE"
    button="LAUNCH IN COLAB"
    link="https://colab.research.google.com/drive/1rY7Ln6rEE1pOlfSHCYOVaqt8OvDO35J0#forceEdit=true&offline=true&sandboxMode=true"
%}