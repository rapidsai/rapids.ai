---
title: "Open GPU Data Science | RAPIDS"
og_title: "RAPIDS: A Data Science & Analytics Pipeline Accelerator"
og_description: "A suite of software libraries for executing end-to-end data science completely on GPUs"
brand_name: ""
brand_tagline: "Open GPU Data Science"
brand_button: "GET STARTED"
brand_link: "start.html"
layout: default
---

# GPU DATA SCIENCE
{: .section-title-full }

{% capture about_top_left %}
## <i class="fas fa-info"></i> Accelerated Data Science
The RAPIDS suite of open source software libraries gives you the freedom to execute end-to-end data science and analytics pipelines entirely on GPUs. **[Learn more <i class="fas fa-angle-double-right"></i>](about.html)**
{% endcapture %}

{% capture about_top_middle %}
## <i class="fas fa-expand-arrows-alt"></i> Scale Out on GPUS
Seamlessly scale from GPU workstations to multi-GPU servers and multi-node clusters with Dask. **[Learn more about Dask <i class="fas fa-angle-double-right"></i>](https://dask.org/){: target="_blank"}**
{% endcapture %}

{% capture about_top_right %}
## <i class="fab fa-python"></i> Python Integration
Accelerate your Python data science toolchain with minimal code changes and no new tools to learn.
{% endcapture %}

{% capture about_bottom_left %}
## <i class="fas fa-bullseye"></i> Top Model Accuracy
Increase machine learning model accuracy by iterating on models faster and deploying them more frequently.
{% endcapture %}

{% capture about_bottom_middle %}
## <i class="far fa-clock"></i> Reduced Training Time
Drastically improve your productivity with more interactive data science.
{% endcapture %}

{% capture about_bottom_right %}
## <i class="fas fa-code-branch"></i> Open Source
RAPIDS is an open source project. Supported by NVIDIA, it also relies on numba, apache arrow, and many more open source projects . **[Learn more <i class="fas fa-angle-double-right"></i>](community.html)**
{% endcapture %}

{% include section-double-thirds.html 
    background="background-white" 
    padding-top="0" padding-bottom="2" 
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
<br>
Find more details on our **[get started section <i class="fas fa-angle-double-right"></i>](start.html)**

{% endcapture %}

{% capture start_right %}
## <i class="far fa-bookmark"></i> 10 Minutes to cuDF
{: .section-subtitle-top-1}

Modeled after 10 Minutes to Pandas, this is a short introduction to cuDF that is geared mainly for new users. **[Go to guide <i class="fa fa-angle-double-right" aria-hidden="true"></i>](https://rapidsai.github.io/projects/cudf/en/latest/10min.html){: target="_blank"}**

## <i class="far fa-bookmark"></i> GDF Cheat Sheet
A handy PDF reference guide for handling GPU Data Frames (GDF) with cuDF. **[Download PDF <i class="fas fa-angle-double-right"></i>](https://rapids.ai/assets/files/cheatsheet.pdf){: target="_blank"}**

## <i class="far fa-bookmark"></i> Example Notebooks
A Github repository with examples for cuML using knn, dbscan, pca and tsvd, the End-to-End Mortgage demo, cuGraph demos, and more. **[Go to repo <i class="fas fa-angle-double-right"></i>](https://github.com/rapidsai/notebooks){: target="_blank"}**

## <i class="fas fa-bolt"></i> Try Now In Colaboratory
Jump right into a GPU powered RAPIDS notebook with **[Colabratory](https://colab.research.google.com/notebooks/welcome.ipynb){: target="_blank"}** for free. **[Go to example notebook <i class="fas fa-angle-double-right"></i>](https://colab.research.google.com/drive/1XTKHiIcvyL5nuldx0HSL_dUa8yopzy_Y#forceEdit=true&offline=true&sandboxMode=true){: target="_blank"}**

{% endcapture %}
{% include slopecap.html 
    background="background-gray" 
    position="top" 
    slope="down" 
%}
{% include section-halfs.html 
    background="background-gray" 
    padding-top="0" padding-bottom="2" 
    content-left-half=start_left 
    content-right-half=start_right 
%} 


{% include medium-thirds-json.html
    background="background-gray"
    padding-top="0" padding-bottom="0" 
%}


{% include tweet-thirds-json.html
    background="background-gray"
    padding-top="0" padding-bottom="2" 
%}


{% capture com_left %}
# RAPIDS Community
{: .section-title-halfs}
RAPIDS is committed to being open sourced. We strive for a major release **every 6 weeks** (give or take). Below is a generalized release schedule. **[Learn more on our road to 1.0 post <i class="fas fa-angle-double-right"></i>](https://medium.com/rapids-ai/the-road-to-1-0-building-for-the-long-haul-657ae1afdfd6){: target="_blank"}**

## <i class="far fa-calendar-check"></i> Release Schedule
JAN-2019 <span class="bold">v0.5</span> (previous)
{: .release-version}
<i class="fas fa-chevron-right"></i> MAR-2019 <span class="bold">v0.6</span> (current)
{: .release-version}
MAY-2019 <span class="bold">v0.7</span> (planned)
{: .release-version}
{% endcapture %}

{% capture com_right %}
## <i class="fas fa-code"></i> RAPIDS APIS and Libraries
{: .section-subtitle-top-1}

RAPIDS is open source licensed under Apache 2.0, spanning multiple projects that range from GPU dataframes to GPU accelerated ML algorithms. Its also provides native array_interface support, allowing Apache Arrow data to be pushed to deep learning frameworks. **[Learn more <i class="fas fa-angle-double-right"></i>](about.html)**

## <i class="fab fa-github"></i> Contributing
Whether you are new to RAPIDS, looking to help, or are part of the team, learn about our contributing guidelines on our contributing page. **[Go to Docs <i class="fas fa-angle-double-right"></i>](https://docs.rapids.ai/contributing){: target="_blank"}**
{% endcapture %}

{% include slopecap.html 
    background="background-purple" 
    position="top" 
    slope="up" 
%}
{% include section-halfs.html 
    background="background-purple" 
    padding-top="1" padding-bottom="1" 
    content-left-half=com_left 
    content-right-half=com_right 
%} 


{% capture lib_top_left %}
## <i class="fas fa-terminal"></i> cuDF
cuDF is a Python GPU DataFrame library (built on the **[Apache Arrow](http://arrow.apache.org/){: target="_blank"}** columnar memory format) for loading, joining, aggregating, filtering, and otherwise manipulating data all in a **[pandas-like](https://pandas.pydata.org/){: target="_blank"}** API familiar to data scientists.
<br>
**[GitHub](https://github.com/rapidsai/cudf){: target="_blank"}** | **[Docs](https://docs.rapids.ai/api/cudf/stable/){: target="_blank"}** | **[Change Log](https://github.com/rapidsai/cudf/blob/branch-0.7/CHANGELOG.md){: target="_blank"}**
{% endcapture %}

{% capture lib_top_middle %}
## <i class="fas fa-terminal"></i> cuML
cuML is a suite of libraries that implement machine learning algorithms and mathematical primitives functions that are compatible with other RAPIDS projects, all in a **[scikit-learn-like](https://scikit-learn.org/stable/index.html){: target="_blank"}** API familiar to data scientists.
<br>
**[GitHub](https://github.com/rapidsai/cuml){: target="_blank"}** | **[Docs](https://docs.rapids.ai/api/cuml/stable/){: target="_blank"}** | **[Change Log](https://github.com/rapidsai/cuml/blob/branch-0.7/CHANGELOG.md){: target="_blank"}**
{% endcapture %}

{% capture lib_top_right %}
## <i class="fas fa-terminal"></i> cuGraph
cuGraph is a collection of graph analytics that process data in GDF. cuGraph aims at providing a **[NetworkX-like](https://networkx.github.io/){: target="_blank"}** API familiar to data scientists, so they can use it to easily accelerate their workflows without going into the details of CUDA programming.
<br>
**[GitHub](https://github.com/rapidsai/cugraph){: target="_blank"}** | **[Docs](https://docs.rapids.ai/api/cugraph/stable/){: target="_blank"}** | **[Change Log](https://github.com/rapidsai/cugraph/blob/branch-0.7/CHANGELOG.md){: target="_blank"}**
{% endcapture %}

{% capture lib_bottom_left %}
## <i class="fas fa-terminal"></i> nvStrings
nvStrings, the Python bindings for **[cuStrings](https://github.com/rapidsai/custrings){: target="_blank"}**, provides a pandas-like API that will be familiar to data engineers & data scientists, so they can use it to easily accelerate their workflows without going into the details of CUDA programming.
<br>
**[GitHub](https://github.com/rapidsai/custrings){: target="_blank"}** | **[Docs](https://docs.rapids.ai/api/nvstrings/stable/){: target="_blank"}** | **[Change Log](https://github.com/rapidsai/custrings/blob/branch-0.4/CHANGELOG.md){: target="_blank"}**
{% endcapture %}

{% capture lib_bottom_middle %}
## <i class="fas fa-terminal"></i> libcudf
libcudf is a C/C++ CUDA library for implementing standard dataframe operations. It is part of the cuDF repository. 
<br>
**[GitHub](https://github.com/rapidsai/cudf){: target="_blank"}** | **[Docs](https://docs.rapids.ai/api/libcudf/stable/){: target="_blank"}** | **[Change Log](https://github.com/rapidsai/cudf/blob/branch-0.7/CHANGELOG.md){: target="_blank"}**
{% endcapture %}

{% capture lib_bottom_right %}
## <i class="fas fa-terminal"></i> RMM 
RAPIDS Memory Manager (RMM) is a central place for all device memory allocations in cuDF (C++ and Python) and other RAPIDS libraries. In addition, it is a replacement allocator for CUDA Device Memory (and CUDA Managed Memory) and a pool allocator to make CUDA device memory allocation / deallocation faster and asynchronous.
<br>
**[GitHub](https://github.com/rapidsai/rmm){: target="_blank"}** | **[Docs](https://docs.rapids.ai/api/rmm/stable/){: target="_blank"}** | **[Change Log](https://github.com/rapidsai/rmm/blob/branch-0.7/CHANGELOG.md){: target="_blank"}**
{% endcapture %}

{% include section-double-thirds.html 
    background="background-purple" 
    padding-top="0" padding-bottom="1" 
    content-top-left-third=lib_top_left 
    content-top-middle-third=lib_top_middle 
    content-top-right-third=lib_top_right 
    content-bottom-left-third=lib_bottom_left 
    content-bottom-middle-third=lib_bottom_middle 
    content-bottom-right-third=lib_bottom_right 
%}
{% include slopecap.html 
    background="background-purple" 
    position="bottom" 
    slope="down"
%}


# Contributors
{: .section-title-full}
{% include contributing-logos.html 
    padding-top="0" padding-bottom="1" 
%}


# Adopters
{: .section-title-full}
{% include adopter-logos.html 
    padding-top="0" padding-bottom="1" 
%}


# Open Source
{: .section-title-full}
{% include open-source-logos.html 
    padding-top="0" padding-bottom="2" 
%}

{% include slopecap.html 
    background="background-darkpurple" 
    position="top" 
    slope="up"
%}
{% include cta-footer.html 
    name="Experience Data Science on GPUs with RAPIDS" 
    tagline=""
    button="GET STARTED"
    link="start.html"
%}

