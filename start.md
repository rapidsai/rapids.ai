---
title: "Getting Started"
description: "Get started with RAPIDS using conda or docker."
tagline: "Get RAPIDS Now"
button_text: "SELECT RELEASE"
button_link: "#get-rapids"
layout: default
redirect_from: "/documentation.html" # redirect from old page to ensure existing links still work
---

# Getting Started
{: .section-title-full}

{% capture intro %}
The RAPIDS data science framework is a collection of libraries for executing end-to-end data science pipelines completely in the GPU.
{: .subtitle}

{% endcapture %}
{% include section-single.html
    background="background-white" 
    padding-top="0em" padding-bottom="0em" 
    content-single=intro
%}


{% capture start_left %}
## <i class="fas fa-bolt"></i> GPU Accelerated Data Science
RAPIDS uses optimized **[NVIDIA CUDA®](https://developer.nvidia.com/cuda-toolkit){: target="_blank"}** primitives and high-bandwidth GPU memory to accelerate data preparation and machine learning. The goal of RAPIDS is not only to accelerate the individual parts of the typical data science workflow, but to accelerate the complete end-to-end workflow.

It is designed to have a familiar look and feel to data scientists working in Python. Here's a code snippet where we read in a CSV file and output some descriptive statistics:

```python
import cudf
df = cudf.read_csv('path/to/file.csv')
for column in df.columns:
    print(df[column].mean())
```

{% endcapture %}
{% capture start_right %}

## <i class="fa-solid fa-arrow-pointer"></i> Test Drive RAPIDS Now

Jump right into a GPU powered RAPIDS notebook, online, with either **[SageMaker Studio Lab](https://studiolab.sagemaker.aws/)** or **[Colab](https://colab.research.google.com/){: target="_blank"}** 
(currently only supports **[RAPIDS v21.12](https://docs.rapids.ai/notices/rsn0014/)**):

<a href="smsl.html" target="_blank"> <img src="{{ site.baseurl }}{% link /assets/images/Open-StudioLab.png%}" alt="Studio Lab"> </a>

<a href="https://colab.research.google.com/drive/1rY7Ln6rEE1pOlfSHCYOVaqt8OvDO35J0#forceEdit=true&offline=true&sandboxMode=true" target="_blank"> <img src="{{ site.baseurl }}{% link /assets/images/Open-Colab.png%}" alt="CoLab"> </a>

{% endcapture %}
{% capture gs_overview %}
# Installation Overview
{: .section-title-full}

In four steps, easily install RAPIDS on a local system or cloud instance with a CUDA enabled GPU for either **[Conda](#conda)** or **[Docker](#docker)** and then explore our user guides and examples.

{% endcapture %}
{% capture gs_left %}
## **[<i class="fad fa-chevron-double-down"></i> Step 1: Provision A System](#requirements)** 
- Check system requirements
- Choose a cloud or local system

## **[<i class="fad fa-chevron-double-down"></i> Step 2: Install Environment](#environment)**
- Choose to use Conda or Docker
- Choose to Build from source 

{% endcapture %}
{% capture gs_right%}
## **[<i class="fad fa-chevron-double-down"></i> Step 3: Install RAPIDS](#get-rapids)**
- Select and install RAPIDS libraries

## **[<i class="fad fa-chevron-double-down"></i> Step 4: Learn More](#next-steps)**
- Check out examples and user guides

{% endcapture %}
{% include section-halfs.html
    background="background-white"
    padding-top="1em" padding-bottom="3em"
    content-left-half=start_left
    content-right-half=start_right
%}
{% include section-single.html
    background="background-white"
    padding-top="3em" padding-bottom="0em"
    content-single=gs_overview
%}
{% include section-halfs.html
    background="background-white"
    padding-top="1em" padding-bottom="10em"
    content-left-half=gs_left
    content-right-half=gs_right
%}


<div id="requirements"></div>
{% capture prov %}
# Step 1: Provision A System
{: .section-title-full}

{: .section-title-halfs}
{% endcapture %}
{% capture req_left%}
## <i class="fa-regular fa-memory"></i> System Requirements

All provisioned systems need to be RAPIDS capable. Here's what is required:

<i class="fas fa-microchip text-purple"></i> **GPU:** NVIDIA Pascal™ or better with **[compute capability](https://developer.nvidia.com/cuda-gpus){: target="_blank"}** 6.0+ **[More details <i class="fa fa-angle-double-right" aria-hidden="true"></i>](https://medium.com/dropout-analytics/which-gpus-work-with-rapids-ai-f562ef29c75f){: target="_blank"}**

<i class="fas fa-desktop text-purple"></i> **OS:** Ubuntu 18.04/20.04 or CentOS 7/8 with <code>gcc/++</code> 9.0+
{: .no-tb-margins }
- <i class="fas fa-info-circle text-purple"></i> RHEL 7/8 support is provided through CentOS 7/8 builds/installs
- <i class="fas fa-desktop text-purple"></i> Experimental WSL2 on Windows11 **[See separate install guide <i class="fa fa-angle-double-right" aria-hidden="true"></i>](https://developer.nvidia.com/blog/run-rapids-on-microsoft-windows-10-using-wsl-2-the-windows-subsystem-for-linux/){: target="_blank"}**

<i class="fas fa-download text-purple"></i> **CUDA & NVIDIA Drivers:** One of the following supported versions:
{: .no-tb-margins }

- <i class="fas fa-check-circle text-purple"></i> [11.0](https://developer.nvidia.com/cuda-11.0-update1-download-archive){: target="_blank"} & v450.80.02+
- <i class="fas fa-check-circle text-purple"></i> [11.2](https://developer.nvidia.com/cuda-11.2.0-download-archive){: target="_blank"} & v460.27.03+
- <i class="fas fa-check-circle text-purple"></i> [11.4](https://developer.nvidia.com/cuda-11-4-0-download-archive){: target="_blank"} & v470.42.01+
- <i class="fas fa-check-circle text-purple"></i> [11.5](https://developer.nvidia.com/cuda-11-5-0-download-archive){: target="_blank"} & v495.29.05+

{% endcapture %}
{% capture req_mid %}
## <i class="fa-regular fa-cloud"></i> RAPIDS Cloud Systems

Learn how to deploy RAPIDS on <br> **[Cloud Service Providers <i class="fa fa-angle-double-right" aria-hidden="true"></i>](https://rapids.ai/cloud){: target="_blank"}**

<a href="cloud.html#aws" target="_blank"> <img class="quarter-image-center" src="{{ site.baseurl }}{% link /assets/images/AWS-logo.png %}" alt="AWS"> </a>

<a href="cloud.html#azure" target="_blank"> <img class="quarter-image-center" src="{{ site.baseurl }}{% link /assets/images/azure-ml.png %}" alt="Azure ML"> </a>

<a href="cloud.html#googlecloud" target="_blank"> <img class="quarter-image-center" src="{{ site.baseurl }}{% link /assets/images/GCP-logo.png %}" alt="GCP"> </a>

<a href="https://www.paperspace.com/gpu-cloud" target="_blank"> <img class="quarter-image-center " src="{{ site.baseurl }}{% link /assets/images/paperspace_small.png %}" alt="Paperspace"> </a>

{% endcapture %}
{% capture req_right %}
## <i class="fa-regular fa-computer"></i> RAPIDS Local Systems

Aside from the system requirements, other considerations for best performance include:
{: .no-tb-margins }

- SSD drive (NVMe preferred)
- Approximately **2:1** ratio of host RAM to total GPU Memory (especially useful for Dask)
- **[NVLink](https://www.nvidia.com/en-us/data-center/nvlink/)** if with 2 or more GPUs

We suggest taking a look at the sample workflow in our Docker container, which illustrates how straightforward a basic XGBoost model training and testing workflow runs with RAPIDS.
{% endcapture %}
{% include slopecap.html
    background="background-gray"
    position="top"
    slope="down"
%}
{% include section-single.html
    background="background-gray" 
    padding-top="3em" padding-bottom="0em" 
    content-single=prov
%}
{% include section-thirds.html 
    background="background-gray" 
    padding-top="0em" padding-bottom="10em" 
    content-left-third=req_left
    content-middle-third=req_mid
    content-right-third=req_right
%}

<div id="environment"></div>
<div id="docker"></div>
<div id="source"></div>
<div id="conda"></div>
{% capture env_overview %}
# Step 2: Install Environment
{: .section-title-full }

For most installations, you will need a Conda or Docker environments installed for RAPIDS. Note, these examples are for Ubuntu. Please modify appropriately for CentOS or RHEL.

{% endcapture %}
{% include slopecap.html
    background="background-white"
    position="top"
    slope="up"
%}
{% include section-single.html
    background="background-white"
    padding-top="3em" padding-bottom="1em"
    content-single=env_overview
%}

{% capture env_right %}
## <i class="fab fa-docker text-purple"></i> Docker
{: .section-title-halfs}

RAPIDS requires both Docker CE v19.03+ and **[nvidia-container-toolkit](https://github.com/NVIDIA/nvidia-docker#quickstart){: target="_blank"}** installed.
{: .no-tb-margins }

- <i class="fas fa-history text-purple"></i> Legacy Support: Docker CE v17-18 and **[nvidia-docker2](https://github.com/NVIDIA/nvidia-docker/wiki/Installation-(version-2.0)){: target="_blank"}**


**1. Download and Install.** Copy command below to download and install the latest Docker CE Edition:

```
curl https://get.docker.com | sh
```
{: .margin-bottom-3em}

**2. Install Latest NVIDIA Docker.** For example, this is the Ubuntu Example:

```
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
curl -s -L https://nvidia.github.io/libnvidia-container/experimental/$distribution/libnvidia-container-experimental.list | sudo tee /etc/apt/sources.list.d/libnvidia-container-experimental.list
sudo apt-get update
sudo apt-get install -y nvidia-docker2
```   
{: .margin-bottom-3em}

**3. Start Docker.** In new terminal window run:
```
sudo service docker stop
sudo service docker start
```
{: .margin-bottom-3em}


**4a. Test NVIDIA Docker:**

```
docker run --gpus all nvcr.io/nvidia/k8s/cuda-sample:nbody nbody -gpu -benchmark
```
{: .margin-bottom-3em}

**4b. Legacy Docker Users.** Docker CE v18 & **[nvidia-docker2](https://github.com/NVIDIA/nvidia-docker/wiki/Installation-(version-2.0)){: target="_blank"}** users will need to replace the following for compatibility:
```bash
'docker run --gpus all' with 'docker run --runtime=nvidia'
```
{: .margin-bottom-3em}

{% endcapture %}



{% capture env_left %}
## <i class="fas fa-laptop-code"></i> Conda
{: .section-title-halfs}

RAPIDS can use either a minimal conda installation with **[Miniconda](https://conda.io/miniconda.html){: target="_blank"}** or a full installation of **[Anaconda](https://www.anaconda.com/download){: target="_blank"}**. Below is a quick installation guide using miniconda.

**1. Download and Run Install Script**. Copy the command below to download and run the miniconda install script:
```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```
{: .margin-bottom-3em}

**2. Customize Conda and Run the Install.** Use the terminal window to finish installation. Note, we recommend enabling `conda-init`.

**3. Start Conda.** Open a new terminal window, which should now show Conda initialized.
{: .padding-bottom-3em }

## <i class="fa-regular fa-binary"></i> Build From Source
{: .section-title-halfs}

To build RAPIDS from source, check each libraries` readme. For example the **[cuDF README](https://github.com/rapidsai/cudf/tree/main#development-setup){: target="_blank"}** has details for source environment setup and build instructions. Further links are provided in the selector tool. If additional help is needed reach out on our [Slack Channel](https://join.slack.com/t/rapids-goai/shared_invite/zt-trnsul8g-Sblci8dk6dIoEeGpoFcFOQ). 
{: .padding-bottom-3em }

## <i class="fas fa-laptop-code"></i> Where is PIP?
{: .section-title-halfs}

Refer to this **[blog post](https://medium.com/rapids-ai/rapids-0-7-release-drops-pip-packages-47fc966e9472){: target="_blank"}** for details on why PIP is not currently supported. PIP may be supported in future releases. 
{% endcapture %}
{% include section-halfs.html
    background="background-white"
    padding-top="1em" padding-bottom="10em"
    content-left-half=env_left
    content-right-half=env_right
%}


<div id="get-rapids"></div>
{% capture selector_header %}
# Step 3: Install RAPIDS
{: .section-title-full}

RAPIDS is available in conda packages, docker images, and from source builds. Use the tool below to select your preferred method, packages, and environment to install RAPIDS. Certain combinations may not be possible and are dimmed automatically. Be sure you've met the required **[Prerequisites above](#requirements)** and see the **[Next Steps](#next-steps)** below.
{: .padding-bottom-3em }

## **Release Selector**
{: .section-title-full}

{% endcapture %}
{% include slopecap.html
    background="background-purple"
    position="top"
    slope="up"
%}
{% include section-single.html
    background="background-purple"
    padding-top="3em" padding-bottom="0em"
    content-single=selector_header
%}
{% include selector.html
	background="background-purple"
	padding-top="0em" padding-bottom="10em"
%}


<div id="next-steps"></div>
{% capture next_steps %}
# Step 4: Learn More
{: .section-title-full}

Once installation has been successful, explore the capabilities of RAPIDS with the provided notebooks, tutorials, and guides below.

{% endcapture %}
{% include slopecap.html
    background="background-gray"
    position="top"
    slope="up"
%}
{% include section-single.html
    background="background-gray"
    padding-top="5em" padding-bottom="0em"
    content-single=next_steps
%}


{% capture use_left %}
# RAPIDS on Conda
{: .section-title-halfs}

## <i class="far fa-bookmark"></i> Get Example Notebooks


**1. Install Jupyter Lab.** If it or Jupyter Notebook is not already installed. 

**2. Get Notebooks.** See links to the RAPIDS Notebooks and Community Notebooks below.

**3. Run RAPIDS.** Use Python directly or start JupyterLab as below:
```
jupyter-lab --allow-root --ip='0.0.0.0' --NotebookApp.token='**your token**'
```
{: .margin-bottom-3em}

**4. Check out the RAPIDS tutorials and workflows examples.**

**5. Explore.** See our integrations or install other favorite Data Science or Machine Learning libraries.
{: .padding-bottom-3em }


## <i class="fa-brands fa-github"></i> RAPIDS User Guide Repositories


**[Go to RAPIDS Notebooks](https://github.com/rapidsai/notebooks){: target="_blank"}** or clone directly:
```
git clone https://github.com/rapidsai/notebooks.git
git submodule update --init --remote --no-single-branch --depth 1
```
{: .margin-bottom-3em}

**[Go To RAPIDS Community Notebooks](https://github.com/rapidsai-community/notebooks-contrib){: target="_blank"}** or clone directly:
```
git clone https://github.com/rapidsai-community/notebooks-contrib.git
```
{: .margin-bottom-3em}

**[Go To Cloud ML Notebooks](https://github.com/rapidsai/cloud-ml-examples){: target="_blank"}** or clone directly:
```
git clone https://github.com/rapidsai/cloud-ml-examples.git
```
{: .margin-bottom-3em}

{% endcapture %}
{% capture use_right %}
# RAPIDS on Docker
{: .section-title-halfs}

## <i class="fa-regular fa-circle-nodes"></i> Running Multi-Node/ <br> Multi-GPU (MNMG) Environment


To start the container in an MNMG environment:

```bash
docker run -t -d --gpus all --shm-size=1g --ulimit memlock=-1 -v $PWD:/ws <container label>
``` 
{: .margin-bottom-3em}

The standard docker command may be sufficient, but the additional arguments ensures more stability.  See the **[NCCL docs](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/troubleshooting.html#sharing-data){: target="_blank"}** and **[UCX docs](https://github.com/openucx/ucx/blob/master/docs/source/running.md#running-in-docker-containers){: target="_blank"}** for more details on MNMG usage.
{: .padding-bottom-3em }


## <i class="far fa-bookmark"></i> Start / Stop Jupyter Lab Notebooks
Either the standard single GPU or the modified MNMG Docker command above should auto-run a Jupyter Lab Notebook server. If it does not, or a restart is needed, run the following command within the Docker container to launch the notebook server:

```bash
bash /rapids/utils/start-jupyter.sh
```
{: .margin-bottom-3em}

If, for whatever reason, you need to shut down the Jupyter Lab server, use:

```bash
bash /rapids/utils/stop-jupyter.sh
```
{: .margin-bottom-3em}

**NOTE:** Defaults will run **[JupyterLab](https://jupyterlab.readthedocs.io/en/stable/){: target="_blank"}** on your host machine at port: `8888`.
{: .padding-bottom-3em }


## <i class="far fa-bookmark"></i> Explore RAPIDS Demo Notebooks

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

You can get more RAPIDS tutorials and workflow examples by `git cloning` the **[RAPIDS Community Notebooks](https://github.com/rapidsai-community/notebooks-contrib){: target="_blank"}**.
{: .padding-bottom-3em }

### <i class="fa-solid fa-screwdriver-wrench"></i> Advanced Usage

See the **[RAPIDS Container README](https://hub.docker.com/r/rapidsai/rapidsai){: target="_blank"}** for more information about using custom datasets. **[Docker Hub](https://hub.docker.com/r/rapidsai/rapidsai/){: target="_blank"}** and **[NVIDIA GPU Cloud](https://ngc.nvidia.com/catalog/containers/nvidia:rapidsai:rapidsai){: target="_blank"}** host RAPIDS containers with full list of available **[tags](https://hub.docker.com/r/rapidsai/rapidsai#full-tag-list){: target="_blank"}**.

{% endcapture %}

{% include section-halfs.html
    background="background-gray"
    padding-top="1em" padding-bottom="10em"
    content-left-half=use_left
    content-right-half=use_right
%}

{% include slopecap.html
    background="background-darkpurple"
    position="top"
    slope="down"
%}

{% include cta-footer.html
    name="INSTALL RAPIDS NOW"
    button="SELECT RELEASE"
    link="start.html#get-rapids"
%}
