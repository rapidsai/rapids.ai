---
title: "Open GPU Data Science"
description: "A suite of software libraries for executing end-to-end data science completely on GPUs"
tagline: "Learn More About RAPIDS"
button_text: "LEARN MORE"
button_link: "https://medium.com/rapids-ai"
layout: default
---

{% capture about_top_left %}
# About RAPIDS 
{: .section-title-halfs}

The RAPIDS suite of open source software libraries and APIs gives you the ability to execute end-to-end data science and analytics pipelines entirely on GPUs. Licensed under Apache 2.0, RAPIDS is incubated by **[NVIDIA®](https://developer.nvidia.com/open-source){: target="_blank"}** based on extensive hardware and data science experience. RAPIDS utilizes **[NVIDIA CUDA®](https://developer.nvidia.com/cuda-toolkit){: target="_blank"}** primitives for low-level compute optimization, and exposes GPU parallelism and high-bandwidth memory speed through user-friendly Python interfaces.
{% endcapture %}
{% capture about_bottom_left %}
RAPIDS also focuses on common data preparation tasks for analytics and data science. This includes a familiar dataframe API that integrates with a variety of machine learning algorithms for end-to-end pipeline accelerations without paying typical serialization costs. RAPIDS also includes support for multi-node, multi-GPU deployments, enabling vastly accelerated processing and training on much larger dataset sizes.

For RAPIDS logos, themes, branding, and other guides, take a look at our **[Branding and Guides page](branding.html)**.

{% endcapture %}
{% capture about_top_right %}
![RAPIDS ease]({{ site.baseurl }}{% link /assets/images/EaseVsPerformance.svg %}){: .half-image-center}
{% endcapture %}
{% capture about_bottom_right %}
![RAPIDS performance]({{ site.baseurl }}{% link /assets/images/rapids-end-to-end-performance-chart-oss-page-r4.svg %}){: .full-image-center}
{% endcapture %}

{% include section-double-halfs.html
    background="background-white" 
    padding-top="1em" padding-bottom="0em" 
    content-top-left-half=about_top_left
	content-bottom-left-half= about_bottom_left
	content-top-right-half=about_top_right
	content-bottom-right-half= about_bottom_right 
%} 	
{% capture info_right %}
## Apache Arrow
{: .section-subtitle-top-1}
RAPIDS had its start from the **[Apache Arrow](https://arrow.apache.org/){: target="_blank"}** and **[GoAi](http://gpuopenanalytics.com){: target="_blank"}** projects based on a columnar, in-memory data structure that delivers efficient and fast data interchange with flexibility to support complex data models.

## Libraries and APIs Overview

Some RAPIDS projects include **[cuDF](https://github.com/rapidsai/cudf){: target="_blank"}**, a pandas-like dataframe manipulation library; **[cuML](https://github.com/rapidsai/cuml){: target="_blank"}**, a collection of machine learning libraries that will provide GPU versions of algorithms available in scikit-learn; **[cuGraph](https://github.com/rapidsai/cugraph){: target="_blank"}**, a NetworkX-like accelerated graph analytics library. Development follows a **[bimonthly release schedule](https://docs.rapids.ai/maintainers)**, so new features and libraries are always on the way. 
{% endcapture %}
{% capture info_left %}
## Integration With Deep Learning Libraries
{: .section-subtitle-top-1}
RAPIDS provides native `array_interface` support. This means data stored in Apache Arrow can be seamlessly pushed to deep learning frameworks that accept `array_interface` or work with **[DLPack](https://github.com/dmlc/dlpack){: target="_blank"}**, such as **[Chainer](https://github.com/chainer){: target="_blank"}**, **[MXNet](https://github.com/apache/incubator-mxnet){: target="_blank"}**, and **[PyTorch](https://github.com/pytorch/pytorch){: target="_blank"}**. 


## Visualization
Our focus on Python allows RAPIDS to play well with most data science visualization libraries. For even greater performance, we are working towards deeper integration with these libraries since a native GPU in-memory data format provides high-performance, high-FPS data visualization capabilities, even with very large datasets.
{% endcapture %}
{% include section-double-halfs.html
    background="background-white" 
    padding-top="1em" padding-bottom="10em" 
    content-bottom-left-half=info_left
    content-bottom-right-half=info_right 
%} 
{% capture com_left %}
# RAPIDS Repositories
{: .section-title-halfs}
RAPIDS is committed to open source. We strive for a **[bimonth release schedule](https://docs.rapids.ai/maintainers){: target="_blank"}** with the generalized release schedule below. Learn more on our **[Release Blogs <i class="fas fa-angle-double-right"></i>](https://medium.com/rapids-ai){: target="_blank"}**

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
    <text class="cls-7" transform="translate(10.00 38.00)"> {{ site.data.releases.legacy-version }} </text>
    <text class="cls-7" transform="translate(295.00 38.00)"> {{ site.data.releases.stable-version }} </text>
    <text class="cls-7" transform="translate(578.00 38.00)"> {{ site.data.releases.nightly-version }} </text>
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

cuDF is a Python GPU DataFrame library (built on the **[Apache Arrow](https://arrow.apache.org/){: target="_blank"}** columnar memory format) for loading, joining, aggregating, filtering, and otherwise manipulating data all in a **[pandas-like](https://pandas.pydata.org/){: target="_blank"}** API familiar to data scientists.

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

**[GitHub](https://github.com/rapidsai/cuspatial){: target="_blank"}** **/** **[Docs](https://docs.rapids.ai/api/cuspatial/stable/){: target="_blank"}** **/** **[Change Log](https://github.com/rapidsai/cuspatial/blob/main/CHANGELOG.md){: target="_blank"}**
{: .no-tb-margins }

cuSpatial is an efficient C++ library accelerated on GPUs with Python bindings to enable use by the data science community. cuSpatial provides significant GPU-acceleration to common spatial and spatiotemporal operations such as point-in-polygon tests, distances between trajectories, and trajectory clustering when compared to CPU-based implementations.

{% endcapture %}
{% capture lib4_left %}
## <i class="fad fa-terminal"></i> cuxfilter <span class="api-tag">API</span>

**[GitHub](https://github.com/rapidsai/cuxfilter){: target="_blank"}** **/** **[Docs](https://docs.rapids.ai/api/cuxfilter/stable/){: target="_blank"}** **/** **[Change Log](https://github.com/rapidsai/cuxfilter/blob/main/CHANGELOG.md){: target="_blank"}**
{: .no-tb-margins }

cuxfilter is a framework to connect web visualizations to GPU accelerated crossfiltering. Inspired by the JavaScript library **[crossfilter](https://github.com/crossfilter/crossfilter){: target="_blank"}**, it enables interactive and super fast multi-dimensional filtering of 100 million+ row tabular datasets via **[cuDF](https://github.com/rapidsai/cudf){: target="_blank"}**.

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
{% capture lib5_right %}
## <i class="fad fa-terminal"></i> cuCIM <span class="lib-tag">API</span>

**[GitHub](https://github.com/rapidsai/cucim){: target="_blank"}** **/** **[Docs](https://docs.rapids.ai/api/cucim/stable/){: target="_blank"}** **/** **[Change Log](https://github.com/rapidsai/cucim/blob/main/CHANGELOG.md){: target="_blank"}**
{: .no-tb-margins }

cuCIM is a an extensible toolkit designed to provide GPU-accelerated I/O, computer vision and image processing primitives for N-Dimensional images with a focus on biomedical imaging.  Our API mirrors [scikit-image](https://scikit-image.org/) for image manipulation and [OpenSlide](https://openslide.org/) for image loading.

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
    content-right-half=lib5_right
%}
{% include slopecap.html
    background="background-purple"
    position="bottom"
    slope="down"
%}


{% include slopecap.html 
    background="background-darkpurple" 
    position="top" 
    slope="down"
%}
{% include cta-footer.html 
	name="Learn more about Data Science on GPUs with RAPIDS" 
	tagline=""
	button="LEARN MORE"
	link="https://medium.com/rapids-ai"
%}


