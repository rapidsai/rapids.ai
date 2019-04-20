---
title: "Open GPU Data Science | RAPIDS"
og_title: "RAPIDS: A Data Science & Analytics Pipeline Accelerator"
og_description: "A suite of software libraries for executing end-to-end data science completely on GPUs"
brand_name: ""
brand_tagline: "More About RAPIDS"
brand_button: "GET STARTED"
brand_link: "start.html"
layout: default
---
{% capture about_top_left %}
## About RAPIDS
The RAPIDS suite of open source software libraries gives you the ability to execute end-to-end data science and analytics pipelines entirely on GPUs. RAPIDS is incubated by <a  href="https://developer.nvidia.com/open-source" class="bold" target="_blank"> NVIDIA® </a> based on years of accelerated data science experience. RAPIDS relies on <a href="https://developer.nvidia.com/cuda-toolkit" class="bold" target="_blank">NVIDIA CUDA®</a> primitives for low-level compute optimization, and exposes GPU parallelism and high-bandwidth memory speed through user-friendly Python interfaces.

RAPIDS also focuses on common data preparation tasks for analytics and data science. This includes a familiar DataFrame API that integrates with a variety of machine learning algorithms for end-to-end pipeline accelerations without paying typical serialization costs. RAPIDS also includes support for multi-node, multi-GPU deployments, enabling vastly accelerated processing and training on much larger dataset sizes.
{% endcapture %}

{% capture about_top_right %}
<img class="full-image" src="{{ site.baseurl }}{% link /assets/images/rapids-end-to-end-performance-chart-oss-page-r4.svg %}" alt="performance">
{: .padding-top-0}
{% endcapture %}

{% capture about_bottom_left %}
## Apache Arrow
This is a columnar, in-memory data structure that delivers efficient and fast data interchange with flexibility to support complex data models.

## Example Libraires and APIs
<span class="bold">cuDF</span> is a DataFrame manipulation library based on Apache Arrow, <span class="bold">cuML</span> a collection of GPU-accelerated machine learning libraries that will provide GPU versions of learning algorithms available in scikit-learn, <span class="bold">cuGraph</span> is a collection of graph analytics libraries that seamlessly integrate into the RAPIDS data science platform.

## Integration With Deep Learning Libraries
RAPIDS provides native array_interface support. This means data stored in Apache Arrow can be seamlessly pushed to deep learning frameworks that accept array_interface such as PyTorch and Chainer. 

## Visualization
RAPIDS is working to integrat with other data visualization libraries, through arrow and cuDF. Native GPU in-memory data format provides high-performance, high-FPS data visualization capabilities, even with very large datasets.
{% endcapture %}

{% capture about_bottom_right %}
<img class="half-image" src="{{ site.baseurl }}{% link /assets/images/EaseVsPerformance.svg %}" alt="ease">
{: .padding-top-0}
{% endcapture %}

{% include section-double-halfs.html
    background="background-white" 
    padding-top="0" padding-bottom="2" 
    content-top-left-half =about_top_left 
    content-top-right-half=about_top_right
    content-bottom-left-half =about_bottom_left
    content-bottom-right-half =about_bottom_right 
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

