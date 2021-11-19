---
title: "Open GPU Data Science"
description: "A suite of software libraries for executing end-to-end data science completely on GPUs"
tagline: "Open GPU Data Science"
button_text: "GET STARTED"
button_link: "start.html"
layout: default
name: index # added to fix issue with nav bar not highlighting index page
---

# GPU DATA SCIENCE
{: .section-title-full }

{% capture about_top_left %}
## <i class="fal fa-info-circle"></i> Accelerated Data Science
The RAPIDS suite of open source software libraries gives you the freedom to execute end-to-end data science and analytics pipelines entirely on GPUs. <br> **[Learn about RAPIDS <i class="fas fa-angle-double-right"></i>](about.html)**
{% endcapture %}

{% capture about_top_middle %}
## <i class="fal fa-expand-arrows-alt"></i> Scale Out on GPUS
Seamlessly scale from GPU workstations to multi-GPU servers and multi-node clusters with Dask. <br> **[Learn about Dask <i class="fas fa-angle-double-right"></i>](dask.html)**
{% endcapture %}

{% capture about_top_right %}
## <i class="fab fa-python"></i> Python Integration
Accelerate your Python data science toolchain with minimal code changes and no new tools to learn. <br> **[Learn about our libraries <i class="fas fa-angle-double-right"></i>](#libraries)**
{% endcapture %}

{% capture about_bottom_left %}
## <i class="fal fa-bullseye"></i> Top Model Accuracy
Increase machine learning model accuracy by iterating on models faster and deploying them more frequently. <br> **[Learn about RAPIDS for model optimization <i class="fas fa-angle-double-right"></i>](hpo.html)**
{% endcapture %}

{% capture about_bottom_middle %}
## <i class="fal fa-clock"></i> Reduced Training Time
Drastically improve your productivity with more interactive data science tools like XGBoost. <br> **[Learn about XGBoost <i class="fas fa-angle-double-right"></i>](xgboost.html)**
<br> **[Learn about accelerated ML with cuML <i class="fas fa-angle-double-right"></i>](https://docs.rapids.ai/api/cuml/stable/){: target="_blank"}**
{% endcapture %}

{% capture about_bottom_right %}
## <i class="fas fa-code-branch"></i> Open Source
RAPIDS is an open source project. Supported by NVIDIA, it also relies on Numba, Apache Arrow, and many more open source projects. <br> **[Learn about our projects <i class="fas fa-angle-double-right"></i>](community.html)**
{% endcapture %}

{% include section-double-thirds.html
    background="background-white"
    padding-top="1em" padding-bottom="10em"
    content-top-left-third=about_top_left
    content-top-middle-third=about_top_middle
    content-top-right-third=about_top_right
    content-bottom-left-third=about_bottom_left
    content-bottom-middle-third=about_bottom_middle
    content-bottom-right-third=about_bottom_right
%}



{% capture start_left %}
# Getting Started
{: .section-title-halfs}

The RAPIDS data science framework is designed to have a familiar look and feel to data scientist working in Python. Here’s a code snippet where we read in a CSV file and output some descriptive statistics:

```python
import cudf

gdf = cudf.read_csv('path/to/file.csv')
for column in gdf.columns:
    print(gdf[column].mean())

```
Find more details on our **[Get Started Page <i class="fas fa-angle-double-right"></i>](start.html)**

## <i class="fas fa-bolt"></i> Try Now Online
Jump right into a GPU powered RAPIDS notebook online.<br>
Try with **[<i class="fab fa-google"></i> Colaboratory <i class="fa fa-angle-double-right" aria-hidden="true"></i>](https://colab.research.google.com/drive/1rY7Ln6rEE1pOlfSHCYOVaqt8OvDO35J0#forceEdit=true&offline=true&sandboxMode=true){: target="_blank"}**

{% endcapture %}

{% capture start_right %}
## <i class="far fa-bookmark"></i> 10 Minutes to cuDF
{: .section-subtitle-top-1}

Modeled after 10 Minutes to Pandas, this is a short introduction to cuDF that is geared mainly for new users. <br> **[Go to guide <i class="fa fa-angle-double-right" aria-hidden="true"></i>](https://docs.rapids.ai/api/cudf/stable/10min.html){: target="_blank"}**

## <i class="far fa-bookmark"></i> Multi-GPU with Dask-cuDF
{: .section-subtitle-top-1}

A short introduction to multi-GPU solutions with a distributed DataFrame via Dask-cuDF. <br> **[Go to guide <i class="fas fa-angle-double-right"></i>](https://docs.rapids.ai/api/cudf/stable/dask-cudf.html){: target="_blank"}**


## <i class="far fa-bookmark"></i> Example Notebooks
{: .section-subtitle-top-1}

A Github repository with our introductory examples of XGBoost, cuML demos, cuGraph demos, and more. <br> **[Go to repo <i class="fas fa-angle-double-right"></i>](https://github.com/rapidsai/notebooks){: target="_blank"}**


## <i class="far fa-bookmark"></i> Example Community Notebooks
{: .section-subtitle-top-1}

A second Github repository with our extended collection of community contributed notebook examples. <br> **[Go to repo <i class="fas fa-angle-double-right"></i>](https://github.com/rapidsai/notebooks-contrib){: target="_blank"}**


{% endcapture %}
{% include slopecap.html
    background="background-gray"
    position="top"
    slope="down"
%}
{% include section-halfs.html
    background="background-gray"
    padding-top="1em" padding-bottom="1em"
    content-left-half=start_left
    content-right-half=start_right
%}
{% capture posts_title %}
# RAPIDS News
{% endcapture %}
{% include section-single.html
    background="background-gray"
    padding-top="0em" padding-bottom="0em"
    content-single=posts_title
%}

{% include medium-thirds-json.html
    background="background-gray"
    padding-top="1em" padding-bottom="1em"
%}


{% include tweet-thirds-json.html
    background="background-gray"
    padding-top="1em" padding-bottom="10em"
%}



# Community and Projects
{: .section-title-full .padding-top-1em}

{% capture com_top_left %}
![BLAZINGSQL]({{ site.baseurl }}{% link /assets/images/blazingsql.png %}){: .third-image-center}
## <i class="fas fa-code-branch"></i> RAPIDS + BlazingSQL

BlazingSQL is an open source project providing distributed SQL for analytics that enables the integration of enterprise data at scale. RAPIDS is actively contributing to BlazingSQL, and it integrates with RAPIDS cuDF, XGBoost, and RAPIDS cuML for GPU-accelerated data analytics and machine learning. <br> **[Learn more on our BlazingSQL page <i class="fa fa-angle-double-right" aria-hidden="true"></i>](blazingsql.html)**

{% endcapture %}

{% capture com_top_right %}
![Dask]({{ site.baseurl }}{% link /assets/images/dask_logo.png %}){: .third-image-center}
## <i class="fas fa-code-branch"></i> RAPIDS + Dask

Dask is an open source project providing advanced parallelism for analytics that enables performance at scale. RAPIDS is actively contributing to Dask, and it integrates with RAPIDS cuDF, XGBoost, and RAPIDS cuML for GPU-accelerated data analytics and machine learning. <br> **[Learn more on our Dask page <i class="fa fa-angle-double-right" aria-hidden="true"></i>](dask.html)**

{% endcapture %}

{% capture com_bottom_left %}
![xgboost]({{ site.baseurl }}{% link /assets/images/xgboost_logo.png %}){: .third-image-center}
## <i class="fas fa-code-branch"></i> RAPIDS + XGBoost

XGBoost is a well-known gradient boosted decision trees (GBDT) machine learning package used to tackle regression, classification, and ranking problems. The RAPIDS team works closely with the Distributed Machine Learning Common (DMLC) XGBoost organization to upstream code and ensure that all components of the GPU-accelerated analytics ecosystem work together. <br> **[Learn more on our XGBoost page <i class="fa fa-angle-double-right" aria-hidden="true"></i>](xgboost.html)**

{% endcapture %}

{% capture com_bottom_right %}
![cloud]({{ site.baseurl }}{% link /assets/images/RAPIDs-cloud.png %}){: .third-image-center}
## <i class="fas fa-code-branch"></i> RAPIDS + Cloud

RAPIDS’s GPU accelerated data science tools can be deployed on all of the major clouds, allowing anyone to take advantage of the speed increases and TCO reductions that RAPIDS enables.
<br>
**[Learn more on our cloud page <i class="fa fa-angle-double-right" aria-hidden="true"></i>](cloud.html)**
{% endcapture %}

{% capture com2_top_left %}
![Plotly]({{ site.baseurl }}{% link /assets/images/Plotly_Dash_logo.png %}){: .third-image-center}
## <i class="fas fa-code-branch"></i> RAPIDS + Plotly Dash

Plotly’s Dash enables Data Science teams to focus on the data and models, while producing and sharing enterprise-ready analytic apps that sit on top of RAPIDS-accelerated Python dataframes. <br> **[Learn more on our Plotly page <i class="fa fa-angle-double-right" aria-hidden="true"></i>](plotly.html)**

{% endcapture %}

{% capture com2_top_right %}
![HPO]({{ site.baseurl }}{% link /assets/images/csp+hpo.png %}){: .third-image-center}
## <i class="fas fa-code-branch"></i> RAPIDS + HPO

Accelerate Hyperparameter Optimization (HPO) in the Cloud. The RAPIDS team works closely with major cloud providers and open source hyperparameter optimization solutions to ensure smooth integration and high performance, regardless of your deployment platform. <br> **[Learn more on our HPO page <i class="fa fa-angle-double-right" aria-hidden="true"></i>](hpo.html)**

{% endcapture %}

{% capture com2_bottom_left %}
![merlin]({{ site.baseurl }}{% link /assets/images/NVLogo_2D_H.png%}){: .third-image-center}
## <i class="fas fa-code-branch"></i> RAPIDS + NVIDIA MERLIN

NVIDIA Merlin is an open source library providing end-to-end GPU-accelerated recommender systems. Merlin leverages RAPIDs cuDF and Dask cuDF for dataframe transformation during ETL and inference, as well as for the optimized dataloaders in TensorFlow, PyTorch or HugeCTR to accelerate deep learning training. <br> **[Learn more on our Merlin page <i class="fa fa-angle-double-right" aria-hidden="true"></i>](merlin.html)**

{% endcapture %}

{% capture com2_bottom_right %}
![slurm]({{ site.baseurl }}{% link /assets/images/slurm-logo.png%}){: .third-image-center}
## <i class="fas fa-code-branch"></i> RAPIDS + HPC

RAPIDS works extremely well in traditional HPC environments where GPUs are often co-located with accelerated networking hardware such as InfiniBand.
<br> **[Learn more on our HPC page <i class="fa fa-angle-double-right" aria-hidden="true"></i>](/hpc)**

{% endcapture %}

{% capture com3_left %}
![spark]({{ site.baseurl }}{% link /assets/images/spark-logo-trademark.png %}){: .third-image-center}
## <i class="fas fa-code-branch"></i> RAPIDS + Spark

NVIDIA is bringing RAPIDS to Apache Spark to accelerate ETL workflows with GPUs.
<br> **[Learn more on the RAPIDS for Apache Spark page <i class="fa fa-angle-double-right" aria-hidden="true"></i>](https://nvidia.github.io/spark-rapids/){: target="_blank"}**

{% endcapture %}

{% capture com3_right %}
  
{% endcapture %}


{% include section-double-halfs.html
    background="background-white"
    padding-top="2em" padding-bottom="0em"
    content-top-left-half=com_top_left
    content-top-right-half=com_top_right
    content-bottom-left-half=com_bottom_left
    content-bottom-right-half=com_bottom_right
%}
{% include section-double-halfs.html
    background="background-white"
    padding-top="2em" padding-bottom="0em"
    content-top-left-half=com2_top_left
    content-top-right-half=com2_top_right
    content-bottom-left-half=com2_bottom_left
    content-bottom-right-half=com2_bottom_right
%}
{% include section-halfs.html
    background="background-white"
    padding-top="0em" padding-bottom="1em"
    content-left-half=com3_left
    content-right-half=com3_right
%}


# Adopters
{: .section-title-full}
{% include adopter-logos.html
    padding-top="0em" padding-bottom="5em"
%}
