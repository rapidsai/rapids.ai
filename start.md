---
title: "Getting Started"
description: "Get started with RAPIDS using conda, docker, or from source builds."
tagline: "Try RAPIDS Now"
button_text: "SELECT RELEASE"
button_link: "#get-rapids"
layout: default
redirect_from: "/documentation.html" # redirect from old page to ensure existing links still work
---

{% capture gs_overview %}
# Getting Started
{: .section-title-full }

The RAPIDS data science framework includes a collection of libraries for executing end-to-end data science pipelines completely in the GPU. It is designed to have a familiar look and feel to data scientists working in Python. Here’s a code snippet where we read in a CSV file and output some descriptive statistics:

```python
import cudf
gdf = cudf.read_csv('path/to/file.csv')
for column in gdf.columns:
    print(gdf[column].mean())
```

## GPU Powered Data Science

RAPIDS uses optimized **[NVIDIA CUDA®](https://developer.nvidia.com/cuda-toolkit){: target="_blank"}** primitives and high-bandwidth GPU memory to accelerate data preparation and machine learning. The goal of RAPIDS is not only to accelerate the individual parts of the typical data science workflow, but to accelerate the complete end-to-end workflow.

You can easily install RAPIDS on an 
- on-prem computer with a CUDA enabled GPU or 
- a CUDA enabled GPU cloud instance.

Using

- [conda](#rapids-conda)
- [docker](#rapids-docker)
- [source build](#env-rapids)  

### <i class="fas fa-bolt"></i> Test Drive RAPIDS Now!
Try out RAPIDS in a GPU powered **[<i class="fab fa-google"></i> Colaboratory Notebook Instance!<i class="fa fa-angle-double-right" aria-hidden="true"></i>](https://colab.research.google.com/drive/1rY7Ln6rEE1pOlfSHCYOVaqt8OvDO35J0#forceEdit=true&offline=true&sandboxMode=true){: target="_blank"}**<br>
Note: requires a RAPIDS installation and that Colaboratory provisions you a RAPIDS compatible GPU instance (P4, P100, T4, or V100).

{% endcapture %}

{% include section-single.html
    background="white"
    padding-top="0em" padding-bottom="5em"
    content-single=gs_overview
%}

{% capture prov_overview %}
<div id="req"></div>
# 1. Provision a RAPIDS Capable System
{: .section-title-full }


All provisioned provisioned systems need to be RAPIDS capable.  Here's what you need:

<i class="fas fa-microchip text-purple"></i> **GPU:** NVIDIA Pascal™ or better with **[compute capability](https://developer.nvidia.com/cuda-gpus){: target="_blank"}** 6.0+ 
**[Any of these GPUs or newer will work](https://medium.com/dropout-analytics/which-gpus-work-with-rapids-ai-f562ef29c75f)**

<i class="fas fa-desktop text-purple"></i> **OS:** Ubuntu 18.04/20.04 or CentOS 7/8 with <code>gcc/++</code> 9.0+
  |||  <i class="fas fa-info-circle text-purple"></i> **Experimental:** WSL2 with Windows 11 **[(please see this separate install guide](https://developer.nvidia.com/blog/run-rapids-on-microsoft-windows-10-using-wsl-2-the-windows-subsystem-for-linux/){: target="_blank"})**
{: .no-tb-margins }

- <i class="fas fa-bullhorn text-purple"></i> See [RDN 8](https://docs.rapids.ai/notices/rdn0008) for recent changes to <code>gcc/++</code> 9.0 requirements<br/>
- <i class="fas fa-info-circle text-purple"></i> RHEL 7/8 support is provided through CentOS 7/8 builds/installs



<i class="fas fa-download text-purple"></i> **CUDA & NVIDIA Drivers:** One of the following supported versions:
{: .no-tb-margins }

- <i class="fas fa-check-circle text-purple"></i> [11.0](https://developer.nvidia.com/cuda-11.0-update1-download-archive){: target="_blank"} & v450.51+
- <i class="fas fa-check-circle text-purple"></i> [11.2](https://developer.nvidia.com/cuda-11.2.0-download-archive){: target="_blank"} & v460.32+
{% endcapture %}
{% include section-single.html
    background="white"
    padding-top="0em" padding-bottom="5em"
    content-single=prov_overview
%}

{% capture prov_right %}
## Use RAPIDS in the Cloud Provisoned System
{: .section-title-halfs}


### <i class="fas fa-bolt"></i> Provision 
Learn how to deploy RAPIDS on **[Cloud Service Providers <i class="fa fa-angle-double-right" aria-hidden="true"></i>](https://rapids.ai/cloud){: target="_blank"}**

{% endcapture %}




{% capture prov_left %}
<div id="local"></div>
## Use RAPIDS on a Local Provisioned System
{: .section-subtitle-top-1}

While RAPIDS requires you to have the 

We suggest that you take a look at the sample workflow in our Docker container (described below), which illustrates just how straightforward a basic XGBoost model training and testing workflow looks in RAPIDS.



{% endcapture %}

{% include section-halfs.html
    background="background-white"
    padding-top="1em" padding-bottom="10em"
    content-left-half=prov_left
    content-right-half=prov_right
%}
<div id="env-rapids"></div>
{% capture env_overview %}
# 2. Select and Installation Environment a RAPIDS Capable System
{: .section-title-full }
For most installations, you will need a Conda or Docker environments installed to install RAPIDS.  If you plan to build RAPIDS from source, please check out the **[cuDF README](https://github.com/rapidsai/cudf/tree/main#development-setup){: target="_blank"}**, **[cuML README](https://github.com/rapidsai/cuml/tree/main#installing-from-source){: target="_blank"}**, or **[cuGraph README](https://github.com/rapidsai/cugraph/tree/main#build-from-source-and-contributing){: target="_blank"}** for from-source environment set up and build instructions.

These examples are for Ubuntu.  Please modify appropriately for CentOS or RHEL.
{% endcapture %}
{% include section-single.html
    background="white"
    padding-top="0em" padding-bottom="5em"
    content-single=env_overview
%}
<div id="rapids-docker"></div>
{% capture env_right %}
## [Docker](#rapids-docker)
{: .section-title-halfs}
### <i class="fab fa-docker text-purple"></i> **Docker Overview** 
PAIDS requires both Docker CE v19.03+ and **[nvidia-container-toolkit](https://github.com/NVIDIA/nvidia-docker#quickstart){: target="_blank"}** installed
{: .no-tb-margins }

- <i class="fas fa-history text-purple"></i> [Legacy Support](#-docker-container) - Docker CE v17-18 and [nvidia-docker2](https://github.com/NVIDIA/nvidia-docker/wiki/Installation-(version-2.0)){: target="_blank"}

### Install Docker
**In Terminal:**
#### 1. Download and Install Latest Docker CE Edition
```
curl https://get.docker.com | sh
```
#### 2. Install Latest NVIDIA Docker (Ubuntu Exmple)
```
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
curl -s -L https://nvidia.github.io/libnvidia-container/experimental/$distribution/libnvidia-container-experimental.list | sudo tee /etc/apt/sources.list.d/libnvidia-container-experimental.list
sudo apt-get update
sudo apt-get install -y nvidia-docker2
```   
#### 3. In new, seperate terminal window/tab, (Window 2) run this
```
sudo service docker stop
sudo service docker start
```

##### You can close or keep use to later git clone additional RAPIDS exmaple notebookes on the side

#### 4. Test NVIDIA Docker

```
docker run --gpus all nvcr.io/nvidia/k8s/cuda-sample:nbody nbody -gpu -benchmark
```
##### Legacy Docker Users
Docker CE v18 & [nvidia-docker2](https://github.com/NVIDIA/nvidia-docker/wiki/Installation-(version-2.0)) users will need to replace the following for compatibility:
```bash
'docker run --gpus all' with 'docker run --runtime=nvidia'
```
{% endcapture %}
<div id="rapids-conda"></div>
{% capture env_left %}
## [Conda](#rapids-conda)

{: .section-title-halfs}
### <i class="fas fa-laptop-code"></i> Conda Overview
You can get a minimal conda installation with **[Miniconda](https://conda.io/miniconda.html){: target="_blank"}** or get the full installation with **[Anaconda](https://www.anaconda.com/download){: target="_blank"}**.

### Install Conda
**In Terminal:**
#### 1. Download and run install conda script
```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```
#### 2. Customize your Conda install
Please interact with your terminal window to finish installation.  We recommend enabling [conda-init]()

#### 3. Open a new conda window with Conda initialized



{% endcapture %}
{% include section-halfs.html
    background="background-white"
    padding-top="1em" padding-bottom="1em"
    content-left-half=env_left
    content-right-half=env_right
%}


{% capture install_overview %}
# 3. Install RAPIDS
{: .section-title-full }
Once you've installed your environment, please use the interactive **[RAPIDS Release Selector](#get-rapids)** tool below to create your custom RAPIDS install script.
{% endcapture %}
{% include section-single.html
    background="white"
    padding-top="0em" padding-bottom="2em"
    content-single=install_overview
%}

<div id="get-rapids"></div>
{% capture get_content %}
## [RAPIDS Release Selector](#get-rapids)
{: .section-title-full }

RAPIDS is available as conda packages, docker images, and from source builds. Use the tool below to select your preferred method, packages, and environment to install RAPIDS. Certain combinations may not be possible and are dimmed automatically. Be sure you've met the required **[prerequisites above](#req)** and see the **[details below](#details)**.
{% endcapture %}

{% include slopecap.html
    background="background-purple"
    position="top"
    slope="down"
%}
{% include section-single.html
    background="background-purple"
    padding-top="1em" padding-bottom="1em"
    content-single=get_content
%}
{% include selector.html
	background="background-purple"
	padding-top="1em" padding-bottom="1em"
%}
{% include selector-commands-stable.html %}
{% include selector-commands-nightly.html %}

{% capture options_details %}
<div id="next"></div>
# 4. Next Steps <br> <i class="fas fa-chevron-down"></i>
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
<div id="next"></div>

{% capture use_left %}
{: .section-title-halfs}
## <i class="fas fa-laptop-code"></i> Next Steps with RAPIDS on Conda
1. Install Jupyter Lab
2. Download and Explore the RAPIDS Repo Notebooks and Community Notebooks
3. Run RAPIDS using Python or JupyterLab
```
jupyter-lab --allow-root --ip='0.0.0.0' --NotebookApp.token='**your token**'
```
4. Check out the RAPIDS tutorials and workflows examples
5. Explore our integrations or Install your other favorite Data Science or Machine Learning libraries

{% endcapture %}

{% capture use_right %}
## <i class="fab fa-docker"></i> Next Steps with RAPIDS Docker Container

The copied Docker command above should auto-run a notebook server. If it does not, run the following command within the Docker container to launch the notebook server.

```bash
bash /rapids/utils/start-jupyter.sh
```

**NOTE:** This will run **[JupyterLab](https://jupyterlab.readthedocs.io/en/stable/){: target="_blank"}** on your host machine at port 8888.

### Use JupyterLab to Explore the Demo Notebooks

RAPIDS demo notebooks can be found in the notebooks directory:

<i class="far fa-folder-open"></i> **`/rapids/notebooks/cuml`** (Machine Learning Algorithms)
{: .no-tb-margins }

<i class="far fa-folder-open"></i> **`/rapids/notebooks/cugraph`** (Graph Analytics)
{: .no-tb-margins }

<i class="far fa-folder-open"></i> **`/rapids/notebooks/cuspatial`** (Spatial Analytics)
{: .no-tb-margins }

<i class="far fa-folder-open"></i> **`/rapids/notebooks/cusignal`** (Signal Analytics)
{: .no-tb-margins }

<i class="far fa-folder-open"></i> **`/rapids/notebooks/clx`** (Cyber Security Log Analytics)
{: .no-tb-margins }

<i class="far fa-folder-open"></i> **`/rapids/notebooks/xgboost`** (XGBoost)
{: .no-tb-margins }

You can get more RAPIDS tutorials and workflow examples by `git cloning` the **[RAPIDS Community Notebooks](<addlink>)**

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
