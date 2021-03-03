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

RAPIDS also focuses on common data preparation tasks for analytics and data science. This includes a familiar dataframe API that integrates with a variety of machine learning algorithms for end-to-end pipeline accelerations without paying typical serialization costs. RAPIDS also includes support for multi-node, multi-GPU deployments, enabling vastly accelerated processing and training on much larger dataset sizes.

For RAPIDS logos, themes, branding, and other guides, take a look at our **[Branding and Guides page](branding.html)**.

{% endcapture %}

{% capture about_top_right %}
## Apache Arrow
{: .section-subtitle-top-1}
RAPIDS had its start from the **[Apache Arrow](https://arrow.apache.org/){: target="_blank"}** and **[GoAi](http://gpuopenanalytics.com){: target="_blank"}** projects based on a columnar, in-memory data structure that delivers efficient and fast data interchange with flexibility to support complex data models.

## Libraries and APIs Overview

Some RAPIDS projects include **[cuDF](https://github.com/rapidsai/cudf){: target="_blank"}**, a pandas-like dataframe manipulation library; **[cuML](https://github.com/rapidsai/cuml){: target="_blank"}**, a collection of machine learning libraries that will provide GPU versions of algorithms available in scikit-learn; **[cuGraph](https://github.com/rapidsai/cugraph){: target="_blank"}**, a NetworkX-like accelerated graph analytics library. Development follows a **[6 week release schedule](https://docs.rapids.ai/maintainers)**, so new features and libraries are always on the way. 

## Integration With Deep Learning Libraries
RAPIDS provides native `array_interface` support. This means data stored in Apache Arrow can be seamlessly pushed to deep learning frameworks that accept `array_interface` or work with **[DLPack](https://github.com/dmlc/dlpack){: target="_blank"}**, such as **[Chainer](https://github.com/chainer){: target="_blank"}**, **[MXNet](https://github.com/apache/incubator-mxnet){: target="_blank"}**, and **[PyTorch](https://github.com/pytorch/pytorch){: target="_blank"}**. 


## Visualization
Our focus on Python allows RAPIDS to play well with most data science visualization libraries. For even greater performance, we are working towards deeper integration with these libraries since a native GPU in-memory data format provides high-performance, high-FPS data visualization capabilities, even with very large datasets.
{% endcapture %}

{% capture about_bottom_left %}
![RAPIDS ease]({{ site.baseurl }}{% link /assets/images/EaseVsPerformance.svg %}){: .half-image-center}
{% endcapture %}

{% capture about_bottom_right %}
![RAPIDS performance]({{ site.baseurl }}{% link /assets/images/rapids-end-to-end-performance-chart-oss-page-r4.svg %}){: .full-image-center}
{% endcapture %}

{% include section-double-halfs.html
    background="background-white" 
    padding-top="1em" padding-bottom="10em" 
    content-top-left-half=about_top_left 
    content-top-right-half=about_top_right
    content-bottom-left-half=about_bottom_left
    content-bottom-right-half=about_bottom_right 
%} 

{% include slopecap.html 
    background="background-darkpurple" 
    position="top" 
    slope="up"
%}
{% include cta-footer.html 
	name="Learn more about Data Science on GPUs with RAPIDS" 
	tagline=""
	button="LEARN MORE"
	link="https://medium.com/rapids-ai"
%}

