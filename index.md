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
RAPIDS is an open source project. Supported by NVIDIA, it also relies on numba, apache arrow, and many more open source projects. <br> **[Learn about our projects <i class="fas fa-angle-double-right"></i>](community.html)**
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
Find more details on our **[get started section <i class="fas fa-angle-double-right"></i>](start.html)**

## <i class="fas fa-bolt"></i> Try Now Online
Jump right into a GPU powered RAPIDS notebook online.<br>
Try with **[<i class="fad fa-fire"></i> BlazingSQL (RAPIDS 0.15+) <i class="fa fa-angle-double-right" aria-hidden="true"></i>](https://app.blazingsql.com/){: target="_blank"}**
<br>
Or with **[<i class="fab fa-google"></i> Colabratory (RAPIDS 0.14 only) <i class="fa fa-angle-double-right" aria-hidden="true"></i>](https://colab.research.google.com/drive/1rY7Ln6rEE1pOlfSHCYOVaqt8OvDO35J0#forceEdit=true&offline=true&sandboxMode=true){: target="_blank"}**

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


{% capture com_left %}
# RAPIDS Repositories
{: .section-title-halfs}
RAPIDS is committed to open source. We strive for a **[6 week release schedule](https://docs.rapids.ai/maintainers){: target="_blank"}**, below is a generalized release schedule. Learn more on our **[Road To 1.0 post <i class="fas fa-angle-double-right"></i>](https://medium.com/rapids-ai/the-road-to-1-0-building-for-the-long-haul-657ae1afdfd6){: target="_blank"}**

## <i class="far fa-calendar-check"></i> Release Schedule
<svg id="Release" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 108">
    <defs>
        <style>
        .cls-1,
        .cls-2 {
            fill: none;
            stroke: #e0e0e0;
            stroke-width: 3px;
        }
        .cls-1,
        .cls-2,
        .cls-3 {
            stroke-miterlimit: 10;
        }

        .cls-2 {
            stroke-dasharray: 10.11 10.11;
        }

        .cls-3,
        .cls-4 {
            fill: #fff;
        }

        .cls-3 {
            stroke: #9943ff;
            stroke-width: 2px;
        }
        .cls-4 {
            font-size: 15px;
            font-family: sans-serif, Helvetica;
        }
        .cls-7 {
            fill: #fff;
            font-weight: bold;
            font-size: 25px;
        }

        </style>
    </defs>
    <title>Release Schedule</title>
    <line class="cls-1" x1="37.36" y1="62.02" x2="320.24" y2="62.02" />
    <line class="cls-1" x1="320.24" y1="62.02" x2="325.24" y2="62.02" />
    <line class="cls-2" x1="335.35" y1="62.02" x2="593.08" y2="62.02" />
    <line class="cls-1" x1="598.13" y1="62.02" x2="603.13" y2="62.02" />
    <circle class="cls-3" cx="37.36" cy="62.02" r="16.61" />
    <circle class="cls-3" cx="320.24" cy="62.02" r="16.61" />
    <circle class="cls-3" cx="603.13" cy="62.02" r="16.61" />
    <text class="cls-4" transform="translate(0 100.00)"> {{ site.data.releases.legacy-date }} </text>
    <text class="cls-4" transform="translate(283.48 100.00)"> {{ site.data.releases.stable-date }} </text>
    <text class="cls-4" transform="translate(564.22 100.00)"> {{ site.data.releases.nightly-date }} </text>
    <text class="cls-4" transform="translate(7.00 12.00)"> LEGACY </text>
    <text class="cls-4" transform="translate(292.00 12.00)"> STABLE </text>
    <text class="cls-4" transform="translate(571.00 12.00)"> NIGHTLY </text>
    <text class="cls-7" transform="translate(16.00 38.00)"> {{ site.data.releases.legacy-version }} </text>
    <text class="cls-7" transform="translate(297.00 38.00)"> {{ site.data.releases.stable-version }} </text>
    <text class="cls-7" transform="translate(581.00 38.00)"> {{ site.data.releases.nightly-version }} </text>
</svg>
{: .padding-top-1em .padding-bottom-2em }
{% endcapture %}

{% capture com_right %}
## <i class="fas fa-code" id="libraries"></i> RAPIDS APIS and Libraries
{: .section-subtitle-top-1}

RAPIDS is open source licensed under Apache 2.0, spanning multiple projects that range from GPU dataframes to GPU accelerated ML algorithms. Its also provides native array_interface support, allowing Apache Arrow data to be pushed to deep learning frameworks. <br> **[Learn more <i class="fas fa-angle-double-right"></i>](about.html)**

## <i class="fab fa-github"></i> Contributing
Whether you are new to RAPIDS, looking to help, or are part of the team, learn about our contributing guidelines on our contributing page. <br> **[Go to Docs <i class="fas fa-angle-double-right"></i>](https://docs.rapids.ai/contributing){: target="_blank"}**
{% endcapture %}

{% include slopecap.html
    background="background-purple"
    position="top"
    slope="up"
%}
{% include section-halfs.html
    background="background-purple"
    padding-top="5em" padding-bottom="6em"
    content-left-half=com_left
    content-right-half=com_right
%}


{% capture lib1_left %}
## <i class="fad fa-terminal"></i> cuDF <span class="api-tag">API</span>

**[GitHub](https://github.com/rapidsai/cudf){: target="_blank"}** **/** **[Docs](https://docs.rapids.ai/api/cudf/stable/){: target="_blank"}** **/** **[Change Log](https://github.com/rapidsai/cudf/blob/main/CHANGELOG.md){: target="_blank"}**
{: .no-tb-margins }

cuDF is a Python GPU DataFrame library (built on the **[Apache Arrow](http://arrow.apache.org/){: target="_blank"}** columnar memory format) for loading, joining, aggregating, filtering, and otherwise manipulating data all in a **[pandas-like](https://pandas.pydata.org/){: target="_blank"}** API familiar to data scientists.

{% endcapture %}
{% capture lib1_right %}
## <i class="fad fa-terminal"></i> libcudf <span class="lib-tag">LIB</span>

**[GitHub](https://github.com/rapidsai/cudf){: target="_blank"}** **/** **[Docs](https://docs.rapids.ai/api/libcudf/stable/){: target="_blank"}** **/** **[Change Log](https://github.com/rapidsai/cudf/blob/main/CHANGELOG.md){: target="_blank"}**
{: .no-tb-margins }

libcudf is a C/C++ CUDA library for implementing standard dataframe operations. It is part of the cuDF repository.

{% endcapture %}
{% capture lib2_left %}
## <i class="fad fa-terminal"></i> cuML <span class="api-tag">API</span>

**[GitHub](https://github.com/rapidsai/cuml){: target="_blank"}** **/** **[Docs](https://docs.rapids.ai/api/cuml/stable/){: target="_blank"}** **/** **[Change Log](https://github.com/rapidsai/cuml/blob/main/CHANGELOG.md){: target="_blank"}**
{: .no-tb-margins }

cuML is a suite of libraries that implement machine learning algorithms and mathematical primitives functions that are compatible with other RAPIDS projects, all in a **[scikit-learn-like](https://scikit-learn.org/stable/index.html){: target="_blank"}** API familiar to data scientists.

{% endcapture %}

{% capture lib2_right %}
## <i class="fad fa-terminal"></i> cuGraph <span class="api-tag">API</span>

**[GitHub](https://github.com/rapidsai/cugraph){: target="_blank"}** **/** **[Docs](https://docs.rapids.ai/api/cugraph/stable/){: target="_blank"}** **/** **[Change Log](https://github.com/rapidsai/cugraph/blob/main/CHANGELOG.md){: target="_blank"}**
{: .no-tb-margins }

cuGraph is a GPU accelerated graph analytics library, with functionality like **[NetworkX](https://networkx.github.io/){: target="_blank"}**, which is seamlessly integrated into the RAPIDS data science platform.

{% endcapture %}
{% capture lib3_left %}
## <i class="fad fa-terminal"></i> cuSignal <span class="api-tag">API</span>

**[GitHub](https://github.com/rapidsai/cusignal){: target="_blank"}** **/** **[Docs](https://docs.rapids.ai/api/cusignal/stable/){: target="_blank"}** **/** **[Change Log](https://github.com/rapidsai/cusignal/blob/main/CHANGELOG.md){: target="_blank"}**
{: .no-tb-margins }

cuSignal is a GPU accelerated signal processing library built around a **[SciPy Signal-like](https://docs.scipy.org/doc/scipy/reference/signal.html){: target="_blank"}** API, CuPy, and custom Numba and CuPy CUDA kernels. cuSignal is written exclusively in Python and demonstrates GPU speeds without a C++ software layer.

{% endcapture %}
{% capture lib3_right %}
## <i class="fad fa-terminal"></i> cuSpatial <span class="api-tag">API</span>

**[GitHub](https://github.com/rapidsai/cuspatial){: target="_blank"}** **/** **[Docs](https://github.com/rapidsai/cuspatial){: target="_blank"}** **/** **[Change Log](https://github.com/rapidsai/cuspatial/blob/main/CHANGELOG.md){: target="_blank"}**
{: .no-tb-margins }

cuSpatial is an efficient C++ library accelerated on GPUs with Python bindings to enable use by the data science community. cuSpatial provides significant GPU-acceleration to common spatial and spatiotemporal operations such as point-in-polygon tests, distances between trajectories, and trajectory clustering when compared to CPU-based implementations.

{% endcapture %}
{% capture lib4_left %}
## <i class="fad fa-terminal"></i> cuxfilter <span class="api-tag">API</span>

**[GitHub](https://github.com/rapidsai/cuxfilter){: target="_blank"}** **/** **[Docs](https://docs.rapids.ai/api/cuxfilter/stable/){: target="_blank"}** **/** **[Change Log](https://github.com/rapidsai/cuxfilter/blob/main/CHANGELOG.md){: target="_blank"}**
{: .no-tb-margins }

cuxfilter is a framework to connect web visualizations to GPU accelerated crossfiltering. Inspired by the javascript version of the **[original](https://github.com/crossfilter/crossfilter){: target="_blank"}**, it enables interactive and super fast multi-dimensional filtering of 100 million+ row tabular datasets via **[cuDF](https://github.com/rapidsai/cudf){: target="_blank"}**.

{% endcapture %}
{% capture lib4_right %}
## <i class="fad fa-terminal"></i> CLX <span class="api-tag">API</span>

**[GitHub](https://github.com/rapidsai/clx){: target="_blank"}** **/** **[Docs](https://docs.rapids.ai/api/clx/stable/){: target="_blank"}** **/** **[Change Log](https://github.com/rapidsai/clx/blob/main/CHANGELOG.md){: target="_blank"}**
{: .no-tb-margins }

Cyber Log Accelerators (CLX), also pronounced "clicks", provides a collection of RAPIDS examples for security analysts, data scientists, and engineers to quickly get started applying RAPIDS and GPU acceleration to real-world cybersecurity use cases.
{% endcapture %}
{% capture lib5_left %}
## <i class="fad fa-terminal"></i> RMM <span class="lib-tag">LIB</span>

**[GitHub](https://github.com/rapidsai/rmm){: target="_blank"}** **/** **[Docs](https://docs.rapids.ai/api/rmm/stable/){: target="_blank"}** **/** **[Change Log](https://github.com/rapidsai/rmm/blob/main/CHANGELOG.md){: target="_blank"}**
{: .no-tb-margins }

RAPIDS Memory Manager (RMM) is a central place for all device memory allocations in cuDF (C++ and Python) and other RAPIDS libraries. In addition, it is a replacement allocator for CUDA Device Memory (and CUDA Managed Memory) and a pool allocator to make CUDA device memory allocation / deallocation faster and asynchronous.

{% endcapture %}

{% include section-halfs.html
    background="background-purple"
    padding-top="0em" padding-bottom="1em"
    content-left-half=lib1_left
    content-right-half=lib1_right
%}
{% include section-halfs.html
    background="background-purple"
    padding-top="0em" padding-bottom="1em"
    content-left-half=lib2_left
    content-right-half=lib2_right
%}
{% include section-halfs.html
    background="background-purple"
    padding-top="0em" padding-bottom="1em"
    content-left-half=lib3_left
    content-right-half=lib3_right
%}
{% include section-halfs.html
    background="background-purple"
    padding-top="0em" padding-bottom="1em"
    content-left-half=lib4_left
    content-right-half=lib4_right
%}
{% include section-halfs.html
    background="background-purple"
    padding-top="0em" padding-bottom="6em"
    content-left-half=lib5_left
%}
{% include slopecap.html
    background="background-purple"
    position="bottom"
    slope="down"
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

Dask is an open source project providing advanced parallelism for analytics that enables performance at scale. RAPIDS is actively contributing to Dask, and it integrates with both RAPIDS cuDF, XGBoost, and RAPIDS cuML for GPU-accelerated data analytics and machine learning. <br> **[Learn more on our Dask page <i class="fa fa-angle-double-right" aria-hidden="true"></i>](dask.html)**

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
![spark]({{ site.baseurl }}{% link /assets/images/spark-logo-trademark.png %}){: .third-image-center}
## <i class="fas fa-code-branch"></i> RAPIDS + Spark

NVIDIA is bringing RAPIDS to Apache Spark to accelerate ETL workflows with GPUs.
<br> **[Learn more on the RAPIDS for Apache Spark page <i class="fa fa-angle-double-right" aria-hidden="true"></i>](https://www.nvidia.com/en-us/deep-learning-ai/solutions/data-science/apache-spark-3/){: target="_blank"}**

{% endcapture %}

{% capture com2_bottom_right %}

{% endcapture %}


{% include section-double-halfs.html
    background="background-white"
    padding-top="1em" padding-bottom="0em"
    content-top-left-half=com_top_left
    content-top-right-half=com_top_right
    content-bottom-left-half=com_bottom_left
    content-bottom-right-half=com_bottom_right
%}
{% include section-double-halfs.html
    background="background-white"
    padding-top="0m" padding-bottom="0em"
    content-top-left-half=com2_top_left
    content-top-right-half=com2_top_right
    content-bottom-left-half=com2_bottom_left
    content-bottom-right-half=com2_bottom_right
%}

# Contributors
{: .section-title-full}
{% include contributing-logos.html
    padding-top="0em" padding-bottom="5em"
%}


# Adopters
{: .section-title-full}
{% include adopter-logos.html
    padding-top="0em" padding-bottom="5em"
%}


# Open Source
{: .section-title-full}
{% include open-source-logos.html
    padding-top="0em" padding-bottom="10em"
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
