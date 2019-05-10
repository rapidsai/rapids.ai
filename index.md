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
A Github repository with examples of XGBoost, cuML demos, cuGraph demos, and more. **[Go to repo <i class="fas fa-angle-double-right"></i>](https://github.com/rapidsai/notebooks){: target="_blank"}**

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


{% capture com_left %}
# RAPIDS Community
{: .section-title-halfs}
RAPIDS is committed to being open sourced. We strive for a major release **every 6 weeks** (give or take). Below is a generalized release schedule. Learn more on our **[Road To 1.0 post <i class="fas fa-angle-double-right"></i>](https://medium.com/rapids-ai/the-road-to-1-0-building-for-the-long-haul-657ae1afdfd6){: target="_blank"}**

## <i class="far fa-calendar-check"></i> Release Schedule
<svg id="release-schedule-svg" data-name="release-schedule" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 309.3 64.97">
    <defs>
        <style> .cls-1, .cls-2 {fill: none; stroke: #e0e0e0; stroke-miterlimit: 10; stroke-width: 3px; } .cls-2 {stroke-dasharray: 5.98 5.98; } .cls-3, .cls-4, .cls-5 {fill: #fff; } .cls-4 {font-size: 12px; font-family: Helvetica; font-weight: 700; } .cls-5 {font-size: 10px; font-family: Helvetica; } .cls-6 {letter-spacing: -0.07em; } .cls-7 {letter-spacing: -0.02em; } </style> </defs>
    <title>Release-Schedule</title>
    <line class="cls-1" x1="22.46" y1="22.78" x2="154.12" y2="22.78" />
    <line class="cls-1" x1="153.75" y1="22.78" x2="156.75" y2="22.78" />
    <line class="cls-2" x1="162.74" y1="22.78" x2="279.42" y2="22.78" />
    <line class="cls-1" x1="282.41" y1="22.78" x2="285.41" y2="22.78" />
    <circle class="cls-3" cx="22.46" cy="22.78" r="7.6" />
    <circle class="cls-3" cx="154.12" cy="22.78" r="7.6" />
    <circle class="cls-3" cx="285.78" cy="22.78" r="7.6" />
    <text class="cls-4" transform="translate(10.28 10.32)">v0.6</text>
    <text class="cls-4" transform="translate(143.08 10.32)">v0.7</text>
    <text class="cls-4" transform="translate(274.74 10.32)">v0.8</text>
    <text class="cls-5" transform="translate(0 49.41)">MAR 2019</text>
    <text class="cls-5" transform="translate(131.13 49.41)">APR 2019</text>
    <text class="cls-5" transform="translate(263.52 49.41)">MAY 2019</text>
    <text class="cls-5" transform="translate(1.76 60.16)">LEGACY</text>
    <text class="cls-5" transform="translate(135.95 60.16)">STABLE</text>
    <text class="cls-5" transform="translate(265.2 60.16)">NIGHTLY</text>
</svg>
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
    padding-top="5em" padding-bottom="5em" 
    content-left-half=com_left 
    content-right-half=com_right 
%} 


{% capture lib_top_left %}
## <i class="fas fa-terminal"></i> cuDF <span class="api-tag">API</span>

**[GitHub](https://github.com/rapidsai/cudf){: target="_blank"}** **/** **[Docs](https://docs.rapids.ai/api/cudf/stable/){: target="_blank"}** **/** **[Change Log](https://github.com/rapidsai/cudf/blob/master/CHANGELOG.md){: target="_blank"}**

cuDF is a Python GPU DataFrame library (built on the **[Apache Arrow](http://arrow.apache.org/){: target="_blank"}** columnar memory format) for loading, joining, aggregating, filtering, and otherwise manipulating data all in a **[pandas-like](https://pandas.pydata.org/){: target="_blank"}** API familiar to data scientists.

{% endcapture %}

{% capture lib_top_middle %}
## <i class="fas fa-terminal"></i> cuML <span class="api-tag">API</span>

**[GitHub](https://github.com/rapidsai/cuml){: target="_blank"}** **/** **[Docs](https://docs.rapids.ai/api/cuml/stable/){: target="_blank"}** **/** **[Change Log](https://github.com/rapidsai/cuml/blob/master/CHANGELOG.md){: target="_blank"}**

cuML is a suite of libraries that implement machine learning algorithms and mathematical primitives functions that are compatible with other RAPIDS projects, all in a **[scikit-learn-like](https://scikit-learn.org/stable/index.html){: target="_blank"}** API familiar to data scientists.


{% endcapture %}

{% capture lib_top_right %}
## <i class="fas fa-terminal"></i> cuGraph <span class="api-tag">API</span>

**[GitHub](https://github.com/rapidsai/cugraph){: target="_blank"}** **/** **[Docs](https://docs.rapids.ai/api/cugraph/stable/){: target="_blank"}** **/** **[Change Log](https://github.com/rapidsai/cugraph/blob/master/CHANGELOG.md){: target="_blank"}**

cuGraph is a collection of graph analytics that process data in GDF. cuGraph aims at providing a **[NetworkX-like](https://networkx.github.io/){: target="_blank"}** API familiar to data scientists, so they can use it to easily accelerate their workflows without going into the details of CUDA programming.

{% endcapture %}

{% capture lib_bottom_left %}
## <i class="fas fa-terminal"></i> nvStrings <span class="api-tag">API</span>

**[GitHub](https://github.com/rapidsai/custrings){: target="_blank"}** **/** **[Docs](https://docs.rapids.ai/api/nvstrings/stable/){: target="_blank"}** **/** **[Change Log](https://github.com/rapidsai/custrings/blob/master/CHANGELOG.md){: target="_blank"}**

nvStrings, the Python bindings for **[cuStrings](https://github.com/rapidsai/custrings){: target="_blank"}**, provides a pandas-like API that will be familiar to data engineers & data scientists, so they can use it to easily accelerate their workflows without going into the details of CUDA programming.


{% endcapture %}

{% capture lib_bottom_middle %}
## <i class="fas fa-terminal"></i> libcudf <span class="lib-tag">LIB</span>

**[GitHub](https://github.com/rapidsai/cudf){: target="_blank"}** **/** **[Docs](https://docs.rapids.ai/api/libcudf/stable/){: target="_blank"}** **/** **[Change Log](https://github.com/rapidsai/cudf/blob/master/CHANGELOG.md){: target="_blank"}**

libcudf is a C/C++ CUDA library for implementing standard dataframe operations. It is part of the cuDF repository. 

{% endcapture %}

{% capture lib_bottom_right %}
## <i class="fas fa-terminal"></i> RMM <span class="lib-tag">LIB</span>

**[GitHub](https://github.com/rapidsai/rmm){: target="_blank"}** **/** **[Docs](https://docs.rapids.ai/api/rmm/stable/){: target="_blank"}** **/** **[Change Log](https://github.com/rapidsai/rmm/blob/master/CHANGELOG.md){: target="_blank"}**

RAPIDS Memory Manager (RMM) is a central place for all device memory allocations in cuDF (C++ and Python) and other RAPIDS libraries. In addition, it is a replacement allocator for CUDA Device Memory (and CUDA Managed Memory) and a pool allocator to make CUDA device memory allocation / deallocation faster and asynchronous.


{% endcapture %}

{% include section-double-thirds.html 
    background="background-purple" 
    padding-top="1em" padding-bottom="3em" 
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
{: .section-title-full .padding-top-2em }
{% include contributing-logos.html 
    padding-top="1em" padding-bottom="5em" 
%}


# Adopters
{: .section-title-full}
{% include adopter-logos.html 
    padding-top="1em" padding-bottom="5em" 
%}


# Open Source
{: .section-title-full}
{% include open-source-logos.html 
    padding-top="1em" padding-bottom="10em" 
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

