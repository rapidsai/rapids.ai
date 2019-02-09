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
## Installation
#### 1. Setup Prerequisites

* NVIDIA Pascal™ GPU architecture or better
* CUDA [9.2](https://developer.nvidia.com/cuda-92-download-archive) or [10.0](https://developer.nvidia.com/cuda-downloads) compatible nvidia driver
* Ubuntu 16.04 or 18.04
* Python 3.6 or 3.7
* For Docker Images
  * [Docker CE v18+](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
  * [nvidia-docker](https://github.com/nvidia/nvidia-docker/wiki/Installation-(version-2.0)) v2+

#### 2. Install  RAPIDS
##### RAPIDS is available as conda or pip packages, docker images, and from source builds. Use the [Installation Script Generator](#IGS) tool below to select your preferred method, packages, and environment to install RAPIDS. Certain combinations may not be possible and are dimmed automatically. Be sure to review the [prerequisites](#prerequisites) section for more details about requirements to use RAPIDS.

### Installation Script Generator ### {#IGS}
{% include options.html %}

{% endcapture %}
{% include sec-left-purple.html content=section_conda %}


{% capture section_info %}
## Next Steps with RAPIDS

Master RAPIDS by reading our Docs, trying our demos and how-tos, and collaborating with us.<br><br>
[Docs and Resources](/docs.html){: .blue-btn }
[Connect with Us](/community.html){: .blue-btn }
{: .text-center }

{% endcapture %}
{% include sec-right-gray.html content=section_info %}