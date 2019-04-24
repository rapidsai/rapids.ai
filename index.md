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
The RAPIDS suite of open source software libraries gives you the freedom to execute end-to-end data science and analytics pipelines entirely on GPUs. <a href="about.html" class="bold">Learn more <i class="fas fa-angle-double-right"></i></a>
{% endcapture %}

{% capture about_top_middle %}
## <i class="fas fa-expand-arrows-alt"></i> Scale Out on GPUS
Seamless scale from GPU workstations to multi-GPU servers and multi-node clusters.
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
The open-source software is customizable, extensible, interoperable --supported by NVIDIA and built on Apache Arrow.
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

The RAPIDS data science framework is designed to have a familiar look and feel to data scientist working in Python. Here’s a code snippet where we read in a CSV file and output some descriptive statistics. Find more details on our <a class="bold" href="start.html"> get started section <i class="fas fa-angle-double-right"></i></a>

```python
import cudf

gdf = cudf.read_csv('path/to/file.csv')
for column in gdf.columns:
    print(gdf[column].mean())

```
{% endcapture %}

{% capture start_right %}
## <i class="far fa-bookmark"></i> 10 Minutes to cuDF
{: .section-subtitle-top}

Modeled after 10 Minutes to Pandas, this is a short introduction to cuDF that is geared mainly for new users. <a class="bold" href="https://rapidsai.github.io/projects/cudf/en/latest/10min.html">Go to guide <i class="fa fa-angle-double-right" aria-hidden="true"></i></a>

## <i class="far fa-bookmark"></i> GDF Cheat Sheet
A handy PDF reference guide for handling GPU Data Frames (GDF) with cuDF. <a class="bold" href="https://rapids.ai/assets/files/cheatsheet.pdf">Download PDF <i class="fas fa-angle-double-right"></i></a>

## <i class="far fa-bookmark"></i> Example Notebooks
A Github repository with examples for cuML using knn, dbscan, pca and tsvd, the End-to-End Mortgage demo, cuGraph demos, and more. <a class="bold" href="https://github.com/rapidsai/notebooks">Go to repo <i class="fas fa-angle-double-right"></i></a>

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
RAPIDS is committed to being open sourced. We strive for a major release <strong>every 6 weeks</strong> (give or take). Below is a generalized release schedule. <a class="bold" href="https://medium.com/rapids-ai/the-road-to-1-0-building-for-the-long-haul-657ae1afdfd6"> Learn more on our road to 1.0 post <i class="fas fa-angle-double-right"></i></a>

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
{: .section-subtitle-top}

RAPIDS is open sourced under the Apache 2.0 open-source license, spanning multiple projects that range from GPU dataframes to GPU accelerated ML algoritms. Its also provides native array_interface support, allowing Apache Arrow stored data to be pushed to deep learning frameworks such as PyTorch and Chainer. Learn more on the <a class="bold" href="about.html">about page <i class="fas fa-angle-double-right"></i></a>

## <i class="fab fa-github"></i> Contributing
Whether you are new to RAPIDS, looking to help, or are part of the team, learn about our contributiong guidelines on the <a class="bold" href="https://docs.rapids.ai/contributing"> docs page <i class="fas fa-angle-double-right"></i></a>
{% endcapture %}

{% include slopecap.html 
    background="background-purple" 
    position="top" 
    slope="up" 
%}
{% include section-halfs.html 
    background="background-purple" 
    padding-top="0" padding-bottom="1" 
    content-left-half=com_left 
    content-right-half=com_right 
%} 


{% capture lib_top_left %}
## <i class="fas fa-terminal"></i> cuDF
cuDF is a Python GPU DataFrame library (built on the <a href="http://arrow.apache.org/" target="_blank">Apache Arrow</a> columnar memory format) for loading, joining, aggregating, filtering, and otherwise manipulating data.
<br>
<a href="https://github.com/rapidsai/cudf" class="lib-link">GitHub</a> | <a href="https://docs.rapids.ai/api/cudf/stable/" class="lib-link">Docs</a> | <a href="https://github.com/rapidsai/cudf/blob/branch-0.7/CHANGELOG.md" class="lib-link">Change Log</a>
{% endcapture %}

{% capture lib_top_middle %}
## <i class="fas fa-terminal"></i> cuML
cuML is a suite of libraries that implement machine learning algorithms and mathematical primitives functions that share compatible APIs with other RAPIDS projects.
<br>
<a href="https://docs.rapids.ai/api/cuml/stable/" class="lib-link">GitHub</a> | <a href="https://github.com/rapidsai/cuml" class="lib-link">Docs</a> | <a href="https://github.com/rapidsai/cuml/blob/branch-0.7/CHANGELOG.md" class="lib-link">Change Log</a> 
{% endcapture %}

{% capture lib_top_right %}
## <i class="fas fa-terminal"></i> cuGraph
cuGraph is a collection of graph analytics that process data in GDF. cuGraph aims at provides a NetworkX-like API that will be familiar to data scientists, so they can use it to easily accelerate their workflows without going into the details of CUDA programming.
<br>
<a href="https://github.com/rapidsai/cugraph" class="lib-link">GitHub</a> | <a href="https://docs.rapids.ai/api/cugraph/stable/" class="lib-link">Docs</a> | <a href="https://github.com/rapidsai/cugraph/blob/branch-0.7/CHANGELOG.md" class="lib-link">Change Log</a> 
{% endcapture %}

{% capture lib_bottom_left %}
## <i class="fas fa-terminal"></i> nvStrings
nvStrings, the Python bindings for <a href="https://github.com/rapidsai/custrings" target="_blank"> cuStrings</a>, provides a pandas-like API that will be familiar to data engineers & data scientists, so they can use it to easily accelerate their workflows without going into the details of CUDA programming.
<br>
<a href="https://github.com/rapidsai/custrings" class="lib-link">GitHub</a> | <a href="https://docs.rapids.ai/api/nvstrings/stable/" class="lib-link">Docs</a> | <a href="https://github.com/rapidsai/custrings/blob/branch-0.4/CHANGELOG.md" class="lib-link">Change Log</a> 
{% endcapture %}

{% capture lib_bottom_middle %}
## <i class="fas fa-terminal"></i> libcudf
libcudf is a C/C++ CUDA library for implementing standard dataframe operations. It is part of the cuDF repository. 
<br>
<a href="https://github.com/rapidsai/cudf" class="lib-link">GitHub</a> | <a href="https://docs.rapids.ai/api/libcudf/stable/" class="lib-link">Docs</a> | <a href="https://github.com/rapidsai/cudf/blob/branch-0.7/CHANGELOG.md" class="lib-link">Change Log</a> 
{% endcapture %}

{% capture lib_bottom_right %}
## <i class="fas fa-terminal"></i> RMM 
RAPIDS Memory Manager (RMM) is a central place for all device memory allocations in cuDF (C++ and Python) and other RAPIDS libraries. In addition, it is a replacement allocator for CUDA Device Memory (and CUDA Managed Memory) and a pool allocator to make CUDA device memory allocation / deallocation faster and asynchronous.
<br>
<a href="https://github.com/rapidsai/rmm" class="lib-link">GitHub</a> | <a href="https://docs.rapids.ai/api/rmm/stable/" class="lib-link">Docs</a> | <a href="https://github.com/rapidsai/rmm/blob/branch-0.7/CHANGELOG.md" class="lib-link">Change Log</a> 
{% endcapture %}

{% include section-double-thirds.html 
    background="background-purple" 
    padding-top="0" padding-bottom="2" 
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

